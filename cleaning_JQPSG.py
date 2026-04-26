# Title: Cleaning of Grammar 'Japanese Question & Positive Sentences Grammar' [JQPSG]
# Author: Rodrigo Hurtado 
# Student ID: A01713854 

# Description: Usage of the Natural Language Processing Toolkit in Python
# to demostrate the ambiguity and left recursion present in the original 
# JQPSG.

# Introduction of the test sentence (correct sentence)
sentence = "ima ni saito-san to mariko-san ha niwa de takai kaban wo kaimasu ka"

# 1. Original Japanese Question & Positive Sentence Grammar 

# Left recursion: T -> T 'ni' | EMPTY | ...
# Ambiguity:    N -> E 'to' N | E
#               E -> M | C | N

import nltk
from nltk import CFG

nltk.download('punkt_tab')

print('===== 1. Original Japanese Question & Positive Sentence Grammar =====')

# Definition of the context-free grammar - JQPSG
grammar = CFG.fromstring("""
    S -> T H F A
    A -> 'ka' |
    T -> T 'ni' | 'ima' | 'kyou' | 'ashita' |
    H -> N 'ha'
    N -> E 'to' N | E
    E -> M | C | N
    M -> 'saito-san' | 'mariko-san' | 'mira-san' | 'santos-san' | 'sakura-san' | 'juan-san' | 'alexis-san' | 'rodrigo-san' | 'nico-san' | 'diego-san' | 'watashi' | 'anata'
    C -> 'gakusei' | 'sensei' | 'isha' | 'keikan' | 'shioubashi'
    F -> P J
    P -> K 'de' |
    K -> 'kouen' | 'niwa' | 'daigaku' | 'ichiba' | 'ginkou' | 'kiisaten' | 'umi' | 'konbini'
    J -> O 'wo' V | O 'ikura' 'desu'
    O -> B W X | W X
    B -> 'kono' | 'sono' | 'ano'
    W -> N 'no' |
    X -> D G | G
    D -> 'kawaii' | 'ookii' | 'chiisai' | 'yasai' | 'takai'
    G -> 'hon' | 'koohi' | 'nooto' | 'zaashi' | 'kasa' | 'kaban' | 'kuruma' | 'terebi' | 'wain'
    V -> 'kaimasu' | 'misemasu' | 'mimasu' | 'agemasu' | 'kashimasu' | 'hoshiimasu' | 'urimasu' | 'hakobimasu' | 'sutemasu'
""")

# Parser creation with the given grammar.
parser = nltk.ChartParser(grammar, trace=0)

# Tokenization of the sentence.
tokens = nltk.word_tokenize(sentence, language='english')

# Creation of the tree by parsing the tokenized sentence with the grammar.
trees = list(parser.parse(tokens))

# Printing of the trees if any.
if trees:
    print(f"Found {len(trees)} parse tree(s):\n")
    for i, tree in enumerate(trees):
        print(f"--- Tree {i+1} ---")

        # Actual print of the parse tree
        tree.pretty_print()
        print()


# 2. Clearning Japanese Question & Positive Sentence Grammar Part 1. Elimination of Left Recursion

# Remaining Ambiguity:  N -> E 'to' N | E
#                       E -> M | C | N


print('==== 2. Clearning Part 1. Elimination of Left Recursion =====')
grammar = CFG.fromstring("""
    S -> T H F A
    A -> 'ka' |
    T -> 'ima' I | 'kyou' I | 'ashita' I |
    I -> 'ni'|    
    H -> N 'ha'
    N -> E 'to' N | E
    E -> M | C | N
    M -> 'saito-san' | 'mariko-san' | 'mira-san' | 'santos-san' | 'sakura-san' | 'juan-san' | 'alexis-san' | 'rodrigo-san' | 'nico-san' | 'diego-san' | 'watashi' | 'anata'
    C -> 'gakusei' | 'sensei' | 'isha' | 'keikan' | 'shioubashi'
    F -> P J
    P -> K 'de' |
    K -> 'kouen' | 'niwa' | 'daigaku' | 'ichiba' | 'ginkou' | 'kiisaten' | 'umi' | 'konbini'
    J -> O 'wo' V | O 'ikura' 'desu'
    O -> B W X | W X
    B -> 'kono' | 'sono' | 'ano'
    W -> N 'no' |
    X -> D G | G
    D -> 'kawaii' | 'ookii' | 'chiisai' | 'yasai' | 'takai'
    G -> 'hon' | 'koohi' | 'nooto' | 'zaashi' | 'kasa' | 'kaban' | 'kuruma' | 'terebi' | 'wain'
    V -> 'kaimasu' | 'misemasu' | 'mimasu' | 'agemasu' | 'kashimasu' | 'hoshiimasu' | 'urimasu' | 'hakobimasu' | 'sutemasu'
""")

parser = nltk.ChartParser(grammar, trace=0)
trees = list(parser.parse(tokens))

if trees:
    print(f"Found {len(trees)} parse tree(s):\n")
    for i, tree in enumerate(trees):
        print(f"--- Tree {i+1} ---")
        tree.pretty_print()
        print()

# 3. Clearning Japanese Question & Positive Sentence Grammar Part 2. Elimination of Ambiguity

# No remaining ambiguity


print('==== 3. Clearning Part 2. Elimination of Ambiguity =====')
grammar = CFG.fromstring("""
    S -> T H F A
    A -> 'ka' |
    T -> 'ima' I | 'kyou' I | 'ashita' I |
    I -> 'ni' |    
    H -> N 'ha'
    N -> M E | C E
    E -> 'to' M E | 'to' C E | 
    M -> 'saito-san' | 'mariko-san' | 'mira-san' | 'santos-san' | 'sakura-san' | 'juan-san' | 'alexis-san' | 'rodrigo-san' | 'nico-san' | 'diego-san' | 'watashi' | 'anata'
    C -> 'gakusei' | 'sensei' | 'isha' | 'keikan' | 'shioubashi'
    F -> P J
    P -> K 'de' |
    K -> 'kouen' | 'niwa' | 'daigaku' | 'ichiba' | 'ginkou' | 'kiisaten' | 'umi' | 'konbini'
    J -> O 'wo' V | O 'ikura' 'desu'
    O -> B W X | W X
    B -> 'kono' | 'sono' | 'ano'
    W -> N 'no' |
    X -> D G | G
    D -> 'kawaii' | 'ookii' | 'chiisai' | 'yasai' | 'takai'
    G -> 'hon' | 'koohi' | 'nooto' | 'zaashi' | 'kasa' | 'kaban' | 'kuruma' | 'terebi' | 'wain'
    V -> 'kaimasu' | 'misemasu' | 'mimasu' | 'agemasu' | 'kashimasu' | 'hoshiimasu' | 'urimasu' | 'hakobimasu' | 'sutemasu'
""")

parser = nltk.ChartParser(grammar, trace=0)
trees = list(parser.parse(tokens))

if trees:
    print(f"Found {len(trees)} parse tree(s):\n")
    for i, tree in enumerate(trees):
        print(f"--- Tree {i+1} ---")
        tree.pretty_print()
        print()

