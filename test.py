import sklearn.svm
import sklearn.feature_extraction.text
import sklearn.linear_model

from func import *


vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(2, 3))
classifier_probability = LogisticRegression()
classifier = LinearSVC()
config = {
    "intents": {
        "weather": {
            "examples": ["weather", "forecast", "погода", "прогноз"],
            "responses": get_weather
        },
        "disk_search": {
            "examples": ["найди файл", "поиск приложения", "файл", "file search",
                         "file", "search"],
            "responses": search_on_disks
        },
        "google_search": {
            "examples": ["найди в гугл", 'найди в интернете'
                         "search on google", "google", "find on google"],
            "responses": web_search
        },
        "farewell": {
                    "examples": ["bye", "goodbye", "quit", "exit", "stop", "пока"],
                    "responses": shutdown
                },
        'math_it': {
            'examplles': ['посчитай', 'сколько', 'math'],
            "responses": math_it
        }
    },
    "help": get_func
}


def prepare_corpus():
    """
    Подготовка модели для угадывания намерения пользователя
    """
    corpus = []
    target_vector = []
    for intent_name, intent_data in config["intents"].items():
        for example in intent_data["examples"]:
            corpus.append(example)
            target_vector.append(intent_name)

    training_vector = vectorizer.fit_transform(corpus)
    classifier_probability.fit(training_vector, target_vector)
    classifier.fit(training_vector, target_vector)


def get_intent(request):
    """
    Получение наиболее вероятного намерения в зависимости от запроса пользователя
    :param request: запрос пользователя
    :return: наиболее вероятное намерение
    """
    best_intent = classifier.predict(vectorizer.transform([request]))[0]

    index_of_best_intent = list(classifier_probability.classes_).index(best_intent)
    probabilities = classifier_probability.predict_proba(vectorizer.transform([request]))[0]

    best_intent_probability = probabilities[index_of_best_intent]

    # при добавлении новых намерений стоит уменьшать этот показатель
    if best_intent_probability > 0.57:
        return best_intent