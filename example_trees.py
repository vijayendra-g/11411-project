from nltk.tree import Tree

# John ate a burrito in the park.
S1 = Tree.fromstring('(ROOT (S (NP (NNP John)) (VP (VBD ate) (NP (DT a) (NN burrito)) (PP (IN in) (NP (DT the) (NN park)))) (. .)))')
# John, a doctor, treated him.
S2 = Tree.fromstring('(ROOT (S (NP (NP (NNP John)) (, ,) (NP (DT a) (NN doctor)) (, ,)) (VP (VBD treated) (NP (PRP him))) (. .)))')
# I saw 10,000 people in the yard.
S3 = Tree.fromstring('(ROOT (S (NP (PRP I)) (VP (VBD saw) (NP (CD 10,000) (NNS people)) (PP (IN in) (NP (DT the) (NN yard)))) (. .)))')
# 10 people ate outside.
S4 = Tree.fromstring('(ROOT (S (NP (CD 10) (NNS people)) (VP (VBD ate) (ADVP (RB outside))) (. .)))')
# John ate in the park slowly.
S5 = Tree.fromstring('(ROOT (S (NP (NNP John)) (VP (VBD ate) (PP (IN in) (NP (DT the) (NN park))) (ADVP (RB slowly))) (. .)))')
# John ate because you did.
S6 = Tree.fromstring('(ROOT (S (NP (NNP John)) (VP (VBD ate) (SBAR (IN because) (S (NP (PRP you)) (VP (VBD did))))) (. .)))')
# John Smith went to Virginia to fight in December 1780.
S7 = Tree.fromstring('(ROOT (S (NP (NNP John) (NNP Smith)) (VP (VBD went) (PP (TO to) (NP (NNP Virginia))) (S (VP (TO to) (VP (VB fight) (PP (IN in) (NP (NNP December) (CD 1780))))))) (.  .)))') 
# John Smith ate potatoes on Tuesday.
S8 = Tree.fromstring('(ROOT (S (NP (NNP John) (NNP Smith)) (VP (VBD ate) (NP (NNS potatoes)) (PP (IN on) (NP (NNP Tuesday)))) (. .)))')
# The green old potatoes are cool.
S9 = Tree.fromstring('(ROOT (S (NP (DT The) (JJ green) (JJ old) (NNS potatoes)) (VP (VBP are) (ADJP (JJ cool))) (. .)))')
# John ate the potatoes.
S10 = Tree.fromstring('(ROOT (S (NP (NNP John)) (VP (VBD ate) (NP (DT the) (NNS potatoes))) (. .)))')
# John ate the green potatoes.
S11 = Tree.fromstring('(ROOT (S (NP (NNP John)) (VP (VBD ate) (NP (DT the) (JJ green) (NNS potatoes))) (. .)))')
# Those books are for John Smith.
S12 = Tree.fromstring('(ROOT (S (NP (DT Those) (NNS books)) (VP (VBP are) (PP (IN for) (NP (NNP John) (NNP Smith)))) (. .)))')
# George Green took the order for John Smith.
S13 = Tree.fromstring('(ROOT (S (NP (NNP George) (NNP Green)) (VP (VBD took) (NP (DT the) (NN order)) (PP (IN for) (NP (NNP John) (NNP Smith)))) (. .)))')
# John took the dog to New York.
S14 = Tree.fromstring('(ROOT (S (NP (NNP John)) (VP (VBD took) (NP (DT the) (NN dog)) (PP (TO to) (NP (NNP New) (NNP York)))) (. .)))')
# John took the dog in 1940.
S15 = Tree.fromstring('(ROOT (S (NP (NNP John)) (VP (VBD took) (NP (DT the) (NN dog)) (PP (IN in) (NP (CD 1940)))) (. .)))')
# John read the book to his youngest children.
S16 = Tree.fromstring('(ROOT (S (NP (NNP John)) (VP (VBD read) (NP (DT the) (NN book)) (PP (TO to) (NP (PRP$ his) (JJS youngest) (NNS children)))) (. .)))')


# Did John eat a burrito in the park?
Q1 = Tree.fromstring('(ROOT (SQ (VBD Did) (NP (NNP John)) (VP (VB eat) (NP (NP (DT a) (NN burrito)) (PP (IN in) (NP (DT the) (NN park))))) (. ?)))')
# Is John a doctor?
Q2 = Tree.fromstring('(ROOT (SQ (VBZ Is) (NP (NNP John)) (NP (DT a) (NN doctor)) (. ?)))')
