from model.contact import Contact


def test_mod_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first(Contact(firstname="New firstname"))


def test_mod_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first(Contact(lastname="New lastname"))


def test_mod_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first(Contact(address="New address"))


def test_mod_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first(Contact(email="New email"))
