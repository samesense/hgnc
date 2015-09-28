import hgnc, nose.tools

def testSearchSymbol():
    nose.tools.assert_equal(hgnc.fetchEnsemblGeneIdForGeneSymbol('RBM5-AS1'),
                            'ENSG00000281691')

def testFindTrueGeneSymbol():
    nose.tools.assert_equal(list(hgnc.findTrueGeneSymbol('LUST'))[0],
                            'RBM5-AS1')
    
