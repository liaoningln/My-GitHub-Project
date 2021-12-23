def check_card_number(card_num):
    s = 0
    card_num_length = len(card_num)
    for _ in range(1, card_num_length + 1):
        t = int(card_num[card_num_length - _])
        print("当前银行卡对应数字t={}".format(t))
        print("当前_为{}".format(_))
        print("_取模{}".format(_ % 2))
        if _ % 2 == 0:
            print("当前是偶数位")
            t *= 2
            print("t={}".format(t))
            s += t if t < 10 else t % 10 + t // 10

        else:
            print("当前为奇数位")
            s += t
        print("s={}".format(s))
    return s % 10 == 0


if __name__ == '__main__':
    print(check_card_number('6226095711989751'))


def check_card_number_str(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        return checksum % 10


def is_luhn_valid(card_number):
    return check_card_number_str(card_number) == 0