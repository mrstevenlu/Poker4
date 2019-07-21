# -*- coding: UTF-8 -*-

# author by : Steven Lu

import random
import os
import codecs
import csv

def create_deck_54(new_deck):
    '推出一副新牌'
    print('\n 新牌')
    jokers = ('♞', '♘')

    marks = ('♠', '♥', '♦', '♣')

    nums = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    for c in jokers:
        new_deck.append(c)

    for cn in nums:
        for cm in marks:
            card = cm + cn
            new_deck.append(card)
    return


def create_deck_52(new_deck):
    '推出一副新牌'
    print('\n 新牌')

    marks = ('♠', '♥', '♦', '♣')

    nums = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    for cn in nums:
        for cm in marks:
            card = cm + cn
            new_deck.append(card)
    return


def shuffled_deck(deck_to_be_shuffled):
    '洗牌'
    print('\n 洗牌完毕')
    random.shuffle(deck_to_be_shuffled)
    return

'''
def record_deck(deck_to_be_record, filename):
    '记录一副牌'
    print('\n 记录扑克牌')
    out_path = os.getcwd() + '\\OutputDecks\\' + filename
    f = codecs.open(out_path, "w", "utf-8")
    for card in deck_to_be_record:
        f.write(card)
        f.write('\n')
    f.close
    return
'''
def record_deck_csv(deck_to_be_record,csv_filename):

    csv_path=os.getcwd()+'\\csv_decks\\'+csv_filename

    with open(csv_path,"w",encoding='utf-8',newline='')as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(deck_to_be_record)
        return

def read_deck_csv(csv_filename, out_deck):
    '读取 CSV 格式的牌，并把它读取到一个列表中去'

    in_path = os.getcwd() + '\\csv_decks\\' + csv_filename
    with open(in_path, "r", encoding='utf8') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            out_deck.extend(line)

    # Poker 4.0 added
#    msg = '从文件 (%s) 中读取了牌的内容' % in_path
#    logger.debug(msg)

    return


def make_deck_by_type(play_type, out_deck):
    if play_type == 1:
        create_deck_54(out_deck)
        shuffled_deck(out_deck)
        record_deck_csv(out_deck, '争上游——刚洗好的牌.csv')

    elif play_type == 2:
        create_deck_52(out_deck)
        shuffled_deck(out_deck)
        record_deck_csv(out_deck, '桥牌——刚洗好的牌.csv')

    elif play_type == 3:
        create_deck_54(out_deck)
        shuffled_deck(out_deck)
        record_deck_csv(out_deck, '三人斗地主——刚洗好的牌.csv')

    elif play_type == 4:
        deck_a = []
        create_deck_54(deck_a)
        out_deck.extend(deck_a)
        deck_b = []
        create_deck_54(deck_b)
        out_deck.extend(deck_b)
        shuffled_deck(out_deck)
        record_deck_csv(out_deck, '四人斗地主——刚洗好的牌.csv')
    return
