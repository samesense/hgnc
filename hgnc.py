"""Use the HGNC REST API to find current gene symbols.
   These can be referenced in biomart."""
import httplib2 as http
import json, time

try:
 from urlparse import urlparse
except ImportError:
 from urllib.parse import urlparse

def findTrueGeneSymbol(gene):
 """What is the current symbol for this gene symbol?
    A current gene symbol will yield nothing."""
 trueGenes = set()
 newGene = searchPreviousSymbol(gene)
 if newGene:
  trueGenes.add(newGene)
 newGene = searchAliasSymbol(gene)
 if newGene:
  trueGenes.add(newGene)
 newGene = searchAliasName(gene)
 if newGene:
  trueGenes.add(newGene)
 return trueGenes

def fetchEnsemblGeneIdForGeneSymbol(gene):
 url = 'http://rest.genenames.org/fetch/symbol/%s' % (gene,)
 headers = {
  'Accept': 'application/json',
 }
 target = urlparse(url)
 method = 'GET'
 body = ''
 
 h = http.Http()
 
 response, content = h.request(
  target.geturl(),
  method,
  body,
  headers)
 ensGene = ''
 if response['status'] == '200':
  # assume that content is a json reply
  # parse content with the json module 
  data = json.loads(content)
  if data['response']['docs']:
   ensGene = data['response']['docs'][0]['ensembl_gene_id']
  return ensGene

def searchPreviousSymbol(gene):
 """What is the current symbol for this gene symbol?
    A current gene symbol will yield nothing."""
 url = 'http://rest.genenames.org/search/prev_symbol/%s' % (gene,)
 headers = {
  'Accept': 'application/json',
 }
 target = urlparse(url)
 method = 'GET'
 body = ''
 
 h = http.Http()
 
 response, content = h.request(
  target.geturl(),
  method,
  body,
  headers)
 newGene = ''
 if response['status'] == '200':
  # assume that content is a json reply
  # parse content with the json module 
  data = json.loads(content)
  if data['response']['docs']:
   newGene = data['response']['docs'][0]['symbol']
 time.sleep(2)
 return newGene 

def searchAliasSymbol(gene):
 """What is the current symbol for this alias gene?"""
 url = 'http://rest.genenames.org/search/alias_symbol/%s' % (gene,)
 headers = {
  'Accept': 'application/json',
 }
 target = urlparse(url)
 method = 'GET'
 body = ''
 
 h = http.Http()
 
 response, content = h.request(
  target.geturl(),
  method,
  body,
  headers)
 newGene = ''
 if response['status'] == '200':
  # assume that content is a json reply
  # parse content with the json module 
  data = json.loads(content)
  if data['response']['docs']:
   newGene = data['response']['docs'][0]['symbol']
 time.sleep(2)
 return newGene 

def searchAliasName(gene):
 """What is the current symbol for this alias gene?"""
 url = 'http://rest.genenames.org/search/alias_name/%s' % (gene,)
 headers = {
  'Accept': 'application/json',
 }
 target = urlparse(url)
 method = 'GET'
 body = ''
 
 h = http.Http()
 
 response, content = h.request(
  target.geturl(),
  method,
  body,
  headers)
 newGene = ''
 if response['status'] == '200':
  # assume that content is a json reply
  # parse content with the json module 
  data = json.loads(content)
  if data['response']['docs']:
   newGene = data['response']['docs'][0]['symbol']
 time.sleep(2)
 return newGene 

#print( searchPreviousSymbol('ADAM1') )
#print( searchPreviousSymbol('BRAF') )
#print( searchSymbol('RBM5-AS1') )
#print( findTrueGeneSymbol('LUST') )
