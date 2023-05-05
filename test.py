import speech_recognition  # распознавание пользовательской речи (Speech-To-Text)
from testGP.func import *

commands = {
    ("hello", "hi", "morning", "привет"): play_greetings,
    # ("bye", "goodbye", "quit", "exit", "stop", "пока"): play_farewell_and_quit,
    # ("search", "google", "find", "найди"): search_for_term_on_google,
    # ("video", "youtube", "watch", "видео"): search_for_video_on_youtube,
    # ("wikipedia", "definition", "about", "определение", "википедия"): search_for_definition_on_wikipedia,
    # ("translate", "interpretation", "translation", "перевод", "перевести", "переведи"): get_translation,
    # ("language", "язык"): change_language,
    # ("weather", "forecast", "погода", "прогноз"): get_weather_forecast,
}


def setup_assistant_voice():
    # Microsoft Irina Desktop - Russian
    ttsEngine.setProperty("voice", ttsEngine.getProperty("voices")[0].id)


def play_voice_assistant_speech(text_to_speech):
    ttsEngine.say(str(text_to_speech))
    ttsEngine.runAndWait()


def record_and_recognize_audio(*args: tuple):
    with microphone:
        recognized_data = ""

        # регулирование уровня окружающего шума
        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print("Listening...")
            audio = recognizer.listen(microphone, 5, 5)

            with open("microphone-results.wav", "wb") as file:
                file.write(audio.get_wav_data())

        except speech_recognition.WaitTimeoutError:
            print("Can you check if your microphone is on, please?")
            return

        # использование online-распознавания через Google
        # (высокое качество распознавания)
        try:
            print("Started recognition...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except:
            ...
        return recognized_data


def execute_command_with_name(command_name: str, *args: list):
    """
    Выполнение заданной пользователем команды с дополнительными аргументами
    :param command_name: название команды
    :param args: аргументы, которые будут переданы в функцию
    :return:
    """
    for key in commands.keys():
        if command_name in key:
            commands[key](*args)
        else:
            pass  # print("Command not found")


if __name__ == "__main__":

    # инициализация инструментов распознавания и ввода речи
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    while True:
        # старт записи речи с последующим выводом распознанной речи
        # и удалением записанного в микрофон аудио
        voice_input = record_and_recognize_audio()
        os.remove("microphone-results.wav")
        print(voice_input)

        # отделение комманд от дополнительной информации (аргументов)
        voice_input = voice_input.split(" ")
        command = voice_input[0]
        command_options = [str(input_part) for input_part in voice_input[1:len(voice_input)]]
        print(command_options)
        execute_command_with_name(command, command_options)