from pasta.restaurante import Restaurante

restaurante_espanhol = Restaurante('Por dios', 'Espanhol')
restaurante_japones = Restaurante('japa food', 'Japones')
Restaurante_italiano = Restaurante('si mangia bene', 'Italiano')

restaurante_espanhol.receber_avaliacao('renata', 9.9)
restaurante_espanhol.receber_avaliacao('renata', 8)

restaurante_japones.receber_avaliacao('Lais', 8)
restaurante_japones.receber_avaliacao('Lais', 4.5)

Restaurante_italiano.receber_avaliacao('Diego', 10)
Restaurante_italiano.receber_avaliacao('Diego', 7)


restaurante_espanhol.alternar_estado()


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()