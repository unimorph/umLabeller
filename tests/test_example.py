from umLabeller.src import UniMorphLabeller

def test_labeller():
    #file_path= '../data/eng.word.full.230613.r7.tsv'
    # BERT Tokenizer example
    uml = UniMorphLabeller()
    assert uml.auto_classify('Ġswappiness', ['Ġswap', 'pi', 'ness']) == 'morph'
    
    # ALBERT Tokenizer example
    uml.setKey('▁')
    assert uml.auto_classify('hiked', ['▁h', 'iked']) == 'alien'