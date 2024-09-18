import pytest

from application import create_app

class TestApplication():
    
    @pytest.fixture
    def client(self):
        app = create_app('config.MockConfig')
        return app.test_client()
    
    @pytest.fixture
    def valid_user(self)
        return {
            "first_name": "Mateus",
            "last_name": "Muller",
            "cpf": "641.396.500-28",
            "email": "contato@mateusmuller.me",
            "birth_date": "1996-09-10"
        }
    @pytest.fixture
    def invalid_user(self)
        return {
            "first_name": "Mateus",
            "last_name": "Muller",
            "cpf": "641.396.500-18",
            "email": "contato@mateusmuller.me",
            "birth_date": "1996-09-10"
        }

    def test_get_users(self, client):
        response = client.get('/users')
        assert response.status_code == 200

    def _post_user(self, client ,valid user, invalid_user):
        response = client.post('/user', json=valid_user)
        assert response.status_code == 200
        assert b"successfully" in response.data
    
        response = client.post('/user', json=invalid_user)
        assert response.status_code == 400
        assert b"invalid" in response.data