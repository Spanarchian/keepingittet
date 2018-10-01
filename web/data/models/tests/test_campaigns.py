from ..campaigns import read_campaigns as rs


def test_read_campaigns():
    act = rs()
    assert act == 5, "not as expect"

