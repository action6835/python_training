from model.contact import Contact
from random import randrange


def test_mod_contact_firstname(app, json_contacts):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = json_contacts
    contact.id = old_contacts[index].id
    app.contact.modify_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_mod_contact_lastname(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    app.contact.modify_first(Contact(lastname="New lastname"))


# def test_mod_contact_address(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    app.contact.modify_first(Contact(address="New address"))


# def test_mod_contact_email(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    app.contact.modify_first(Contact(email="New email"))
