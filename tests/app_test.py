import json

# TEST: x,y missing
def test_route_no_param(app, client):
    del app
    response = client.get('/')
    assert response.status_code == 400
    result = {"error":"Both X param value and Y param value has not been entered.","status":400}
    assert result == json.loads(response.get_data(as_text=True))

# TEST: x missing
def test_route_no_x_param(app, client):
    del app
    response = client.get('/?y=2')
    assert response.status_code == 400
    result = {"error":"X param value has not been entered.","status":400}
    assert result == json.loads(response.get_data(as_text=True))

# TEST: y missing
def test_route_no_y_param(app, client):
    del app
    response = client.get('/?x=2')
    assert response.status_code == 400
    result = {"error":"Y param value has not been entered.","status":400}
    assert result == json.loads(response.get_data(as_text=True))

# TEST: x,y non integer  
def test_route_x_y_non_integer(app, client):
    del app
    response = client.get('/?x=A&y=Z')
    assert response.status_code == 400
    result = {"error":"Both X and Y param must be of integer type.","status":400}
    assert result == json.loads(response.get_data(as_text=True))

# TEST: x,y params integer, complete
def test_route_successful(app, client):
    del app
    response = client.get('/?x=2&y=2')
    assert response.status_code == 200
    result = {"error": "false", "status":200, "answer":"0"}
    assert result == json.loads(response.get_data(as_text=True))

