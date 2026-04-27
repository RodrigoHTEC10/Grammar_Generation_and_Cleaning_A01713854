# Title: Final Grammar 'Japanese Polar Question Grammar' [JPQG]
# Author: Rodrigo Hurtado 
# Student ID: A01713854 

# Usage of the Natural Language Processing Toolkit (Demostration of Functionallity 1 / 2)

# Description: Final version of the JPQG result from the cleaning of the left recursion
# and ambiguity introduced. 
# The demostration of this will be given by printing the parsing tree of the test sentence.
# Afterwards, testing of the valid and invalid sentences will print in console the number
# of parser trees obtained per sentence if valid, else invalid.

# Introducing the testing sentences: 25 valid sentences and 25 invalid sentences

valid_sentences = [
    # Simple sentences — no time, single noun
    "saito-san ha kono kaban wo kaimasu ka",
    "mariko-san ha sono hon wo mimasu ka",
    "mira-san ha ano koohi wo hoshiimasu ka",
    "watashi ha kono nooto wo kaimasu ka",
    "anata ha sono wain wo kaimasu ka",

    # With time — ima, kyou, ashita
    "ima saito-san ha kono hon wo kaimasu ka",
    "ashita ni mariko-san ha sono koohi wo kaimasu ka",
    "ima ni watashi ha ano kaban wo kaimasu ka",
    "kyou sensei ha kono nooto wo misemasu ka",
    "kyou ni gakusei ha sono terebi wo mimasu ka",

    # With time + place 
    "kyou saito-san ha ichiba de kono kaban wo kaimasu ka",
    "ima ni watashi ha daigaku de sono hon wo mimasu ka",
    "ashita mariko-san ha umi de ano koohi wo kaimasu ka",
    "kyou ni sensei ha ginkou de nooto wo misemasu ka",
    "ashita ni isha ha umi de sono kuruma wo mimasu ka",

    # With place + adjective
    "saito-san ha niwa de takai kaban wo kaimasu ka",
    "mariko-san ha kouen de kawaii hon wo mimasu ka",
    "watashi ha daigaku de ookii nooto wo kaimasu ka",
    "sensei ha ichiba de chiisai koohi wo kaimasu ka",
    "isha ha konbini de yasai kaban wo kaimasu ka",

    # Multiple nouns — to particle
    "saito-san to mariko-san ha kono kaban wo kaimasu ka",
    "watashi to anata ha sono hon wo mimasu ka",
    "sensei to gakusei ha ano nooto wo kaimasu ka",
    "isha to keikan ha kono kuruma wo mimasu ka",
    "saito-san to mariko-san to mira-san ha kono kaban wo kaimasu ka",

    # With adjective
    "saito-san ha takai kaban wo kaimasu ka",
    "mariko-san ha kawaii hon wo mimasu ka",
    "watashi ha ookii nooto wo kaimasu ka",
    "sensei ha chiisai koohi wo kaimasu ka",
    "isha ha yasai kaban wo kaimasu ka",

    # With simple possesive
    "saito-san ha kono watashi no kaban wo kaimasu ka",
    "mariko-san ha sono saito-san no hon wo mimasu ka",
    "mira-san ha ano sensei no koohi wo hoshiimasu ka",
    "watashi ha alexis-san no nooto wo kaimasu  ka",
    "anata ha sono keikan no wain wo kaimasu  ka",

    # With collective possesive
    "saito-san ha kono watashi to anata no kaban wo kaimasu ka",
    "mariko-san ha sono saito-san to mariko-san to nico-san no hon wo mimasu ka",
    "mira-san ha ano sensei to isha to rodrigo-san no koohi wo hoshiimasu ka",
    "watashi ha alexis-san to diego-san no nooto wo kaimasu ka",
    "nico-san ha sono keikan to isha no wain wo kaimasu ka",

    # With time + place + possesive + adjective
    "rodrigo-san ha konbini de kono watashi no chiisai kaban wo kaimasu ka",
    "nico-san ha daigaku de sono saito-san no yasai hon wo mimasu ka",
    "mariko-san ha ginkou de sono saito-san no takai hon wo mimasu ka",
    "watashi ha niwa de alexis-san to diego-san no ookii nooto wo kaimasu ka",
    "nico-san ha ichiba de sono keikan to isha no kawaii zaashi wo kaimasu ka",

    # With place + possesive + adjective
    "rodrigo-san ha konbini de kono watashi no chiisai kaban wo kaimasu ka",
    "nico-san ha daigaku de sono saito-san no yasai hon wo mimasu ka",
    "mariko-san ha ginkou de sono saito-san no takai hon wo mimasu ka",
    "watashi ha niwa de alexis-san to diego-san no ookii nooto wo kaimasu ka",
    "nico-san ha ichiba de sono keikan to isha no kawaii zaashi wo kaimasu ka",

    # With time + place + possesive + adjective
    "ima rodrigo-san ha konbini de kono watashi no chiisai kaban wo kaimasu ka",
    "kyou nico-san ha daigaku de sono saito-san no yasai hon wo mimasu ka",
    "ashita ni mariko-san ha ginkou de sono saito-san no takai hon wo mimasu ka",
    "ima ni watashi ha niwa de alexis-san to diego-san no ookii nooto wo kaimasu ka",
    "kyou ni nico-san ha ichiba de sono keikan to isha no kawaii zaashi wo kaimasu ka",
]

