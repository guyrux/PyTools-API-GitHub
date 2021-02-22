from libpythonpro_github.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Gustavo')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Gustavo'), Usuario(nome='Cintia')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
