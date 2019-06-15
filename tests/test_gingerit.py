import pytest

from gingerit.gingerit import GingerIt


@pytest.mark.parametrize("text,expected", [
    (
        "The smelt of fliwers bring back memories.",
        "The smell of flowers brings back memories."
    ),
    (
        "Edwards will be sck yesterday",
        "Edwards was sick yesterday"
    ),
    (
        "Edwards was sick yesterday.",
        "Edwards was sick yesterday."
    ),
    (
        "",
        ""
    )
])
def test_gingerit(text, expected):
    parser = GingerIt()
    assert parser.parse(text)["result"] == expected
