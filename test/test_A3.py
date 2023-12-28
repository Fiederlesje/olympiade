import pytest
from src import A3


@pytest.mark.parametrize("grondtal_bron, getal_bron, grondtal_doel, verwachting",
                                        [
                                                (6, '132', 10, '56'),
                                                (10, '132', 17,'7d')
                                                (36, 'z', 2,'100011')
                                        ])

def test_A3(grondtal_bron: int, getal_bron: str, grondtal_doel: str, verwachting):
    assert A3.bereken_getal_doel(grondtal_bron, getal_bron, grondtal_doel) == verwachting