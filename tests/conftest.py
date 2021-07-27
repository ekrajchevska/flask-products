import pytest
from app import init_app

# pytest conftest file 

@pytest.fixture(scope="session")        # so scope=function ne raboti, investigate why
def client():
    app = init_app(testing=True)

    with app.app_context():
        with app.test_client() as client:
            yield client