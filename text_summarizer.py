import spacy 
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
text="""It’s a big year for the 911. The legendary Porsche sportscar is 60 years old in 2023. Here's a handy guide to an automotive icon that continues to define pure driving enjoyment
When the dust sheet was pulled back on a brand-new Porsche model at the 1963 Frankfurt International Motor Show, few could have predicted the huge impact it would have on motoring in the decades to come. Its name was the 901. Today it's better known as the legendary 911, its name having been changed before it went on sale. Over the 60 years between 1963 and 2023, over 1.2m 911 sportscars have been made. Each one is evidence of the endless pursuit of innovation by Porsche, particularly when it comes to delivering memorable drive after memorable drive for all who experience it.'
 From its early days to most recognisable models and standout moments, this is a celebration of a true automotive phenomenon.
 
 
 
 When was the Porsche 911 first launched?
The Porsche 911 was first unveiled to the public on 12 September 1963 when it was launched at the Frankfurt International Motor Show. Full production of the car began a year later in September 1964 at the Porsche factory in Zuffenhausen.

The second production model to be made by the company after the Porsche 356, interestingly the 911 was originally called the 901. However, by the time the model went on sale it had become the 911 after a claim about naming rights from French car manufacturer, Peugeot. 
The 911 name not only stuck but has since become synonymous with success on both road and racetrack.

The first ever Porsche 911 was designed by F.A. Porsche – son of the founder of the company, Ferry Porsche – and his team. The original 911 had an air-cooled flat-six engine instead of the four-cylinder boxer engine of the 356. It developed 130PS, could accelerate from 0-100km/h in 9.1 seconds and had a top speed of 210km/h. These were hugely impressive figures for a production sportscar at the time. Although there have been many versions of the 911 since then, much has remained the same, like its 2 + 2 seating layout and rear engine position.

Many great Porsche designers have been involved in updating and evolving the 911 over the decades. They include such legendary figures as Anatole Lapine, who designed the G series, the successor to the original 911, and Harm Lagaay. This Dutchman was chief designer at Porsche from 1989 to 2004 and was the man who, among many other highlights, introduced the much talked about ‘fried egg’ headlights on the 911 (type 996). And, since 2004, it's been Michael Mauer who has overseen design of the 911 in his role as Head of Style Porsche.

These days you can choose a Porsche 911 to fit a wide range of lifestyles, like the new 911 Dakar, the first standard off-road model in the series, or the fastest production car in the current 911 line-up, the 911 Turbo S. Or, as Ferry Porsche once famously said, “The 911 is the only car that you can drive from an African safari to Le Mans, then to the theatre and onto the streets of New York.”
  
 """
def summazier(rawdocs): 
    stopwords=list(STOP_WORDS)
    #print("Stop words:",stopwords)
    nlp=spacy.load('en_core_web_sm')
    doc=nlp(rawdocs)
    #print(doc)
    tokens=[tokens.text for tokens in doc]
    #print("Tokens :",tokens)
    word_frequnccy={}
    for word in doc:
        word=word.text.lower()
        if word not in stopwords and word not in punctuation:
            if word not in word_frequnccy.keys():
                word_frequnccy[word]=1
            else:
                word_frequnccy[word]+=1

    #print("Word frequncy:",word_frequnccy)
    max_frequency=max(word_frequnccy.values())
    #print("Max frequncy:",max_frequency)
    for word in word_frequnccy.keys():
        word_frequnccy[word]=(word_frequnccy[word]/max_frequency)

    #print("Word frequncy:",word_frequnccy)
    sent_tokens=[sent for sent in doc.sents]
    #print("Sent tokens:",sent_tokens)
    sent_score={}
    for sent in sent_tokens:
        for word in sent:
            word=word.text.lower()
            if word in word_frequnccy.keys():
                if sent not in sent_score.keys():
                    sent_score[sent]=word_frequnccy[word]
                else:
                    sent_score[sent]+=word_frequnccy[word]

    #print("Sent Score:",sent_score)
    select_length=int(len(sent_tokens)*0.4)
    #print("Select length:",select_length)
    summary=nlargest(select_length,sent_score,key=sent_score.get)
    #print("Summary:",summary)
    final_summary=[word.text for word in summary]
    summary=" ".join(final_summary)

    return summary,doc,len(rawdocs.split(" ")),len(summary.split(" "))
   # print("Summary:",summary)
   # print("Text :",text)
   # print("Length of original text:",len(text.split(' ')))
   # print("Length of original text:",len(summary.split(' ')))

