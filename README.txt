scriptLattes V8.10
------------------

SINOPSIS
	scriptLattes.py <nome_arquivo_de_configuracao>


REQUISITOS
	Para a compilação precisam-se de alguns módulos Python. Para instalar esses  módulos execute como root (admin):
	# apt-get install python-all python-setuptools python-utidylib python-matplotlib python-levenshtein python-pygraphviz python-numpy tidy python-scipy python-imaging python-mechanize python-simplejson
	# easy_install pytidylib

	Em Ubuntu pode executar as seguintes instruções no terminal (linha de comandos):
	sudo apt-get install python-all python-setuptools python-utidylib python-matplotlib python-levenshtein python-pygraphviz python-numpy tidy python-scipy python-imaging python-mechanize python-simplejson
	sudo easy_install pytidylib


EXECUÇÃO
	Teste o scriptLattes com os seguintes dois exemplos (linha de comandos):

	(*) EXEMPLO 01:
	cd <nome_diretorio_scriptLattes>
	python scriptLattes.py ./exemplo/teste-01.config

	Nesse exemplo consideram-se todas as produções cujos anos de publicações
	estão entre 2006 e 2014. Nenhum rótulo foi considerado para os membros. 
	
	Os IDs Lattes dos 3 membros está listada em:
	./exemplo/teste-01.list

	O resultado da execução estará disponível em:
	./exemplo/teste-01/


	(*) EXEMPLO 02:
	cd <nome_diretorio_scriptLattes>
	python scriptLattes.py ./exemplo/teste-02.config

	Nesse exemplo consideram-se todas as produções cadastradas nos CVs Lattes.
	São considerados rótulos para os membros do grupo (professor, colaborador, aluno)
	Adicionalmente também são apresentadas as informações de Qualis para os
	artigos publicados (congressos e journals).

	Os IDs Lattes dos membros está listada em:
	./exemplo/teste-02.list

	O resultado da execução estará disponível em:
	./exemplo/teste-02/


URL DO PROJETO
	http://scriptlattes.sourceforge.net/


=========================================================================================
LOG

Sun Apr 10 00:23:32 BRT 2016
-- Melhora na identificação dos anos das produções acadêmicas.

Seg Mai 18 17:09:23 BRT 2015
-- ScriptLattes modificado para processar os CVs com captcha. Para a execução
   deverá instalar o pacote mechanize (veja requisitos do programa).

Dom Set 21 13:42:30 BRT 2014
-- Melhora nos procedimento de identificação de anos para os projetos de pesquisa.
-- Melhora da função de geração das informações em formato XML.

Sáb Ago  9 12:29:06 BRT 2014
-- Melhora do procedimento para tratar publicações com DOI.

Dom Jun 29 16:35:20 BRT 2014
-- Melhora da identificação da editora na seção: Livros publicados.


Seg Abr 21 22:05:40 BRT 2014
-- Foram melhorados/corrigidos alguns procedimentos com a identificação dos nomes das
   revistas.

Seg Mar  3 08:42:28 BRT 2014
-- A identificação de Qualis foi melhorada. Os ISSN para os artigos completos
  em periódicos agora estão sendo identificados. Também foi modificado o parser
  para identificar melhor o título da publicação e nome da revista.

Dom Mar  2 18:31:39 BRT 2014
-- A rede de coautoria armazenada em formato GDF (gephi). 
   Veja o arquivo 'rede.gdf' (automaticamente gerado)
-- Foram melhorados alguns procedimentos de criação dos grafos.

Seg Ago 26 03:09:50 BRT 2013
-- Algumas melhoras no parser (<x<).
-- Armazenamento das geolocalizações.

Sex Jun 28 17:04:13 BRT 2013
-- Um bug na criação do mapa de geolocalização foi consertado.

Wed May 29 12:24:23 BRT 2013
-- Criação do arquivo de colaboradores

Qui Mai  2 22:03:37 BRT 2013
-- A lista de Prêmios e títulos é avaliada de forma individual (i.e., não é
   identificada coautoria na lista de Prêmios e títulos).

Dom Abr 14 12:32:54 BRST 2013
-- Foi corrigida a função de localização geográfica.

Sáb Fev 16 17:08:53 BRST 2013
-- Foi melhorada a função de busca/associação de Qualis em publicações.
-- Melhora do parser de internacionalização.
-- Melhora do procedimento para a criação de grafos: from PIL import Image
   Correção de um bug.
-- A identificação das partes constituintes de uma publicação foi melhorada
   para as publicações com grande número de coautores (mais do que 10).
-- Os períodos para as orientações em andamento foram corrigidas.

Sáb Jan 19 10:18:29 BRST 2013
-- O parser do scriptLattes foi corrigido/atualizado. Atualmente, alguns
   projetos de pesquisa apresentam informação de validação do tipo:
   "Projeto certificado pelo(a) coordenador(a) XXX YYY em 28/12/2012."
   "Projeto certificado pela empresa XXX em 21/08/2012."

