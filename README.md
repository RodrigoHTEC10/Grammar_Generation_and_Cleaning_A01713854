# Evidence: Grammar Generation and Cleaning - TC2037 - Group 603

Author: Rodrigo Alejandro Hurtado Cortés - A01713854

Date: April 25th, 2026

<br>

# Introduction
A **Grammar** is a formal system that determines a set of rules for generating valid strings within a language. It plays an essential role in determining the syntactic correctness of languages, and forms the foundation for parsing and interpreting languages in the Theory of Computation. (Sudkamp, 1998)

To truly comprehend the previous definition, it is necessary to understand not only the elements that form a grammar and the process for determining the correctness of a given *string* (a sentence of a language), but also the definition of a language and its innermost relevance for the mentioned theory.

A **language** is the collection of all the available strings *w* over a finite alphabet **Σ**. This concept is key for the **Theory of Computation** as any given problem to a computer can be reduced to the question: *Does this string belong to this language?*. This is the foundation for the computer ability to understand and interpret any programming language, solve any arithmetic expression, or perform any other action.

The grammar *G(L)* is the system that the computer can apply to determine this correctness and afterwards generate valid strings of the supported language *L*. However, to understand the concept as a whole, its elements must be analyzed.

A grammar is composed of two concepts:
- **Terminal symbols** are the elements of the language.
```
'hello', 'bye', 'dog', 'cat', ...
```

- **Nonterminals** are intermediate symbols used during the construction of a string to enforce the syntactic relationships of the language.
```
noun -> 'dog', 'cat', 'I', 'you', ...
```

From these elements the **rules** or **productions** of the grammar are defined as the formal instructions of how a nonterminal symbol can be rewritten as a sequence of terminals and non-terminals.

To generate a string starting from the starting point of the grammar *S*, we perform a series of derivations using the defined productions of the grammar to substitute nonterminal symbols for other equivalent nonterminals or terminals until we end up with a valid string of the language. 

In a similar yet inverse process, to validate a string *w* belonging to a concrete language *L*, the grammar must determine if there is a series of derivations that lead from the starting point *S* to the actual string *w*.

The current evidence consist of the design of a *Context-Free Grammar*, its cleaning from left recursion and ambiguity to make it available to be parsed, the validation of its design through a testing using an LL(1) parser, a Top-Down non-recursive descent parser, a given explanation of the grammar placing in the Chomsky Hierarchy, and a time and space complexity analysis of the grammar in its original and final version.

Through the development of the evidence, the definition of more concepts and their connection to the previous mentioned topics will be opportunely presented, and  can be consulted from the mainly obtained source of *Languages and Machines - An introduction to Computer Science from Thomas A. Sudkamp*.

<br>

# Development

A **Context-Free Grammar** is a quadruple (V, Σ, P, S) where V is a finite set of variables (or non-terminal symbols), Σ (the alphabet) is a finite set of terminal symbols,  P is a finite set of rules (or productions), and S is a distinguished element of V called the start symbol. The set V and Σ are assumed to be disjoint. It is called *COntext-Free* as a rule can be applied to a variable whenever and wherever it occurs; context placing no limitation on the applicability of the rule. (Sudkamp, 1998)

For the creation of a grammar there are is one of two ways, either to create the grammar of a new language from beginning, or select an already created language and create a grammar that fits over its already declared structure and defined vocabulary. For the current evidence the second method was chosen, over the language of Japanese (日本語).

As Japanese is a complex and wide language, just a small section of it will be correctly represented, more specifically:
- Polar Questions in the polite form (丁寧形). 

As Japanese is very different from English or Spanish, the following section will be a brief introduction to the basics of Japanese in order to understand the designed grammar.
<br>

## Introduction to Japanese

The japanese writing system uses three scripts:

- Hiragana (ひらがな) phonetic script of 46 characters each representing a sound, that is used to write words, particles and conjugations.
- Katana (カタカナ) phonetic script of the same 46 characters of hiragana used to write foreign loanwords, onomatopoeia, scientific terms and foreign names.
- Kanji (患者 [かんじ]) logographic characters where each kanji represents one word or concept.

However, in this evidence, only romaji (ローマ字) will be used, which is the writting of japanese sounds in the Latin alphabet. This due to avoid problems during parsing and make a more understandable grammar.

