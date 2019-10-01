import pytest
import vcr

from apidatamosru.apidatamos import ApiClient
from apidatamosru.exceptions import APIDataMosError, APIDataMosCountLimitError, APIDataMosAuthError


API_KEY = '7e5b3dd05fbfe77c66a8c356c45eea81'

@vcr.use_cassette('test-invalid_api_key.yml')
@pytest.mark.parametrize('api_key', [
        (''),
        ('31337'),
        ('dreams'),
        ('d870b8ec9ae96da2f33493f85f01999f'),
        ('-1'),
        ('31337.31337'),
    ])
def test_invalid_api_key(api_key):

    client = ApiClient(api_key, 8)
    with pytest.raises(APIDataMosCountLimitError):
        response = client.get_datasets_list()
        assert (response.status_code == 403)
        # assert (response.json()['Items'])