Seg Nov 19 17:42:32 BRST 2012
-- Foi implementada a identificação automática de publicações com Qualis. Para a
   associação de Qualis deve de se informar um arquivo CSV contendo a lista de
   publicações (em periódicos ou congressos) aprovados pelo Comitê Avalidor de
   cada Área (CAPES).

   Veja alguns exemplos de arquivos CSV de QUALIS em 
   http://scriptlattes.sourceforge.net/qualis.html

   Três novos parâmetros foram considerados:
   - global-identificar_publicacoes_com_qualis = [sim|nao]
   - global-arquivo_qualis_de_periodicos = [arquivo.csv]
   - global-arquivo_qualis_de_congressos = [arquivo.csv]
   A qualidade de identificação de publicações com Qualis depende:
   (i) da qualidade dos dados cadastrados nos CVs Lattes e
   (ii) das listas CSV informadas na execução do scriptLattes.
   Evite o uso de listas CSVs, desatualizadas, incompletas ou mal formatadas.
   Essa característica foi inicialmente desenvolvida por Helena Caseli.

-- Foi considerado, mediante o novo parâmetro:
   - relatorio-incluir_internacionalizacao = [sim|nao]
   um relatório de 'internacionalização'. Para os artigos publicados em
   periódicos (journals), com DOI cadastrado nos CVs Lattes. Para esse relatório,
   são identificados todos os países dos coautores das publicações.
   Maiores detalhes do procedimento estão disponíveis no artigo: 'Towards a quantitative
   academic internationalization assessment of brazilian research group'
   (eScience 2012).
   Essa característica está sendo desenvolvida em colaboração com Evelyn Perez Cervantes.

-- As informações individuais de cada pesquisador também podem ser armazenadas,
   localmente, em formato XML. Para isso foi criado um novo parâmetro:
   - global-salvar_informacoes_em_formato_xml = [sim|nao]
   Durante a execução um novo arquivo é gerado: 'database.xml'. 
   Essa característica foi inicialmente desenvolvida por Richard W. Valdivia.


Dom Ago 12 08:12:39 BRT 2012
-- A classe parserLattes foi adaptada para suportar o novo formato HTML dos CVs
   Lattes.
-- O critério utilizado para comparar produções bibliográficas foi atualizado.
   Duas produções são consideradas iguais (ou similares) se a distância
   Levenshtein entre eles for menor ou igual do que 5.

Ter Jun 12 22:30:15 BRT 2012
-- As vezes os IDs Lattes cadastrados nos CVs Lattes não são válidos (erros na escrita),
   assim, o scriptLattes tenta 5 vezes baixar o CV. Caso contrário o CV é desconsiderado.

Thu Jun  7 14:13:35 BRT 2012
-- Foi corrigido o procedimento para baixar os CVs Lattes. 
-- O parâmetro 'mapa-google_map_key' não é mais requerido para o Mapa de Geolocalização.
   A versão 2 da API do google maps está obsoleta. Atualmente usamos a versão 3. Assim,
   não é mais necessário ter um cadastro no googleMaps.
-- A página de membros foi atualizada. Foi acrescentada uma coluna com o rótulo
   de cada membro (se este for informado no arquivo .config). Essa informação é
   útil para na criação de relatórios que contenham membros afastados temporariamente
   do grupo (e.g. professores aposentados, professores transferidos a outra unidade).
-- Foi corrigido um erro de codificação no pygraphviz (python 2.7.3 disponível na 
   distribuição Ubuntu 12.04)

Tue Feb 28 12:00:34 BRT 2012
-- São utilizados estruturas de dados que permitam representar as matrizes de coautoria 
   através de matrizes esparsas. Nesse caso deve de se instalar o pacote python-scipy 
   (a instrução para a instalar o pacote está indicada na seção 'Requisitos').
-- Compatibilidade com exceções (except) de python.
-- Melhora de alguns procedimentos pontuais. Não é necessário carregar o X para a
   geração dos gráficos de barras.

Mon Jan 23 11:49:54 BRST 2012
-- Foi considerado, mediante um novo parâmetro 'global-diretorio_de_armazenamento_de_cvs',
   o armazenamento temporário (cache) de CVs.
   Esta característica permite realizar diferentes análises baixando apenas
   uma vez cada CV. Se nenhum valor for indicado para o parâmetro não for indicado, então
   serão utilizadas as últimas versões dos CVs. Isto é, para toda nova execução serão
   baixados os CVs.
-- São consideradas inúmeras tentativas para baixar os CVs Lattes.
   Algumas vezes o servidor Lattes não consegue distribuir o CV. Nesse caso, o programa
   faz uma pausa de 20seg para, seguidamente, realizar uma nova tentativa.

