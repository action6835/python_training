from model.contact import Contact


def test_mod_contact(app):
    app.contact.modify_first(
        Contact(firstname="FIRST NAME", middlename="INITIAL", lastname="LAST NAME", nickname="NICKNAME", title="TITLE",
                company="COMPANY", address="ADDRESS", home="111-111",
                mobile="222-222", work="333-333", fax="444-444", email="111-111@m.ru", email2="222-222@m.ru", email3="333-333@m.ru",
                homepage="HOMEPAGE", address2="ADDRESS2", phone2="555-555",
                notes="NOTES"))
