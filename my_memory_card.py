from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup
from random import shuffle, randint


class Question():
    def __init__(self, quastionL, right_answer, wwq1, wwq2, wwq3):
        self.quastionL = quastionL
        self.right_answer = right_answer
        self.wwq1 = wwq1
        self.wwq2 = wwq2
        self.wwq3 = wwq3


questions_list = []
questions_list.append(Question('кадкаМ ждуркС жаносреп йынноицакилпитьлум ястеялвя меК', 'медебеЛ', 'йобаж', 'мёсуГ', 'йоктУ'))
questions_list.append(Question('Какой национальности не существует?', 'Энцы', 'Чулымцы', 'Смурфы', 'Алеуты'))
questions_list.append(Question('?!йиншил тнаирав йокак', 'роткарТ', 'дзеоП', 'лирфиМ', 'трофмоК'))


def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    _1.setChecked(False)
    _2.setChecked(False)
    _3.setChecked(False)
    _4.setChecked(False)
    RadioGroup.setExclusive(True)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def show_test():
    if btn_OK.text() == 'Ответить':
        show_result()
    else:
        show_question() 


def next_question():
    window.total += 1
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)


def ask(q: Question):
    shuffle(spic)
    spic[0].setText(q.right_answer)
    spic[1].setText(q.wwq1)
    spic[2].setText(q.wwq2)
    spic[3].setText(q.wwq3)
    quastion.setText(q.quastionL)
    b_Correct.setText(q.right_answer)
    show_question()


def check_answer():
    if spic[0].isChecked():
        show_correct('Правильно!')
        window.total += 1
    else:
        if spic[1].isChecked() or spic[2].isChecked() or spic[3].isChecked():
            show_correct('Не правильно')
    print('Статистика\n-Всего вопросов:', window.total, '\n-Правильных ответов:',window.total)
    print('Рейтинг', (window.score/window.total*100), '%')
def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()


def show_correct(res):
    b_Result.setText(res)
    show_result()


app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')


quastion = QLabel('Какой национальности не существует?')
###RadioGroupBox = QGroupBox("Варианты ответов") - это не надо здесь
###lb_Question = QLabel('Это вопрос на засыпку?') - это не надо здесь
btn_OK = QPushButton('Ответить')

RadioGroupBox = QGroupBox("Варианты ответов") ### - добавил сверху
_1 = QRadioButton('Энцы')
_2 = QRadioButton('Чулымцы')
_3 = QRadioButton('Смурфы')
_4 = QRadioButton('Алеуты')

spic = [_1, _2, _3, _4]

RadioGroup = QButtonGroup()
RadioGroup.addButton(_1)
RadioGroup.addButton(_2)
RadioGroup.addButton(_3)
RadioGroup.addButton(_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() ### вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(_1) ### два ответа в первый столбец
layout_ans2.addWidget(_2)
layout_ans3.addWidget(_3) ### два ответа во второй столбец
layout_ans3.addWidget(_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) ### разместили столбцы в одной строке

RadioGroupBox.setLayout(layout_ans1) ### готова "панель" с вариантами ответов 

AnsGroupBox = QGroupBox("Результаты ответов")
b_Result = QLabel('прав ты или нет?')
b_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(b_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(b_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout() ### вопрос
layout_line2 = QHBoxLayout() ### варианты ответов или результат теста
layout_line3 = QHBoxLayout() ### кнопка "Ответить"

layout_line1.addWidget(quastion, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) ### кнопка должна быть большой
layout_line3.addStretch(1)

### Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) ### пробелы между содержимым

window.cur_question = -1

window.setLayout(layout_card)
###ask('Гросударственный язык Бразилии', 'Португальский', 'Испанский', 'Итальянский', 'Бразильский')
q = Question('Гросударственный язык Бразилии', 'Португальский', 'Испанский', 'Итальянский', 'Бразильский')
ask(q)
btn_OK.clicked.connect(click_OK)
window.score = 0
window.total = 0
next_question()

window.show()
app.exec_()