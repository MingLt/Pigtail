import sys
from PyQt5 import QtWidgets
from PyQt5.Qt import *
from webWar import *
from AIWar import *
from AIWar import reminant_cards as re
from AIWar import ran as raan
from AIWar import dispostion_pok as disai
from localWar import *
from enter_uuid import Ui_Dialog as Uuid_Ui
from pattern import Ui_Dialog as Pattern_Ui
from login_1 import Ui_Dialog as Login_Ui
from local import Ui_MainWindow as Local_Ui
from wait import Ui_Dialog as Wait_Ui
from over import Ui_Dialog as Over_Ui

status = []
uuid = []
p1 = Player()
p5 = aiwar_Player()
p6 = AI_player()
p1.name += 'P1'
p2 = Player()
p2.name += 'P2'


class show_login(QtWidgets.QDialog, Login_Ui):
    def __init__(self):
        super(show_login, self).__init__()
        self.setupUi(self)
        self.login = 1
        self.pushbutton.clicked.connect(self.login_btn)

    def login_btn(self):
        if self.login:
            user = self.usernameEdit.text()
            psw = self.pswEdit.text()
            if not psw == '' and not user == '':
                self.status = login(user, psw)
                status.append(self.status)
                if self.status != 0:
                    self.hide()
                    self.w = show_wait()
                    self.w.show()
                else:
                    msgBox = QMessageBox()
                    msgBox.setWindowTitle(u'提示')
                    msgBox.setText(u"username or password is wrong!")
                    msgBox.exec_()
            else:
                msgBox = QMessageBox()
                msgBox.setWindowTitle(u'提示')
                msgBox.setText(u"please input username and password!")
                msgBox.exec_()


class show_pattern(QtWidgets.QDialog, Pattern_Ui):
    def __init__(self):
        super(show_pattern, self).__init__()
        self.setupUi(self)
        self.online.clicked.connect(self.goLogin)
        self.local.clicked.connect(self.goAll)
        self.machine.clicked.connect(self.goMachine)

    def goLogin(self):
        self.login = show_login()
        self.login.show()
        self.close()

    def goAll(self):
        self.close()
        self.all = show_local()
        self.all.show()
        msgBox = QMessageBox()
        msgBox.setWindowTitle(u'提示')
        if ran == 1:
            msgBox.setText("玩家1先开始")
        else:
            msgBox.setText("玩家2先开始")
        msgBox.exec_()

    def goMachine(self):
        self.mch = show_machine()
        self.mch.show()
        self.close()


class show_over(QtWidgets.QDialog, Over_Ui):
    def __init__(self):
        super(show_over, self).__init__()
        self.setupUi(self)
        self.lose.setVisible(False)
        self.ping.setVisible(False)
        if len(p1.cards) > len(p2.cards):
            self.pl.setText("玩家2")
        elif len(p1.cards) < len(p2.cards):
            self.pl.setText("玩家1")
        else:
            self.pl.setVisible(False)
            self.ping.setVisible(True)


