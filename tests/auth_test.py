"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data

def test_auth_pages(client):
    """This makes the index page"""
    response = client.get("/dashboard")
    assert response.status_code == 302
    response = client.get("/register")
    assert response.status_code == 200
    response = client.get("/login")
    assert response.status_code == 200

def test_setup(client):
    driver.get("https://www.facebook.com")
    driver.find_element(By.NAME,"email").send_keys("XXXX@gmail.com")
    driver.find_element(By.NAME,"pass").send_keys("XXX@ABC")
    driver.find_element(By.NAME,"login").click()
    driver.close()
    assert True

