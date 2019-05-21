from SpacyConjugatorFR import SpacyConjugatorFR

import spacy
nlp = spacy.load('fr_core_news_md')

SpacyConjugator = SpacyConjugatorFR()


verb = nlp("les chien boivent")[2]
print(SpacyConjugator.conjugate_verb("rêver", verb))
# $> rêvent

sentence = nlp("les petits oiseaux planent au dessus du lac. Le chat joue avec les oiseaux")
print(SpacyConjugator.replace_verb_in_sentence(sentence, "manger"))
# $> les petits oiseaux mangent au dessus du lac . Le chat mange avec les oiseaux