class show_local(QtWidgets.QMainWindow, Local_Ui):
    def __init__(self):
        super(show_local, self).__init__()
        self.setupUi(self)
        self.tuoguan1.hide()
        self.tuoguan2.hide()
        self.und.clicked.connect(self.und_btn)
        self.pushButton.clicked.connect(self.tuoguan1.show)
        self.pushButton_2.clicked.connect(self.tuoguan1.hide)
        self.pushButton_3.clicked.connect(self.tuoguan2.show)
        self.pushButton_4.clicked.connect(self.tuoguan2.hide)
        # 托管和取消托管
        self.pushButton.clicked.connect(self.call_tactics_1)
        self.pushButton_3.clicked.connect(self.call_tactics_2)
        self.pushButton_2.clicked.connect(self.change_flag1)
        self.pushButton_4.clicked.connect(self.change_flag2)
        self.total = 52
        self.flag1 = 0
        self.flag2 = 0
        self.HH1.clicked.connect(self.H1_set)
        self.DD1.clicked.connect(self.D1_set)
        self.CC1.clicked.connect(self.C1_set)
        self.SS1.clicked.connect(self.S1_set)
        self.HH2.clicked.connect(self.H2_set)
        self.DD2.clicked.connect(self.D2_set)
        self.CC2.clicked.connect(self.C2_set)
        self.SS2.clicked.connect(self.S2_set)
        self.r = ran
        self.i = 0

    def H1_set(self):
        self.r = 0
        if len(p1.poker_h) != 0:
            dicard = p1.poker_h[-1]
            p1.poker_h.remove(dicard)
            p1.cards.remove(dicard)
            p1.Poker_statistics(dicard)
            if len(dispostion_pok) == 0:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + dicard + ".png);}")
                self.card.setStyleSheet("QPushButton{background:transparent;}")
                self.H1_update()
                self.D1_update()
                self.C1_update()
                self.S1_update()
                return
            else:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + dispostion_pok[-1] + ".png);}")
        self.H1_update()
        if self.flag2:
            self.call_tactics_2()
        else:
            self.r = 0

    def D1_set(self):
        self.r = 0
        if len(p1.poker_d) != 0:
            dicard = p1.poker_d[-1]
            p1.poker_d.remove(dicard)
            p1.cards.remove(dicard)
            p1.Poker_statistics(dicard)
            if len(dispostion_pok) == 0:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + dicard + ".png);}")
                self.card.setStyleSheet("QPushButton{background:transparent;}")
                self.H1_update()
                self.D1_update()
                self.C1_update()
                self.S1_update()
                return
            else:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + dispostion_pok[-1] + ".png);}")
        self.D1_update()
        if self.flag2:
            self.call_tactics_2()
        else:
            self.r = 0

    def S1_set(self):
        self.r = 0
        if len(p1.poker_s) != 0:
            dicard = p1.poker_s[-1]
            p1.poker_s.remove(dicard)
            p1.cards.remove(dicard)
            p1.Poker_statistics(dicard)
            if len(dispostion_pok) == 0:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + dicard + ".png);}")
                self.card.setStyleSheet("QPushButton{background:transparent;}")
                self.H1_update()
                self.D1_update()
                self.C1_update()
                self.S1_update()
                return
            else:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + dispostion_pok[-1] + ".png);}")
        self.S1_update()
        if self.flag2:
            self.call_tactics_2()
        else:
            self.r = 0

    def C1_set(self):
        self.r = 0
        if len(p1.poker_c) != 0:
            dicard = p1.poker_c[-1]
            p1.poker_c.remove(dicard)
            p1.cards.remove(dicard)
            p1.Poker_statistics(dicard)
            if len(dispostion_pok) == 0:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + dicard + ".png);}")
                self.card.setStyleSheet("QPushButton{background:transparent;}")
                self.H1_update()
                self.D1_update()
                self.C1_update()
                self.S1_update()
                return
            else:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + dispostion_pok[-1] + ".png);}")
        self.C1_update()
        if self.flag2:
            self.call_tactics_2()
        else:
            self.r = 0

    def H2_set(self):
        self.r = 1
        if len(p2.poker_h) != 0:
            dicard = p2.poker_h[-1]
            p2.poker_h.remove(dicard)
            p2.cards.remove(dicard)
            p2.Poker_statistics(dicard)
            if len(dispostion_pok) == 0:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + dicard + ".png);}")
                self.card.setStyleSheet("QPushButton{background:transparent;}")
                self.H2_update()
                self.D2_update()
                self.C2_update()
                self.S2_update()
                return
            else:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + dispostion_pok[-1] + ".png);}")
        self.H2_update()
        if self.flag1:
            self.call_tactics_1()
        else:
            self.r = 1

    def D2_set(self):
        self.r = 1
        if len(p2.poker_d) != 0:
            dicard = p2.poker_d[-1]
            p2.poker_d.remove(dicard)
            p2.cards.remove(dicard)
            p2.Poker_statistics(dicard)
            if len(dispostion_pok) == 0:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + dicard + ".png);}")
                self.card.setStyleSheet("QPushButton{background:transparent;}")
                self.H2_update()
                self.D2_update()
                self.C2_update()
                self.S2_update()
                return
            else:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + dispostion_pok[-1] + ".png);}")
        self.D2_update()
        if self.flag1:
            self.call_tactics_1()
        else:
            self.r = 1

    def S2_set(self):
        self.r = 1
        if len(p2.poker_s) != 0:
            dicard = p2.poker_s[-1]
            p2.poker_s.remove(dicard)
            p2.cards.remove(dicard)
            p2.Poker_statistics(dicard)
            if len(dispostion_pok) == 0:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + dicard + ".png);}")
                self.card.setStyleSheet("QPushButton{background:transparent;}")
                self.H2_update()
                self.D2_update()
                self.C2_update()
                self.S2_update()
                return
            else:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + dispostion_pok[-1] + ".png);}")
        self.S2_update()
        if self.flag1:
            self.call_tactics_1()
        else:
            self.r = 1

    def C2_set(self):
        self.r = 1
        if len(p2.poker_c) != 0:
            dicard = p2.poker_c[-1]
            p2.poker_c.remove(dicard)
            p2.cards.remove(dicard)
            p2.Poker_statistics(dicard)
            if len(dispostion_pok) == 0:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + dicard + ".png);}")
                self.card.setStyleSheet("QPushButton{background:transparent;}")
                self.H2_update()
                self.D2_update()
                self.C2_update()
                self.S2_update()
                return
            else:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + dispostion_pok[-1] + ".png);}")
        self.C2_update()
        if self.flag1:
            self.call_tactics_1()
        else:
            self.r = 1

    def change_flag1(self):
        self.flag1 = 0

    def change_flag2(self):
        self.flag2 = 0

    def call_tactics_1(self):
        if len(reminant_cards) == 0:
            return self.und_btn()
        self.flag1 = 1
        self.r = 0
        c = p1.Tactics(p2.sum, p2.state)
        if len(dispostion_pok) == 0:
            self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + c + ".png);}")
            self.card.setStyleSheet("QPushButton{background:transparent;}")
            self.H1_update()
            self.D1_update()
            self.C1_update()
            self.S1_update()
        else:
            if p1.state:  # 出牌
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + dispostion_pok[-1] + ".png);}")
                self.H1_update()
                self.D1_update()
                self.C1_update()
                self.S1_update()
            else:  # 抽牌
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + c + ".png);}")
                self.H1_update()
                self.D1_update()
                self.C1_update()
                self.S1_update()
        if self.flag2:
            self.call_tactics_2()

    def call_tactics_2(self):
        if len(reminant_cards) == 0:
            return self.und_btn()
        self.flag2 = 1
        self.r = 1
        c = p2.Tactics(p1.sum, p1.state)
        if len(dispostion_pok) == 0:
            self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + c + ".png);}")
            self.card.setStyleSheet("QPushButton{background:transparent;}")
            self.H2_update()
            self.D2_update()
            self.C2_update()
            self.S2_update()
        else:
            if p2.state:  # 出牌
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + dispostion_pok[-1] + ".png);}")
                self.H2_update()
                self.D2_update()
                self.C2_update()
                self.S2_update()
            else:  # 抽牌
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + c + ".png);}")
                self.H2_update()
                self.D2_update()
                self.C2_update()
                self.S2_update()
        if self.flag1:
            self.call_tactics_1()

    def H1_update(self):
        self.H_1.setText(str(len(p1.poker_h)))
        self.sum_1.setText(str(len(p1.cards)))
        if len(p1.poker_h) == 0:
            self.HH1.setStyleSheet("QPushButton{background:transparent;}")
        else:
            self.HH1.setStyleSheet("QPushButton{border-image: url(:/gamei/" + p1.poker_h[0] + ".png);}")

    def D1_update(self):
        self.D_1.setText(str(len(p1.poker_d)))
        self.sum_1.setText(str(len(p1.cards)))
        if len(p1.poker_d) == 0:
            self.DD1.setStyleSheet("QPushButton{background:transparent;}")
        else:
            self.DD1.setStyleSheet("QPushButton{border-image: url(:/gamei/" + p1.poker_d[0] + ".png);}")

    def C1_update(self):
        self.C_1.setText(str(len(p1.poker_c)))
        self.sum_1.setText(str(len(p1.cards)))
        if len(p1.poker_c) == 0:
            self.CC1.setStyleSheet("QPushButton{background:transparent;}")
        else:
            self.CC1.setStyleSheet("QPushButton{border-image: url(:/gamei/" + p1.poker_c[0] + ".png);}")

    def S1_update(self):
        self.S_1.setText(str(len(p1.poker_s)))
        self.sum_1.setText(str(len(p1.cards)))
        if len(p1.poker_s) == 0:
            self.SS1.setStyleSheet("QPushButton{background:transparent;}")
        else:
            self.SS1.setStyleSheet("QPushButton{border-image: url(:/gamei/" + p1.poker_s[0] + ".png);}")

    def H2_update(self):
        self.H_2.setText(str(len(p2.poker_h)))
        self.sum_2.setText(str(len(p2.cards)))
        if len(p2.poker_h) == 0:
            self.HH2.setStyleSheet("QPushButton{background:transparent;}")
        else:
            self.HH2.setStyleSheet("QPushButton{border-image: url(:/gamei/" + p2.poker_h[0] + ".png);}")

    def D2_update(self):
        self.D_2.setText(str(len(p2.poker_d)))
        self.sum_2.setText(str(len(p2.cards)))
        if len(p2.poker_d) == 0:
            self.DD2.setStyleSheet("QPushButton{background:transparent;}")
        else:
            self.DD2.setStyleSheet("QPushButton{border-image: url(:/gamei/" + p2.poker_d[0] + ".png);}")

    def C2_update(self):
        self.C_2.setText(str(len(p2.poker_c)))
        self.sum_2.setText(str(len(p2.cards)))
        if len(p2.poker_c) == 0:
            self.CC2.setStyleSheet("QPushButton{background:transparent;}")
        else:
            self.CC2.setStyleSheet("QPushButton{border-image: url(:/gamei/" + p2.poker_c[0] + ".png);}")

    def S2_update(self):
        if self.flag1:
            self.call_tactics_1()
        else:
            self.r = 1
        self.S_2.setText(str(len(p2.poker_s)))
        self.sum_2.setText(str(len(p2.cards)))
        if len(p2.poker_s) == 0:
            self.SS2.setStyleSheet("QPushButton{background:transparent;}")
        else:
            self.SS2.setStyleSheet("QPushButton{border-image: url(:/gamei/" + p2.poker_s[0] + ".png);}")

    def und_btn(self):  # 抽牌
        if len(reminant_cards):
            if self.r == 1:
                c = p1.draw_poker()
                if len(dispostion_pok) == 0:
                    self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + c + ".png);}")
                    self.card.setStyleSheet("QPushButton{background:transparent;}")
                    self.H1_update()
                    self.D1_update()
                    self.C1_update()
                    self.S1_update()
                else:
                    self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + c + ".png);}")
                self.total = self.total - 1
                self.r = 0
                if self.flag2:
                    self.call_tactics_2()
                else:
                    self.r = 0
            else:
                c = p2.draw_poker()
                if len(dispostion_pok) == 0:
                    self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + c + ".png);}")
                    self.card.setStyleSheet("QPushButton{background:transparent;}")
                    self.H2_update()
                    self.D2_update()
                    self.C2_update()
                    self.S2_update()
                else:
                    self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + c + ".png);}")
                self.total = self.total - 1
                if self.flag1:
                    self.call_tactics_1()
                else:
                    self.r = 1
        else:
            self.close()
            self.ol = show_over()
            self.ol.show()


