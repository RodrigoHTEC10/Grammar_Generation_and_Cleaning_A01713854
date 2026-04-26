# Title: Final Grammar 'Japanese Question & Positive Sentences Grammar' [JQPSG]
# Author: Rodrigo Hurtado 
# Student ID: A01713854 

# Usage of the Natural Language Processing Toolkit (Demostration of Functionallity 1 / 2)

# Description: Final version of the JQPSG result from the cleaning of the left recursion
# and ambiguity introduced. 
# The demostration of this will be given by printing the parsing tree of the test sentence.
# Afterwards, testing of the valid and invalid sentences will print in console the number
# of parser trees obtained per sentence if valid, else invalid.

# Introducing the testing sentences: 25 valid sentences and 25 invalid sentences

valid_sentences = [
    # Simple sentences — no time, single noun
    "saito-san ha kono kaban wo kaimasu",
    "mariko-san ha sono hon wo mimasu",
    "mira-san ha ano koohi wo hoshiimasu",
    "watashi ha kono nooto wo kaimasu",
    "anata ha sono wain wo kaimasu",

    # With time — ima, kyou, ashita
    "ima saito-san ha kono hon wo kaimasu",
    "ashita ni mariko-san ha sono koohi wo kaimasu",
    "ima ni watashi ha ano kaban wo kaimasu",
    "kyou sensei ha kono nooto wo misemasu",
    "kyou ni gakusei ha sono terebi wo mimasu",

    # With time + place 
    "kyou saito-san ha ichiba de kono kaban wo kaimasu ka",
    "ima ni watashi ha daigaku de sono hon wo mimasu",
    "ashita mariko-san ha umi de ano koohi wo kaimasu ka",
    "kyou ni sensei ha ginkou de nooto wo misemasu",
    "ashita ni isha ha umi de sono kuruma wo mimasu ka",

    # With place + adjective
    "saito-san ha niwa de takai kaban wo kaimasu ka",
    "mariko-san ha kouen de kawaii hon wo mimasu ka",
    "watashi ha daigaku de ookii nooto wo kaimasu",
    "sensei ha ichiba de chiisai koohi wo kaimasu ka",
    "isha ha konbini de yasai kaban wo kaimasu",

    # Multiple nouns — to particle
    "saito-san to mariko-san ha kono kaban wo kaimasu ka",
    "watashi to anata ha sono hon wo mimasu",
    "sensei to gakusei ha ano nooto wo kaimasu",
    "isha to keikan ha kono kuruma wo mimasu ka",
    "saito-san to mariko-san to mira-san ha kono kaban wo kaimasu ka",

    # With adjective
    "saito-san ha takai kaban wo kaimasu ka",
    "mariko-san ha kawaii hon wo mimasu ka",
    "watashi ha ookii nooto wo kaimasu",
    "sensei ha chiisai koohi wo kaimasu ka",
    "isha ha yasai kaban wo kaimasu",

    # With simple possesive
    "saito-san ha kono watashi no kaban wo kaimasu",
    "mariko-san ha sono saito-san no hon wo mimasu",
    "mira-san ha ano sensei no koohi wo hoshiimasu",
    "watashi ha alexis-san no nooto wo kaimasu",
    "anata ha sono keikan no wain wo kaimasu",

    # With collective possesive
    "saito-san ha kono watashi to anata no kaban wo kaimasu",
    "mariko-san ha sono saito-san to mariko-san to nico-san no hon wo mimasu",
    "mira-san ha ano sensei to isha to rodrigo-san no koohi wo hoshiimasu",
    "watashi ha alexis-san to diego-san no nooto wo kaimasu",
    "nico-san ha sono keikan to isha no wain wo kaimasu",

    # With time + place + possesive + adjective
    "rodrigo-san ha konbini de kono watashi no chiisai kaban wo kaimasu",
    "nico-san ha daigaku de sono saito-san no yasai hon wo mimasu",
    "mariko-san ha ginkou de sono saito-san no takai hon wo mimasu",
    "watashi ha niwa de alexis-san to diego-san no ookii nooto wo kaimasu",
    "nico-san ha ichiba de sono keikan to isha no kawaii zaashi wo kaimasu",

    # With place + possesive + adjective
    "rodrigo-san ha konbini de kono watashi no chiisai kaban wo kaimasu",
    "nico-san ha daigaku de sono saito-san no yasai hon wo mimasu",
    "mariko-san ha ginkou de sono saito-san no takai hon wo mimasu",
    "watashi ha niwa de alexis-san to diego-san no ookii nooto wo kaimasu",
    "nico-san ha ichiba de sono keikan to isha no kawaii zaashi wo kaimasu",

    # With time + place + possesive + adjective
    "ima rodrigo-san ha konbini de kono watashi no chiisai kaban wo kaimasu",
    "kyou nico-san ha daigaku de sono saito-san no yasai hon wo mimasu",
    "ashita ni mariko-san ha ginkou de sono saito-san no takai hon wo mimasu",
    "ima ni watashi ha niwa de alexis-san to diego-san no ookii nooto wo kaimasu",
    "kyou ni nico-san ha ichiba de sono keikan to isha no kawaii zaashi wo kaimasu",
]

