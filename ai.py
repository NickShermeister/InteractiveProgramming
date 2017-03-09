import card_def
import card_game
import deck_def
import hand_def
import game_constants
import pygame
import card_game
import sys
import time
from pygame.locals import *

class AI(object):
    """This is where the AI does its stuff.

    If an AI can play it will play.

    For the current mode, there will be no card counting and the AI will always play its lowest valued card that it can play. It has a chance of playing Trump, based on the value of the trump."""

    def __init__(self):
        self.difficulty = 'easy'
        self.playing = True

    def play_cards(self, hands, rule_book):
        playing = rule_book.turn
        if rule_book.turn:
            temp_card = self.find_lowest_playable_card(hands, rule_book, hands.player1_field[-1])
            if temp_card is not None:
                temp_card.play(-1, -1, hands, hands.player1_field[-1])
                playing = rule_book.turn
            if len(hands.player1_field) > len(hands.player2_field): #player 1's turn
                rule_book.play(2)
            else:
                pass
                #rule_book.play(1)
        else:
            temp_card = self.find_lowest_playable_card(hands, rule_book, card)
            if temp_card is not None:
                temp_card.play(-1, -1, hands)
            else:
                rule_book.play(2)
            playing = not rule_book.turn

    def find_lowest_playable_card(self, hand, rule_book, cards_on = None):
        i = len(hand.player1_field)-1
        lowval = 15
        tempcard = None
        print("hi")
        print(rule_book.turn)
        if rule_book.turn:
            for card in hand.cards_in_opponent:
                print("one")
                print(rule_book.playable_defense(hand.player1_field[i], card))
                if rule_book.playable_defense(hand.player1_field[i], card):
                    print("here")
                    if card.value < lowval and card.suit != rule_book.trump and card.value>hand.player1_field[i].value and card.suit==hand.player1_field[i].suit:
                        lowval = card.value
                        tempcard = card
                    elif card.value < lowval and card.suit == rule_book.trump and lowval > 14 and card.value>hand.player1_field[i].value:
                        lowval = card.value
                        tempcard = card
        else:
            for card in hand.cards_in_opponent:
                if rule_book.playable_offense(hand, card):
                    if card.value < lowval:
                        lowval = card.value
                        tempcard = card
        return tempcard