### Sentence Structure

The basic sentence structure in Japanese has the form: SOV (Subject + Object + Verb) instead of the English or Spanish SVO (Subject + Verb + Object).

Example.
```
I eat sushi
私 (I) は 寿司 (sushi) を 食べます (eat)
```

### Particles

Particles are words that indicate the role of words within a sentence. These provide clarity over the subjects being treated and the overall context and construction of a sentence.

The particles being used in the created grammar are:

- は (wa | ha): Indicates the subject of the sentence.
- を (wo): Indicates the direct object of the verb.
- に (ni): Indicates the direction, destination, indirect object, or point in time (specific use in this grammar).
- で (de): Indicates the location where an action takes place.


### Politeness and Formality

Japanese grammar may suffer modifications depending the level of politeness or formality being applied to the situation or depending the people we are talking to. There are three levels of formallity:

- Plain Form (辞書形, Jisho-kei): Used with friends, family, or in informal settings.
- Polite Form (丁寧形, Teinei-kei): Used in everyday polite speech. This form is appropriate in most situations where respect is due.
- Honorific and Humble Forms (敬語, Keigo): Includes sonkeigo (respectful language), kenjougo (humble language), and teineigo (polite language). 

As mentioned before in this evidence the grammar will be in the Teinen-kei which is characterized for the verb termination of -masu (ます).


### Grammar focused particularities

In addition to the general context of Japanese, the following topics are good to know for the specific designed grammar:

1. **Posession**. The posession of an object to an owner is shown by the usage of the particle no (の), in the form: [owner]の[object]. Many people can be owners of the same object and as long as all of them are mentioned before the particle, the posession is understood for all of them.

2. **Connection**. To connect several people together, the particle to(と) is used in the following form: [person]と[person]と...と[person].

3. **Question**. In order to form a question from a positive sentence, it is neccesary to add the termination ka(か) at the end of the sentence.

4. **Adjectives**. There are two types of adjectives in Japanese i (-い) and na (-な). For easier use, only i-adjectives are used in this grammar, their particular form is the following: [adjective][noun].

<br>

## Japanese Polar Question Grammar
The designed grammar is called "Japanese Polar Question Grammar", but will be abbreviated as the JPQG.

Below, the original grammar with left recursion and ambiguity is presented:

<div align=center>

### Formal Grammar Definition

$$G = (V_T, V_N, S, R)$$

**$V_N$ — Non-terminal symbols**

$$V_N = \{ S, A, T, I, H, N, E, M, C, F, P, K, J, O, B, W, X, D, G, V \}$$

**$V_T$ — Terminal symbols**

| Category | Terminals |
|---|---|
| Particles | `ka` `ni` `ha` `to` `de` `wo` `no` |
| Time | `ima` `kyou` `ashita` |
| Names | `saito-san` `mariko-san` `mira-san` `santos-san` `sakura-san` `juan-san` `alexis-san` `rodrigo-san` `nico-san` `diego-san` `watashi` `anata` |
| Professions | `gakusei` `sensei` `isha` `keikan` `shioubashi` |
| Places | `kouen` `niwa` `daigaku` `ichiba` `ginkou` `kiisaten` `umi` `konbini` |
| Demonstratives | `kono` `sono` `ano` |
| Adjectives | `kawaii` `ookii` `chiisai` `yasai` `takai` |
| Objects | `hon` `koohi` `nooto` `zaashi` `kasa` `kaban` `kuruma` `terebi` `wain` |
| Verbs | `kaimasu` `misemasu` `mimasu` `agemasu` `kashimasu` `hoshiimasu` `urimasu` `hakobimasu` `sutemasu` |
| Expression | `ikura` `desu` |


**$S$ — Start symbol**

**$R$ — Production rules**

