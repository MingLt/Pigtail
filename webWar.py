import requests
import random
import time

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
P2_pokers = []
P2_pokerd = []
P2_pokerc = []
P2_pokerh = []
P2_id = 0
dispostion_pok = []  # 放置区手牌


# 在这里完成在线对战


def login(id, passw):
    url_api = 'http://172.17.173.97:8080/api/user/login'
    # 登录
    id = id
    passw = passw
    data = {  # 这里传递参数
        "student_id": id,
        "password": passw
    }
    response1 = requests.post(url=url_api, data=data)
    dict1 = response1.json()
    if dict1['status'] != 200:
        return False
    re_data1 = dict1['data']
    token = re_data1["token"]
    return token


def createGame(pri, token):
    # 创建对局
    url_api2 = "http://172.17.173.97:9000/api/game"
    data2 = {
        "private": pri
    }
    headers = {'Authorization': 'Bearer {}'.format(token)}
    response2 = requests.post(url=url_api2, headers=headers, data=data2)
    dict2 = response2.json()
    re_data2 = dict2['data']
    uuid = re_data2["uuid"]
    print(dict2)
    return uuid


def joinGame(uuid, token):
    # 加入对局
    url_api3 = "http://172.17.173.97:9000/api/game/{}".format(uuid)
    headers = {'Authorization': 'Bearer {}'.format(token)}
    response3 = requests.post(url=url_api3, headers=headers)
    dict3 = response3.json()
    print(dict3)


def previousOption(token, uid):
    # 获取上一步操作
    headers = {'Authorization': 'Bearer {}'.format(token)}
    url_api4 = "http://172.17.173.97:9000/api/game/{}/last".format(uid)
    response4 = requests.get(url_api4, headers=headers)
    dict4 = response4.json()
    print(dict4)
    return dict4


def executeActions(token, uid, params):
    # 玩家执行操作
    headers = {'Authorization': 'Bearer {}'.format(token)}
    url_api5 = "http://172.17.173.97:9000/api/game/{}".format(uid)
    data5 = params
    response5 = requests.put(url_api5, headers=headers, data=data5)
    dict5 = response5.json()
    print(dict5)
    return dict5


def pPRO():
    cnt_d = 13 - len(al_d)  # 顺序递选
    cnt_s = 13 - len(al_s)
    cnt_h = 13 - len(al_h)
    cnt_c = 13 - len(al_c)
    dProbality = cnt_d / len(reminant_cards)
    cProbality = cnt_c / len(reminant_cards)
    hProbality = cnt_h / len(reminant_cards)
    sProbality = cnt_s / len(reminant_cards)
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


def Judge_dis(digit):
    if len(dispostion_pok) == 0:
        return True
    if dispostion_pok[-1] == digit:  # 判定结果：花色相同
        return False
    else:
        return True


