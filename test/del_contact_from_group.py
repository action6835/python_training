from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture


db2 = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_del_first_contact_from_group(app, db):
    # проверка на наличие контакта
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="New contact"))
    # проверка на наличие группы
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="New group"))
    # проверка на наличие контактов в первой группе
    old_groups = db.get_group_list()
    group_id = old_groups[0].id
    if len(db2.get_contacts_in_group(Group(id=group_id))) == 0:
        app.contact.add_first_contact_to_group(group_id)
    # зачитывание старого списка контактов в группе
    old_contacts_in_group = db2.get_contacts_in_group(Group(id=group_id))
    # получение первого контакта в группе
    contact = old_contacts_in_group[0]
    # удаление первого контакта из группы
    app.contact.del_contact_from_group(group_id=group_id, contact_id=contact.id)
    # зачитывание нового списка контактов в группе
    new_contacts_in_group = db2.get_contacts_in_group(Group(id=group_id))
    # удалениепервого контакта из старого списка контактов группы
    old_contacts_in_group.remove(contact)
    # сравнение старого и нового списков контактов в группе
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)





