from ..client import Client as mc

newUser = {"name":"John", "email":"spanarchian@gmail.com", "":"" }


def test_create_user():
    expected = "ABCDE12345"
    actual = mc.create_user(newUser["email"], newUser)
    assert expected == actual["uREF"]
