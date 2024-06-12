import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser

listener = sr.Recognizer()

def parler(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()  # Assurez-vous d'arrêter l'instance après utilisation

def ecoute():
    command = ""
    try:
        with sr.Microphone() as source:
            print("Parler")
            voix = listener.listen(source)
            command = listener.recognize_google(voix, language='fr-FR')
            print("Vous avez dit:", command)
    except sr.UnknownValueError:
        print("Je n'ai pas compris ce que vous avez dit")
    except sr.RequestError as e:
        print(f"Erreur de service de reconnaissance vocale : {e}")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la reconnaissance vocale : {e}")
    return command.lower()

def assistant(command):
    response = ""

    if 'bonjour' in command or 'salut' in command:
        response = 'Bonjour ! Comment allez-vous ?'
        parler(response)

    elif 'oui ça va et toi' in command or 'ça va et toi' in command:
        response = "Oui ça va de mon côté, comment puis-je vous aider ?"
        parler(response)

    elif 'mets la chanson' in command or 'joue la chanson' in command:
        chanteur = command.replace('mets la chanson', '').replace('joue la chanson', '').strip()
        response = f"Je mets la chanson de {chanteur} sur YouTube."
        parler(response)
        pywhatkit.playonyt(chanteur)

    elif 'quelle heure est-il' in command or 'donne-moi l\'heure' in command:
        heure = datetime.datetime.now().strftime('%H:%M')
        response = "Il est " + heure
        parler(response)

    elif 'au revoir' in command or 'bye' in command:
        response = "Au revoir, c'était un plaisir à la prochaine"
        parler(response)
        return response  # Indiquer que le programme doit se terminer

    elif 'ton nom' in command or 'comment tu t\'appelles' in command:
        response = "Je n'ai pas de nom spécifique, mais je suis un assistant programmé en Python par Ali."
        parler(response)

    elif 'adresse de ce restaurant' in command or "l'adresse de" in command:
        restaurant = command.replace('adresse de ce restaurant', '').replace("l'adresse de", '').strip()
        response = f"Je cherche {restaurant} sur Google Maps."
        parler(response)
        url = f"https://www.google.com/maps/search/{restaurant.replace(' ', '+')}"
        webbrowser.open(url)

    elif 'va sur le site de' in command or 'ouvre le site de' in command:
        site = command.replace('va sur le site de', '').replace('ouvre le site de', '').strip()
        url = f"https://www.{site.replace(' ', '')}.com"
        response = f"Je vais ouvrir le site de {site}."
        parler(response)
        try:
            webbrowser.open(url)
        except Exception as e:
            response = "Une erreur s'est produite lors de l'ouverture du site."
            parler(response)

    else:
        response = "Désolé, je n'ai pas compris votre demande. Pouvez-vous reformuler ?"
        parler(response)

    return response