| Non-terminal | Production |
|---|---|
| $S$ | $\rightarrow T \ H \ F \ A$ |
| $A$ | $\rightarrow$ `ka` $\mid \varepsilon$ |
| $T$ | $\rightarrow T$ `ni` $\mid$ `ima` $\mid$ `kyou` $\mid$ `ashita` $\mid \varepsilon$ |
| $H$ | $\rightarrow N$ `ha` |
| $N$ | $\rightarrow E$ `to` $N \mid E$ |
| $E$ | $\rightarrow M \mid C$ |
| $M$ | $\rightarrow$ `saito-san` $\mid$ `mariko-san` $\mid$ `mira-san` $\mid$ `santos-san` $\mid$ `sakura-san` $\mid$ `juan-san` $\mid$ `alexis-san` $\mid$ `rodrigo-san` $\mid$ `nico-san` $\mid$ `diego-san` $\mid$ `watashi` $\mid$ `anata` |
| $C$ | $\rightarrow$ `gakusei` $\mid$ `sensei` $\mid$ `isha` $\mid$ `keikan` $\mid$ `shioubashi` |
| $F$ | $\rightarrow P \ J$ |
| $P$ | $\rightarrow K$ `de` $\mid \varepsilon$ |
| $K$ | $\rightarrow$ `kouen` $\mid$ `niwa` $\mid$ `daigaku` $\mid$ `ichiba` $\mid$ `ginkou` $\mid$ `kiisaten` $\mid$ `umi` $\mid$ `konbini` |
| $J$ | $\rightarrow O$ `wo` $V \mid O$ `ikura` `desu` |
| $O$ | $\rightarrow B \ W \ X \mid W \ X$ |
| $B$ | $\rightarrow$ `kono` $\mid$ `sono` $\mid$ `ano` |
| $W$ | $\rightarrow M$ `no` $\mid C$ `no` $\mid \varepsilon$ |
| $X$ | $\rightarrow D \ G \mid G$ |
| $D$ | $\rightarrow$ `kawaii` $\mid$ `ookii` $\mid$ `chiisai` $\mid$ `yasai` $\mid$ `takai` |
| $G$ | $\rightarrow$ `hon` $\mid$ `koohi` $\mid$ `nooto` $\mid$ `zaashi` $\mid$ `kasa` $\mid$ `kaban` $\mid$ `kuruma` $\mid$ `terebi` $\mid$ `wain` |
| $V$ | $\rightarrow$ `kaimasu` $\mid$ `misemasu` $\mid$ `mimasu` $\mid$ `agemasu` $\mid$ `kashimasu` $\mid$ `hoshiimasu` $\mid$ `urimasu` $\mid$ `hakobimasu` $\mid$ `sutemasu` |

</div>
<br>

### Allowed words
The designed grammar supports the following words used in the following categories:

<div align=center>

**Time Expressions (T)**
| Japanese | Romaji | English |
|---|---|---|
| 今 | ima | now |
| 今日 | kyou | today |
| 明日 | ashita | tomorrow |

<br>

**Names and Pronouns (M)**

| Japanese | Romaji | English |
|---|---|---|
| 斉藤さん | saito-san | Mr./Ms. Saito |
| 真理子さん | mariko-san | Mr./Ms. Mariko |
| ミラさん | mira-san | Mr./Ms. Mira |
| サントスさん | santos-san | Mr./Ms. Santos |
| 桜さん | sakura-san | Mr./Ms. Sakura |
| フアンさん | juan-san | Mr./Ms. Juan |
| アレクシスさん | alexis-san | Mr./Ms. Alexis |
| ロドリゴさん | rodrigo-san | Mr./Ms. Rodrigo |
| ニコさん | nico-san | Mr./Ms. Nico |
| ディエゴさん | diego-san | Mr./Ms. Diego |
| 私 | watashi | I / me |
| あなた | anata | you |

<br>

**Professions (C)**

| Japanese | Romaji | English |
|---|---|---|
| 学生 | gakusei | student |
| 先生 | sensei | teacher |
| 医者 | isha | doctor |
| 警官 | keikan | police officer |
| 塩橋 | shioubashi | Shioubashi (proper noun) |

<br>

**Places (K)**

| Japanese | Romaji | English |
|---|---|---|
| 公園 | kouen | park |
| 庭 | niwa | garden |
| 大学 | daigaku | university |
| 市場 | ichiba | market |
| 銀行 | ginkou | bank |
| 喫茶店 | kiisaten | coffee shop |
| 海 | umi | sea |
| コンビニ | konbini | convenience store |

<br>

**Demonstratives (B)**

| Japanese | Romaji | English |
|---|---|---|
| この | kono | this (near speaker) |
| その | sono | that (near listener) |
| あの | ano | that (far from both) |

<br>

**Adjectives (D)**

