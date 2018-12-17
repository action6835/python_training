import re
from model.contact import Contact


def test_contact_on_home_page(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for row in contacts_from_home_page:
        index = contacts_from_home_page.index(row)
        assert row.firstname == contacts_from_db[index].firstname
        assert row.lastname == contacts_from_db[index].lastname
        assert row.address == contacts_from_db[index].address
        assert row.all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[index])
        assert row.all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db[index])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))
