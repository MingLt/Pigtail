import random

# 所有的牌S黑桃 H红心 C梅花 D方块
reminant_cards = ['S1', 'H1', 'C1', 'D1', 'S2', 'H2', 'C2', 'D2', 'S3', 'H3', 'C3', 'D3',
                  'S4', 'H4', 'C4', 'D4', 'S5', 'H5', 'C5', 'D5',
                  'S6', 'H6', 'C6', 'D6', 'S7', 'H7', 'C7', 'D7',
                  'S8', 'H8', 'C8', 'D8', 'S9', 'H9', 'C9', 'D9',
                  'S10', 'H10', 'C10', 'D10', 'SJ', 'HJ', 'CJ', 'DJ',
                  'SQ', 'HQ', 'CQ', 'DQ', 'SK', 'HK', 'CK', 'DK']
already_pok = []
dispostion_pok = []  # 放置区手牌
al_d = []
al_s = []
al_c = []
al_h = []

ran = random.randint(1, 2)  # 决定谁先开始


class Player():
    def __init__(self):
        self.sum = 0
        self.poker_s = []  # 分别对应红桃方块梅花黑桃
        self.poker_h = []
        self.poker_c = []
        self.poker_d = []
        self.cards = []
        self.name = ''
        self.state = 0  # 默认抽牌

    def pPRO(self):
        cnt_d = 13 - len(al_d)  # 顺序递选
        cnt_s = 13 - len(al_s)
        cnt_h = 13 - len(al_h)
        cnt_c = 13 - len(al_c)
        dProbality = 0
        cProbality = 0
        hProbality = 0
        sProbality = 0
        dProbality = cnt_d / len(reminant_cards)
        cProbality = cnt_c / len(reminant_cards)
        hProbality = cnt_h / len(reminant_cards)
        sProbality = cnt_s / len(reminant_cards)
        if len(dispostion_pok) == 0:
            dict = {
                'S': sProbality,
                'H': hProbality,
                'C': cProbality,
                'D': dProbality
            }
        else:
            digit = dispostion_pok[-1]
            if digit[0] == 'S':  # 只能从另外三个花色选出
                dict = {
                    'H': hProbality,
                    'C': cProbality,
                    'D': dProbality
                }
            elif digit[0] == 'H':
                dict = {
                    'S': sProbality,
                    'C': cProbality,
                    'D': dProbality
                }
            elif digit[0] == 'C':
                dict = {
                    'S': sProbality,
                    'H': hProbality,
                    'D': dProbality
                }
            else:
                dict = {
                    'S': sProbality,
                    'H': hProbality,
                    'C': cProbality
                }
        dict = sorted(dict.items())  # 对概率排序
        return dict

    def Judge_dis(self, digit):
        card = dispostion_pok[-1]
        if len(dispostion_pok) == 0:
            return True
        if card[0] == digit[0]:  # 判定结果：花色相同
            return False
        else:
            return True

    def Poker_statistics(self, digit):
        # 自己手牌数据
        if len(dispostion_pok) != 0:
            if self.Judge_dis(digit):
                dispostion_pok.append(digit)
            else:
                dispostion_pok.append(digit)
                for card in dispostion_pok:
                    if card[0] == 'S':
                        self.poker_s.append(card)
                    elif card[0] == 'H':
                        self.poker_h.append(card)
                    elif card[0] == 'C':
                        self.poker_c.append(card)
                    else:
                        self.poker_d.append(card)
                dispostion_pok.clear()
        elif len(dispostion_pok) == 0:
            dispostion_pok.append(digit)
        self.cards = self.poker_s + self.poker_h + self.poker_c + self.poker_d
        self.sum = len(self.cards)

    def draw_poker(self):
        self.state = 0
        while True:
            digit = random.choice(reminant_cards)
            if digit in already_pok:
                pass
            else:
                break
        reminant_cards.remove(digit)
        already_pok.append(digit)
        if digit[0] == 'S':
            al_s.append(digit)
        elif digit[0] == 'H':
            al_h.append(digit)
        elif digit[0] == 'C':
            al_c.append(digit)
        else:
            al_d.append(digit)
        self.Poker_statistics(digit)
        return digit

    """
    在这里增加函数来绑定鼠标点击动作
    """

    def AIPlay_poker(self, card):  # AI的出牌动作
        self.state = 1
        print(card)
        print(1234567)
        click = card[0]
        print(90898989)
        dicard = ''
        if click == 'S':
            dicard = self.poker_s[-1]
            self.poker_s.remove(dicard)
            self.cards.remove(dicard)
        elif click == 'H':
            dicard = self.poker_h[-1]
            self.poker_h.remove(dicard)
            self.cards.remove(dicard)
        elif click == 'C':
            dicard = self.poker_c[-1]
            self.poker_c.remove(dicard)
            self.cards.remove(dicard)
        elif click == 'D':
            dicard = self.poker_d[-1]
            self.poker_d.remove(dicard)
            self.cards.remove(dicard)
        self.sum -= 1
        dispostion_pok.append(dicard)
        return dicard

    def Tactics(self, sum, state):  # 调用策略分析,即为AI
        d = ''
        if len(already_pok) >= 26:
            if self.sum + len(dispostion_pok) + len(reminant_cards) <= sum:
                d = self.draw_poker()  # 滚去抽牌
            if sum - self.sum >= 13:  # 我是少的
                d = self.draw_poker()
            elif sum + len(dispostion_pok) + 2 * len(reminant_cards) < self.sum:
                d = self.draw_poker()
            elif self.sum - sum >= 13:  # 我是多的
                dict = self.pPRO()
                card = ''
                for decor in dict:
                    if decor[0] == 'S' and len(self.poker_s):
                        card = self.poker_s[-1]
                        break
                    if decor[0] == 'H' and len(self.poker_h):
                        card = self.poker_h[-1]
                        break
                    if decor[0] == 'C' and len(self.poker_c):
                        card = self.poker_c[-1]
                        break
                    if decor[0] == 'D' and len(self.poker_d):
                        card = self.poker_d[-1]
                        break
                self.AIPlay_poker(card)
                d = card
            elif abs(sum - self.sum) < 13:  # 相差不多
                if len(dispostion_pok) >= 13:
                    if state == 0:  # 对方出牌
                        if len(self.cards) != 0:
                            dict = self.pPRO()
                            card = ''
                            for decor in dict:
                                if decor[0] == 'S' and len(self.poker_s):
                                    card = self.poker_s[-1]
                                    break
                                if decor[0] == 'H' and len(self.poker_h):
                                    card = self.poker_h[-1]
                                    break
                                if decor[0] == 'C' and len(self.poker_c):
                                    card = self.poker_c[-1]
                                    break
                                if decor[0] == 'D' and len(self.poker_d):
                                    card = self.poker_d[-1]
                                    break
                            self.AIPlay_poker(card)
                            d = card
                        else:
                            d = self.draw_poker()
                else:
                    d = self.draw_poker()
        else:
            if sum - self.sum >= 13:  # 我是少的
                d = self.draw_poker()
            elif self.sum - sum >= 13:  # 我是多的
                dict = self.pPRO()
                card = ''
                for decor in dict:
                    if decor[0] == 'S' and len(self.poker_s):
                        card = self.poker_s[-1]
                        break
                    if decor[0] == 'H' and len(self.poker_h):
                        card = self.poker_h[-1]
                        break
                    if decor[0] == 'C' and len(self.poker_c):
                        card = self.poker_c[-1]
                        break
                    if decor[0] == 'D' and len(self.poker_d):
                        card = self.poker_d[-1]
                        break
                self.AIPlay_poker(card)
                d = card
            else:
                d = self.draw_poker()
        return d


def local_main():
    p1 = Player()
    p1.name += 'P1'
    p2 = Player()
    p2.name += 'P2'
    flag = True
    flag2 = False
    while len(reminant_cards) != 0:
        if ran == 1:
            # flag为True代表从手里出牌 ，绑定点击动作
            p1.draw_poker()
            if flag2:  # 调用托管功能
                p1.Tactics(p2.sum, p2.state)
            p2.draw_poker()
        else:
            p2.draw_poker()
            p1.draw_poker()


if __name__ == '__main__':
    local_main()
