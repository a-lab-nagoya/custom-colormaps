import demonstration as demo


def test_author():
    assert demo.__author__ == "Rin Yamada"


def test_version():
    assert demo.__version__ == "0.2.0"
