def calcula_media (n1 , n2 , n3 ):
    return ( n1 + n2 + 2 * n3 ) / 4

def _valida(nota):
    if nota < 0 or nota > 10:
        raise ValueError(f"Nota invalida: {nota}")


def calcula_media(n1, n2, n3):
    for n in (n1, n2, n3):
        _valida(n)

    return (n1 + n2 + 2 * n3) / 4

def situacao(media):
    if media >= 7:
        return "aprovado"

    if media >= 4:
        return "recuperacao"

    return "reprovado"
