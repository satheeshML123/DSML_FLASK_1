from predictions import app
import pytest
import json

@pytest.fixture
def client():
    return app.test_client()

def test_pinger(client):
    res = client.get('/ping')
    assert res.status_code==200
    assert res.json=={'Message': 'Hi I am pinging.............'}

def test_predictions(client):

    test_data = {
    "Gender":"Male",
    "Married":"No",
    "ApplicantIncome":5000000,
    "LoanAmount":50000,
    "Credit_History":1.0
    }
    res=client.post("/predict", json=test_data)
    assert res.status_code==200

    assert res.json == {"loan_approval_status": "Rejected"}