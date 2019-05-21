import mlconjug


class SpacyConjugatorFR(object):
    """class SpacyConjugatorFR."""

    def __init__(self):
        super(SpacyConjugatorFR, self).__init__()

        self.Conjugator = mlconjug.mlconjug.Conjugator(language='fr')

        self.MATCH_PERSON_SING = {
            "1": "1s",
            "2": "2s",
            "3": "3s",
        }

        self.MATCH_PERSON_PLUR = {
            "1": "1p",
            "2": "2p",
            "3": "3p",
        }

        self.MATCH_TENSE = {
            "Pres": "Indicatif.Présent",
            "Imp": "Indicatif.Imparfait",
            "Past": "Indicatif.Passé Simple",
            "Fut": "Indicatif.Futur",
        }

    def get_ref(self, tok):
        return {x.split("=")[0]: x.split("=")[1] for x in tok.tag_.split("|")}

    def get_tense_and_person(self, spacy_token):
        try:
            refs = self.get_ref(spacy_token)
#             if 'Person' not in refs:
#                 refs['Person'] = '1'

#             print("TOKEN : ", spacy_token, "   REFS : ", refs)
            Person = None
            if refs['Number'] == 'Sing':
                Person = self.MATCH_PERSON_SING[refs['Person']]
            elif refs['Number'] == 'Plur':
                Person = self.MATCH_PERSON_PLUR[refs['Person']]

            Tense = self.MATCH_TENSE[refs['Tense']]
            return Tense, Person

        except Exception as e:
            print("ERROR  : " , e)
            return None, None

    def conjugate_verb(self, verb, spacy_token):
        try:
            Tense, Person = self.get_tense_and_person(spacy_token)
#             print("TENSE : ", Tense, "PERSON : ", Person)
            interim = self.Conjugator.conjugate(verb).conjug_info
            _tense = Tense.split(".")

            for t in _tense:
                interim = interim[t]
            return interim.get(Person)
        except Exception as e:
            return None

    def replace_verb_in_sentence(self, sentence, verb):

        new_sent = []
        for tok in sentence:
            if (tok.pos_ == "VERB"):
                new_verb = self.conjugate_verb(verb, tok)
                if new_verb is not None:
                    new_sent.append(new_verb)
                else:
                    new_sent.append(tok.text)
            else:
                new_sent.append(tok.text)
        return " ".join(new_sent)
