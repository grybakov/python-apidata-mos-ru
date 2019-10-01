class APIDataMosError(Exception):

    def __init__(self, error_msg, error_code=None):
        self.error_code = error_code
        if error_code == 403:
            raise APIDataMosAuthError(error_msg)
        elif error_code == 413:
            raise APIDataMosCountLimitError(error_msg)
        else:
            super(APIDataMosError, self).__init__(error_msg)


class APIDataMosCountLimitError(APIDataMosError):
    """ Count of entries more than 10000pcs """
    pass


class APIDataMosAuthError(APIDataMosError):
    """ Request without an API key or key is invalid."""
    pass

