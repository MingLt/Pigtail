import random

reminant_cards = ['S1', 'H1', 'C1', 'D1', 'S2', 'H2', 'C2', 'D2', 'S3', 'H3', 'C3', 'D3',
                  'S4', 'H4', 'C4', 'D4', 'S5', 'H5', 'C5', 'D5',
                  'S6', 'H6', 'C6', 'D6', 'S7', 'H7', 'C7', 'D7',
                  'S8', 'H8', 'C8', 'D8', 'S9', 'H9', 'C9', 'D9',
                  'S10', 'H10', 'C10', 'D10', 'SJ', 'HJ', 'CJ', 'DJ',
                  'SQ', 'HQ', 'CQ', 'DQ', 'SK', 'HK', 'CK', 'DK']
already_pok = []

al_d = []
al_s = []
al_c = []
al_h = []
dispostion_pok = []  # 放置区手牌
ran = random.randint(1, 2)  # 决定谁先开始


class aiwar_Player():
    def __init__(self):
        self.sum = 0
        self.poker_s = []  # 分别对应红桃方块梅花黑桃
        self.poker_h = []
        self.poker_c = []
        self.poker_d = []
        self.cards = []
        self.name = ''
        self.state = 0  # 默认抽牌

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


class AI_player():
    def __init__(self):
        self.sum = 0
        self.poker_s = []  # 分别对应红桃方块梅花黑桃
        self.poker_h = []  # 各花色手牌
        self.poker_c = []
        self.poker_d = []
        self.cards = []  # 所持手牌
        self.name = 'AI'

    def Judge_dis(self, digit):
        card = dispostion_pok[-1]
        if len(dispostion_pok) == 0:
            return True
        if card[0] == digit[0]:  # 判定结果：花色相同
            return False
        else:
            return True

    def pPRO(self):  # 计算概率
        cnt_d = 13 - len(al_d)  # 顺序递选
        cnt_s = 13 - len(al_s)
        cnt_h = 13 - len(al_h)
        cnt_c = 13 - len(al_c)
        dProbality = cnt_d / len(reminant_cards)
        cProbality = cnt_c / len(reminant_cards)
        hProbality = cnt_h / len(reminant_cards)
        sProbality = cnt_s / len(reminant_cards)
        if not len(dispostion_pok):
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
        dict = sorted(dict.items())
        return dict

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

    def Play_poker(self, card):  # AI的出牌动作
        self.state = 1
        click = card[0]
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
                self.Play_poker(card)
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
                            self.Play_poker(card)
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
                self.Play_poker(card)
                d = card
            else:
                d = self.draw_poker()
        return d


def AI_main():
    player = aiwar_Player()
    player.name = 'P1'
    AI = AI_player()
    flag = False  # false代表抽牌
    while len(reminant_cards) != 0:
        if ran == 1:
            player.draw_poker()
            num = player.sum
            state = player.state
            AI.Tactics(num, state)
        else:
            num = player.sum
            state = player.state
            AI.Tactics(num, state)
            player.draw_poker()


if __name__ == '__main__':
    AI_main()
