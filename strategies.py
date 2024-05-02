# -*- coding: utf-8 -*-
"""strategies.py"""

import random

# Function to let the computer choose a suit from the remaining two
def computer_choose_suit(selected_suit):
    remaining_suits = ['Spades', 'Clubs', 'Hearts']
    remaining_suits.remove(selected_suit)
    computer_suit = random.choice(remaining_suits)
    print("Computer suit:", computer_suit)  # Print computer's chosen suit
    return computer_suit

# Player 2 bid function
def player2_bid(diamond_card, player_cards, option, opponent_bids, scores, sub_option):
    if option == 1:
        return max(player_cards)
    elif option == 2:
        return min(player_cards)
    else:
        return bid_solver(diamond_card, player_cards, sub_option, opponent_bids, scores)

# Adaptive bidding strategy function
def adaptive_bidding_strategy(diamond_card, player_cards, opponent_bids):
    aggressiveness_threshold = 8

    if len(opponent_bids) != 0 and max([all_cards[_] for _ in opponent_bids]) > aggressiveness_threshold:
        return max(player_cards)
    elif all_cards[diamond_card] < 8:
        return min(player_cards)
    else:
        return max(player_cards)

# Balanced bidding strategy function
def balanced_bidding_strategy(diamond_card, player_cards):
    if all_cards[diamond_card] >= 10:
        return max(player_cards)
    elif all_cards[diamond_card] <= 5:
        return min(player_cards)
    else:
        return max(player_cards)

# Dynamic adaptation strategy function
def dynamic_adaptation_strategy(diamond_card, player_cards, opponent_aggressiveness, player_score):
    if opponent_aggressiveness == "aggressive" and player_score < 50:
        return min(player_cards)
    elif opponent_aggressiveness == "conservative" and player_score >= 50:
        return max(player_cards)
    else:
        return max(player_cards)

def pick_diamond(cards):
    return random.choice(cards)

def update_suit(suits, cards):
    for i in range(len(suits)):
        suits[i].remove(cards[i])
    return suits

def scoreboard(diamond_card, bid1, bid2):
    global scores
    if all_cards[bid1] > all_cards[bid2]:
        scores[0] = scores[0] + all_cards[diamond_card]
    elif all_cards[bid2] > all_cards[bid1]:
        scores[1] = scores[1] + all_cards[diamond_card]
    else:
        scores = [scores[_] + all_cards[diamond_card] / 2 for _ in range(2)]
    return 

def winner():
    m = max(scores)
    if m == scores[0] and m != scores[1]:
        return "Player 1"
    elif m == scores[1] and m != scores[0]:
        return "Player 2"
    return "Draw"
