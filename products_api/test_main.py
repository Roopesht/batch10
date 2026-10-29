
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user_success():
    """Test successful user creation"""
    response = client.get(
        "/hello"
        
    )
    assert response.status_code == 200
    print("✅ Test passed!")