# Reasons for being invalid. 
# 1. Usage of words not available in the JQPSG.
# 2. Incorrect order of words in the sentence.
#   2.1 Incorrect word with incorrect particle.
# 3. Lack of required particle.
# 4. Absence of required section as H (noun) or O (object of the verb).

invalid_sentences = [
    # 1. Words not in grammar
    "saito-san ha kono ringo wo kaimasu",  # ringo not in G
    "mariko-san ha sono pan wo mimasu",
    "watashi ha kono sushi wo kaimasu",
    "anata ha pizza wo tabemasu",
    "ima saito-san ha kono juice wo kaimasu",

    # 2. Incorrect word order
    "ha saito-san kono kaban wo kaimasu",
    "saito-san kono ha kaban wo kaimasu",
    "saito-san ha wo kono kaban kaimasu",
    "kono kaban saito-san ha wo kaimasu",
    "saito-san ha kaban kono wo kaimasu",

    # 2.1 Incorrect particle usage
    "saito-san ga kono kaban wo kaimasu",   # ga not allowed
    "mariko-san ha kono hon ga mimasu",     # ga instead of wo
    "watashi ha kono nooto ni kaimasu",     # ni instead of wo
    "anata ha kono kaban de kaimasu",       # de instead of wo
    "saito-san ha kono hon wo ni kaimasu",  # extra particle

    # 3. Missing required particles
    "saito-san kono kaban wo kaimasu",      # missing ha
    "mariko-san ha kono hon kaimasu",       # missing wo
    "watashi ha kono nooto kaimasu",
    "anata ha kono kaban mimasu",
    "saito-san to mariko-san kono kaban wo kaimasu",

    # 4. Missing required sections (H or O)
    "ima kono kaban wo kaimasu",            # missing H
    "saito-san ha kaimasu",                 # missing O
    "kyou ha kono hon wo mimasu",           # missing noun before ha
    "ashita ni ha kono kaban wo kaimasu",   # missing H noun
    "watashi ha",                           # missing F

    # Mixed structural errors
    "ima ni ni saito-san ha kono kaban wo kaimasu",
    "kyou saito-san ha de kono kaban wo kaimasu",
    "ashita ni mariko-san ha kono kaban de wo kaimasu",
    "watashi ha kono kaban wo wo kaimasu",
    "anata ha kono kaban kaimasu wo",

    # Invalid noun phrase constructions
    "saito-san ha kono no kaban wo kaimasu",   # 'no' misplaced
    "mariko-san ha no hon wo mimasu",
    "watashi ha kono saito-san kaban wo kaimasu",
    "anata ha kono watashi kaban wo kaimasu",
    "saito-san ha kono kaban no wo kaimasu",

    # Invalid adjective placement
    "saito-san ha kaban takai wo kaimasu",
    "mariko-san ha hon kawaii wo mimasu",
    "watashi ha nooto ookii wo kaimasu",
    "anata ha kaban chiisai wo kaimasu",
    "saito-san ha kaban yasai wo kaimasu",

    # Incorrect verb placement
    "saito-san ha kaimasu kono kaban wo",
    "mariko-san ha mimasu sono hon wo",
    "watashi ha kaimasu kono nooto wo",
    "anata ha hoshiimasu ano koohi wo",
    "saito-san ha kaimasu kaban wo",

    # Broken coordination (E rules)
    "saito-san to ha mariko-san kono kaban wo kaimasu",
    "watashi to anata to ha kono hon wo mimasu",
    "saito-san to to mariko-san ha kono kaban wo kaimasu",
    "saito-san mariko-san to ha kono kaban wo kaimasu",
    "to saito-san mariko-san ha kono kaban wo kaimasu",

    # Time misuse
    "ima ima saito-san ha kono kaban wo kaimasu",
    "kyou ashita saito-san ha kono kaban wo kaimasu",
    "ashita ima ni saito-san ha kono kaban wo kaimasu",
    "ima de saito-san ha kono kaban wo kaimasu",
    "kyou wo saito-san ha kono kaban wo kaimasu",

    # Place misuse
    "saito-san ha de kono kaban wo kaimasu",
    "mariko-san ha kouen kono kaban wo kaimasu",
    "watashi ha konbini ni kono kaban wo kaimasu",
    "anata ha daigaku kono kaban wo kaimasu",
    "saito-san ha ichiba wo kono kaban kaimasu",
]

