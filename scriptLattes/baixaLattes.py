#!/usr/bin/python
# encoding: utf-8
# filename: baixaLattes.py
#
#  scriptLattes V8
#  Copyright 2005-2013: Jesús P. Mena-Chalco e Roberto M. Cesar-Jr.
#  http://scriptlattes.sourceforge.net/
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

import sys, time, random, re, os, numpy, cookielib

try:
	import mechanize
except:
	print "Erro, voce precisa do Mechanize instalado no sistema, instale no Ubuntu com 'sudo apt-get install python-mechanize"

try:
	from cStringIO import StringIO
except:
	from StringIO import StringIO

try:
	from PIL import Image
	import simplejson
except:
	print """# Erro, voce precisa dos seguintes pacotes instalados no sistema: 'python-imaging', 'simplejson'.
	 **************************************************************************
	 # Instruções para o Ubuntu, instale: 
	 sudo apt-get install python-simplejson python-imaging
	 """
	sys.exit(1)
	
VERSION = '2015-05-29T16'

REMOTE_SCRIPT = 'https://api.bitbucket.org/2.0/snippets/scriptlattes/g5Bx'

HEADERS =  [('Accept-Language', 'en-us,en;q=0.5'),
	('Accept-Encoding', 'deflate'),
	('Keep-Alive', '115'),
	('Connection', 'keep-alive'),
	('Cache-Control', 'max-age=0'),
	('Host', 'buscatextual.cnpq.br'),
	('Origin', 'http,//buscatextual.cnpq.br'),
	('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'),
]

GET_CAPTCHA = 'http://buscatextual.cnpq.br/buscatextual/servlet/captcha?metodo=getImagemCaptcha'
VALIDA_CAPTCHA = 'http://buscatextual.cnpq.br/buscatextual/servlet/captcha?metodo=validaCaptcha&informado='
# TESSERACT_PATH = "/usr/share/tesseract-ocr/tessdata/"