class show_machine(QtWidgets.QMainWindow, Local_Ui):
    def __init__(self):
        super(show_machine, self).__init__()
        self.setupUi(self)
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        self.tuoguan1.hide()
        self.tuoguan2.hide()
        self.und.clicked.connect(self.und_btn)

        self.HH1.clicked.connect(self.H1_set)
        self.DD1.clicked.connect(self.D1_set)
        self.CC1.clicked.connect(self.C1_set)
        self.SS1.clicked.connect(self.S1_set)
        self.r = raan
        self.i = 0
        self.total = 52
    """
        def und_btn(self):
        self.close()
        self.ol = show_over()
        self.ol.show()
    """
    def H1_set(self):
        self.r = 0
        if len(p5.poker_h) != 0:
            dicard = p5.poker_h[-1]
            p5.poker_h.remove(dicard)
            p5.cards.remove(dicard)
            p5.Poker_statistics(dicard)
            if len(disai) == 0:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + dicard + ".png);}")
                self.card.setStyleSheet("QPushButton{background:transparent;}")
                self.H1_update()
                self.D1_update()
                self.C1_update()
                self.S1_update()
                return
            else:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + disai[-1] + ".png);}")

    def D1_set(self):
        self.r = 0
        if len(p5.poker_d) != 0:
            dicard = p5.poker_d[-1]
            p5.poker_d.remove(dicard)
            p5.cards.remove(dicard)
            p5.Poker_statistics(dicard)
            if len(disai) == 0:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + dicard + ".png);}")
                self.card.setStyleSheet("QPushButton{background:transparent;}")
                self.H1_update()
                self.D1_update()
                self.C1_update()
                self.S1_update()
                return
            else:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + disai[-1] + ".png);}")

    def S1_set(self):
        self.r = 0
        if len(p5.poker_s) != 0:
            dicard = p5.poker_s[-1]
            p5.poker_s.remove(dicard)
            p5.cards.remove(dicard)
            p5.Poker_statistics(dicard)
            if len(disai) == 0:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + dicard + ".png);}")
                self.card.setStyleSheet("QPushButton{background:transparent;}")
                self.H1_update()
                self.D1_update()
                self.C1_update()
                self.S1_update()
                return
            else:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + disai[-1] + ".png);}")

    def C1_set(self):
        self.r = 0
        if len(p5.poker_c) != 0:
            dicard = p5.poker_c[-1]
            p5.poker_c.remove(dicard)
            p5.cards.remove(dicard)
            p5.Poker_statistics(dicard)
            if len(disai) == 0:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + dicard + ".png);}")
                self.card.setStyleSheet("QPushButton{background:transparent;}")
                self.H1_update()
                self.D1_update()
                self.C1_update()
                self.S1_update()
                return
            else:
                self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + disai[-1] + ".png);}")

    def H1_update(self):
        self.H_1.setText(str(len(p5.poker_h)))
        self.sum_1.setText(str(len(p5.cards)))
        if len(p5.poker_h) == 0:
            self.HH1.setStyleSheet("QPushButton{background:transparent;}")
        else:
            self.HH1.setStyleSheet("QPushButton{border-image: url(:/gamei/" + p5.poker_h[0] + ".png);}")

    def D1_update(self):
        self.D_1.setText(str(len(p5.poker_d)))
        self.sum_1.setText(str(len(p5.cards)))
        if len(p5.poker_d) == 0:
            self.DD1.setStyleSheet("QPushButton{background:transparent;}")
        else:
            self.DD1.setStyleSheet("QPushButton{border-image: url(:/gamei/" + p5.poker_d[0] + ".png);}")

    def C1_update(self):
        self.C_1.setText(str(len(p5.poker_c)))
        self.sum_1.setText(str(len(p5.cards)))
        if len(p5.poker_c) == 0:
            self.CC1.setStyleSheet("QPushButton{background:transparent;}")
        else:
            self.CC1.setStyleSheet("QPushButton{border-image: url(:/gamei/" + p5.poker_c[0] + ".png);}")

    def S1_update(self):
        self.S_1.setText(str(len(p5.poker_s)))
        self.sum_1.setText(str(len(p5.cards)))
        if len(p5.poker_s) == 0:
            self.SS1.setStyleSheet("QPushButton{background:transparent;}")
        else:
            self.SS1.setStyleSheet("QPushButton{border-image: url(:/gamei/" + p5.poker_s[0] + ".png);}")

    def H2_update(self):
        self.H_1.setText(str(len(p6.poker_h)))
        self.sum_1.setText(str(len(p6.cards)))
        if len(p6.poker_h) == 0:
            self.HH1.setStyleSheet("QPushButton{background:transparent;}")
        else:
            self.HH1.setStyleSheet("QPushButton{border-image: url(:/gamei/" + p6.poker_h[0] + ".png);}")

    def D2_update(self):
        self.r = 1
        self.D_1.setText(str(len(p6.poker_d)))
        self.sum_1.setText(str(len(p6.cards)))
        if len(p6.poker_d) == 0:
            self.DD1.setStyleSheet("QPushButton{background:transparent;}")
        else:
            self.DD1.setStyleSheet("QPushButton{border-image: url(:/gamei/" + p6.poker_d[0] + ".png);}")

    def C2_update(self):
        self.C_1.setText(str(len(p6.poker_c)))
        self.sum_1.setText(str(len(p6.cards)))
        if len(p6.poker_c) == 0:
            self.CC1.setStyleSheet("QPushButton{background:transparent;}")
        else:
            self.CC1.setStyleSheet("QPushButton{border-image: url(:/gamei/" + p6.poker_c[0] + ".png);}")

    def S2_update(self):
        self.S_1.setText(str(len(p6.poker_s)))
        self.sum_1.setText(str(len(p6.cards)))
        if len(p6.poker_s) == 0:
            self.SS1.setStyleSheet("QPushButton{background:transparent;}")
        else:
            self.SS1.setStyleSheet("QPushButton{border-image: url(:/gamei/" + p6.poker_s[0] + ".png);}")

    def und_btn(self):  # 抽牌
        if len(re):
            if self.r == 1:
                c = p5.draw_poker()
                if len(disai) == 0:
                    self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + c + ".png);}")
                    self.card.setStyleSheet("QPushButton{background:transparent;}")
                    self.H1_update()
                    self.D1_update()
                    self.C1_update()
                    self.S1_update()
                else:
                    self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + c + ".png);}")
                self.total = self.total - 1
                self.r = 0
            else:
                c = p6.Tactics(p5.sum, p5.state)
                if len(disai) == 0:
                    self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + c + ".png);}")
                    self.card.setStyleSheet("QPushButton{background:transparent;}")
                    self.H2_update()
                    self.D2_update()
                    self.C2_update()
                    self.S2_update()
                else:
                    self.card.setStyleSheet("QPushButton{border-image: url(:/gamei/" + c + ".png);}")
                self.total = self.total - 1
        else:
            self.close()
            self.ol = show_over()
            self.ol.show()


