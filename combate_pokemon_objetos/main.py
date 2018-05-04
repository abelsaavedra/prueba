from combate_pokemon_objetos.pokemon import Pikachu
from combate_pokemon_objetos.pokemon import Squirtle
from combate_pokemon_objetos.pokemon import Charmander
from combate_pokemon_objetos.pokemon import Bulbasaur


def main():
    pikachu = Pikachu()

    pokemon_elegido = input("¿Contra qué Pokemon quieres combatir? (Squirtle / Charmander / Bulbasaur): ")
    if pokemon_elegido == "Squirtle":
        enemigo = Squirtle()

    elif pokemon_elegido == "Charmander":
        enemigo = Charmander()

    elif pokemon_elegido == "Bulbasaur":
        enemigo = Bulbasaur()

    while True:
        tipo = input("¿Qué ataque quieres hacer? (Básico/Chispazo/Bola voltio) ")
        pikachu.atacar(enemigo, tipo)
        if enemigo.get_puntos_vida() <= 0:
            print("Pikachu ha ganado!")
            break
        enemigo.atacar(pikachu)
        if pikachu.get_puntos_vida() <= 0:
            print("Pikachu ha perdido!")
            break


if __name__ == '__main__':
    main()
