from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture


db2 = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    # проверка на наличие контакта
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="New contact"))
    # проверка на наличие группы
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="New group"))
    # получение id первой группы
    old_groups = db.get_group_list()
    group_id = old_groups[0].id
    # зачитывание старого списка контактов в первой группе
    old_contacts_in_group = db2.get_contacts_in_group(Group(id=group_id))
    # добавление контакта в группу
    app.contact.add_first_contact_to_group(group_id)
    # получение первого контакта
    old_contacts = db.get_contact_list()
    contact = old_contacts[0]
    # добавление полученного контакста к старому списку контактов группы
    old_contacts_in_group.append(contact)
    # зачитывание нового списка контактов в группах
    new_contacts_in_group = db2.get_contacts_in_group(Group(id=group_id))
    # сравнение старого и нового списков контактов в группах
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)




