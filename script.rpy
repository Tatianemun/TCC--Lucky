define l = Character("Lucky")
define i = Character("Lily")
define r = Character("Rose")
define p = Character("Peter")
define a = Character("Ravi")
define g = Character("Gangue")

# The game starts here.
```
Capítulo 1
```
label start:
    
    play music "audio/inicio.mp3"

    scene flor
    with fade

    "Em um vilarejo encantado, Lucky, um pequeno duende, enfrenta dificuldades na escola devido ao bullying de Peter, um duende mais velho e maldoso."

    "No pátio, Lucky estava sozinho quando Peter apareceu, cercado por colegas"   
    stop music 
    scene patio
    show lucky at left
    show peter at center
    show gangue at right


    p "Olha só quem está aqui, o azarado do Lucky!"
    
    hide lucky
    show lucky_tenso2 at left

    p "E aí parceiro, tá querendo problemas?"

    l "Eu...Eu..."

    p "Olha só gente"
    p "Nem conseguir completar uma frase ele consegue"

    hide lucky_tenso2
    show luckytriste at left

    g "hahahahahahahahahaha"


    hide luckytriste
    hide peter
    hide gangue
    "Você acha que Lucky deve confrontar Peter?"

menu:

    "Sim":
        jump sim

    "Não":
        jump nao

label sim:
    show lucky_serio at left
    show peter at center
    show gangue at right

    l "Quer saber, já estou cansado dessas suas provocações"
    l "Pare de querer bancar o valentão!"

    hide peter
    show peter_rindo
    p "He, he, he olha só rapazes, o Lucky ta se sentindo o tal"
    p "Virou piadista agora?"
    p "Se não quer ser motivo de piada, é melhor sair da minha frente!"

    hide lucky_serio
    hide peter_rindo
    hide gangue


    "Lucky ficou abalado, mas um pouco mais confiante."
    jump principal

label nao:
    show lucky_tenso at left
    show peter at center
    show gangue at right

    p "Ih, olha lá!"
    p "O covarde decidiu fugir"

    hide lucky_tenso
    hide peter

    show peter_rindo2 at left
    p "Aprendeu rapazes? É assim que temos que tratar esse tipo de gente"

    hide peter_rindo2
    hide gangue
    jump principal

label principal:
    scene flor
    show luckytriste at center
    "Lucky decidiu voltar para casa, e usou a floresta como um atalho"


    scene casa
    show rose2 at left 
    show luckytriste2 at right

    "Ao chegar em casa, Lucky se depara com sua mãe"
    r "Ei, querido, você parece preocupado"
    r "O que aconteceu?"

    l "Nada mãe"
    l "Não precisa ficar preocupada"

    r "Tem certeza?"
    r "Parece ser algo a mais"

    

    hide rose2
    hide luckytriste2

    "Lucky deve desabafar com sua mãe?"

menu:

    "Sim":
        jump bom

    "Não":
        jump ruim

label bom:

    show rose2 at left 
    show luckytriste2 at right

    l "Na verdade, aconteceu uma coisa"
    l "É o Peter, ele sempre está me zoando"
    l "Hoje estava no pátio e ele veio me irritar, junto com os amigos dele"

    r "Ele sempre faz isso?"

    l "Sim"
    l "Já faz um tempo"

    r "Filho, devia ter me contado desde quando ele te incomodou da primeira vez"
    r "É inadmissível esse comportamento do Peter"
    r "Tenho ir lá na escola falar desse problema"
    r "Só quero que você saiba que eu vou estar sempre aqui e pode contar comigo"

    hide luckytriste2
    show lucky2 at right
    l "Tá bom mãe, obrigado"

    r "De nada querido"
    r "Espero que Peter pare de vez de te incomodar"

    l "Também espero"

    hide lucky2
    jump alternativo


label ruim:

    show rose2 at left 
    show lucky_serio2 at right

    l "Não, não é"
    l "Fica despreocupada"

    hide lucky_serio2
    jump alternativo

label alternativo:
    show rose2 at left 
    show lucky2 at right

    l "Agora vou relaxar um pouco"
    
    r "Que tal um passeio?"

    l "Pode ser"
    l "Acho que vou explorar a floresta"

    r "Tá bom filho, toma cuidado lá fora"

    l "Ok, pode deixar"
    l "Tchau"

    r "Tchau"

    hide rose2
    hide luckytriste2

    scene flor
    "Ao explorar a floresta, Lucky encontra uma duende alegre"

    show lily2 at left
    show lucky2 at right

    i "Oi! Eu sou a Lily e você?"

    l "Oi, sou o Lucky"

    i "O que te trouxe até aqui?"

    l "Vim relaxar um pouco"

    l "E você?"

    i "Estou cuidando dos animais"
    i "Gosto de cuidar deles, dá uma paz"

    l "Parece divertido"

    i "E realmente é"
    i "Por que você não me ajuda?"
    i "Assim podemos aproveitar o tempo e conversar"
    
    hide lily2
    hide lucky2
    
    "Lucky deve ajudar Lily com os animais?"

menu:

    "Sim":
        jump otimo

    "Não":
        jump pessimo

