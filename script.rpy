
# personagens
define p = Character("Pisquinha")
define h = Character("Husk")
define k = Character("Kai")


# o Jogo começa aqui

label start:

    scene cena1

    "Dois irmãos Pisquinha e Husk lutam pela liderança do clã dos lobos"

    p "Não quero brigar com você irmão"

    p "Esta luta não faz sentido pra mim"

    show husk

    h "Deixa de conversa mole Pisquinha"

    h "Isto pra mim tem outro nome"

    h "Covardia!"  

    hide husk

    "Pisquinha deve enfrentar o irmão Husk?"

menu:

    "Sim":
        jump game

    "Não":
        jump book

label game:

    p "Se não outra escolha, eu estou pronto irmão"

    h "Farei o que deve ser feito"

    jump marry

label book:

    h "Você não tem escolha, lembre-se a força vem do seu interior"

    p "Eu não queria, mas é o unico jeito"

    jump marry

label marry:

    "Os irmão batalham"  

    return
