# RegEx

Estudo feito sobre o capitulo 7 do livro *Automate the Boring Stuff with Python, 2nd Edition Practical Programming for Total Beginners*

# Padrões correspondentes com expressões regulares(RegEx)

Conhecer RegEx pode ser a diferença entre resolver um problema
em 3 passos ou resolver em 3000 passos.

## Achando padrões no texto com expressões regulares

\d -> significa um digito, um número de 0 a 9.

Para procurar um número de telefone o padrão usado seria :\d\d\d\d\d-\d\d\d\d, porém existe um jeito mais sofisticado para procurar esse mesmo padrão. 
Por exemplo, adicionando o numero 5 dentro de chaves({5}) depois do padrão é a mesma coisa que dizer, "ache esse padrão 3 vezes". 
Assim aquele mesmo padrão ficaria assim: \d{5}-\d{4}.


### Criando objetos regex

Primeiro importe o modulo re python.
```py
>>> import re
```

Passe uma string com o padrão que você deseja buscar para re.compile() que vai retornar um objeto RegEx.
Assim a variavel criada vai conter o objeto Regex.
```py
>>> numeroTelRegex = re.compile('\d\d\d\d\d-\d\d\d\d')
```

### Correspondentes com objeto regex

O metodo search() pesquisa na string que foi passada para ele o padrão estabelecido. Caso ele encontre o padrão ele vai retornar o objeto Match, que tem o método group() quer vai retornar o objeto correspondente.
```py
>>> numeroTelRegex = re.compile('\d\d\d\d\d-\d\d\d\d')
>>> num = numeroTelRegex.search('Meu numero é 99999-9999')
>>> print(f'Numero achado: {num.group()}') # 99999-9999
```

## Encontrando mais padrões com expressões regulares

Agora que ja passamos pelo básico, vamos tentar algo mais poderoso ainda.

### Agrupando com parenteses

Agora vamos separa a área do telefone do resto do número. Usando o método group() para pegar o objeto correspondente em um único grupo. O primeiro parentese é o primeiro o grupo. O segundo vai ser o segundo grupo. E para recuperar cada grupo separadamente passamos os números 1 ou 2 dentro do parentese do metodo group().

```py
>>> numeroTelRegex = re.compile('(\d\d)-(\d\d\d\d\d-\d\d\d\d)')
>>> num = numeroTelRegex.search('Meu numero é 31-99999-9999')
>>> num.group(1)
'31'
>>> num.group(2)
'99999-9999'
>>> num.group()
'31-99999-9999'
```

Caso você queira receber uma tupla com todo conteudo do grupo de uma vez use o metodo groups() - note o plural no final
```py
>>> num.groups()
('31','99999-9999')
>>> area, numero = num.groups()
```

Os parenteses tem um função especial quando passamos o padrão regex a ser encontrado. Então caso você queira encontra o parenteses dentro da expressão, será necessário um caracter de escape como esse: \ . Assim o parenteses vai passar para ser encontrado dentro do padrão:
```py
>>> numeroTelRegex = re.compile('(\(\d\d\)) (\d\d\d-\d\d\d\d)')
>>> num = phoneNumRegex.search('Meu número é (31) 99999-9999.')
>>> num.group(1)
'(31)'
>>> num.group(2)
'99999-9999'
```

### Econtrando multiplos grupos com o Pipe(|)

O caracter | é chamado de *pipe* Por exemplo, a expressão regular 'Batman|Tina Fey' vai buscar Batman ou Tina Fey. Quando os dois estiverem dentro do texto onde estamos procurando o **primeiro** a ser encontrado vai ser o objeto que vai ser retornado.
```py
>>> heroiRegex = re.compile ('Batman|Tina Fey')
>>> mo1 = heroRegex.search('Batman and Tina Fey')
>>> mo1.group()
'Batman'
>>> mo2 = heroRegex.search('Tina Fey and Batman')
>>> mo2.group()
'Tina Fey'
```

