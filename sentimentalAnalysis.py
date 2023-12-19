# prompt: make a speech recogonition file that takes input and do sentimental analysis also
import speech_recognition as sr
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pyttsx3

def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: {}".format(text))
        sia = SentimentIntensityAnalyzer()
        sentiment = sia.polarity_scores(text)
        print("Sentiment: {}".format(sentiment))
        if sentiment['pos'] > sentiment['neg']:
            print("Sentiment: positive")
        else:
            print("Sentiment: negative")
        engine = pyttsx3.init()
        engine.say(sentiment)
        engine.runAndWait()
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

if __name__ == "__main__":
    main()


#     @app.route('/api/start_speech_recognition', methods=['GET'])
# def start_speech_recognition():
#     try:
#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#             print("Say something:")
#             audio = r.listen(source)
        
#         text = r.recognize_google(audio)
#         print("You said: {}".format(text))
        
#         sia = SentimentIntensityAnalyzer()
#         sentiment = sia.polarity_scores(text)
#         print("Sentiment: {}".format(sentiment))
        
#         sentiment_result = 'positive' if sentiment['pos'] > sentiment['neg'] else 'negative'

#         # Speak the sentiment using pyttsx3
#         engine = pyttsx3.init()
#         engine.say(sentiment_result)
#         engine.runAndWait()

#         result = {
#             'text': text,
#             'sentiment': sentiment_result
#         }

#         return jsonify(result)

#     except sr.UnknownValueError:
#         print("Could not understand audio")
#         return jsonify({'error': 'Could not understand audio'})

#     except sr.RequestError as e:
#         print("Could not request results; {0}".format(e))
#         return jsonify({'error': 'Could not request results; {0}'.format(e)})

# if __name__ == "__main__":