| Japanese | Romaji | English |
|---|---|---|
| 可愛い | kawaii | cute |
| 大きい | ookii | big |
| 小さい | chiisai | small |
| 安い | yasui | cheap |
| 高い | takai | expensive / tall |

<br>

**Objects (G)**

| Japanese | Romaji | English |
|---|---|---|
| 本 | hon | book |
| コーヒー | koohi | coffee |
| ノート | nooto | notebook |
| 雑誌 | zaashi | magazine |
| 傘 | kasa | umbrella |
| カバン | kaban | bag |
| 車 | kuruma | car |
| テレビ | terebi | television |
| ワイン | wain | wine |

<br>

**Verbs and Expressions (V)**

| Japanese | Romaji | English |
|---|---|---|
| 買います | kaimasu | to buy |
| 見せます | misemasu | to show |
| 見ます | mimasu | to see / watch |
| あげます | agemasu | to give |
| 貸します | kashimasu | to lend |
| 欲しいです | hoshiimasu | to want |
| 売ります | urimasu | to sell |
| 運びます | hakobimasu | to carry |
| 捨てます | sutemasu | to throw away |
| いくらですか | ikura desu ka | how much is it? |

<br>

**Particles**
| Particle | Usage |
|---|---|
|は| Subject |
|で| Place |
|に| Time |
|を| Direct Object |
|の| Posessive |
|か| Question |

</div>
<br>

### Allowed forms
Using the previous vocabulary, the Japanese Polar Question Grammar allows to create polar questions starting from a basic form and being able to add more information to it. Below, the forms and examples of them are presented for the reader to be aware of the capabilities of the grammar.

**Basic Form**
```
Subject + Object + Verb + ka (か)
saito-san ha kaban wo kaimasu ka
```

**Additional information**:
- Multiple subjects
```
Subject(s) + Object + Verb + ka (か)
saito-san to mariko-san hakaban wo kaimasu ka
```

- Add a time
```
Time + Subject(s) + Object + Verb + ka (か)
kyou saito-san to mariko-san ha kaban wo kaimasu ka
```

- Add a place 
```
Subject(s) + Place + Object + Verb + ka (か)
saito-san to mariko-san ha niwa de kaban wo kaimasu ka
```

- Add a possessive over the object of one or multiple subjects.
```
Subject(s) + Owner(s) + Object + Verb + ka (か)
saito-san to mariko-san ha rodrigo-san no kaban wo kaimasu ka
```

- Add an adjective to describe the object.
```
Subject + Adjective + Object + Verb + ka (か)
saito-san to mariko-san ha takai kaban wo kaimasu ka"
```

- Add a placement for the object 
```
Subject + Placement + Object + Verb + ka (か)
saito-san to mariko-san ha niwa de sono kaban wo kaimasu ka
```

The **complete** sentence or any other variation was long as it restects the previous placemenents is allowed:

```
Time + Subject + Place + Placement + Possessive + Adjective + Object + Verb + ka (か)
kyou saito-san to mariko-san ha niwa de sono rodrigo-san no takai kaban wo kaimasu ka
```
<br>

### Example.

Example sentence: kyou saito-san to mariko-san ha niwa de sono rodrigo-san no takai kaban wo kaimasu ka

<div align=center>

<img width="600" alt="Screenshot From 2026-04-26 22-29-56" src="https://github.com/user-attachments/assets/291f7bb1-76a0-4fea-83d2-f8db0d20cbbb" />
  
<img width="600" alt="Screenshot From 2026-04-26 22-30-14" src="https://github.com/user-attachments/assets/e7499ba5-1904-4e87-b65c-24c7cf5f02cb" />

</div>

## Cleaning
At this point the grammar is complete, yet it present some problems that make the parse of the grammar by a given string to find more than one path for

<br>

### Left recursion cleaning


<br>

### Ambiguity cleaning



<br>

### Final clean version


<br>

## Implementation

<br>

### Use of the Natural Language Processing Toolkit

<br>

### Use of the LL(1) Parser Visualzation

<br>

## Testing

<br>

### Use of the Natural Language Processing Toolkit

<br>

### Use of the LL(1) Parser Visualzation

<br>

## Analysis

<br>

### Original JQPSG Complexity

<br>

### Final JQPSG Complexity

<br>

# Conclusion

<br>

# References
