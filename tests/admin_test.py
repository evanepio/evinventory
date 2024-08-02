import pytest
from django.test import Client


def test_land_on_logon_page_get_200(client: Client):
    response = client.get('/admin/login/')
    assert response.status_code == 200


@pytest.mark.parametrize("is_superuser,is_staff,expected", [
    pytest.param(False, False, 302, id='superuser=False, staff=False, redirects'),
    pytest.param(False, True, 200, id='superuser=False, staff=True, success'),
    pytest.param(True, False, 302, id='superuser=True, staff=False, redirects'),
    pytest.param(True, True, 200, id='superuser=True, staff=True, success'),
])
def test_admin_page_access(client: Client, django_user_model, is_superuser: bool, is_staff: bool, expected: int):
    user = django_user_model.objects.create_user(username='donotcare', password='donotcare',
                                                 is_superuser=is_superuser, is_staff=is_staff)
    client.force_login(user)
    response = client.get('/admin/')
    assert response.status_code == expected