# Tree sentence

sentence = "saito-san to mariko-san ha niwa de takai kaban wo kaimasu ka"

import nltk
from nltk import CFG

nltk.download('punkt_tab')

# Corrected grammar JQPSG
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
tokens = nltk.word_tokenize(sentence, language='english')
trees = list(parser.parse(tokens))

if trees:
    print(f"Found {len(trees)} parse tree(s):\n")
    for i, tree in enumerate(trees):
        print(f"--- Tree {i+1} ---")
        tree.pretty_print()
        print()

counter = 0
rej_counter = 0

print("=============== APPROVED SENTENCES ===============\n")
for ele in valid_sentences:
    try:
        tokens = nltk.word_tokenize(ele, language='english')
        trees = list(parser.parse(tokens))
        if (len(trees) == 1):
            counter = counter + 1
            print(f"APPROVED: {ele}")
        else:
            rej_counter = rej_counter + 1
            print(f"REJECTED: {ele} Found {len(trees)} parse tree(s)")
    except:
        rej_counter = rej_counter + 1
        print(f"REJECTED IN PROCESSING: {ele} Not able to parse.")

print()
print(f"Approved sentences: {counter} / {len(valid_sentences)}")
print(f"Rejected sentences: {rej_counter} / {len(valid_sentences)}")



counter = 0
rej_counter = 0

print()
print("=============== REJECTED SENTENCES ===============\n")
print()

for ele in invalid_sentences:
    try:
        tokens = nltk.word_tokenize(ele, language='english')
        trees = list(parser.parse(tokens))
        if (len(trees) == 1):
            counter = counter + 1
            print(f"APPROVED: {ele}")
        else:
            rej_counter = rej_counter + 1
            print(f"REJECTED: {ele} Found {len(trees)} parse tree(s)")
    except:
        rej_counter = rej_counter + 1
        print(f"REJECTED IN PROCESSING: {ele} Not able to parse.")

print()
print(f"Approved sentences: {counter} / {len(invalid_sentences)}")
print(f"Approved sentences: {rej_counter} / {len(invalid_sentences)}")

