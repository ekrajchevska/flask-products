class InvalidAPIUsage(Exception):
    status_code = 400

    def __init__(self, message: str, status_code=None):
        super().__init__()

        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        response = dict()
        response["message"] = self.message
        return response


class ProductNotFoundException(Exception):
    def __init__(self, message: str, status_code: int):
        message = "No product with such ID."
        status_code = 404


class InvalidQuantityException(Exception):
    def __init__(self, message: str, status_code: int):
        message = "Order exceeds available quantity"
        status_code = 400


class CategoryNotFoundException(Exception):
    def __init__(self, message: str, status_code: int):
        message = "No category with such ID."
        status_code = 404
