#!/usr/bin/python
# encoding: utf-8
# filename: baixaLattes.py
#
#  scriptLattes V8
#  Copyright 2005-2013: Jesús P. Mena-Chalco e Roberto M. Cesar-Jr.
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

import sys, time, random, re

import mechanize
import cookielib

HEADERS =  [('Accept-Language', 'en-us,en;q=0.5'),
	('Accept-Encoding', 'deflate'),
	('Keep-Alive', '115'),
	('Connection', 'keep-alive'),
	('Cache-Control', 'max-age=0'),
	('Host', 'buscatextual.cnpq.br'),
	('Origin', 'http,//buscatextual.cnpq.br'),
	('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'),
]

def __get_data(id_lattes):
	p = re.compile('[a-zA-Z]+')
	if p.match(id_lattes):
		url = 'http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id='+id_lattes
	else:
		url = 'http://lattes.cnpq.br/'+id_lattes
	br = mechanize.Browser()
	br.set_cookiejar(cookielib.LWPCookieJar())

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

	br.select_form(nr=0)
	br.form.set_all_readonly(False)
	#br.form['metodo'] = 'captchaValido'	
	r = br.submit()
	return r.read()

def baixaCVLattes(id_lattes, debug=True):
	tries = 200
	while tries > 0:
		try:
			data = __get_data(id_lattes)
			#time.sleep(random.random()*1.5+0.5) #0.5 a 2 segs de espera, nao altere esse tempo para não ser barrado do servidor do lattes
			if 'infpessoa' not in data:
				print "."
				tries -= 1
			else:
				return data
		except Exception, e:
			if debug:
				print e
			tries -= 1
	if debug:
		print '[AVISO] Nao é possível obter o CV Lattes: ', id_lattes
		print '[AVISO] Certifique-se que o CV existe.'
	
	#raise Exception("Nao foi possivel baixar o CV Lattes em varias tentativas")
	print "Nao foi possivel baixar o CV Lattes em varias tentativas"
	return ""

