``` python
import spacy
from SpacyConjugatorFR import SpacyConjugatorFR

nlp = spacy.load('fr_core_news_md')
SpacyConjugator = SpacyConjugatorFR()


verb = nlp("les chien boivent")[2]
print(SpacyConjugator.conjugate_verb("rêver", verb))
# $> rêvent

sentence = nlp("les petits oiseaux planent au dessus du lac. Le chat joue avec les oiseaux")
print(SpacyConjugator.replace_verb_in_sentence(sentence, "manger"))
# $> les petits oiseaux mangent au dessus du lac . Le chat mange avec les oiseaux
```


### Credit

this code is based on [Spacy](https://github.com/explosion/spaCy) and [mlconjug](https://github.com/SekouD/mlconjug)
