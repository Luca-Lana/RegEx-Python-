"""
* PASSOS A QUER O CODIGO PRECISA FAZER
1- retirar o texto da area de transferencia
2- encontrar todos os números de telefone e emails no texto
3- colar eles na areas de transferencia

* COMO ESSES PASSOS VÃO FUNCIONAR NO CODIGO
1- criar dois regex um para telefone outro para o email
2- encontrar todos os correspondentes não só o primeiro
"""
import re

textoTeste = """Oi jose tudo bem? Aqui é seu chefe te ligue no 31 99643-2145 não se voce viu enfim preciso que voce
mande um email para fernanda o email dela é fernandinha14@hotmail.com e com copia para o meu seuchfe_34@gmail.com caso n de certo
me liga no (31) 888889999 e se eu n atender avisa afernandinha no numero dela (31) 989324444! desde ja obgg"""


telefoneRegex = re.compile(r'''(
                           (\d{2}|\(\d{2}\))?   # codigo da area(opcional)
                           (\s)?                # espaço entre codigo e numero (opcional)
                           (\d{5})              # primeiros 5 numeros
                           (\s|-)?              # separador(opcional)
                           (\d{4})              # 4 ultimos numeros
                           )''',re.VERBOSE)


emailRegex = re.compile(r'''(
                        [a-zA-Z0-9._-]+     # username
                        @                   # arroba
                        (\w+)               #provedor
                        (\.\w{2,4})         # .com, .gov, etc
                        (\.[a-zA-Z]{2,3})?  # .br  (opicional)      
                        )''', re.VERBOSE)

telefones = telefoneRegex.findall(textoTeste) # vai retornar uma lista de tuplas com os numeros contidos no texto
emails = emailRegex.findall(textoTeste) # vai retornar uma lista de tuplas com os emails contidos no texto

