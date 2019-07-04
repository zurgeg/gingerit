import pytest

from gingerit.gingerit import GingerIt


@pytest.mark.parametrize("text,expected,corrections", [
    (
        "The smelt of fliwers bring back memories.",
        "The smell of flowers brings back memories.",
        [
            {'start': 21, 'definition': None, 'correct': u'brings', 'text': 'bring'},
            {'start': 13, 'definition': u'a plant cultivated for its blooms or blossoms', 'correct': u'flowers',
             'text': 'fliwers'},
            {'start': 4, 'definition': None, 'correct': u'smell', 'text': 'smelt'}
        ]
    ),
    (
        "Edwards will be sck yesterday",
        "Edwards was sick yesterday",
        [
            {'start': 16, 'definition': u'affected by an impairment of normal physical or mental function',
             'correct': u'sick', 'text': 'sck'},
            {'start': 8, 'definition': None, 'correct': u'was', 'text': 'will be'}
        ]
    ),
    (
        "Edwards was sick yesterday.",
        "Edwards was sick yesterday.",
        []
    ),
    (
        "",
        "",
        []
    )
])
def test_gingerit(text, expected, corrections):
    output = GingerIt().parse(text)

    assert output["result"] == expected
    assert output["corrections"] == corrections
