from model.contact import Contact


def test_mod_contact_firstname(app):
    app.contact.modify_first(Contact(firstname="New firstname"))


def test_mod_contact_lastname(app):
    app.contact.modify_first(Contact(lastname="New lastname"))


def test_mod_contact_address(app):
    app.contact.modify_first(Contact(address="New address"))


def test_mod_contact_email(app):
    app.contact.modify_first(Contact(email="New email"))
