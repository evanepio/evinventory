from django.test import Client


def test_land_on_admin_page_get_redirected(client: Client):
    response = client.get('/admin/')
    assert response.status_code == 302
