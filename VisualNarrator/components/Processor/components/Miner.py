import token
from spacy import load
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English
from spellchecker import SpellChecker


class Miner:
    def __init__(self):
        self.nlp = (English())
        self.tokenizer = Tokenizer(self.nlp.vocab)
        self.spell = SpellChecker()

    def __preprocess_text(self, text):
        # Process the text with Spacy
        doc = self.nlp(text)

        # Remove stop words, punctuations, and apply lowercasing
        processed_text = ' '.join(token.text.lower(
        ) for token in doc if not token.is_stop and not token.is_punct)

        # Remove links
        processed_text = ' '.join(
            word for word in processed_text.split() if not word.startswith('http'))

        # Remove unnecessary punctuations
        cleaned_text = ' '.join(word.text for word in doc if not word.is_punct)

        # Correct spelling errors
        words = cleaned_text.split()
        corrected_words = [self.spell.correction(word) for word in words]
        corrected_words = [word for word in words if word != None]
        processed_text = ' '.join(corrected_words)

        return processed_text

    def tokenize(self, userStorySet: list[str]):
        processedSet = [self.__preprocess_text(sent) for sent in userStorySet]
        processedSet = list(set(processedSet))
        return self.tokenizer.pipe(processedSet)


if(__name__ == "__main__"):
  miner = Miner()
  tokens = miner.tokenize(["lk;sad,,,,.,.,., d asl;dja sd;fjasdfj;al sd;lajksdf oasd ifjasdj asdkfj;adf j;aid jf;df"])
  for val in tokens: 
    print(val.text)