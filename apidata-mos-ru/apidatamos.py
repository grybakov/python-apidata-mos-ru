import requests


class APIDataMos(object):

    def __init__(self, app_key, timeout=10):

        self.base_api_url = 'https://apidata.mos.ru'
        self.api_version = 'v1'
        self.api_url = '{0}/{1}'.format(self.base_api_url, self.api_version)

        if not app_key:
            raise Exception('API key is required.')
        self.app_key = app_key

        if not isinstance(timeout, (int, float)):
            raise TypeError('Timeout must be numeric.')
        self.timeout = timeout

        self.session = requests.Session()

    def get_datasets_list(self):



    def get_dataset_meta(self):
        pass

    def get_dataset_count(self):
        pass

    def get_dataset_version(self):
        pass

    def get_dataset_icons(self):
        pass

    def get_dataset_image(self):
        pass

    def get_dataset(self):
        pass

    def get_geodata(self):
        pass

    def _exe_request(self, ):
