import stanza

stanza.download(lang='en')

nlp = stanza.Pipeline(lang='en', processors= 'tokenize, sentiment' )

def sentiment_analyzer(text):
    sentiment_score = 0
    document = nlp(text)

    for sentence in document.sentences:
        sentiment_score += sentence.sentiment

    return sentiment_score


    