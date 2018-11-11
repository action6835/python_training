# -*- coding: utf-8 -*-
from model.group import Group


def test_mod_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(name="New group"))
    app.session.logout()


def test_mod_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(header="New header"))
    app.session.logout()


def test_mod_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(footer="New footer"))
    app.session.logout()
