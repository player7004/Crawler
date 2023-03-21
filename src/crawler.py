import re
import threading
from urllib.parse import urlparse
import requests
from queue import Queue
from bs4 import BeautifulSoup
from src.windows import MainWindow


class Page:
    def __init__(self, url='empty', scheme='http', timeout=5, domain_length=63):
        self.timeout = timeout
        self.base_scheme = scheme
        self.domain_length = domain_length

        self.url = url
        self.code = 0
        self.length = 0
        self.data = ''
        self.headers = {}
        self.domain = ''
        self.scheme = ''
        self.port = 0

    def get_webpage(self):
        '''
            Getting a webpage
        '''
        headers = {'user-agent': 'Mozilla/5.0 (X11; Firefox/72.0'}
        try:
            r = requests.get(self.url, verify=False, headers=headers, timeout=self.timeout)
            self.data = r.text
            self.headers = r.headers
            self.length = len(r.text)
            self.code = r.status_code
            return True
        except requests.ConnectionError as e:
            print(f'[!] Connection error: {e}')
            return False
        except requests.exceptions.RequestException as e:
            print(f'[!] Get webpage error: {e}')
            return False

    @staticmethod
    def url_parse(link):

        obj = urlparse(link)
        url_obj = {'scheme': obj.scheme}

        # netloc contains a port
        if obj.netloc.find(':') != -1:
            url_obj['domain'] = obj.netloc[:obj.netloc.find(':')]
            url_obj['port'] = obj.netloc[obj.netloc.find(':') + 1:]
        else:
            url_obj['domain'] = obj.netloc
            if url_obj['scheme'] == 'https':
                url_obj['port'] = 443
            else:
                url_obj['port'] = 80

        url_obj['domain'] = url_obj['domain'].strip('.')
        return url_obj

    def url_maker(self):
        '''
            Create a full URL
        '''
        obj = self.url_parse(self.url)
        if obj is False:
            return False

        self.domain = obj['domain']
        if obj['scheme'] == '':
            self.scheme = self.base_scheme
        else:
            self.scheme = obj['scheme']
        self.port = obj['port']

        if self.domain == '' or len(self.domain) > self.domain_length:
            return False
        return True


class Crawler(MainWindow):

    def __init__(self):
        super().__init__()

        self.base_scheme = 'http'
        self.domain_length = 63
        self.timeout = 5
        self.threads_count = 10

        self.sites = []
        self.regulars = {}
        self.working_queue = Queue()
        self.result = {}

    def _force_close(self):
        self._set_running(False)
        self.working_queue = Queue()

    def _start(self):
        self.__drop_result()

        self._set_running(True)

        self.sites = self._get_sites()
        self.regulars = self._get_regulars()

        for i in self.sites:
            self.working_queue.put(i)

        for th in range(self.threads_count):
            threading.Thread(target=self.__handle_url, args=(), daemon=True).start()
        threading.Thread(target=self.__end_handler, args=(), daemon=True).start()

    def __get_category(self, url_art):
        for category, signs in self.regulars.items():
            for sign in signs:
                pattern = re.compile(sign, re.IGNORECASE)
                if (pattern.search(url_art['title']) or pattern.search(url_art['description']) or
                        pattern.search(url_art['keywords'])):
                    return category

    def __drop_result(self):
        self.sites = []
        self.regulars = {}
        self.working_queue = Queue()
        self.result = {}

    def __end_handler(self):
        while self._get_running():
            self.working_queue.join()
            self._set_running(False)
            self._done(self.result)

    def __handle_url(self):
        while self._get_running():
            current_line = self.working_queue.get()

            check_url = current_line.strip()
            category_meta = ['Unknown']
            url_artifacts = {}
            url_artifacts['title'] = ''
            url_artifacts['description'] = ''
            url_artifacts['keywords'] = ''

            pg = Page(check_url)
            if pg.url_maker():
                pg.get_webpage()

                if pg.code == 200:

                    soup = BeautifulSoup(pg.data, 'html.parser')
                    if soup.title:
                        url_artifacts['title'] = str(soup.title.string).strip()
                    url_artifacts['text'] = soup.get_text('|', strip=True)

                    if soup.find('meta', {'name': 'description'}):
                        url_artifacts['description'] = str(
                            soup.find('meta', {'name': 'description'}).get('content')).strip()

                    if soup.find('meta', {'name': 'keywords'}):
                        url_artifacts['keywords'] = str(soup.find('meta', {'name': 'keywords'}).get('content')).strip()

                    category_meta = self.__get_category(url_artifacts)
                self.result.update({check_url: [pg.code, category_meta]})

            self.working_queue.task_done()
