import pytest
import vcr

from apidatamosru.apidatamos import ApiClient
from apidatamosru.exceptions import APIDataMosError, APIDataMosCountLimitError, APIDataMosAuthError


API_KEY = '7e5b3dd05fbfe77c66a8c356c45eea81'


@vcr.use_cassette()
def test_of_datasets_list():
    client = ApiClient(API_KEY)
    response = client.get_datasets_list()
    assert (response.status_code == 200)
    assert (response.json() is not None)

@vcr.use_cassette()
def test_count_datasets_list():
    client = ApiClient(API_KEY)
    response = client.get_datasets_list(inlinecount='allpages')
    assert (response.status_code == 200)
    assert ('Items' in response.json())
    assert ('Count' in response.json())

@vcr.use_cassette()
def test_top_datasets_list():
    client = ApiClient(API_KEY)
    response = client.get_datasets_list(top=6)
    assert (response.status_code == 200)
    assert (len(response.json()) == 6)

# todo

@vcr.use_cassette()
def test_invalid_api_key():
    api_key = 'd870b8ec9ae96da2f33493f85f01999f'

    client = ApiClient(api_key, 8)
    with pytest.raises(APIDataMosAuthError):
        response = client.get_datasets_list()
        assert (response.status_code == 403)
        assert (response.json() is None)

