import speech_recognition as sr


def dinle():
    r = sr.Recognizer()

    mic = sr.Microphone(
        device_index=6
    )

    with mic as kaynak:
        print("ARES dinliyor...")

        r.adjust_for_ambient_noise(kaynak, duration=1)

        ses = r.listen(kaynak)

    try:
        komut = r.recognize_google(
            ses,
            language="tr-TR"
        )

        print("Sen:", komut)
        return komut.lower()

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        return "internet_hatasi"

