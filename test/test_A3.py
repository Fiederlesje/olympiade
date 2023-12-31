import pytest
from src import A3


@pytest.mark.parametrize("grondtal_bron, getal_bron, verwachting",
                                        [
                                                (10, '3', 3),
                                                (2, '11', 3),
                                                (36, 'z', 35),
                                                (10, '132', 132)
                                        ])

def test_A3_decimaal(grondtal_bron: int, getal_bron: str, verwachting):
    assert A3.bereken_getal_decimaal(grondtal_bron, getal_bron) == verwachting


@pytest.mark.parametrize("modulus, verwachting",
                                        [
                                                (13, 'd'),
                                                (3, '3')
                                        ])

def test_A3_letters(modulus: int, verwachting):
    assert A3.maak_letters(modulus) == verwachting


@pytest.mark.parametrize("getal_decimaal, grondtal_doel, verwachting",
                                        [
                                                (3, 2, '11'),
                                                (132, 17, '7d')
                                        ])

def test_A3_getal_doel(getal_decimaal: int, grondtal_doel: int, verwachting):
    assert A3.bereken_getal_doel(getal_decimaal, grondtal_doel) == verwachting