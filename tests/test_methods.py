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
    client.close()

@vcr.use_cassette()
def test_count_datasets_list():
    client = ApiClient(API_KEY)
    response = client.get_datasets_list(inlinecount='allpages')
    assert (response.status_code == 200)
    assert ('Items' in response.json())
    assert ('Count' in response.json())
    client.close()

@vcr.use_cassette()
def test_top_datasets_list():
    client = ApiClient(API_KEY)
    response = client.get_datasets_list(top=6)
    assert (response.status_code == 200)
    assert (len(response.json()) == 6)
    client.close()

@vcr.use_cassette()
def test_dataset_meta():
    client = ApiClient(API_KEY)
    response = client.get_dataset_meta(658)
    assert (response.status_code == 200)
    assert ('Id' in response.json())
    assert (response.json()['Id'] == 658)
    client.close()

@vcr.use_cassette()
def test_dataset_count():
    client = ApiClient(API_KEY)
    response = client.get_dataset_count(658)
    assert (response.status_code == 200)
    assert (isinstance(int(response.text), int))
    client.close()

@vcr.use_cassette()
def test_dataset_version():
    client = ApiClient(API_KEY)
    response = client.get_dataset_version(658)
    assert ('versionNumber' in response.json())
    assert ('releaseNumber' in response.json())
    client.close()

@vcr.use_cassette()
def test_dataset_icons():
    client = ApiClient(API_KEY)
    response = client.get_dataset_icons(658)
    assert (response.status_code == 200)
    assert (isinstance(response.content, bytes))
    client.close()

@vcr.use_cassette()
def test_dataset_image():
    client = ApiClient(API_KEY)
    response = client.get_dataset_image(658)
    assert (response.status_code == 200)
    assert (isinstance(response.content, bytes))
    client.close()

@vcr.use_cassette()
def test_dataset_marker():
    client = ApiClient(API_KEY)
    response = client.get_dataset_marker(658)
    assert (response.status_code == 200)
    assert (isinstance(response.content, bytes))
    client.close()

@vcr.use_cassette()
def test_get_dataset():
    client = ApiClient(API_KEY)
    response = client.get_dataset(658, top=5)
    assert (response.status_code == 200)
    assert (len(response.json()) == 5)
    client.close()

@vcr.use_cassette()
def test_get_geodata():
    client = ApiClient(API_KEY)
    response = client.get_geodata(658)
    assert (response.status_code == 200)
    assert ('features' in response.json())
    client.close()

@vcr.use_cassette()
def test_invalid_api_key():
    invalid_api_key = 'd870b8ec9ae96da2f33493f85f01999f'
    client = ApiClient(invalid_api_key, 8)
    with pytest.raises(APIDataMosAuthError):
        response = client.get_datasets_list()
        assert (response.status_code == 403)
        assert (response.json() is None)

@vcr.use_cassette()
def test_count_limit():
    client = ApiClient(API_KEY)
    with pytest.raises(APIDataMosCountLimitError):
        response = client.get_dataset(3013)
        assert (response.status_code == 413)
        assert (response.json() is None)

