# -*- coding: utf-8 -*-
from model.group import Group


def test_mod_group_name(app):
    app.group.modify_first(Group(name="New group"))


def test_mod_group_header(app):
    app.group.modify_first(Group(header="New header"))


def test_mod_group_footer(app):
    app.group.modify_first(Group(footer="New footer"))
