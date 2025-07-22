import spacy
nlp=spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion. The deal was finalized in September, and everyone was excited about the acquisition.")
for i in doc:
    print(i)
from spacy.symbols import ORTH
doc1=nlp("gimme that")
print(doc1)
for token in doc1:
    print(token.text)
special_case=[{ORTH:"gim"},{ORTH:"me"}]
nlp.tokenizer.add_special_case("gimme",special_case)
for token in nlp("gimme that"):
    print(token.text)
doc3=nlp("python is a programming language. Current year is 2022. Dollar symbol is $")
for i in doc3:
    print(i,"->",i.pos_)
print("stopword removal:")
from spacy.lang.en.stop_words import STOP_WORDS
for token in doc:
    if not nlp.vocab[token.text].is_stop:
        print(token.text)

print("Lemmatization:")
for token in doc:
    print(token,"->",token.lemma_)

"""output:
        (venv) (base) PS C:\Users\shaim\Desktop\pythonlab> python task12.py
Apple
is
looking
at
buying
U.K.
startup
for
$
1
billion
.
The
deal
was
finalized
in
September
,
and
everyone
was
excited
about
the
acquisition
.
gimme that
gimme
that
gim
me
that
python -> NOUN
is -> AUX
a -> DET
programming -> NOUN
language -> NOUN
. -> PUNCT
Current -> ADJ
year -> NOUN
is -> AUX
2022 -> NUM
. -> PUNCT
Dollar -> NOUN
symbol -> NOUN
is -> AUX
$ -> SYM
stopword removal:
Apple
looking
buying
U.K.
startup
$
1
billion
.
deal
finalized
September
,
excited
acquisition
.
Lemmatization:
Apple -> Apple
is -> be
looking -> look
at -> at
buying -> buy
U.K. -> U.K.
startup -> startup
for -> for
$ -> $
1 -> 1
billion -> billion
. -> .
The -> the
deal -> deal
was -> be
finalized -> finalize
in -> in
September -> September
, -> ,
and -> and
everyone -> everyone
was -> be
excited -> excited
about -> about
the -> the
acquisition -> acquisition
. -> .
    """