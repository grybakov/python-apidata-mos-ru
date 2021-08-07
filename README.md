# mos.ru API

A Python wrapper for the [mos.ru API](https://apidata.mos.ru/Docs). It supports extracting datasets (list, metadata, geodata, icons and images, etc) from Moscow Government Open Data Portal API.

## Usage

Register for [apidata.mos.ru](https://apidata.mos.ru) and get the API key.

### Importing

```from apidatamosru.apidatamos import ApiClient```

### How to get datasets list

``` 
    client = ApiClient(API_KEY)
    response = client.get_datasets_list()
```

### How to get dataset
``` 
    client = ApiClient(API_KEY)
    response = client.get_dataset(658)
```

### ...and other

See [tests_methods.py](./tests/test_methods.py)

## Testing

```python -m pytest tests/test_methods.py```

## Requirements

  - [requests](https://github.com/requests/requests)
  - [vcrpy](https://github.com/kevin1024/vcrpy)
  - other requirements you can see in requirements.txt