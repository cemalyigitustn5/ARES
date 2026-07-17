import speech_recognition as sr


def dinle():
    r = sr.Recognizer()

    with sr.Microphone() as kaynak:
        print("ARES dinliyor...")
        
        r.adjust_for_ambient_noise(kaynak)

        ses = r.listen(kaynak)

    try:
        komut = r.recognize_google(
            ses,
            language="tr-TR"
        )

        return komut.lower()

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        return "internet_hatasi"