# -*- coding: utf-8 -*-

from python_training.model.contact import Contact
from python_training.fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_new(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="first name", middlename="inital", lastname="last name", nickname="nickname", title="title", company="company", address="address", home="111",
                               mobile="222", work="333", fax="444", email="111@m.ru", email2="222@m.ru", email3="333@m.ru", homepage="homepage", address2="address2", phone2="home",
                               notes="notes"))
    app.session.logout()


def test_add_new_empty(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="",
                               title="", company="", address="", home="",
                               mobile="", work="", fax="", email="", email2="", email3="",
                               homepage="", address2="", phone2="",
                               notes=""))
    app.session.logout()

