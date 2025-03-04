import os
import random

class InvalidOption(Exception):
    """
        Excetion for invalid option
    """
    def __init__(self,message=f"""
                The selected option is invalid
                A opção selecionada é inválida
        """):
        self.message = message
    def __str__(self):
        return self.message

def print_color(message, cor):
    colors = {
        "red": "\033[91m",
        "white": "\033[97m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m"
    }
    reset = "\033[0m"  # reset color

    if cor in colors:
        print(f"{colors[cor]}{message}{reset}")
    else:
        print(message)  # Caso a cor não seja reconhecida, imprime normalmente

def show_info():
    exit = True
    while exit:
        os.system("clear")
        if language == 1:
            print(f"""
                Lizard spock is a free expansion pack for the much-loved game of rock paper scissors. 
                The additional characters were added by Sam Kass and Karen Bryla before being adopted, 
                reordered, and overpopularised by The Big Bang Theory.
            """)
        exit = input("""
                Press ENTER to exit""")
    else:
        ...

def show_rules():
    exit = True
    while exit:
        os.system("clear")
        if language == 1:
            print(f"""
            Scissors cuts paper. 
            Paper covers rock. 
            Rock crushes lizard. 
            Lizard poisons Spock. 
            Spock smashes scissors. 
            Scissors decapitates lizard. 
            Lizard eats paper. 
            Paper disproves Spock. 
            Spock vaporizes rock. 
            Rock crushes scissors.
            """)
            exit = input("""
            Press ENTER to exit
            """)
        else:
            ...
    

def play():
    if language == 2:
        print("""
            Faça sua jogada:

                Pedra - 1
                Papel - 2
                Tesoura - 3 
                Lagarto - 4
                Spock - 5
        """)
        # move = int(input("""
        #         """))
    else:
        print("""
            Make Your Move:

                Rock - 1
                Papper - 2
                Scissors - 3
                Lizard - 4
                Spock - 5
        """)
        move = int(input("""
                """))
    
    return move

def get_option():
    os.system("clear")
    if language == 1:
        # os.system("clear")
        print("""
                What you want to do?
                Show info - 1
                Show the Rules - 2
                Play a Game - 3
        """)
        option = int(input("""
                """))
    else:
        # os.system("clear")
        print("""
                O que desejas fazer?
                Mostrar informações - 1
                Mostrar as Regras - 2
                Jogar um Jogo - 3
        """)
        option = int(input("""
                """))
    return option


def judge(player):
    # Antes de mostar a jogada do bot fazer um contdown até 3 mostrando na tela de maneira grande
    # Para mostar na tela trazer uma arte ASCII assim https://www.reddit.com/r/Python/comments/y6gn1g/rock_paper_scissors_game_in_the_terminal_with/?rdt=41443 
    if language == 1:
        plays = {
            1:"Rock",
            2:"Papper",
            3:"Scissors",
            4:"Lizard",
            5:"Spock"
        }
    else:
        plays = {
            1:"Pedra",
            2:"Papel",
            3:"Tesoura",
            4:"Lagarto",
            5:"Spock"
        }

    bot_play = language[random.randrange(1,6)]

    if bot_play == player:
        print("Empate!")
        #return

    elif (bot_play == 3 and player == 2) or   \
         (bot_play == 2 and player == 1) or   \
         (bot_play == 1 and player == 4) or   \
         (bot_play == 4 and player == 5) or   \
         (bot_play == 5 and player == 3) or   \
         (bot_play == 3 and player == 4) or   \
         (bot_play == 4 and player == 2) or   \
         (bot_play == 2 and player == 5) or   \
         (bot_play == 5 and player == 1) or   \
         (bot_play == 1 and player == 3):      
        
        print("\033[91mYOU LOSE!\033[0m")  # Texto vermelho

        """
            Jogadas do ELIF:

                1 .Tesoura corta papel
                2 .Papel cobre pedra
                3 .Pedra esmaga lagarto
                4 .Lagarto envenena Spock
                5 .Spock esmaga tesoura
                6 .Tesoura decapita lagarto
                7 .Lagarto come papel
                8 .Papel refuta Spock
                9 .Spock vaporiza pedra
            10 .Pedra esmaga tesoura
        """

    else:
        print("\033[92mYOU WIN!\033[0m")   # Texto verde

    continuer = input("")


def select_language():
        print(""" 
                Pick Up a Language (1 - US)
                Escolha um Idioma (2 - PT-BR)    
            """)
        try:
            language = int(input(""))
            if language < 1 or language > 2:
                raise InvalidOption
        except InvalidOption as e:
            os.system("clear")
            print(f"{str(e)}")
            continuer = input("""
                Press ENTER to continue""" if language == 1 else
                """
                Pressione ENTER para continuar
                """)
            return None
        except ValueError:
            os.system("clear")
            print(""" Tente Novamente """)
            return None

        return language

language = None
player_wins = False

while True:
    move = None
    option = None
    if language is None:
        os.system("clear")
        language = select_language()
        if language is None:
            continue
    
    
    try:
        option = get_option()
        if option < 1 or option > 3:
            raise InvalidOption("""
                Por favor, escolha uma opção entre 1 e 3""" if language == 2 else """
                Please, select a option between 1 and 3""")
    except InvalidOption as e:
        os.system("clear")
        print(f"{str(e)}")
        # option = int(input(""))
        continuer = input("""
                Press ENTER to continue""" if language == 1 else
                """
                Pressione ENTER para continuar
                """)
        continue
    except ValueError:
        os.system("clear")
        print("Tente novamente")
        continuer = input("""
                Press ENTER to continue""" if language == 1 else
                """
                Pressione ENTER para continuar
                """)
        continue

    match option:
        case 1:
            show_info()
            continue
        case 2:
            show_rules()
            continue        
        case 3:    
            play()
            continue

    move = play()
    judge(move)
    # print(move)