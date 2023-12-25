import pytest
from src import A1


@pytest.mark.parametrize("opdracht, verwachting",
                                        [
                                                ("NOZW", 0),
                                                ("NONO", 4),
                                                ("ZWNNNOONZWWZ", 2),
                                                ("NNNNNNN", 7)
                                        ])

def test_A1(opdracht: str, verwachting: int):
    assert A1.bereken_minimaal_aantal_stappen(opdracht) == verwachting
