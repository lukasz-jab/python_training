import random
import re

from src.model.contact import Contact


def test_contacts_from_home_with_db(app, db):
    contacts_ui = app.contact.get_contacs_list()
    contacts_db = db.get_contacts_list()
    #check the id and firstname between ui and db elements:
    assert sorted(contacts_ui, key=Contact.id_or_max) == sorted(contacts_db, key=Contact.id_or_max)
    #check other fields:
    for c_ui in contacts_ui:
        for c_db in contacts_db:
            if c_db.id == c_ui.id:
                assert c_ui.lastname == c_db.lastname
                assert c_ui.address == c_db.address
                assert c_ui.all_phones_from_home_page == merge_phones_like_on_home_page(c_db)
                assert c_ui.all_emails == merge_emails_like_on_home_page(c_db)


def test_data_home_edit_sites(app, db):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(
            Contact("Precond name", "Precond last", "Precon address", "00000", " Precond notes notes notes"))
    index = len(db.get_contacts_list())
    contact_from_home_page = app.contact.get_contacs_list()[random.randint(0, index - 1)]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(contact_from_home_page.id)
    # test all phones in file: test_phones.py
    assert contact_from_home_page.all_emails == merge_emails_like_on_home_page(contact_from_edit_page)
    # main page cut more than one space " "
    assert clear_h(contact_from_home_page.address) == clear_h(contact_from_edit_page.address)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", (map(lambda x: x, (filter(lambda x: x is not None,
                                                                         [contact.emial_1, contact.emial_2,
                                                                          contact.emial_3]))))))


def clear_h(s):
    return re.sub(" ", "", s)


def test_phones_on_main_page(app):
    contact_from_home_page = app.contact.get_contacs_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(contact_from_home_page.id)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    # in aplication version 9.0, secondaryphone(fax) is not displayed in home page in the table


def test_phones_on_view_page(app):
    test_contact = app.contact.get_contacs_list()[0]
    contact_from_view_page = app.contact.get_contact_info_from_view_page(test_contact.id)
    print(contact_from_view_page.all_phones_from_home_page)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(test_contact.id)
    assert clear(contact_from_view_page.all_phones_from_home_page) == merge_phones_like_on_home_page(
        contact_from_edit_page)
    # in aplication version 9.0, secondaryphone is field fax not added due to incompatibility with home page test


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            (map(lambda x: clear(x), filter(lambda x: x is not None,
                                                            [contact.homephone, contact.mobilephone,
                                                             contact.workphone])))))
