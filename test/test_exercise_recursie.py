import pytest
from src import excercise_recusie


@pytest.mark.parametrize("s, verwachting",
                                        [
                                                ('outlul', 6),
                                                ('prik', 4),
                                                ('kut', 3)
                                        ])

def test_len_str(s: str, verwachting):
    assert excercise_recusie.bepaal_len_str(s) == verwachting


