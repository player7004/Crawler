import sys
import re
from json import load, dumps

from ui import MainWindowUI
from views import RegularTableModel
from windows import RegularEditWindow
from windows import ErrorMessageWindow

from PySide6.QtWidgets import QMainWindow, QFileDialog


class MainWindow(QMainWindow, MainWindowUI):

    # Инициализация
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        self.__init_variables()
        self.__init_buttons()
        self.__init_ui()

    # Инициализирует базовые переменные для работы программы
    def __init_variables(self):
        # Флаг работы программы
        # Если программа работает, то мы не можем редактировать категории
        # Если программа работает, то мы не можем менять базу сайтов
        # Если программа работает, то мы не можем выйти из неё по кнопке выход
        self.__running = False

        # Путь к файлу с базой сайтов
        self.__sites_file = None
        # Содержимое файла с базой сайтов
        self.__sites_file_containment = []
        # Флаг указывающий на то загружена база сайтов или нет
        # Если база сайтов не загружена, то мы не можем запустить программу
        self.__sites_loaded = False

        # Путь к файлу с регулярными выражениями
        self.__regulars_file = None
        # Содержимое файла с регулярными выражениями
        self.__regulars_file_containment = {}
        # Флаг указывающий на то загружены регулярные выражения или нет
        # Если регулярные выражения загружены, то мы не можем запустить программу
        self.__regulars_loaded = None
        self.__regulars_model = RegularTableModel(self.tableView, self.__regulars_file_containment)

        # Путь сохранения результата
        self.__output_file = None
        # Содержимое результатов
        self.__output_file_containment = {}
        # Флаг того был файл с результатами загружен или нет
        self.__output_loaded = False
        # Путь к файлу с результатами
        self.__output_existing_file = None

    def __init_ui(self):
        # Окно вывода информации об ошибке
        self.__error_window = ErrorMessageWindow()
        # Окно редактирования регулярных выражения
        self.__regulars_edit_window = RegularEditWindow()

        self.__update_regulars_table()

    # Инициализирует функционал кнопок
    def __init_buttons(self):
        # Кнопка выхода
        self.bt_exit.clicked.connect(self.__exit)
        # Кнопка включения работы программы
        self.bt_start.clicked.connect(self._start)

        # Кнопка открытия окна редактирования регулярных выражений
        self.bt_regul.clicked.connect(self.__open_change_reg_window)
        # Кнопка загрузки регулярных выражений
        self.bt_regul_load.clicked.connect(self.__open_regulars)
        # Кнопка сохранения регулярных выражений
        self.bt_regul_save.clicked.connect(self.__save_regulars_as)

        # Кнопка открытия существующей БД
        self.bt_base_open.clicked.connect(self.__open_existing_base)
        # Кнопка сохранения текущих результатов
        self.bt_base_save.clicked.connect(self.__save_base_as)

        # Кнопка загрузки базы сайтов
        self.pushButton.clicked.connect(self.__open_sites)
        # Костыль, блокирующий смену состояния флага состояния загрузки базы
        self.sites_button.toggled.connect(self.__toggle_sites_label_change)

    # Загрузка базы сайтов
    def __open_sites(self):
        # Запрет смены базы во время работы программы
        if self.__running:
            self.__error_window.showMessage("Смена базы сайтов невозможна во время работы программы."
                                            " Остановите программу или дождитесь окончания её работы для"
                                            "загрузки новой базы сайтов.",
                                            "sites_program_working_error")
            return

        # Получаем путь к искомому файлу
        sites_file = (QFileDialog.getOpenFileName(self, "Открыть базу сайтов", sys.argv[0],
                                                  "Текстовый файл (*.txt)"))[0]
        # Проверяем валидность пути
        # Если была нажата кнопка отмены, то сохраняем текущую базы и ничего не делаем
        if sites_file == '':
            return

        # Сбрасываем старую базу сайтов
        self.__drop_sites()

        # Готовим регулярное выражение для проверки валидности URL
        url_pattern = re.compile(r"^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:["
                                 r"-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$")
        # Готовим временный лист для сохранения
        temp_base = []
        # Открываем файл в режиме только чтения с кодировкой UTF-8
        with open(sites_file, mode='r', encoding='UTF-8') as file:
            for site in file:
                # Удаляем символы конца строки
                site = site.replace("\n", "")
                # Проверяем валидность URL
                result = url_pattern.search(site)
                # Если сайт прошёл проверку, то добавляем его
                if result:
                    temp_base.append(site)

        # Проверяем были ли загружены сайты
        # Если есть хотя бы один сайт, то обновляем флаг и состояние флага состояния загрузки базы
        # Иначе ничего не делаем
        if len(temp_base) > 0:
            self.__sites_file = sites_file
            self.__sites_loaded = True
            self.__sites_file_containment = temp_base
            print(self.__sites_file_containment)
            self.__toggle_sites_label_change()
        else:
            return

    def __drop_sites(self):
        self.__sites_file = None
        self.__sites_loaded = False
        self.__sites_file_containment = []
        self.__toggle_sites_label_change()

    def __open_regulars(self):
        # Запрет смены регулярных выражений во время работы программы
        if self.__running:
            self.__error_window.showMessage("Смена регулярных выражений невозможна во время работы программы."
                                            " Остановите программу или дождитесь окончания её работы для"
                                            "загрузки новых регулярных выражений."
                                            , "regulars_program_working_error")
            return

        # Получаем путь к искомому файлу
        reg_file = (QFileDialog.getOpenFileName(self, "Загрузить регулярные выражения", sys.argv[0],
                                                       "JSON файл (*.json)"))[0]

        # Проверяем валидность пути
        # Если была нажата кнопка отмены, то сохраняем текущие регулярны выражения и ничего не делаем
        if reg_file == '':
            return

        # Сбрасываем старые регулярные выражения
        self.__drop_regulars()

        # Открываем файл в режиме только чтения с кодировкой UTF-8
        with open(reg_file, mode='r', encoding="UTF-8") as file:
            try:
                json_data = load(file)
            except:
                self.__error_window.showMessage(f"Не удалось загрузить файл: {reg_file}."
                                                f" Во время обработки содержимого файла возникла ошибка - "
                                                f"файл имеет ошибки синтаксиса."
                                                f" Проверьте содержимое файла и повторите загрузку."
                                                , "regulars_loading_file_broken_error")
                return

        # Проверяем содержимое загруженной информации
        if json_data:
            # Обновляем флаг
            # Обновляем файл
            # Обновляем содержимое файла
            self.__regulars_loaded = True
            self.__regulars_file_containment = json_data
            self.__regulars_file = reg_file

            # Обновляем модель таблицы
            self.__update_regulars_table()
        else:
            self.__error_window.showMessage(f"Не удалось загрузить файл: {reg_file}."
                                            f" Во время обработки содержимого файла возникла ошибка - "
                                            f"файл пуст."
                                            f" Проверьте содержимое файла и повторите загрузку."
                                            , "regulars_loading_file_empty_error")
            return

    def __save_regulars_as(self):
        # Проверяем были ли загружены регулярные выражения
        # Если они не были загружены, то ничего не делаем
        if not self.__regulars_loaded:
            self.__error_window.showMessage("Невозможно сохранить регулярные выражения"
                                            " - регулярные выражения не были загружены."
                                            , "regulars_not_loaded_error")
            return
        # Получаем путь к файлу для сохранения
        output_file = (QFileDialog.getSaveFileName(self, "Сохранить регулярные выражения", sys.argv[0],
                                                   "JSON файл (*.json)"))[0]
        # Проверяем валидность пути
        # Если была нажата кнопка отмены, то сохраняем текущие регулярны выражения и ничего не делаем
        if output_file == '':
            return

        # Открываем файл в режиме записи с кодировкой UTF-8
        with open(output_file, mode='w', encoding="UTF-8") as file:
            file.write(dumps(self.__regulars_file_containment, ensure_ascii=False).encode("UTF-8").decode("UTF-8"))

    def __open_change_reg_window(self):
        # Запрет редактирования регулярных выражений во время работы программы
        if self.__running:
            self.__error_window.showMessage("Редактирование регулярных выражений невозможна во время работы программы."
                                            " Остановите программу или дождитесь окончания её работы для"
                                            "загрузки новых регулярных выражений."
                                            , "regulars_program_working_error")
            return
        self.__regulars_edit_window.update_regulars_data(self.__regulars_file_containment)
        self.__regulars_edit_window.exec()
        self.__regulars_file_containment = self.__regulars_edit_window.get_regulars_data()
        self.__update_regulars_table()

    def __drop_regulars(self):
        self.__regulars_file = None
        self.__regulars_file_containment = {}
        self.__regulars_loaded = None
        self.__update_regulars_table()

    def __update_regulars_table(self):
        self.__regulars_model = RegularTableModel(self.tableView, self.__regulars_file_containment)
        self.tableView.setModel(self.__regulars_model)
        self.tableView.setColumnWidth(0, self.tableView.width() / 3 - 23)
        self.tableView.setColumnWidth(1, (self.tableView.width() * 2) / 3)

    def __save_base_as(self):
        self.__output_file = (QFileDialog.getSaveFileName(self, "Сохранить базу результатов", sys.argv[0],
                                                          "Текстовый файл (*.txt)"))[0]

    def __open_existing_base(self):
        self.__output_existing_file = (QFileDialog.getOpenFileName(self, "Открыть базу результатов", sys.argv[0],
                                                                   "Текстовый файл (*.txt)"))[0]

    def _start(self):
        pass

    def __toggle_sites_label_change(self):
        if self.__sites_loaded:
            self.sites_button.setChecked(True)
            self.sites_button.setText(f"База загружена: {self.__sites_file}")
        else:
            self.sites_button.setChecked(False)
            self.sites_button.setText("База не загружена")

    # Закрывает программу
    def __exit(self):
        self.close()
