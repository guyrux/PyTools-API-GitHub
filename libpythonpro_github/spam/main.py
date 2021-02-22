class EnviadorDeSpam():

    def __init__(self, sessao, enviador) -> None:
        self.sessao = sessao
        self.enviador = enviador

    def envia_emails(self, rementente, assunto, corpo):
        pass