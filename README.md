# Nota (2015-10-13)

Prezados,

Nesta semana, conjuntamente com vários pesquisadores, criamos uma petição com alguns argumentos que discutem o porquê a adoção dos captchas não é uma boa estratégia para o Brasil.

A adoção de captcha nos currículos Lattes:

- Gera um custo elevado, oneroso e desnecessário para a coleta de dados;
- Constitui um freio à promoção da Ciência Brasileira;
- Desencoraja a consulta de dados da Plataforma Lattes;
- Diminui a visibilidade e o impacto da produção científica brasileira nos âmbitos nacional e internacional; e
- Impossibilita estudos acadêmicos envolvendo mais de uma instituição, gerando prejuízo à Ciência Brasileira.

Por favor, se concordar, **[assine a petição online e a divulgue](https://www.change.org/p/presid%C3%AAncia-do-cnpq-conselho-nacional-de-desenvolvimento-cient%C3%ADfico-e-tecnol%C3%B3gico-cnpq-peti%C3%A7%C3%A3o-para-a-retirada-dos-captchas-dos-curr%C3%ADculos-da-plataforma-lattes)**.

Abraços,

Jesús P. Mena-Chalco e equipe


---

# scriptLattes V8.12

## SINOPSE

`scriptLattes.py <nome_arquivo_de_configuracao>`


## REQUISITOS

Para a compilação precisam-se de alguns módulos Python. Para instalar esses módulos execute como root (admin):
```
$ apt-get install python-all python-setuptools python-utidylib python-matplotlib python-levenshtein python-pygraphviz python-numpy tidy python-scipy python-imaging python-mechanize
$ easy_install pytidylib
$ pip install beautifulsoup
```	

Em Ubuntu pode executar as seguintes instruções no terminal (linha de comandos):
```
$ sudo apt-get install python-all python-setuptools python-utidylib python-matplotlib python-levenshtein python-pygraphviz python-numpy tidy python-scipy python-imaging python-mechanize
$ sudo easy_install pytidylib
$ sudo pip install beautifulsoup
```

## EXECUÇÃO

Teste o scriptLattes com os seguintes dois exemplos (linha de comandos):

### EXEMPLO 01:

```
$ cd <nome_diretorio_scriptLattes>
$ python scriptLattes.py ./exemplo/teste-01.config
```

Nesse exemplo consideram-se todas as produções cujos anos de publicações estão entre 2006 e 2014. Nenhum rótulo foi considerado para os membros. 
	
Os IDs Lattes dos 3 membros está listada em: `./exemplo/teste-01.list`

O resultado da execução estará disponível em: `./exemplo/teste-01/`

### EXEMPLO 02

```
$ cd <nome_diretorio_scriptLattes>
$ python scriptLattes.py ./exemplo/teste-02.config
```

Nesse exemplo consideram-se todas as produções cadastradas nos CVs Lattes. São considerados rótulos para os membros do grupo (professor, colaborador, aluno).

Adicionalmente também são apresentadas as informações de Qualis para os artigos publicados (congressos e journals).

Os IDs Lattes dos membros está listada em: `./exemplo/teste-02.list`

O resultado da execução estará disponível em: `./exemplo/teste-02/`


## IDEALIZADORES DO PROJETO

* Jesús P. Mena-Chalco <jesus.mena@ufabc.edu.br>
* Roberto M. Cesar-Jr <cesar@vision.ime.usp.br>

## URL DO PROJETO

http://bitbucket.org/scriptlattes