dicionarioCarateres = dict([])
dicionarioCarateres['1'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1, 1, 1, 2, 3, 3, 3, 3, 3, 4, 5, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['1'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1, 1, 1, 2, 3, 3, 3, 3, 3, 4, 5, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['1'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 6, 4, 3, 3, 3, 3, 3, 3, 2, 1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 4, 6, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['2'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 11, 9, 7, 7, 6, 5, 4, 3, 3, 3, 3, 3, 2, 6, 3, 3, 3, 2, 2, 2, 5, 4, 4, 7, 14, 13, 8, 0, 0, 0, 0])
dicionarioCarateres['3'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 8, 4, 4, 3, 3, 2, 3, 3, 4, 4, 5, 4, 4, 3, 3, 2, 3, 2, 4, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['4'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 4, 4, 5, 5, 6, 6, 5, 6, 6, 6, 7, 6, 6, 6, 5, 4, 5, 8, 19, 20, 18, 5, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0])
dicionarioCarateres['5'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 5, 8, 11, 13, 13, 9, 7, 5, 5, 7, 9, 8, 7, 7, 7, 6, 4, 6, 9, 5, 5, 5, 5, 5, 4, 3, 2, 2, 3, 4, 3, 5, 8, 8, 9, 0, 0, 0, 0])
dicionarioCarateres['6'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 6, 3, 3, 4, 4, 4, 4, 4, 5, 4, 5, 13, 10, 9, 9, 8, 9, 8, 8, 8, 9, 8, 8, 8, 6, 6, 4, 4, 5, 3, 0, 0])
dicionarioCarateres['7'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 8, 11, 10, 7, 5, 5, 4, 2, 2, 3, 3, 3, 3, 2, 2, 2, 3, 3, 2, 2, 2, 2, 2, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['8'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 9, 7, 6, 8, 8, 10, 10, 7, 8, 9, 9, 9, 9, 10, 9, 8, 7, 9, 8, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['9'] = numpy.asarray([0, 0, 0, 0, 0, 6, 5, 6, 7, 7, 7, 6, 7, 7, 7, 7, 7, 8, 8, 10, 13, 5, 4, 4, 3, 10, 4, 4, 4, 3, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['B'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 11, 9, 9, 8, 8, 8, 9, 10, 9, 9, 10, 15, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 10, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['C'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 11, 8, 8, 7, 6, 6, 4, 5, 5, 5, 5, 4, 4, 4, 5, 5, 5, 5, 6, 7, 7, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['D'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 11, 10, 9, 8, 8, 9, 9, 8, 9, 8, 8, 9, 9, 8, 8, 8, 9, 10, 9, 9, 9, 9, 9, 10, 10, 13, 11, 0, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['F'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 10, 9, 10, 7, 5, 5, 5, 6, 7, 9, 16, 8, 7, 9, 6, 5, 5, 4, 4, 9, 5, 6, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['F'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 10, 9, 10, 7, 5, 5, 5, 6, 7, 9, 16, 8, 7, 9, 6, 5, 5, 4, 4, 9, 5, 6, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['G'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 7, 8, 8, 7, 6, 4, 5, 3, 4, 4, 4, 9, 8, 7, 6, 6, 7, 7, 7, 7, 7, 9, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['H'] = numpy.asarray([0, 0, 0, 0, 0, 1, 2, 5, 7, 5, 4, 3, 6, 10, 9, 8, 8, 8, 10, 11, 12, 11, 11, 9, 8, 8, 8, 8, 9, 9, 7, 7, 5, 5, 6, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['H'] = numpy.asarray([0, 0, 0, 0, 0, 1, 2, 4, 6, 4, 4, 3, 6, 10, 9, 8, 8, 8, 10, 11, 12, 11, 11, 9, 8, 8, 8, 8, 9, 9, 7, 7, 5, 5, 6, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['J'] = numpy.asarray([0, 0, 0, 0, 13, 8, 6, 4, 4, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 8, 5, 4, 4, 4, 4, 4, 4, 4, 10, 11, 8, 10, 7, 4, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['J'] = numpy.asarray([0, 0, 0, 0, 13, 7, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 11, 6, 4, 4, 4, 4, 4, 4, 5, 11, 12, 8, 10, 8, 4, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['J'] = numpy.asarray([0, 0, 0, 0, 11, 7, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 8, 4, 4, 4, 4, 4, 4, 4, 4, 13, 8, 7, 10, 7, 3, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['K'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 9, 8, 6, 6, 6, 7, 7, 9, 8, 8, 9, 11, 10, 9, 9, 9, 10, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['L'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 5, 4, 3, 3, 3, 4, 4, 3, 4, 3, 4, 3, 3, 4, 3, 4, 4, 3, 4, 6, 6, 7, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['L'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 5, 4, 3, 3, 3, 4, 4, 3, 4, 3, 4, 3, 3, 4, 4, 4, 4, 3, 4, 6, 5, 6, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['M'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 9, 9, 10, 10, 12, 13, 15, 14, 11, 9, 9, 9, 9, 11, 11, 11, 8, 6, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['N'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 5, 11, 8, 8, 7, 8, 9, 9, 10, 11, 12, 10, 9, 9, 10, 11, 9, 8, 11, 14, 10, 10, 10, 10, 9, 8, 8, 9, 7, 6, 8, 8, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['P'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 7, 6, 7, 7, 7, 7, 8, 6, 7, 7, 6, 7, 6, 4, 3, 4, 9, 3, 3, 3, 4, 7, 1, 0, 0, 0])
dicionarioCarateres['R'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 10, 8, 8, 10, 9, 9, 9, 9, 9, 9, 9, 9, 4, 4, 10, 9, 8, 8, 8, 9, 9, 8, 9, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['R'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 10, 8, 8, 10, 9, 9, 9, 9, 9, 9, 9, 9, 4, 4, 10, 9, 9, 8, 8, 9, 9, 9, 10, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['S'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 15, 14, 11, 10, 9, 8, 9, 9, 8, 10, 10, 11, 12, 11, 13, 10, 15, 9, 7, 8, 8, 9, 10, 12, 13, 16, 12, 0, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['T'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 5, 3, 3, 4, 8, 6, 6, 5, 4, 3, 4, 4, 4, 3, 4, 4, 3, 4, 3, 5, 7, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['V'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 9, 7, 6, 4, 6, 6, 5, 5, 3, 5, 5, 5, 6, 5, 5, 7, 6, 5, 4, 3, 2, 2, 0, 0, 0, 0])
dicionarioCarateres['W'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 12, 9, 7, 8, 10, 8, 8, 10, 9, 11, 12, 9, 10, 11, 13, 13, 14, 14, 12, 10, 9, 13, 7, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2])
dicionarioCarateres['W'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 13, 9, 7, 7, 9, 8, 8, 10, 9, 11, 12, 9, 9, 11, 13, 13, 14, 14, 12, 10, 9, 13, 7, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['X'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 4, 7, 5, 4, 4, 3, 4, 6, 5, 3, 3, 4, 5, 5, 4, 4, 4, 4, 6, 8, 4, 5, 3, 0, 0, 0, 0, 0, 0, 0])
dicionarioCarateres['Z'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 10, 8, 7, 7, 7, 6, 5, 6, 6, 6, 6, 6, 5, 6, 10, 7, 6, 6, 7, 7, 8, 8, 10, 26, 0, 0, 0])
dicionarioCarateres['Z'] = numpy.asarray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 10, 10, 11, 10, 8, 7, 9, 7, 6, 6, 6, 11, 6, 7, 10, 7, 6, 6, 8, 10, 10, 11, 15, 26, 0, 0, 0])
                           
def getCharacter(profile):
	profile = numpy.asarray(profile)
	minDistance = 9999999
	bestChar    = '@'

	for c in dicionarioCarateres.keys():
		dist = numpy.linalg.norm(profile - dicionarioCarateres[c])
		if minDistance > dist:
			minDistance = dist
			bestChar = c
			# print ">>>", minDistance, bestChar
	return bestChar


def setLimits(pix, m, n, forte):
	# print n, m
	for y in xrange(m):
		for x in xrange(n):
			if pix[x, y][0] >= 225 and pix[x, y][1] >= 225 and pix[x, y][2] >= 225:
				pix[x, y] = (255, 255, 255)
			else:
				pix[x, y] = (0, 0, 0)

	# preenche buracos
	for y in range(1,m-1):
		for x in range(1,n-1):
			if (pix[x, y][0]==0 and pix[x-1, y][0]==255 and pix[x+1, y][0]==255) or (pix[x, y][0]==0 and pix[x, y-1][0]==255 and pix[x, y+1][0]==255):
				pix[x, y] = (255, 0, 0)
			if (pix[x, y][0]==0 and pix[x-1, y+1][0]==255 and pix[x+1, y-1][0]==255) or (pix[x, y][0]==0 and pix[x+1, y+1][0]==255 and pix[x-1, y-1][0]==255): 
				pix[x, y] = (255, 0, 255)
			if ((pix[x, y][0]==0 and pix[x-1, y][0]==255 and pix[x+1, y-1][0]==255) or (pix[x, y][0]==0 and pix[x+1, y][0]==255 and pix[x-1, y-1][0]==255) ) and (pix[x,y-1][0]==0 and pix[x,y+1][0]==0 ) : 
				pix[x, y] = (255, 0, 255)

	# limpa ruido
	for y in range(1,m-1):
		for x in range(1,n-1):
			if pix[x, y][0]==255 and (pix[x-1, y][0]==0 and pix[x+1, y][0]==0 and pix[x, y-1][0]==0 and pix[x, y+1][0]==0 and pix[x-1, y-1][0]==0 and pix[x+1, y+1][0]==0 and pix[x-1, y+1][0]==0 and pix[x+1, y-1][0]==0):
				pix[x, y] = (0, 255, 0)
				#pix[x, y] = (0, 0, 0)

	# soma colunas
	cc = [0]*n
	for x in xrange(n):
		for y in xrange(m-1):
			if pix[x, y][0]==255:
				cc[x] += 1

	# ajuste fino (ruido)
	if forte==True:
		for x in xrange(n-2):
			if cc[x]<=1: # and cc[x+1]<=1 :
				cc[x] = 0
	#print cc

	# identificacao de limites entre letras (3 brancos para separar carateres)
	limites = []
	inicio = None
	fim = None
	for x in range(30, 170):
		if cc[x]!=0 and inicio==None:
			inicio = x
		if (inicio!=None and cc[x]==0 and cc[x+1]==0 and cc[x+2]==0) or (inicio!=None and cc[x]==0 and cc[x+1]==0 and x-inicio>=10):
			fim = x-1
			limites.append([inicio, fim])
			x = x+2
			inicio = None
			fim = None
	#print limites

	# eliminando grupos pequenos
	if len(limites)>4:
		limites2 = []
		for (lim1, lim2) in limites:
			if lim2-lim1>=2:
				limites2.append([lim1, lim2])
		#print limites2
		limites = limites2

	# agrupando regioes
	if len(limites)>4:
		separacoes = []
		for i in range(0,len(limites)-1):
			ss = limites[i+1][0] - limites[i][1]
			separacoes.append(ss)
		minSep = min(separacoes)
		#print separacoes
		#print minSep
		
		#print limites
		limites3 = []
		i = 0
		while i<=len(limites)-1:
		#for i in range(0,len(limites)-1):
			#print i
			if (limites[i+1][0]-limites[i][1])<=minSep:
				limites3.append( [ limites[i][0] , limites[i+1][1] ] )
				#print "juntando" , [ limites[i][0] , limites[i+1][1] ]
				i = i+1
			else:
				limites3.append([ limites[i][0] , limites[i][1] ] )
			i = i+1
		if (limites[len(limites)-1][1]-limites[len(limites)-1][0])>=minSep:
			limites3.append([ limites[len(limites)-1][0] , limites[len(limites)-1][1] ] )

		#print limites3
		limites = limites3

	return limites

def extract(image):
	im = Image.open(image)
	#im = im.convert("RGBA")
	im = im.convert("RGB")
	#im.show()
	pix = im.load()

	m = im.size[1]
	n = im.size[0]

	limites = setLimits(pix, m, n, False)
	if len(limites)<4:
		limites = setLimits(pix, m, n, True)
	
	# visualizando os limites entre os blocos
	for (lim1, lim2) in limites:
		for y in xrange(m):
			(a1, a2, a3) = pix[lim1, y]
			pix[lim1, y] = (a1, a2, 200)
			(a1, a2, a3) = pix[lim2, y]
			pix[lim2, y] = (a1, a2, 200)

	captcha = ''
	if len(limites)==4:
		for (lim1, lim2) in limites:
			profile = [0]*m
			for y in xrange(m):
				for x in range(lim1, lim2+1):
					if (pix[x,y][0]==255):
						profile[y] += 1
			ci = getCharacter(profile)
			#print ci , lim2-lim1 , profile
			captcha += ci
			
	# finalizando
	#fake_file = StringIO()
	#im.save(fake_file,"png")
	#mBuffer = fake_file.getvalue()
	
	#im.show()

	#x  = raw_input("insira captcha: ")
	#return x
        print 'captcha ===>', captcha
	return captcha
		
		
def solve(br, cookies, tries=20):
	if tries == 0:
		raise Exception("Erro, captcha nao pode ser validado em 10 tentativas")
	image_response = br.open_novisit(GET_CAPTCHA)
	image = StringIO(image_response.read())
	#print ">>>>>>>>>>>>>", image
	code = extract(image)
	response = br.open_novisit(VALIDA_CAPTCHA + code)
	data = simplejson.loads(response.read())
	#print "------------------------------"
	print data
	#print data.get('estado')
	#print "------------------------------"
	#if data.get('estado')!='sucesso':
	#	tries-=1
	#	solve(browser, cookies, tries)
		

def __self_update():
	import inspect
	br = mechanize.Browser()
	r = br.open(REMOTE_SCRIPT)
	d = simplejson.loads(r.read())
	if d['updated_on'][:13] != VERSION:
		print "BaixaLattes desatualizado, atualizando..."
		r = br.open(d['files']['baixaLattes.py']['links']['self']['href'])
		content = r.read()
		fpath = os.path.abspath(inspect.getfile(inspect.currentframe()))
		try:
			handler = file(fpath, 'w')
		except:
			print "Erro na escrita do novo arquivo, verifique se o arquivo '%s' tem permissao de escrita" % fpath
			sys.exit(1)
		handler.write(content)
		handler.close()
		print "BaixaLattes atualizado, reinicie o programa para utilizar a nova versão, encerrando o ScriptLattes"
		sys.exit(0)


def __get_data(id_lattes):
	p = re.compile('[a-zA-Z]+')
	if p.match(id_lattes):
		url = 'http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id='+id_lattes
	else:
		url = 'http://lattes.cnpq.br/'+id_lattes
	br = mechanize.Browser()
	cookies = cookielib.LWPCookieJar()
	br.set_cookiejar(cookies)

	br.set_handle_equiv(True)
	br.set_handle_gzip(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	br.addheaders = HEADERS

	r = br.open(url)
	response = r.read()
	if 'infpessoa' in response:
		return response
	solve(br, cookies)

	br.select_form(nr=0)
	br.form.set_all_readonly(False)
	br.form['metodo'] = 'captchaValido'	
	r = br.submit()
	return r.read()

def baixaCVLattes(id_lattes, debug=True):
	tries = 50
	while tries > 0:
		try:
			data = __get_data(id_lattes)
			#time.sleep(random.random()+0.5) #0.5 a 1.5 segs de espera, nao altere esse tempo para não ser barrado do servidor do lattes
			if 'infpessoa' not in data:
				tries -= 1
			else:
				return data
		except Exception, e:
			if debug:
				print e
			tries -= 1
	# depois de 5 tentativas, verifiquemos se existe uma nova versao do baixaLattes
	#__self_update()
	if debug:
		print '[AVISO] Nao é possível obter o CV Lattes: ', id_lattes
		print '[AVISO] Certifique-se que o CV existe.'
	
	print "Nao foi possivel baixar o CV Lattes em 5 tentativas"
	return "   "
	#raise Exception("Nao foi possivel baixar o CV Lattes em 5 tentativas")
