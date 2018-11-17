# -*- coding: utf-8 -*-

from model.contact import Contact

    
def test_add_new(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="first name", middlename="inital", lastname="last name", nickname="nickname", title="title", company="company", address="address", home="111",
                               mobile="222", work="333", fax="444", email="111@m.ru", email2="222@m.ru", email3="333@m.ru", homepage="homepage", address2="address2", phone2="home",
                               notes="notes")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_new_empty(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", middlename="", lastname="", nickname="",
                               title="", company="", address="", home="",
                               mobile="", work="", fax="", email="", email2="", email3="",
                               homepage="", address2="", phone2="",
                               notes="")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