class Player_w():
    def __init__(self):
        self.sum = 0
        self.poker_s = []  # 分别对应红桃方块梅花黑桃
        self.poker_h = []
        self.poker_c = []
        self.poker_d = []
        self.cards = []
        self.name = ''
        self.state = 0  # 默认抽牌
        self.token = ''
        self.uuid = ''
        self.id = 0

    #  绑定点击事件返回牌型数据
    def Poker_statistics(self, dict):
        data = dict["data"]
        str = data["last_code"]
        i = 0
        digit = ''
        for c in str:
            if c == 0 or c == 1:
                i += 1
                if c == 0:
                    self.id = 1
                else:
                    self.id = 0
            if i == 2:
                self.state = c  # 对面玩家选择的状态
            if c != ' ' and i == 2:
                i = -10
                digit = digit + c
        reminant_cards.remove(digit)
        if Judge_dis(digit):
            dispostion_pok.append(digit)
            if digit[0] == 'S':
                self.poker_s.append(digit)
            elif digit[0] == 'H':
                self.poker_h.append(digit)
            elif digit[0] == 'C':
                self.poker_c.append(digit)
            else:
                self.poker_d.append(digit)
        else:
            dispostion_pok.append(digit)
            for card in dispostion_pok:
                if card[0] == 'S':
                    self.poker_s.append(digit)
                elif card[0] == 'H':
                    self.poker_h.append(digit)
                elif card[0] == 'C':
                    self.poker_c.append(digit)
                else:
                    self.poker_d.append(digit)
            dispostion_pok.clear()
        self.sum = len(self.poker_h) + len(self.poker_s) + len(self.poker_c) + len(self.poker_d)
        self.cards = self.poker_s + self.poker_h + self.poker_c + self.poker_d

    """
    在这里增加函数来绑定鼠标点击动作
    """

    def draw_poker(self):
        params = {
            "type": 0
        }
        return params

    def play_poker(self, card):
        params = {
            "type": 0,
            "card": card
        }
        dispostion_pok.append(card)
        return params

    def play(self, flag):
        if flag:
            params = self.draw_poker()
            digit = executeActions(self.token, self.uuid, params)  # 滚去抽牌
            self.Poker_statistics(digit)
        else:
            card = 'S1'
            params = self.play_poker(card)
            self.cards.remove(card)
            self.sum -= 1
            executeActions(self.token, self.uuid, params)
            dispostion_pok.append(card)

    def Tactics(self, sum, state):  # 调用策略分析,即为AI
        if len(already_pok) >= 26:
            if self.sum + len(dispostion_pok) + 2*len(reminant_cards) < sum:  # 我是少的
                params = self.draw_poker()
                digit = executeActions(self.token, self.uuid, params)  # 滚去抽牌
                self.Poker_statistics(digit)
            if sum - self.sum >= 13:  # 我是少的
                params = self.draw_poker()
                digit = executeActions(self.token, self.uuid, params)  # 抽牌
                self.Poker_statistics(digit)
            elif sum + len(dispostion_pok) + 2*len(reminant_cards) < self.sum:
                params = self.draw_poker()
                digit = executeActions(self.token, self.uuid, params)  # 抽牌
                self.Poker_statistics(digit)
            elif self.sum - sum >= 13:  # 我是多的
                dict = pPRO()
                card = ''
                for decor in dict:
                    if decor[0] == 'S' and len(self.poker_s):
                        card = random.choice(self.poker_s)
                        self.poker_s.remove(card)
                        break
                    if decor[0] == 'H' and len(self.poker_h):
                        card = random.choice(self.poker_h)
                        self.poker_h.remove(card)
                        break
                    if decor[0] == 'C' and len(self.poker_c):
                        card = random.choice(self.poker_c)
                        self.poker_c.remove(card)
                        break
                    if decor[0] == 'D' and len(self.poker_d):
                        card = random.choice(self.poker_d)
                        self.poker_d.remove(card)
                        break
                dispostion_pok.append(card)
                params = self.play_poker(card)
                self.cards.remove(card)
                self.sum -= 1
                executeActions(self.token, self.uuid, params)
            elif abs(sum - self.sum) < 13:
                if len(dispostion_pok) >= 13:
                    if state == 0:
                        if len(self.cards) != 0:
                            dict = pPRO()
                            card = ''
                            for decor in dict:
                                if decor[0] == 'S' and len(self.poker_s):
                                    card = random.choice(self.poker_s)
                                    self.poker_s.remove(card)
                                    break
                                if decor[0] == 'H' and len(self.poker_h):
                                    card = random.choice(self.poker_h)
                                    self.poker_h.remove(card)
                                    break
                                if decor[0] == 'C' and len(self.poker_c):
                                    card = random.choice(self.poker_c)
                                    self.poker_c.remove(card)
                                    break
                                if decor[0] == 'D' and len(self.poker_d):
                                    card = random.choice(self.poker_d)
                                    self.poker_d.remove(card)
                                    break
                            dispostion_pok.append(card)
                            params = self.play_poker(card)
                            self.sum -= 1
                            executeActions(self.token, self.uuid, params)
                        else:
                            params = self.draw_poker()
                            digit = executeActions(self.token, self.uuid, params)
                            self.Poker_statistics(digit)
                else:
                    params = self.draw_poker()
                    digit = executeActions(self.token, self.uuid, params)
                    self.Poker_statistics(digit)
        else:
            if sum - self.sum >= 13:  # 我是少的
                params = self.draw_poker()
                digit = executeActions(self.token, self.uuid, params)
                self.Poker_statistics(digit)
            elif self.sum - sum >= 13:  # 我是多的
                dict = pPRO()
                card = ''
                for decor in dict:
                    if decor[0] == 'S' and len(self.poker_s):
                        card = random.choice(self.poker_s)
                        self.poker_s.remove(card)
                        break
                    if decor[0] == 'H' and len(self.poker_h):
                        card = random.choice(self.poker_h)
                        self.poker_h.remove(card)
                        break
                    if decor[0] == 'C' and len(self.poker_c):
                        card = random.choice(self.poker_c)
                        self.poker_c.remove(card)
                        break
                    if decor[0] == 'D' and len(self.poker_d):
                        card = random.choice(self.poker_d)
                        self.poker_d.remove(card)
                        break
                dispostion_pok.append(card)
                params = self.play_poker(card)
                self.sum -= 1
                executeActions(self.token, self.uuid, params)
            else:
                params = self.draw_poker()
                digit = executeActions(self.token, self.uuid, params)
                self.Poker_statistics(digit)


