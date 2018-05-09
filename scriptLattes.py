#!/usr/bin/env python 
# encoding: utf-8
#
#
#  scriptLattes V8
#  Copyright 2005-2014: Jesús P. Mena-Chalco e Roberto M. Cesar-Jr.
#  http://scriptlattes.sourceforge.net/
#
#
#  Este programa é um software livre; você pode redistribui-lo e/ou 
#  modifica-lo dentro dos termos da Licença Pública Geral GNU como 
#  publicada pela Fundação do Software Livre (FSF); na versão 2 da 
#  Licença, ou (na sua opinião) qualquer versão.
#
#  Este programa é distribuído na esperança que possa ser util, 
#  mas SEM NENHUMA GARANTIA; sem uma garantia implicita de ADEQUAÇÂO a qualquer
#  MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
#  Licença Pública Geral GNU para maiores detalhes.
#
#  Você deve ter recebido uma cópia da Licença Pública Geral GNU
#  junto com este programa, se não, escreva para a Fundação do Software
#  Livre(FSF) Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#

import sys
import shutil
import Levenshtein
import os, errno
import warnings
warnings.filterwarnings('ignore')

sys.path.append('scriptLattes')
sys.path.append('scriptLattes/producoesBibliograficas/')
sys.path.append('scriptLattes/producoesTecnicas/')
sys.path.append('scriptLattes/producoesArtisticas/')
sys.path.append('scriptLattes/producoesUnitarias/')
sys.path.append('scriptLattes/orientacoes/')
sys.path.append('scriptLattes/eventos/')
sys.path.append('scriptLattes/charts/')
sys.path.append('scriptLattes/internacionalizacao/')
sys.path.append('scriptLattes/qualis/')
sys.path.append('scriptLattes/patentesRegistros/')

from grupo import *

if __name__ == "__main__":
	arquivoConfiguracao = sys.argv[1]

	novoGrupo = Grupo(arquivoConfiguracao)
	#novoGrupo.imprimirListaDeParametros()
	novoGrupo.imprimirListaDeRotulos()

	if criarDiretorio(novoGrupo.obterParametro('global-diretorio_de_saida')):
		novoGrupo.carregarDadosCVLattes() #obrigatorio
		novoGrupo.compilarListasDeItems() # obrigatorio
		novoGrupo.identificarQualisEmPublicacoes() # obrigatorio
		novoGrupo.calcularInternacionalizacao() # obrigatorio
		#novoGrupo.imprimirMatrizesDeFrequencia() 

		novoGrupo.gerarGrafosDeColaboracoes() # obrigatorio
		novoGrupo.gerarGraficosDeBarras() # obrigatorio
		novoGrupo.gerarMapaDeGeolocalizacao() # obrigatorio
		novoGrupo.gerarPaginasWeb() # obrigatorio
		novoGrupo.gerarArquivosTemporarios() # obrigatorio

		# copiar imagens e css
		copiarArquivos(novoGrupo.obterParametro('global-diretorio_de_saida'))

		# finalizando o processo
		#print '[AVISO] Quem vê \'Lattes\', não vê coração! B-)'
		#print '[AVISO] Por favor, cadastre-se na página: http://scriptlattes.sourceforge.net\n'
		print '\n\n\n[PARA REFERENCIAR/CITAR ESTE SOFTWARE USE]'
		print '    Jesus P. Mena-Chalco & Roberto M. Cesar-Jr.'
		print '    scriptLattes: An open-source knowledge extraction system from the Lattes Platform.'
		print '    Journal of the Brazilian Computer Society, vol.15, n.4, páginas 31-39, 2009.'
		print '    http://dx.doi.org/10.1007/BF03194511'
		print '\n\nscriptLattes executado!'

# ---------------------------------------------------------------------------- #
def compararCadeias(str1, str2, qualis=False):
	str1 = str1.strip().lower()
	str2 = str2.strip().lower()

	# caso especial
	if (u'apresentação'==str1 or u'apresentação'==str2 or u'apresentacao'==str1 or u'apresentacao'==str2 ):
		return 0

	if len(str1)==0 or len(str2)==0:
		return 0
	
	if len(str1)>=20 and len(str2)>=20 and (str1 in str2 or str2 in str1):
		return 1

	if qualis:
		dist = Levenshtein.ratio(str1, str2)
		if len(str1)>=10 and len(str2)>=10 and dist>=0.90:
			#return 1
			return dist

	else:
		if len(str1)>=10 and len(str2)>=10 and Levenshtein.distance(str1, str2)<=5:
			return 1
	return 0

def criarDiretorio(dir):
	if not os.path.exists(dir):
		try:
			os.makedirs(dir)
		### except OSError as exc:
		except:
			print "\n[ERRO] Não foi possível criar ou atualizar o diretório: "+dir.encode('utf8')
			print "[ERRO] Você conta com as permissões de escrita? \n"
			return 0
	return 1

def copiarArquivos(dir):
	shutil.copy2(sys.path[0]+'/css/scriptLattes.css', dir)
	shutil.copy2(sys.path[0]+'/imagens/lattesPoint0.png', dir)
	shutil.copy2(sys.path[0]+'/imagens/lattesPoint1.png', dir)
	shutil.copy2(sys.path[0]+'/imagens/lattesPoint2.png', dir)
	shutil.copy2(sys.path[0]+'/imagens/lattesPoint3.png', dir)
	shutil.copy2(sys.path[0]+'/imagens/lattesPoint_shadow.png', dir)
	shutil.copy2(sys.path[0]+'/imagens/doi.png', dir)