O *pipe* pode ser usado tambem para encontra um dentre varios padrões regex. Por exemplo você quer encontrar qualquer um desses textos 'Batman', 'Batmobile', 'Batcopter', and 'Batbat'. Assim como todas essas string começam com Bat você so precisa especificar o prefixo uma vez e usar o parenteses no resto juntamente com o *pipe*.
```py
>>> batRegex = re.compile('Bat(man|mobile|copter|bat)')
>>> mo = batRegex.search('Batmobile lost a wheel')
>>> mo.group()
'Batmobile'
>>> mo.group(1)
'mobile'
```

### Correspondente opcional com o ponto de interrogação

As vezes vai existir um padrão que deve ser capturado mas opcionalmente. Ou seja o regex deve encontrar um padrão mesmo que aquele texto não esteja lá.
```py
>>> batRegex = re.compile('Bat(wo)?man')
>>> mo1 = batRegex.search('The Adventures of Batman')
>>> mo1.group()
'Batman'
>>> mo2 = batRegex.search('The Adventures of Batwoman')
>>> mo2.group()
'Batwoman'
```
A parte (wo)? da expressão regular significa que esse padrão wo é um grupo opcional. O regex vai capturar textos que não tenha nenhuma instancia desse padrão ou que tenha uma.

### Encontrando zero ou mais com o asterisco

O * siginifica "encontre 0 ou mais"
```py
>>> batRegex = re.compile('Bat(wo)*man')
>>> mo1 = batRegex.search('The Adventures of Batman')
>>> mo1.group()
'Batman'
>>> mo2 = batRegex.search('The Adventures of Batwoman')
>>> mo2.group()
'Batwoman'
>>> mo3 = batRegex.search('The Adventures of Batwowowowoman')
>>> mo3.group()
'Batwowowowoman'
```
No 'Batman' o (wo)* parte do regex encontrou 0 instancias do wo, em 'Batwoman' o (wo)*  encontrou uma instancia, e no 'Batwowowowowoman' o (wo)* encontrou quatro instancias.

### Encontrando um ou mais com o mais(+)

O + significa "encontre 1 ou mais"
```py
>>> batRegex = re.compile('Bat(wo)+man')
>>> mo1 = batRegex.search('The Adventures of Batwoman')
>>> mo1.group()
'Batwoman'
>>> mo2 = batRegex.search('The Adventures of Batwowowowoman')
>>> mo2.group()
'Batwowowowoman'
>>> mo3 = batRegex.search('The Adventures of Batman')
>>> mo3 == None
True
```

### Encontrando repetições especificas com as chaves

Caso você queira encontrar um grupo com um número específico de repetições utilize as chaves logo após o grupo em seu regex (Ha){3}, vai ser correspondente com 'HaHaHa' mas não com 'HaHa'. Ao inves de colocar um número específico você pode tambem um número minimo uma virgula e o numero maximo entre as chaves. Por exemplo (Ha){3,5} isso vai corresponder com 'HaHaHa', 'HaHaHaHa' e 'HaHaHaHaHa'. 
Você pode tambem colocar (Ha){3,} que vai procurar no minimo 3 e no maximo o tanto que tiver, outro jeito seria (Ha){,5} que vai procurar no minimo 0 e no maximo 5.
```py
>>> haRegex = re.compile('(Ha){3}')
>>> mo1 = haRegex.search('HaHaHa')
>>> mo1.group()
'HaHaHa'
>>> mo2 = haRegex.search('Ha')
>>> mo2 == None
True
```

## Correspondente ambicioso e não-ambicioso

Como vimos anteriormente (Ha){3,5} vai buscar no minimo 3 e no maximo 5 instancias de Ha na string. Por padrão essa expressão é ambiciosa ou seja vai retornar o maior valor possível. Para que você tenha um retorno não ambicioso ou seja o menor resultado capturado no fim da expressão coloque um ponto de interrogação assim será retornado o menor resultado encontrado.
```py
>>> haRegexAmbicioso = re.compile('(Ha){3,5}')
>>> mo1 = haRegexAmbicioso.search('HaHaHaHaHa')
>>> mo1.group()
'HaHaHaHaHa'
>>> haRegexNaoAmbicioso = re.compile('(Ha){3,5}?')
>>> mo2 = haRegexNaoAmbicioso.search('HaHaHaHaHa')
>>> mo2.group()
'HaHaHa'
```
Note que a interrogação pode ter dois significados no RegEx o primeiro para capturar menor valor possível/não-ambicioso ou para marcar grupos como opcionais