class show_online(QtWidgets.QMainWindow, Local_Ui):
    def __init__(self):
        super(show_online, self).__init__()
        self.setupUi(self)
        self.tuoguan1.hide()
        self.tuoguan2.hide()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        self.pushButton.clicked.connect(self.tuoguan1.show)
        self.pushButton_2.clicked.connect(self.tuoguan1.hide)
        self.und.clicked.connect(self.und_btn)
        self.card = ''

    def und_btn(self):
        self.close()
        self.w = show_over()
        self.w.show()


class show_wait(QtWidgets.QDialog, Wait_Ui):
    def __init__(self):
        super(show_wait, self).__init__()
        self.setupUi(self)
        self.join.clicked.connect(self.join_btn)
        self.cr.clicked.connect(self.create_btn)

    def join_btn(self):
        self.uuid = uuidDialog()
        uuid.append(self.uuid)
        self.uuid.show()

    def create_btn(self):
        pri = True
        cb = createGame(pri, status[0])
        msgBox = QMessageBox()
        msgBox.setWindowTitle(u'提示')
        msgBox.setText(str(cb))
        msgBox.exec_()


class uuidDialog(QDialog, Uuid_Ui):
    def __init__(self):
        super(uuidDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("请输入邀请码")
        self.cancel.clicked.connect(self.close)
        self.ok.clicked.connect(self.ok_btn)

    def ok_btn(self):
        u = self.uuid.text()
        self.flag = joinGame(u, status[0])
        if not u == '':
            if self.flag == 0:
                msgBox = QMessageBox()
                msgBox.setWindowTitle(u'提示')
                msgBox.setText(u"您提供的UUID码错误！")
                msgBox.exec_()
            else:
                self.close()
                self.w = show_online()
                self.w.show()
        else:
            msgBox = QMessageBox()
            msgBox.setWindowTitle(u'提示')
            msgBox.setText(u"请输入您的UUID码")
            msgBox.exec_()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = show_pattern()
    window.setFixedSize(1024, 747)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
