from ..touchpoints import read_touchpoints


def test_read_touchpoints():
    data = read_touchpoints()
    for elem in data:
        print("Element : {}".format(elem))
    assert data == []
