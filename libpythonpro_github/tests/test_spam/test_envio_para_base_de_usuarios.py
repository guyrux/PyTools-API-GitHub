from libpythonpro_github.spam.enviador_de_email import Enviador
from libpythonpro_github.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.envia_emails('guyrux@gmail.com', 'Curso Python Pro', 'Testando essa parte do codigo')
