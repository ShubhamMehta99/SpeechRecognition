import speech_recognition as sr

r = sr.Recognizer()

for i in range(3):
    with sr.Microphone() as source:
        print('Start Speaking: ')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            #text = r.recognize_google(audio)
            #print('This is what you said: {}'.format(text))
            #text = r.recognize_google(audio)
            print('This is what you said: '+ r.recognize_google(audio))
        except sr.UnknownValueError:
            print('Did not catch that!')
        except sr.RequestError as e:
            print('no result caught'.format(e))

