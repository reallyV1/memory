#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication,QButtonGroup,QLabel,QPushButton,QVBoxLayout,QGroupBox,QRadioButton,QHBoxLayout
from random import shuffle
from random import shuffle, randint
#Класс вопрос,свойство:текст вопроса,провильный вопрос и не правельный
class Question():
    def __init__(self,question_text,fine_answer,bed1,bed2,bed3):
        self.question_text=question_text
        self.fine_answer=fine_answer
        self.bed1=bed1
        self.bed2=bed2
        self.bed3=bed3
        #умеротваренье это не когда кто-то умер от варенья
def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.fine_answer)
    answers[1].setText(q.bed1)
    answers[2].setText(q.bed2)
    answers[3].setText(q.bed3)
    question.setText(q.question_text)
    result_text.setText(q.fine_answer)
    show_Question()
def check_answer():
    if answers[0].isChecked():
        result_text.setText("Правильно") 
        show_result()
        main_win.score += 1
    else:
        result_text.setText('Непрабильна')
        show_result()
    print('всего вопросов',main_win.total)
    print('общий cчёт',main_win.score)
    print('рейтинг',int(main_win.score/main_win.total * 100))
def show_result():
    ansewr_group.hide()
    result_box.show()
    button.setText("Следущий вопрос")
def show_Question():
    buttongroup.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    buttongroup.setExclusive(True)
    result_box.hide()
    ansewr_group.show()
    button.setText('Ответить')
def nextquetion():
    main_win.total += 1
    cur_quextion = randint(0, len(questionlist)-1)
    q=questionlist[cur_quextion]
    ask(q)
def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        nextquetion()


app = QApplication ([])
main_win = QWidget()
main_win.total = 0
main_win.score = 0

question = QLabel('Вопрос')

button = QPushButton('Ответить')
ansewr_group = QGroupBox('Ваианты ответа')
answer1 = QRadioButton('Вариант1')
answer2 = QRadioButton('Вариант2')
answer3 = QRadioButton('Вариант3')
answer4 = QRadioButton('Вариант4')
answers = [answer1,answer2,answer3,answer4]
buttongroup=QButtonGroup()
buttongroup.addButton(answer1)
buttongroup.addButton(answer2)
buttongroup.addButton(answer3)
buttongroup.addButton(answer4)

main_win.resize(400,300)
main_win.setWindowTitle('Memory Card')
v1 = QVBoxLayout()
v1.addWidget(answer1)
v1.addWidget(answer2)
v2 = QVBoxLayout()
v2.addWidget(answer3)
v2.addWidget(answer4)
h = QHBoxLayout()
h.addLayout(v1)
h.addLayout(v2)
ansewr_group.setLayout(h)
result_box = QGroupBox('Результат')
result_text = QLabel('Правильно-не правильно')
reght_ansewer = QLabel('Верный ответ')
v3 = QVBoxLayout()
v3.addWidget(result_text)
v3.addWidget(reght_ansewer)
result_box.setLayout(v3)

#привязываем к главно направляющей(2группы , кнопку)
vline = QVBoxLayout()
vline.addWidget(question, alignment = Qt.AlignCenter)
vline.addWidget(ansewr_group)
vline.addWidget(result_box)
vline.addWidget(button)
main_win.setLayout(vline)
button.clicked.connect(click_ok)
question1=Question('зимой и летом одним цветом','елка','почему кровать','лиственница','vline = QVBoxLayout()')
question2=Question('Когда был официальный релиз «Майнкрафт»?','18 ноября 2011','11 сентября 3011','я не зная','vline.addWidget(result_box)')
question3=Question(' каком году Европейский Союз впервые ввел евро в качестве валюты?','1999','235','1899','4566')
question4=Question('Какой национальный цветок Японии?','сакура','rtohiju','йцукенгшщз','гг')
question5=Question('Сколько полос на флаге США?','13','24','54','99')
question6=Question('Какое национальное животное Австралии?','Красный кенгуру','кенгуру','крокодил','додо')
question7=Question('Сколько дней нужно, чтобы Земля совершила оборот вокруг Солнца?','365','367','331','364')
question8=Question('До 1923 года как назывался турецкий город Стамбул?','Константинополь','Россия','Рим','Греция')
question9=Question('Где находится самая маленькая кость в теле человека?','ухо','нос','палец','череп')
question10=Question('Из какого зерна делается японский спирт саке','рис','чай','яблоко','гречка')
questionlist=[question1,question2,question3,question4,question5,question6,question7,question8,question9,question10]
nextquetion()
#спрятать группу
main_win.curquestion=-1
main_win.show()
app.exec_()
