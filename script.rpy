define l = Character("Lucky")
define i = Character("Lily")
define r = Character("Rose")
define p = Character("Peter")
define g = Character("Gangue")

# The game starts here.
```
Capítulo 1
```
label start:
    
    play music "audio/inicio.mp3"

    scene flor
    with fade

    show lucky at center

    ""

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
    show lucky at left

menu:

    "Sim":
        jump sim

    "Não":
        jump nao

label sim:
    hide lucky
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
    hide lucky
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
    "O horário de aula acabou, então Lucky decidiu voltar para casa, e usou a floresta como um atalho"


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
    r "Tenho que ir lá na escola falar desse problema"
    r "Só quero que você saiba que eu vou estar sempre aqui e que pode contar comigo"

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
    l "Pode ficar despreocupada"

    hide lucky_serio2
    jump alternativo

label alternativo:
    show rose2 at left 
    show lucky2 at right

    l "Agora vou relaxar um pouco"
    
    r "Que tal um passeio? O dia está tão lindo"

    l "Pode ser"
    l "Acho que vou explorar a floresta"
    l "Tem lugares lá que não conheço"

    r "Tá bom filho, só toma cuidado lá fora"

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

    l "Vim relaxar um pouco e você?"

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

    l "Que legal! Também estudo de manhã, acho que estudamos na mesma escola"

    i "Sim"
    i "Você veio aproveitar esse sol também?"

    l "Pra falar a verdade, estou aqui para esquecer os problemas"
    l "A vida na escola não está muito fácil"

    i "Ué, o que aconteceu?"

    l "Tem um garoto que faz bullying comigo"
    l "Ele fica me incomodando junto com os amigos dele"
    l "E isso me deixa muito triste"

    i "Te entendo" 
    i "É horrivel como algumas pessoas se sentem no direito de fazer isso com os outros"

    l "Sim, o pior é que eles se sentem bem em ter esse comportamento"

    i "Sim, mas você já falou isso com alguém?" 

    l "Sim, com a minha mãe"  
    l "Ela me ajudou e disse que vai falar com a escola"

    i "Ah, é sempre bom ter alguém para conversar"

    l "Pois é, ajuda a se livrar um pouco desse peso"

    i "Mas você falou com o seus professores?"
    i "É sempre bom avisar eles"

    l "Sei que é bom, mas não falei"
    l "Tenho medo de falar e piorar as coisas"
    l "E se eles começarem a me zoar ainda mais?! E se começarem a me bater?!"
    
    i "Sei que você tem motivo para ter medo, mas se você não contar pode ser pior"

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
    l "Sabe às vezes, me sinto tão inseguro que acabo acreditando nas coisas ruins que ele diz sobre mim"

    i "Eu sei, mas você sabe que não é"
    i "Mas saiba que a coragem vem de dentro e temos que apenas absorver coisas boas, as ruins não agregam em nada"

    l "Tem razão, daqui em diante vou seguir esse conselho"
    l "Agora tenho que ir"

    i "Ok"
    i "Tchau, até logo"

    l "Tchau, até"

    "Lucky ficou contente e foi para casa"

    hide lily2
    hide lucky2
    jump festa

label pessimo:

    show lily2 at left
    show lucky2 at right

    l "Agradeço a oferta, mas vou seguindo meu caminho sozinho"

    i "Tudo bem, então nos vemos por aí"
    i "Tchau"

    l "Tchau"

    hide lily2
    hide lucky2

    "Lucky se sentiu um pouco perdido e a solidão o deixou mais reflexivo"
    jump continuacao

label festa:
    scene festa
    "NOVO DIA"
    "Lucky foi para a escola como de costume, mas esse seria um grande dia, era a festa de outono que é comemorada todos os anos na escola junto com os pais"
    "Lucky estava nervoso para sua primeira festa de outono, até que avistou Lily e foi conversar com ela"

    show lily2 at left
    show lucky2 at right

    l "Oi Lily, que bom que você veio"
    i "Oi Lucky, como eu poderia deixar de vir nessa festa maneira?"   
 
    hide lily2
    hide lucky2

    "Ambos riram e Lily foi buscar algo para eles comerem. Peter percebeu que Lucky estava sozinho e decidiu ir lá falar com ele"

    show peter2 at left
    show luckytriste2 at right

    p "Olha só se não é o azarado do Lucky de novo!"
    p "Não sei pra que veio, sua presença nem é importante mesmo"

    hide peter2
    hide luckytriste2
    show luckytriste 

    "Lucky ficou cabisbaixo e decidiu ir embora. Quando já estava indo, Lily o viu"

    hide luckytriste
    show lily2 at left
    show luckytriste2 at right

    i "Lucky! Lucky! Pra onde você vai?!"

    l "Estou indo embora"
    l "Peter tem razão, minha presença aqui não é importante"

    i "É claro que é"
    i "E toda aquela nossa conversa sobre não acreditar no que ele diz sobre você?"

    l "Sei que você tem razão, mas na hora em que ele veio me irritar, travei e a única coisa que pensei foi em fugir, então corri"

    i "Lembra do que eu falei sobre a coragem? Que ela vem de dentro?"

    l "Sim"

    i "Então volta lá e ponha o Peter em seu lugar"

    hide lily2
    hide luckytriste2

    "Lucky deve responder a Peter?"