## O método findall()

O metodo findall() vai retornar todos os correspondentes encontrados em uma lista de strings. 
```py
>>> numeroTelRegex = re.compile('\d\d\d\d\d-\d\d\d\d') # has no groups
>>> numeroTelRegex.findall('Cell: 99999-9999 Work: 88888-8888')
['99999-9999', '88888-8888']
```

Se existir algum grupo na expressão regular o metodo findall() vai retornar uma lista de tuplas.
```py
>>> numeroTelRegex = re.compile('(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
>>> numeroTelRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
[('415', '555', '9999'), ('212', '555', '0000')]
```

## Classes de caracter

O \d é uma simplificação da expressão regular (0|1|2|3|4|5|6|7|8|9). Existe muitas outras seimplificações que vão ser descritas na tabela abaixo.

|Classes de caracter|Significado                                                        |
|-------------------|-------------------------------------------------------------------|
|\d                 |Qualquer digito numerico de 0 a 9                                  |
|\D                 |Qualquer caracter **não** numérico de 0 a 9                        |
|\w                 |Qualquer letra,numero ou underline.        |
|\W                 |Qualquer caracter não numerico, que não seja uma letra ou underline|
|\s                 |Qualquer espaço em branco                                          |
|\S                 |Qualquer coisa que não seja espaço em branco                       |

```py
>>> xmasRegex = re.compile('\d+\s\w+')
>>> xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7
swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6
geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
```
Neste RegEx \d+\s\w+ vai corresponder com textos que tenham 1 ou mais numeros, seguidos de 1 espaço e 1 ou mais letras/numeros/underline e o findall() vai trazer todos os resultados.

## Faça sua própria classe de caracter

Você pode definir sua própria classe de caracter usando os colchetes. Por exemplo esta classe de caracter [aeiouAEIOU] vai corresponder com todas as vogais, tanto maiusculas quanto minusculas.
```py
>>> vogalRegex = re.compile('[aeiouAEIOU]')
>>> vogalRegex.findall('RoboCop eats baby food. BABY FOOD.')
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
```

Você pode incluir distancias entre as letras usando um hifen. Por exemplo a classe de caracter [a-zA-Z0-9] vai pegar todas as letras maiusculas e minusculas e numeros de 0 a 9.
Colocando um (^) no início da classe de caracter você cria a *negação da classe de caracter*, ou seja ela vai capturar o oposto do que está la dentro.
```py
>>> consoanteRegex = re.compile('[^aeiouAEIOU]')
>>> consoanteRegex.findall('RoboCop eats baby food. BABY FOOD.')
['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', '
', 'B', 'B', 'Y', ' ', 'F', 'D', '.']
```

## O sinal de circunflexo e o dolar

O simbolo do ^ no incio de um expressão regex significa que a string correspondente tem que começar com aquela respectiva regra. 
Já o $ colocado ao final da expressão regex significa que a string correspondente tem que terminar com aquela respectiva regra.
```py
>>> comecaComHello = re.compile(r'^Hello')
>>> comecaComHello.search('Hello, world!')
<re.Match object; span=(0, 5), match='Hello'>
>>> comecaComHello.search('He said hello.') == None
True
```

A expressão regular '\d$' significa que a string tem que terminar com um digito numerico.
```py
>>> endsWithNumber = re.compile(r'\d$')
>>> endsWithNumber.search('Your number is 42')
<re.Match object; span=(16, 17), match='2'>
>>> endsWithNumber.search('Your number is forty two.') == None
True
```

A expressão regular '^\d+$' siginifica que a string vai ter que começar com digito numerico ter um tamanho de 1 ou mais e terminar com digito numerico.
```py
>>> wholeStringIsNum = re.compile(r'^\d+$')
>>> wholeStringIsNum.search('1234567890')
<re.Match object; span=(0, 10), match='1234567890'>
>>> wholeStringIsNum.search('12345xyz67890') == None
True
>>> wholeStringIsNum.search('12 34567890') == None
True
```

## O caracter coringa

O . (ou ponto) na expressão regular é chamado de *coringa* e vai corresponder a qualquer caracter com excessão o de uma nova linha.
```py
>>> atRegex = re.compile(r'.at')
>>> atRegex.findall('The cat in the hat sat on the flat mat.')
['cat', 'hat', 'sat', 'lat', 'mat']
```
O ponto so vai pegar um caracter antes do padrão selecionado como exemplo da string flat que ficou lat.

