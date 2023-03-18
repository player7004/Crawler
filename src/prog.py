import json
import sys
import os
import time
import re
import threading
from urllib.parse import urlparse
import requests
from queue import Queue
from bs4 import BeautifulSoup

from operator import itemgetter

from json import load, dumps

from ui import MainWindowUI
from ui import CategoryUI
from ui import RegularUI
from table_views import RegulTableModel
from PySide6.QtWidgets import QMainWindow, QFileDialog
from sub_windows import CategoryEditWindow, RegulaEditWindow


class CrawlerWindow(QMainWindow, MainWindowUI):
    # Инициализация
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.__init_buttons()
        self.__init_variables()

    def __init_variables(self):
        self.sites_file = None
        self.sites_file_containment = None
        self.sites_loaded = False

        self.reg_file = None
        self.reg_file_containment = None
        self.reg_loaded = None

        self.output_file = None
        self.output_existing_file = None

    def __init_buttons(self):
        self.bt_exit.clicked.connect(self.__exit)
        self.bt_start.clicked.connect(None)

        self.bt_regul.clicked.connect(self.__open_change_reg_window)
        self.bt_regul_load.clicked.connect(self.__open_regs)
        self.bt_regul_save.clicked.connect(self.__save_reg_as)

        self.bt_base_open.clicked.connect(self.__open_existing_base)
        self.bt_base_save.clicked.connect(self.__save_base_as)

        self.pushButton.clicked.connect(self.__open_sites)
        self.sites_button.toggled.connect(self.__toggle_sites_label_change)

    def __open_existing_base(self):
        self.output_existing_file = (QFileDialog.getOpenFileName(self, "Открыть базу результатов", sys.argv[0],
                                                                 "Текстовый файл (*.txt)"))[0]

    def __open_sites(self):
        self.sites_file = (QFileDialog.getOpenFileName(self, "Открыть базу сайтов", sys.argv[0],
                                                       "Текстовый файл (*.txt)"))[0]
        if self.sites_file == '':
            self.sites_file = None
            self.sites_file_containment = None
            self.sites_loaded = False
            return

        self.sites_file_containment = []
        url_pattern = re.compile(r"^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:["
                                 r"-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$")
        with open(self.sites_file) as file:
            for site in file:
                site = site.replace("\n", "")
                result = url_pattern.search(site)
                if result:
                    self.sites_file_containment.append(site)

        if len(self.sites_file_containment) > 0:
            self.sites_loaded = True
        else:
            self.sites_loaded = False
        self.__toggle_sites_label_change()

    def __save_base_as(self):
        self.output_file = (QFileDialog.getSaveFileName(self, "Сохранить базу результатов", sys.argv[0],
                                                        "Текстовый файл (*.txt)"))[0]

    def __save_reg_as(self):
        output_file = (QFileDialog.getSaveFileName(self, "Сохранить регулярные выражения", sys.argv[0],
                                                        "JSON файл (*.json)"))[0]
        if output_file == '':
            return

        with open(output_file, mode='w', encoding="UTF-8") as file:
            print(dumps(self.reg_file_containment, ensure_ascii=False).encode("UTF-8").decode("UTF-8"))
            file.write(dumps(self.reg_file_containment, ensure_ascii=False).encode("UTF-8").decode("UTF-8"))

    def __open_change_reg_window(self):
        dialog = RegulaEditWindow()
        dialog.exec()

    def __open_regs(self):
        if self.reg_loaded:
            self.tableView.setModel(None)
            self.reg_file = None
            self.reg_loaded = False
            self.reg_file_containment = None

        self.reg_file = (QFileDialog.getOpenFileName(self, "Загрузить регулярные выражения", sys.argv[0],
                                                     "JSON файл (*.json)"))[0]
        if self.reg_file == '':
            self.reg_file = None
            self.reg_loaded = False
            self.reg_file_containment = None
            return

        self.reg_file_containment = {}
        with open(self.reg_file, mode='r', encoding="UTF-8") as file:
            try:
                json_data = load(file)
            except:
                self.reg_file_containment = None
                return
            normalised_data = []
            for i in json_data:
                for j in json_data[i]:
                    normalised_data.append([i, j])
            model = RegulTableModel(self.tableView, normalised_data)
            self.reg_file_containment = json_data

            self.reg_loaded = True

            self.tableView.setModel(model)
            self.tableView.setColumnWidth(0, self.tableView.width() / 3 - 15)
            self.tableView.setColumnWidth(1, (self.tableView.width() * 2) / 3 - 8)

    def __start_button(self):
        pass

    def __toggle_sites_label_change(self):
        if self.sites_loaded:
            self.sites_button.setChecked(True)
            self.sites_button.setText(f"База загружена: {self.sites_file}")
        else:
            self.sites_button.setChecked(False)
            self.sites_button.setText("База не загружена")

    def __add_json_to_table_view(self, Json):
        for i in Json:
            print(i, Json[i])

    # Закрывает программу
    def __exit(self):
        self.close()



