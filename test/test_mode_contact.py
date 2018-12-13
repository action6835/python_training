from model.contact import Contact
from random import randrange


def test_mod_contact_firstname(app, db, json_contacts, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = json_contacts
    contact.id = old_contacts[index].id
    app.contact.modify_by_id(contact, contact.id)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
