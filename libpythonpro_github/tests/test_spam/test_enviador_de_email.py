from libpythonpro_github.spam.enviador_de_email import Enviador, EmailInvalido
import pytest


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('remetente', ['', 'foo'])
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(
            remetente,
            'gustavo.suto@live.com',
            'Curso Pytohn Pro',
            'Usando TDD e baby steps no desenvolvimento de soluções python.'
            )
        assert remetente in resultado
