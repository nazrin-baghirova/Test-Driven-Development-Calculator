from dataclasses import dataclass
import json
import pytest
from src.entrypoints.api.app import app


def test_root_route():
  response = app.test_client().get("/")
  assert response.data.decode("utf-8") == "Hello there"


def test_add_endpoint_int_and_float(get_test_client_with_context):

  data = {"num1": 2, "num2": 4.5}
  response = get_test_client_with_context.get("/add", query_string=data)
  res = json.loads(response.data.decode("utf-8"))
  assert response.status_code == 200
  assert res == {'result': 6.5}


def test_add_endpoint_int_and_list(get_test_client_with_context):
  data = {"num1": 2, "num2": []}
  response = get_test_client_with_context.get("/add", query_string=data)
  assert response.status_code == 400


def test_subtract_endpoint_int_and_float(get_test_client_with_context):

  data = {"num1": 20, "num2": 4.5}
  response = get_test_client_with_context.get("/subtract", query_string=data)
  res = json.loads(response.data.decode("utf-8"))
  assert response.status_code == 200
  assert res == {'result': 15.5}


def test_subtract_endpoint_int_and_list(get_test_client_with_context):

  data = {"num1": 20, "num2": []}
  response = get_test_client_with_context.get("/subtract", query_string=data)
  assert response.status_code == 400


def test_multiply_endpoint_int_and_float(get_test_client_with_context):

  data = {"num1": 20, "num2": 2}
  response = get_test_client_with_context.get("/multiply", query_string=data)
  res = json.loads(response.data.decode("utf-8"))
  assert response.status_code == 200
  assert res == {'result': 40}


def test_multiply_endpoint_int_and_list(get_test_client_with_context):

  data = {"num1": 20, "num2": []}
  response = get_test_client_with_context.get("/subtract", query_string=data)
  assert response.status_code == 400


def test_divide_endpoint_int_and_int(get_test_client_with_context):

  data = {"num1": 20, "num2": 2}
  response = get_test_client_with_context.get("/divide", query_string=data)
  res = json.loads(response.data.decode("utf-8"))
  assert response.status_code == 200
  assert res == {'result': 10}


def test_divide_endpoint_int_and_zero(get_test_client_with_context):

  data = {"num1": 20, "num2": 0}
  response = get_test_client_with_context.get("/divide", query_string=data)
  assert response.status_code == 500
