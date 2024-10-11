import random

hand = ["グー", "チョキ", "パー"]


def random_hand():
    return random.randint(0, 2)


def judge(a, b):
    if a == b:
        return "引き分け"
    elif (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
        return "Aの勝ち"
    else:
        return "Bの勝ち"


def play_rock():
    A_win_count = 0
    B_win_count = 0

    while A_win_count <= 2 and B_win_count <= 2:

        a_hand = random_hand()
        b_hand = random_hand()
        result = judge(a_hand, b_hand)
        print(f"A: {hand[a_hand]} vs. B: {hand[b_hand]} → {result}")

        if result == "Aの勝ち" and result != "引き分け":
            A_win_count += 1
        elif result == "Bの勝ち" and result != "引き分け":
            B_win_count += 1

    if A_win_count > B_win_count:
        print("最終的にAの勝ち")
    else:
        print("最終的にBの勝ち")


play_rock()
