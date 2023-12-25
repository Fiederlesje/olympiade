import pytest
from src import A2


@pytest.mark.parametrize("tekst, verwachting",
                                        [
                                                ("LETTERTELLERTEKST", "ET"),
                                                ("AGBDEFC", "ABCDEFG"),
                                                ("ALGEBRA", "A")
                                        ])

def test_A2(tekst: str, verwachting: str):
    assert A2.meest_voorkomende_letters(tekst) == verwachting
