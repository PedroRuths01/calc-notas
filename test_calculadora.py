from calculadora import calcula_media

def test_media_simples():
    n1, n2, n3 = 8.0, 7.0, 9.0

    resultado = calcula_media(n1, n2, n3)

    assert resultado == 8.25