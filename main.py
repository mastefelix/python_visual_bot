from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton,\
    QHBoxLayout, QVBoxLayout, QLineEdit, QTextEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

def start_window():
    description_text.setText("Для перехода к действию, нажми кнопку!")
    button_wiki.show()
    button_wiki.setText("Википедия")
    button_translate.show()
    button_translate.setText("Переводчик")
    button_weather.show()
    button_weather.setText("Погода")
    button_game.show()
    button_game.setText("Игра")
    request.clear()
    request.hide()
    info.clear()
    info.hide()
    button_back.setText("Выход")

def choice_action_back():
    if button_back.text() == "Выход":
        exit()
    elif button_back.text() == "Назад":
        start_window()

def show_wiki():
    hello_text.hide()
    button_translate.hide()
    button_weather.hide()
    button_game.hide()
    button_back.setText("Назад")
    description_text.setText("Для поиска информации в Википедии\nвведите запрос:")
    request.show()
    info.show()
    button_wiki.setText("Искать")

def get_request_wiki():
    if request.text():
        result = wiki.get_wiki(request.text())
        info.setText(result)

def choice_action_wiki():
    if button_wiki.text() == "Википедия":
        show_wiki()
    elif button_wiki.text() == "Искать":
        get_request_wiki()

def show_translator():
    hello_text.hide()
    button_wiki.hide()
    button_weather.hide()
    button_game.hide()
    button_back.setText("Назад")
    description_text.setText("Для перевода\nвведите слово или текст:")
    request.show()
    info.show()
    button_translate.setText("Искать")

def get_request_translator():
    if request.text():
        result = translator.translate(request.text())
        info.setText(result)

def choice_action_traslator():
    if button_translate.text() == "Переводчик":
        show_translator()
    elif button_translate.text() == "Искать":
        get_request_translator()

app = QApplication([])
window = QWidget()
window.resize(450, 500)
window.setWindowTitle("Чат-бот")
window.setWindowIcon(QIcon("bot.png"))

hello_text = QLabel("Привет! Это чат бот Алекс!\n\tДобро пожаловать!")
description_text = QLabel("Для перехода к действию, нажми кнопку!")
request = QLineEdit()
request.hide()
info = QTextEdit()
info.setReadOnly(True)
info.hide()
button_wiki = QPushButton("Википедия")
button_translate = QPushButton("Переводчик")
button_weather = QPushButton("Погода")
button_game = QPushButton("Игра")
button_back = QPushButton("Выход")

main_line = QVBoxLayout()
line_h1 = QHBoxLayout()
line_h2 = QHBoxLayout()
main_line.addWidget(hello_text, alignment=Qt.AlignmentFlag.AlignCenter)
main_line.addWidget(description_text, alignment=Qt.AlignmentFlag.AlignCenter)
main_line.addWidget(request, alignment=Qt.AlignmentFlag.AlignCenter)
main_line.addWidget(info, alignment=Qt.AlignmentFlag.AlignCenter)
line_h1.addWidget(button_wiki)
line_h1.addWidget(button_translate)
line_h2.addWidget(button_weather)
line_h2.addWidget(button_game)

main_line.addLayout(line_h1)
main_line.addLayout(line_h2)
main_line.addWidget(button_back)
window.setLayout(main_line)

button_wiki.clicked.connect(show_wiki)
button_translate.clicked.connect(choice_action_traslator)
# button_weather.clicked.connect(choice_action_weather)
# button_game.clicked.connect(choice_action_game)
button_back.clicked.connect(choice_action_back)

window.setStyleSheet("background-color: #7192BE; color: #000; font-family: fantasy, Comic Sans MS;"
                     "font-size: 18px;")
hello_text.setStyleSheet("font-size: 24px;")
description_text.setStyleSheet("")
request.setStyleSheet("background-color: #FFF; ")
info.setStyleSheet("background-color: #FFF; font-size: 12px; width: 150px; height: 100px;")
button_wiki.setStyleSheet("background-color: #70BDB5; border-radius: 10px; max-width: 300px;")
button_translate.setStyleSheet("background-color: #70BDB5; border-radius: 10px; max-width: 300px;")
button_weather.setStyleSheet("background-color: #70BDB5; border-radius: 10px; max-width: 300px;")
button_game.setStyleSheet("background-color: #70BDB5; border-radius: 10px; max-width: 300px;")
button_back.setStyleSheet("background-color: #70BDB5; border-radius: 10px; width: 300px;")

window.show()
app.exec()


###########################
# import random
# import wiki
# import translator
# import weather
#

#


#
# def show_weather():
#     hello_text.hide()
#     button_translate.hide()
#     button_wiki.hide()
#     button_game.hide()
#     button_back.setText("Назад")
#     description_text.setText("Город:")
#     request.show()
#     info.show()
#     button_weather.setText("Искать")
#
# def get_request_weather():
#     result = weather.get_weather(request.text())
#     info.setText(result)
#
# def choice_action_weather():
#     if button_weather.text() == "Погода":
#         show_weather()
#     elif button_weather.text() == "Искать":
#         get_request_weather()
#
# def show_game():
#     global win_number
#     hello_text.hide()
#     button_translate.hide()
#     button_wiki.hide()
#     button_weather.hide()
#     button_back.setText("Назад")
#     description_text.setText("Отгадай число от 1 до 10:")
#     request.show()
#     info.show()
#     button_game.setText("Угадать")
#     win_number = random.randint(1, 10)
#
# def get_request_game():
#     # print(win_number)
#     if request.text() != "":
#         if int(request.text()) > win_number:
#             info.insertPlainText("Многовато!\n")
#         elif int(request.text()) < win_number:
#             info.insertPlainText("Маловато!\n")
#         else:
#             info.insertPlainText("Угадал!\nСледующая попытка!\n")
#             request.clear()
#             show_game()
#
# def choice_action_game():
#     if button_game.text() == "Игра":
#         show_game()
#     elif button_game.text() == "Угадать":
#         get_request_game()
#

