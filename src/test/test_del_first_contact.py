from src.model.contact import Contact


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact("Precond name", "Precond last", "Precon address", "00000", " Precond notes notes notes"))
    old_contacts = app.contact.get_contacs_list()
    app.contact.delete()
    new_contacts = app.contact.get_contacs_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
