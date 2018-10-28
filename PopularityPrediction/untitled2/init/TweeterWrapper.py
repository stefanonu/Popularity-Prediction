class TweeterConnection:
    _consumer_key = ''
    _consumer_secret = ''
    _access_token = ''
    _access_secret = ''

    def __init__(self):
        self._consumer_key = "tRirzunNllF1qIOWkar88qBRJ"
        self._consumer_secret = "tGMfSD5GaclwcvMxM3qCEvy3i84yfVybP7deSyiTKxfCNOzUaM"
        self._access_token = "1050747496702640128-OLFuNxYb11dB2zAjaiYIpt9MxCtlvN"
        self._access_secret = "BQWGs2l8Dn2NzMoKlMCIchJxznZwnHTwS2B71l5pyOp4q"

    def get_consumer_key(self):
        return self._consumer_key

    def get_consumer_secret(self):
        return self._consumer_secret

    def get_access_token(self):
        return self._access_token

    def get_access_secret(self):
        return self._access_secret


