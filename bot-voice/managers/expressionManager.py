import sys
sys.path.append(sys.path[0] + "/..")
#import speech_recognition as sr
import talkBot as talk
import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig



exceptionActive = False

def getExpresion():
    try:
        speech_config = speechsdk.SpeechConfig(subscription="f4a486d08bca481e93bd13210256cad5", region="southcentralus")
        # speech_config = speechsdk.SpeechConfig(subscription="<paste-your-subscription-key>", region="<paste-your-region>")
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, language="es-CL	")
        result = speech_recognizer.recognize_once_async().get()
        #print(result.text)
        return result.text.lower()
    except Exception as e:
        print(e)
        if exceptionActive:
            talk.talkBot(e)


speech_config = speechsdk.SpeechConfig(subscription="f4a486d08bca481e93bd13210256cad5", region="southcentralus")
speech_config.speech_synthesis_language = "es-CO"
speech_config.speech_synthesis_voice_name = "es-CO-SalomeNeural"
#audio_config = speechsdk.AudioOutputConfig(use_default_speaker=True)
synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
r = synthesizer.speak_text_async("En 200 metros, gira a la derecha, luego gira a la izquierda").get()
print(r)