# Reasons for being invalid. 
# 1. Usage of words not available in the JQPSG.
# 2. Incorrect order of words in the sentence.
#   2.1 Incorrect word with incorrect particle.
# 3. Lack of required particle.
# 4. Absence of required section as H (noun) or O (object of the verb).

invalid_sentences = [
    # 1. Words not in grammar
    "saito-san ha kono ringo wo kaimasu ka",  # ringo not in G
    "mariko-san ha sono pan wo mimasu ka",
    "watashi ha kono sushi wo kaimasu ka",
    "anata ha pizza wo tabemasu ka",
    "ima saito-san ha kono juice wo kaimasu ka",

    # 2. Incorrect word order
    "ha saito-san kono kaban wo kaimasu ka",
    "saito-san kono ha kaban wo kaimasu ka",
    "saito-san ha wo kono kaban kaimasu ka",
    "kono kaban saito-san ha wo kaimasu ka",
    "saito-san ha kaban kono wo kaimasu ka",

    # 2.1 Incorrect particle usage
    "saito-san ga kono kaban wo kaimasu ka",   # ga not allowed
    "mariko-san ha kono hon ga mimasu ka",     # ga instead of wo
    "watashi ha kono nooto ni kaimasu ka",     # ni instead of wo
    "anata ha kono kaban de kaimasu ka",       # de instead of wo
    "saito-san ha kono hon wo ni kaimasu ka",  # extra particle

    # 3. Missing required particles
    "saito-san kono kaban wo kaimasu ka",      # missing ha
    "mariko-san ha kono hon kaimasu ka",       # missing wo
    "watashi ha kono nooto kaimasu ka",
    "anata ha kono kaban mimasu ka",
    "saito-san to mariko-san kono kaban wo kaimasu ka",

    # 4. Missing required sections (H or O)
    "ima kono kaban wo kaimasu ka",            # missing H
    "saito-san ha kaimasu ka",                 # missing O
    "kyou ha kono hon wo mimasu ka",           # missing noun before ha
    "ashita ni ha kono kaban wo kaimasu ka",   # missing H noun
    "watashi ha",                           # missing F

    # Mixed structural errors
    "ima ni ni saito-san ha kono kaban wo kaimasu ka",
    "kyou saito-san ha de kono kaban wo kaimasu ka",
    "ashita ni mariko-san ha kono kaban de wo kaimasu ka",
    "watashi ha kono kaban wo wo kaimasu ka",
    "anata ha kono kaban kaimasu wo",

    # Invalid noun phrase constructions
    "saito-san ha kono no kaban wo kaimasu ka",   # 'no' misplaced
    "mariko-san ha no hon wo mimasu ka",
    "watashi ha kono saito-san kaban wo kaimasu ka",
    "anata ha kono watashi kaban wo kaimasu ka",
    "saito-san ha kono kaban no wo kaimasu ka",

    # Invalid adjective placement
    "saito-san ha kaban takai wo kaimasu ka",
    "mariko-san ha hon kawaii wo mimasu ka",
    "watashi ha nooto ookii wo kaimasu ka",
    "anata ha kaban chiisai wo kaimasu ka",
    "saito-san ha kaban yasai wo kaimasu ka",

    # Incorrect verb placement
    "saito-san ha kaimasu kono kaban wo",
    "mariko-san ha mimasu sono hon wo",
    "watashi ha kaimasu kono nooto wo",
    "anata ha hoshiimasu ano koohi wo",
    "saito-san ha kaimasu kaban wo",

    # Broken coordination (E rules)
    "saito-san to ha mariko-san kono kaban wo kaimasu ka",
    "watashi to anata to ha kono hon wo mimasu ka",
    "saito-san to to mariko-san ha kono kaban wo kaimasu ka",
    "saito-san mariko-san to ha kono kaban wo kaimasu ka",
    "to saito-san mariko-san ha kono kaban wo kaimasu ka",

    # Time misuse
    "ima ima saito-san ha kono kaban wo kaimasu ka",
    "kyou ashita saito-san ha kono kaban wo kaimasu ka",
    "ashita ima ni saito-san ha kono kaban wo kaimasu ka",
    "ima de saito-san ha kono kaban wo kaimasu ka",
    "kyou wo saito-san ha kono kaban wo kaimasu ka",

    # Place misuse
    "saito-san ha de kono kaban wo kaimasu ka",
    "mariko-san ha kouen kono kaban wo kaimasu ka",
    "watashi ha konbini ni kono kaban wo kaimasu ka",
    "anata ha daigaku kono kaban wo kaimasu ka",
    "saito-san ha ichiba wo kono kaban kaimasu ka",
]

# Tree sentence

sentence = "saito-san to mariko-san ha niwa de takai kaban wo kaimasu ka"

import nltk
from nltk import CFG

nltk.download('punkt_tab')

# Corrected grammar JQPSG
grammar = CFG.fromstring("""
    S -> T H F A
    A -> 'ka'
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

