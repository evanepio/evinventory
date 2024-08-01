from django.contrib.auth.models import User
from django.test import Client


def test_unauthenticated_user_lands_on_admin_page_get_redirected(client: Client):
    response = client.get('/admin/')
    assert response.status_code == 302

def test_authenticated_admin_user_lands_on_admin_page_get_redirected(client: Client, django_user_model: User):
    user = django_user_model.objects.create_user(username='donotcare', password='donotcare', is_staff=True)
    client.force_login(user)
    response = client.get('/admin/')
    assert response.status_code == 200

def test_authenticated_non_admin_user_lands_on_admin_page_get_redirected(client: Client, django_user_model: User):
    user = django_user_model.objects.create_user(username='donotcare', password='donotcare', is_staff=False)
    client.force_login(user)
    response = client.get('/admin/')
    assert response.status_code == 302


def test_land_on_logon_page_get_200(client: Client):
    response = client.get('/admin/login/')
    assert response.status_code == 200