### Correspondendo com todos usando ponto e asterisco

As vezes você vai querer pegar tudo e qualquer coisa. Por exemplo você quer pegar a string 'Primeiro nome':, seguida por qualquer valor que venha depois dela e a string 'sobrenome:' seguida por qualquer coisa novamente. Então nosa vamos usar o ponto junto com o asterisco (.*), já que o ponto significa qualquer caracter com o exceção da quebra de linha, e o asterisco que busca 0 ou mais padrões.
```py
>>> nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
>>> mo = nameRegex.search('First Name: Al Last Name: Sweigart')
>>> mo.group(1)
'Al'
>>> mo.group(2)
'Sweigart'
```

### Pegando quebra de linha com o caracter .

O caracter ponto vai pegar qualquer coisa com execessão da quebra de linha (\n). Mas passando o argumento re.DOTALL como segundo argumento na função re.compile(), você vai fazer o caracter ponto  pegar tudo incluindo caracter de quebra de linha.
```py
>>> noNewlineRegex = re.compile('.*')
>>> noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
'Serve the public trust.'
>>> newlineRegex = re.compile('.*', re.DOTALL)
>>> newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
'Serve the public trust.\nProtect the innocent.\nUphold the law.'
```

## Correspondente a maisculas e minusculas

Normalmente as expressões regulares são sensiveis com relação as letras maiusculas e minisculas. Mas quando você quer buscar sem se importar com as maiusculas e minusculas é so passar re.IGNORECASE ou re.I como segundo argumento na função re.compile().
```py
>>> robocop = re.compile('robocop', re.I)
>>> robocop.search('RoboCop is part man, part machine, all cop.').group()
'RoboCop'
>>> robocop.search('ROBOCOP protects the innocent.').group()
'ROBOCOP'
>>> robocop.search('Al, why does your programming book talk about robocop so much?').group()
'robocop'
```

## Substituindo strings com o metodo sub()

As expressões regulares conseguem não somente achar o padrão selecionado mas tambem substituir as string. O sub() vai receber dois argumentos, o primeiro vai ser a string que vai substituir qualquer correspondente. O segundo vai ser a string que vai ser analisada pelo RegEx. O metodo sub() vai retornar a string ja com as substituições feitas.
```py
>>> namesRegex = re.compile(r'Agent \w+')
>>> namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
'CENSORED gave the secret documents to CENSORED.'
```

## Administrando RegEx complexos

As expressões regulares são tranquilas se os padrões que você busca são simples. Mas buscar padrão mais dificeis é necessário monstar uma expressão regular maior e mais complexa. Mas voce pode mitigar isso falando para a função re.compile() mitigar isso ignorando os espações em branco e comentarios dentro da expressao regular.
Este 'verbose mode' pode ser habilitado passado como segundo argumento  re.VERBOSE para a função re.compile().

Assim ao inves de ter uma expressão regular dificil de ser lida como essa:
```py
phoneRegex = re.compile('((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
```

Voce pode escrever a expressão em multiplas linhas com comentarios como essa:
```py
phoneRegex = re.compile('''(
(\d{3}|\(\d{3}\))?              # area code
(\s|-|\.)?                      # separator
\d{3}                           # first 3 digits
(\s|-|\.)                       # separator
\d{4}                           # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})?    # extension
)''', re.VERBOSE)
```
Todos os espações em branco tudo quer estiver depois da # é ignorado.

## Combinando re.IGNORECASE, re.DOTALL e re.VERBOSE

E se você quiser usar o re.VERBOSE para separar o codigo e escrever comentarios mas você tambem quer usar o re.IGNORECASE para ignorar a captalização. Infelizmente a função re.compile() só aceita um único valor como segundo argumento na função. Mas para quebrar essa limitação nos vamos usar o caracter pipe (|), que nesse contexto é conhecido como operador *bitwise or*.
Então caso você queira usar mais de um como segundo argumento vai ficar assim:
```py
>>> someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
```

Incluindo todas as três opções vai ficar assim:
```py
>>> someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
```