label otimo:

    show lily2 at left
    show lucky2 at right

    l "Claro"
    l "Até acho ótimo para relaxar um pouco"
    l "E olha que realmente estou precisando"

    i "hahahaha você é engraçado"
    i "Mora aqui perto?"

    l "Sim e você?"

    i "Também"
    i "Estudo de manhã, aí aproveitei essa tarde ensolarada e vim aqui"

    l "Que legal! Também estudo de manhã"

    i "Veio aproveitar esse sol também?"

    l "Na verdade, estou aqui para esquecer os problemas"
    l "A vida na escola não está muito fácil"

    i "Ué, o que aconteceu?"

    l "Tem um garoto que faz bullying comigo"
    l "Ele fica me incomodando junto com os amigos dele"
    l "E isso me deixa muito triste"

    i "Te entendo" 
    i "É horrivel como algumas pessoas se sentem no direito de fazer isso com os outros"

    l "Sim, o pior é que eles se sentem bem em ter esse comportamento"

    i "Sim"
    i "Você já falou isso com alguém?" 

    l "Sim, com a minha mãe"  
    l "Ela me ajudou e disse que vai falar com a escola"

    i "Ah, é sempre bom ter alguém para conversar"

    l "Pois é, ajuda a se livrar um pouco desse peso"

    i "Mas você falou com o seus professores?"
    i "É sempre bom avisar eles"

    l "Sei que é bom, mas não falei"
    l "Tenho medo de falar e piorar as coisas"
    l "E se eles começarem a me zoar ainda mais?! E se começarem a me bater?!"
    
    i "Sei que você tem motivo para ter medo, mas se você não contar, pode ser pior"

    l "Sei que você está certa, mas fico pensando que se eu falar, vão me achar fraco"

    i "Não, Lucky!"
    i "Pedir ajuda não é sinal de fraqueza, é de coragem"
    i "Olha, você não está sozinho. Sua mãe está do seu lado e agora, eu também"

    l "Sabe, gostaria de me expressar melhor"

    i "Te entendo, tive esse problema e o que me ajudou foi o teatro, acho que pode te ajudar também"

    l "Teatro?"

    i "Sim, ele me ajudou a desenvolver a autoestima e a comunicação"

    l "Ah, então vou pensar nisso, talvez me juntar a um grupo de teatro me faça bem"

    i "Com certeza!"
    i "Com a autoestima, os comentários do Peter não vão te afetar"

    l "Verdade"
    l "Às vezes, me sinto tão inseguro que acabo acreditando nas coisas ruins que ele fala de mim"

    i "Eu sei, mas você sabe que não é"
    i "Mas saiba que a coragem vem de dentro"

    hide lily2
    hide lucky2
    jump continuacao

label pessimo:

    show lily2 at left
    show lucky2 at right

    l "Agradeço a oferta, mas vou seguindo meu caminho sozinho"

    i "Tudo bem, então nos vemos por aí"
    i "Tchau"

    l "Tchau"

    hide lily2
    hide lucky2

    "Lucky se sente um pouco perdido e a solidão o deixa mais reflexivo"
    jump continuacao

```
Capítulo 2
```

```
No outro dia, ocorreu a festa anual de outono da escola, uma festa onde são coroados o rei e rainha.
Lucky estava nervoso para sua primeira festa de outono, e com a ajuda da Lily (ou por conta própria, dependendo da escolha anterior)
```
label continuacao:
    scene festa
    show peter2 at left
    show lucky at right
    "Durante a festa, Peter tenta zombar de Lucky novamente."

    hide peter2
    hide lucky

    show peter2 at left
    show luckytriste2 at right

    p "Olha só, se não é o azarado do Lucky de novo!"

    l "Me deixa em paz!"

    p "Tá levantando a voz pra mim?!"
    p "O que? Resolveu ser corajoso agora?!"


    hide peter2
    hide luckytriste2

    "Lucky deve responder a Peter?"

menu:

    "Sim":
        jump confiante 

    "Não":
        jump silencio

label confiante:
    show lucky at center
    "Lucky se levanta com confiança e responde que ele não é azarado, mas sim um duende bondoso e corajoso. Os outros duendes começam a admirar sua atitude, e Peter percebe que suas provocações não estão funcionando mais"
    jump finalfeliz

label silencio:
    "Lucky permanece em silêncio, mas Lily e Ravi, que estão com ele, o defendem. Peter se surpreende com a solidariedade dos amigos de Lucky e começa a perceber que está isolado em suas provocações"
    jump finaltriste

label finalfeliz:
    "Peter, tocado pela coragem e bondade de Lucky, se aproxima com sinceridade"

    p "Desculpe por ter sido tão cruel"

    p "Eu não devia ter te tratado assim"

    p "Me desculpe pelas minhas atitudes"

    l "Tudo bem, podemos começar de novo?"

    p "Claro"

    "Peter, agora amigo, se junta a Lucky, Lily e Ravi. Eles brincam juntos na floresta, e Lucky sente que encontrou seu valor e seu lugar no mundo, transformando sua situação com coragem e bondade"

label finaltriste:
    "Peter continua sendo rude e Lucky percebe que não precisa de aprovação de Peter para ser feliz"

    
    "Lucky, Lily e Ravi saem juntos, deixando Peter para trás. Lucky percebe que sua confiança não depende da opinião dos outros, mas sim de sua própria força interior"

    return