Sat Oct 15 23:32:21 BRT 2011
-- Foi melhorado o procedimento para baixar CVs da Plataforma Lattes.

Sun Jul  3 12:01:50 BRT 2011
-- Foi corrigido o procedimento para baixar CVs Lattes.

Qua Mai  4 16:38:51 BRT 2011
-- Foi considerado, mediante novos parâmetros, os seguintes relatórios adicionais:
   - Participação em eventos.
   - Organização de eventos.

Seg Abr 11 07:40:23 BRT 2011
-- O scriptLattes foi re-programado inteiramente em Python. Foram acrescentadas novas
  características como a criação de novos grafos de colaboração, relatórios de projetos de pesquisa,
  relatórios de prêmios, arquivos RIS com a lista de publicações, matrizes de adjacência. Em particular
  a abordagem usada para o tratamento de redundâncias foi modificada.

Sat Apr 17 13:47:32 BRT 2010
-- Foi acrescentado um ícone para a indicação do DOI nas publicações.

Wed Mar 24 14:44:38 BRT 2010
-- Foram consideradas, mediante novos parâmetros, os seguintes relatórios adicionais:
   - Projetos de pesquisa.
   - Prêmios.
-- As páginas correspondentes aos curriculums mostram também:
   - Formação acadêmica/Titulação.
   - Áreas de atuação.
-- O arquivo database.json contêm todas essas novas informações.

Mon Mar 15 08:02:22 BRT 2010
-- Melhoramento da função de comparação. Em média o algoritmo de comparação da
   versão 7.02 é 13X mais rápido que o anterior.
-- Criação do grafo de colaborações com indicadores de produção usando um mapa
   de cores (hotcolors).
-- Foram consideradas, mediante novos parâmetros, os seguintes relatórios adicionais:
   - Participação em bancas examinadoras.
   - Participação em comissões julgadoras.
   - Eventos.

Ter Out 20 13:32:13 BRST 2009
-- Geração de relatórios disponíveis para os idiomas: inglês, português e espanhol.
-- Criação de uma página de 'detalhe de colaborações'. Clique nas arestas do Grafo de colaborações
   para listar as publicações realizadas entre os membros.
-- Melhoramento da função de localização geográfica (com suporte para endereços do exterior).
   Utilize o arquivo 'scriptLattes.cep' para refinar a localização no googleMaps.
-- Criação de listas de produções em formato JSON: 'database.json'. Tais listas poderiam
   ser utilizadas para exportar as produções ou popular bancos de dados.
-- Melhoramento na visualização/apresentação/compilação dos relatórios.
   O scriptLattes não usa o script 'terminalTags.sh'.

Sáb Abr 18 16:23:31 BRT 2009
-- Foram considerados nas Produções técnicas os "Processos ou técnicas"
-- Foram considerados nas Orientações as "Monografias de conclusão de curso de aperfeiçoamento/especialização"
-- O procedimento para identificação do ano nas produções foi corrigido.
-- "Itens sem ano" estão sendo listados no final de cada relatório.

Ter Mar 24 07:59:43 BRT 2009
-- Mapa de pesquisa, considerando os alunos com doutorado concluído.
-- Foram corrigidos alguns pequenos erros de inicialização de variáveis.

Qua Mar  4 12:45:40 BRT 2009
-- Uso de um arquivo de configuração.
-- Delimitação de produções por períodos (global e local).
-- Mapa de pesquisa (usando o maps.google.com).
-- Produções técnicas e artísticas foram consideradas nos relatórios.
-- Criação de páginas para cada pesquisador.
-- Produção automática de páginas JSP (opcional)
-- Divisão automática de produções em páginas (ex. 1000 produções por página).
-- CSS para todas as páginas.
-- Refatoração do script.

Sáb Nov  8 16:11:46 BRST 2008
-- Versão interativa e postscript do grafo de colaborações.
-- Lista de pesquisadores considerados na execução.
-- Criação de um indice geral.

Seg Mar 24 12:30:03 BRT 2008
-- Refatoração.
-- Link para busca da publicação no Google.
-- Compilação de orientações (em andamento/concluídas).

Sex Fev  8 18:24:33 BRST 2008
-- Criadas as funções de compilação de todas as publicações.
-- Geração automática da página index.html.
-- Geração automática de um grafo de colaborações.

Ter Mar 13 12:04:40 BRT 2007 : 
-- Barras estatísticas das publicações (uso do GD::Graph do perl).
-- Criada a função de similaridade LCS (longest common sequence).
-- Modificada a função de extração de datas das publicações.

Seg Mar 20 17:50:21 BRT 2006 :
-- Atualização das funções básicas.

Sex Mar 25 13:04:27 BRT 2005 : 
-- Criada a função de similaridade básica.

=========================================================================================