menu:
    "Sim":
        jump comemoracao

    "Não":
        jump festival

label comemoracao:

    show lucky_serio at left
    show peter_rindo at right
    l "Ei! Peter!"

    p "Ué, o covarde fujão decidiu voltar, foi? hahahahahahahaha"

    l "Respondendo a sua pergunta: não, eu não sou azarado, sou apenas um duende bondoso e corajoso"

    p "Hahahahahahahaahaha"
    p "Não tá falando sério, né?"
    p "Essa coisa mais tosca que eu já ouvi"

    l "Você só está falando isso, porque não se sente bem consigo mesmo e desconta a sua frustação nos outros"

    hide lucky_serio
    hide peter_rindo

    "Peter percebeu que suas provocações não estão funcionando mais, então ficou calado e revoltado e foi embora"
    "Lily viu tudo o que tinha acontecido de longe e foi até Lucky"

    show lily2 at left
    show lucky2 at right
    
    i "Estou admirada com sua coragem!"
    i "Parabéns por ter enfrentado Peter"

    l "Obrigado, não teria enfrentado ele se não fosse você"

    i "A verdade é que você sempre teve essa coragem, mas nunca se permitiu acessá-la"

    l "Tem razão"

    hide lily2
    hide lucky2

    "Rose que estava na festa conversando com os outros pais, viu Lucky e foi atrás dele"

    show rose2 at left
    show lucky2 at right

    r "Oi filho, está tudo bem?"

    l "Oi mãe, está sim"
    l "A senhora não sabe o que aconteceu"

    r "O que?"

    l "Finalmente enfrentei o Peter e o coloquei no lugar dele, agora ele não vai mais me incomodar"

    r "Que bom filho, agora você vai ter paz!"
    
    hide rose2
    hide lucky2
 

label festival:
    "Lucky com medo, não respondeu Peter, mas Lily decidiu tomar uma atitude"

    show lily2 at left 
    show peter at right

    i "Peter!"

    p "O covarde chamou reforços foi? Hahahahahahahahaha"

    i "Ele não é um covarde!"
    i "Você deveria se tocar e ver que o bullying que você pratica é errado"
    i "A real é que você desconta sua raiva nos outros em vez de tratá-la. Deveria olhar para si mesmo e procurar mudar!"

    hide lily2
    hide peter

    "Lily deixou Peter irritado e foi embora para se encontrar com Lucky"

    show lily2 at left
    show lucky2 at right

    l "Obrigado por ter me defendido"

    i "Não foi nada, saiba que sempre estarei aqui pra te defender"
    i "Afinal, é isso que os amigos fazem"

    hide lily2
    hide lucky2
    show lucky at left
    show lily at center
    show rose at right

    "Felizes, Lucky e Lily se encontram com Rose e todos curtem as festa juntos"

    hide lucky
    hide lily
    hide rose
    
label continuacao:
    "NOVO DIA"
    "Lucky foi para a escola como de costume, mas esse seria um grande dia, era a festa de outono que é comemorada todos os anos na escola junto com os pais"
    "Peter percebeu que Lucky estava sozinho e foi até ele"

    show peter2 at left
    show luckytriste2 at right

    p "Olha só se não é o azarado de novo!"
    p "Não sei pra que veio, sua presença nem é importante mesmo"

    hide peter2
    hide luckytriste2

    "Lucky deve responder a Peter?"

menu:
    "Sim":
        jump responder

    "Não":
        jump ignorar

label responder:
    show lucky_serio at left
    show peter at right

    l "Quer saber? Já cansei das suas brincadeiras de mal gosto, me deixa
em paz!"

    p "Ui, estou morrendo de medo hahahahahahahaha"
    p "Fala sério? Acha mesmo que vou te deixar em paz? Nem você acredita
nisso"

    l "Você só me irrita porque desconta sua frustração nos outros!"
    l "Quer saber: vou embora e é melhor me deixar quieto!"

    hide lucky_serio
    hide peter

    "Lucky decidiu ser feliz e foi curtir a festa"
    
label ignorar:
    "Lucky, triste, saiu correndo de medo"

    




 