# BASE_SCHEME = 'http'
# DOMAIN_LENGTH = 63
# REPORT_DIR = 'file_report'
# TIMEOUT = 5
# THREADS_NUMBER = 10
#
# categories = {
#     "Новости": (r"новости", r"события", r"журнал", r"телеканал", r"\bСМИ\b"),
#     "Искусство": (r"искусство", r"театр", r"музей"),
#     "Форумы": (r"(форум|портал)", r"доск[аи] объявлений"),
#     "Ресурсы загрузки": (r"скачать", r"бесплатные программы", r"\b(download|free software)\b"),
#     "Образование": (
#     r"образовани|образоват", r"справочные материалы", r"интерактивные курсы", r"энциклопедия", r"университет",
#     r"институт", r"академия", r"колледж", r"техникум", r"Приёмная комиссия", r"Выпускники", r"научно-образовательн",
#     r"\b(ВАК|ДПО)\b", r"Аспирант", r"факультет", r"образоват(.+?)программ"),
#     "Финансы": (r"\bбанк", r"финанс", r"котировки акций", r"курсы валют"),
#     "Государственные ресурсы": (
#     r"правительств", r"министерство", r"полиция", r"пожарная охрана", r"таможенная служба", r"аварийная служба",
#     r"гражданская оборона", r"\bФТС\b", r"\bМЧС\b", r"главное управление", r"конституция", r"\bМФЦ\b", r"госуслуги",
#     r"роспотребнадзор", r"администрац", r"муниципальный район", r"Казначейств", r"Уполномочен", r"прокуратура",
#     r"ГИС\b",),
#     "Здравоохранение и медицина": (r"поликлиника", r"больница", r"аптека", r"\b(врач|доктор)"),
#     "Поиск работы": (r"работа", r"вакансии", r"поиск вакансий", r"резюме"),
#     "Личный сайт": (r"личный блог", r"персональный сайт", r"(дневник|записки)"),
#     "Интернет-магазин": (r"Интернет-магазин", r"аукцион", r"рекламные объявления"),
# }
#
#
# # ==============================================================================
#
# class Page:
#     '''
#         Class Page is a class for storaging and processing a url
#     '''
#
#     def __init__(self, url='empty'):
#         self.url = url
#         self.code = 0
#         self.length = 0
#         self.data = ''
#         self.headers = {}
#         self.domain = ''
#         self.scheme = ''
#         self.port = 0
#
#     def get_webpage(self):
#         '''
#             Getting a webpage
#         '''
#         headers = {'user-agent': 'Mozilla/5.0 (X11; Firefox/72.0'}
#         try:
#             r = requests.get(self.url, verify=False, headers=headers, timeout=TIMEOUT)
#             self.data = r.text
#             self.headers = r.headers
#             self.length = len(r.text)
#             self.code = r.status_code
#             return True
#         except requests.ConnectionError as e:
#             print(f'[!] Connection error: {e}')
#             return False
#         except requests.exceptions.RequestException as e:
#             print(f'[!] Get webpage error: {e}')
#             return False
#
#     def url_parse(self, link):
#
#         try:
#             obj = urlparse(link)
#         except ValueError as e:
#             print(f'[!] Urlparse ValueError: {e}')
#             return False
#
#         url_obj = {}
#         url_obj['scheme'] = obj.scheme
#
#         # netloc contains a port
#         if obj.netloc.find(':') != -1:
#             url_obj['domain'] = obj.netloc[:obj.netloc.find(':')]
#             url_obj['port'] = obj.netloc[obj.netloc.find(':') + 1:]
#         else:
#             url_obj['domain'] = obj.netloc
#             if url_obj['scheme'] == 'https':
#                 url_obj['port'] = 443
#             else:
#                 url_obj['port'] = 80
#
#         url_obj['domain'] = url_obj['domain'].strip('.')
#         return url_obj
#
#     def url_maker(self):
#         '''
#             Create a full URL
#         '''
#         obj = self.url_parse(self.url)
#         if obj is False:
#             return False
#
#         self.domain = obj['domain']
#         if obj['scheme'] == '':
#             self.scheme = BASE_SCHEME
#         else:
#             self.scheme = obj['scheme']
#         self.port = obj['port']
#
#         if (self.domain == '' or len(self.domain) > DOMAIN_LENGTH):
#             return False
#
#         return True
#
#
# # ==============================================================================
#
# def get_category(url_art):
#     '''
#         Get categories for url
#     '''
#     cat_meta = []
#
#     # searching in meta
#     for category, signs in categories.items():
#         for sign in signs:
#             # print(sign)
#             pattern = re.compile(sign, re.IGNORECASE)
#             if (pattern.search(url_art['title']) or pattern.search(url_art['description']) or \
#                     pattern.search(url_art['keywords'])):
#                 cat_meta.append(category)
#                 break
#
#     return cat_meta
#
#
# def handle_url(q):
#     while True:
#         line = q.get()
#         global cur_line
#         global amount_lines
#         global fr_desc
#         global fl_desc
#
#         check_url = line.strip()
#         category_meta = ['Unknown']
#         url_artifacts = {}
#         url_artifacts['title'] = ''
#         url_artifacts['description'] = ''
#         url_artifacts['keywords'] = ''
#
#         pg = Page(check_url)
#         if pg.url_maker():
#             pg.get_webpage()
#
#             if pg.code == 200:
#
#                 # parsing a page source
#                 soup = BeautifulSoup(pg.data, 'html.parser')
#                 if soup.title:
#                     url_artifacts['title'] = str(soup.title.string).strip()
#                 url_artifacts['text'] = soup.get_text('|', strip=True)
#
#                 # meta description
#                 if soup.find('meta', {'name': 'description'}):
#                     url_artifacts['description'] = str(
#                         soup.find('meta', {'name': 'description'}).get('content')).strip()
#
#                 # meta keywords
#                 if soup.find('meta', {'name': 'keywords'}):
#                     url_artifacts['keywords'] = str(soup.find('meta', {'name': 'keywords'}).get('content')).strip()
#
#                 category_meta = get_category(url_artifacts)
#
#             report_str = f'{check_url}\t{pg.code}\t{url_artifacts["title"]}\t \
#             {category_meta}\n'
#             print(report_str, end='')
#
#             fr_desc.write(report_str)
#             fr_desc.flush()
#
#         print(f'{cur_line} / {amount_lines}')
#         cur_line += 1
#
#         q.task_done()
#
#
# # ==============================================================================
#
# if __name__ == '__main__':
#
#     if len(sys.argv) not in [2]:
#         sys.exit(0)
#
#     # file with URLs
#     url_file = sys.argv[1]
#
#     # getting a file prefix
#     file_prefix = f'{os.path.basename(url_file)}-{time.strftime("%Y-%m-%d_%H-%M")}'
#     file_report = "C:\\Users\\playe\\PycharmProjects\\Parser\\" + REPORT_DIR + '\\' + file_prefix + '.txt'
#
#     fr_desc = open(file_report, 'w', encoding='UTF-8')
#
#     # counter
#     cur_line = 1
#     with open(url_file, 'r', encoding='UTF-8') as f:
#         amount_lines = sum(1 for _ in f)
#
#     # creating queue
#     main_queue = Queue()
#     with open(url_file, 'r', encoding='UTF-8') as f:
#         for line in f:
#             main_queue.put(line)
#
#     # creating threads
#     th_i = 0
#     for th_i in range(THREADS_NUMBER):
#         threading.Thread(target=handle_url, args=(main_queue,), daemon=True).start()
#     main_queue.join()
#     fr_desc.close()

