class D2APIException(Exception):
    def __str__(self) -> str:
        return self.__repr__()


class APIError(D2APIException):
    def __init__(self, error_code: int, error_status: str, message: str):
        self.error_code = error_code
        self.error_status = error_status
        self.message = message

    def __repr__(self) -> str:
        return f"<API Error {self.error_code}> {self.error_status}: {self.message}"


class APICallFailed(D2APIException):
    def __init__(self, status_code: int):
        self.status_code = status_code

    def __repr__(self) -> str:
        return f"<API Calling Failed> Network Error {self.status_code}"
