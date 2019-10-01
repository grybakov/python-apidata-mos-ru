import requests

from .exceptions import APIDataMosError


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
        self.client = requests.Session()

    def get_datasets_list(self, **kwargs):
        kwargs['app_key'] = self.app_key
        endpoint = '{0}/{1}/datasets'.format(self.base_api_url, self.api_version)
        return self._request(endpoint, params=kwargs)

    def get_dataset_meta(self, id, **kwargs):
        self._check_id(id)
        kwargs['app_key'] = self.app_key
        endpoint = '{0}/{1}/datasets/{2}'.format(self.base_api_url, self.api_version, str(id))
        return self._request(endpoint, params=kwargs)

    def get_dataset_count(self, id, **kwargs):
        self._check_id(id)
        kwargs['app_key'] = self.app_key
        endpoint = '{0}/{1}/datasets/{2}/count'.format(self.base_api_url, self.api_version, str(id))
        return self._request(endpoint, params=kwargs)

    def get_dataset_version(self, id, **kwargs):
        self._check_id(id)
        kwargs['app_key'] = self.app_key
        endpoint = '{0}/{1}/datasets/{2}/version'.format(self.base_api_url, self.api_version, str(id))
        return self._request(endpoint, params=kwargs)

    def get_dataset_icons(self, id, size='m', **kwargs):
        # todo Пересечение
        self._check_id(id)
        kwargs['app_key'] = self.app_key
        endpoint = '{0}/{1}/datasets/{2}/icon/{3}'.format(self.base_api_url, self.api_version, str(id), size)
        return self._request(endpoint, params=kwargs)

    def get_dataset_image(self, id, width=70, **kwargs):
        self._check_id(id)
        kwargs['app_key'] = self.app_key
        endpoint = '{0}/{1}/datasets/{2}/image/{3}'.format(self.base_api_url, self.api_version, str(id), width)
        return self._request(endpoint, params=kwargs)

    def get_dataset_marker(self, id, **kwargs):
        self._check_id(id)
        kwargs['app_key'] = self.app_key
        endpoint = '{0}/{1}/datasets/{2}/marker'.format(self.base_api_url, self.api_version, str(id))
        return self._request(endpoint, params=kwargs)

    def get_dataset(self, id, **kwargs):
        self._check_id(id)
        kwargs['app_key'] = self.app_key
        endpoint = '{0}/{1}/datasets/{2}/rows'.format(self.base_api_url, self.api_version, str(id))
        return self._request(endpoint, params=kwargs)

        # todo Проекция данных
        # Для указанного метода доступна возможность проекции данных.
        # Для ее использования необходимо формировать POST запрос с перечислением в теле запроса требуемых для вывода атрибутов.

    def get_geodata(self, id, **kwargs):
        self._check_id(id)
        kwargs['app_key'] = self.app_key
        endpoint = '{0}/{1}/datasets/{2}/features'.format(self.base_api_url, self.api_version, str(id))
        return self._request(endpoint, params=kwargs)

        # todo Проекция данных
        # Для указанного метода доступна возможность проекции данных.
        # Для ее использования необходимо формировать POST запрос с перечислением в теле запроса требуемых для вывода атрибутов.

    def close(self):
        self.client.close()

    def _check_id(self, id):
        if not isinstance(id, int):
            raise TypeError('id must be int.')
        return True

    def _request(self, endpoint, params=None):
        response = self.client.get(endpoint, params=params)
        if response.status_code != 200:
            raise APIDataMosError('{0} {1}'.format(response.status_code, response.reason), response.status_code)
        return response

