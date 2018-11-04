# -*- coding: utf-8 -*-
from model.group import Group


def test_mod_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(name="111", header="222", footer="333"))
    app.session.logout()