def gameover(token, uid):
    # 玩家执行操作
    headers = {'Authorization': 'Bearer {}'.format(token)}
    url_api5 = "http://172.17.173.97:9000/api/game/{}".format(uid)
    response5 = requests.get(url_api5, headers=headers)
    dict5 = response5.json()
    return dict5


def enemy(data):
    state = 0
    str = data["last_code"]
    i = 0
    card = ''
    for c in str:
        if c == 0 or c == 1:
            i += 1
            if c == 0:
                P2_id = 1
            else:
                P2_id = 0
        if i == 2:
            state = c  # 对面玩家选择的状态
        if c != ' ' and i == 2:
            i = -10
            card = card + c
    if state == 1:  # 出牌
        if card[0] == 'S':  # 存储数据
            P2_pokers.remove(card)
        elif card[0] == 'D':
            P2_pokerd.remove(card)
        elif card[0] == 'C':
            P2_pokerc.remove(card)
        elif card[0] == 'H':
            P2_pokerh.remove(card)
        dispostion_pok.append(card)
    else:  # 抽牌
        if card[0] == 'S':  # 存储数据
            P2_pokers.append(card)
            al_s.append(card)
        elif card[0] == 'D':
            P2_pokerd.append(card)
            al_d.append(card)
        elif card[0] == 'C':
            P2_pokerc.append(card)
            al_c.append(card)
        elif card[0] == 'H':
            P2_pokerh.append(card)
            al_h.append(card)
        already_pok.append(card)
        reminant_cards.remove(card)
        return state


def web_main():
    # 存储对方花色

    # 这里要另加是选择加入对局还是 创建对局
    player = Player()
    id = '031902341'
    passw = '20011013.s'
    token1 = login(id, passw)  # 玩家1的token
    player.token = token1
    if token1 is False:
        print('账号或密码错误')
    is_private = True
    uuid = createGame(is_private, token1)  # 玩家1创建对局
    if token1 is False:
        print('账号或密码错误')
    joinGame(uuid, token1)  # 玩家1加入自己对局
    player.uuid = uuid

    while len(reminant_cards):
        while True:  # 每隔5秒定时申请一次
            dict = previousOption(token1, uuid)  # 玩家1获取对局上一步操作
            if dict["code"] == 403:
                print('未开始对局')
            else:
                break
            time_remaining = 5 - time.time() % 5
            time.sleep(time_remaining)

        while True:
            dict = previousOption(token1, uuid)  # 玩家1获取对局上一步操作
            if dict["code"] != 200:
                dict1 = gameover(token1, uuid)
                data1 = dict1["data"]
            data = dict["data"]
            if data["your_turn"]:
                break
        # 将对面玩家的数据存起来
        state = enemy(data)
        flag1 = True
        player.play(flag1)  # 监听是抽牌还是打牌
        sum = len(P2_pokers) + len(P2_pokerc) + len(P2_pokerd) + len(P2_pokerh)
        flag = False
        if flag:     # 托管功能
            player.Tactics(sum, state)


if __name__ == '__main__':
    web_main()
