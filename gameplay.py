import pygame
import sys
from strategies import computer_choose_suit, player2_bid, adaptive_bidding_strategy, balanced_bidding_strategy,dynamic_adaptation_strategy, pick_diamond, update_suit, scoreboard, winner
from ui import countdown, get_player_suit, get_player_input

# Pygame initialization
pygame.init()

# Set up the screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Diamond Card Auction Game")

WHITE = (255, 255, 255)
GREEN = (0, 100, 0)

font = pygame.font.SysFont(None, 46)

def main_game(screen, font, option1, option2, sub_option2, player_suit, computer_suit):
    global scores
    player1_bids = []
    player2_bids = []
    cards = list(all_cards.keys())  # Assuming all_cards is defined in strategies.py
    player1_cards = list(all_cards.keys())  # Assuming all_cards is defined in strategies.py
    player2_cards = list(all_cards.keys())  # Assuming all_cards is defined in strategies.py
    for i in range(13):
        diamond_card = pick_diamond(cards)
        screen.fill(GREEN)
        screen.blit(card_images['diamonds'][all_cards[diamond_card] - 2], (150, 40))
        pygame.time.delay(2000)
        bid1 = get_player_input(screen, font, player1_cards, player_suit, player2_cards, computer_suit)
        player1_bids.append(bid1)
        bid2 = player2_bid(diamond_card, player2_cards, option2, player1_bids, scores, sub_option2)
        player2_bids.append(bid2)
        print(diamond_card, bid1, bid2)

        # Display player 1 cards
        [cards, player1_cards, player2_cards] = update_suit([cards, player1_cards, player2_cards], [diamond_card, bid1, bid2])
        player_text = font.render(f"Player 1 Cards: ", True, WHITE)
        screen.blit(player_text, (20, 400))
        player_text = font.render(f"Player 2 Cards: ", True, WHITE)
        screen.blit(player_text, (20, 520))
        for i in player1_cards:
            screen.blit(card_images[player_suit][all_cards[i] - 2], (300+((all_cards[i]-2)*60), 350))
        for i in player2_cards:
            screen.blit(card_images[computer_suit][all_cards[i] - 2], (300+((all_cards[i]-2)*60), 450))
        # Display bids
        bid_text = font.render(f"Player 1 Bid: ", True, WHITE)
        screen.blit(bid_text, (450, 100))
        screen.blit(card_images[player_suit][all_cards[bid1] - 2], (650, 40))
        bid_text = font.render(f"Player 2 Bid: ", True, WHITE)
        screen.blit(bid_text, (850, 100))
        screen.blit(card_images[computer_suit][all_cards[bid2] - 2], (1050, 40))
        pygame.display.flip()
        pygame.time.delay(4000)
        scoreboard(diamond_card, bid1, bid2)
        print(scores)
        # Display scoreboard
        screen.fill(GREEN)
        scoreboard_text = font.render(f"Scores: {scores[0]} - {scores[1]}", True, WHITE)
        scoreboard_rect = scoreboard_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(scoreboard_text, scoreboard_rect)
        pygame.display.flip()
        pygame.time.delay(2000)

    # Display winner
    screen.fill(GREEN)
    winner_text = font.render(f"Winner: {winner()}", True, WHITE)
    winner_rect = winner_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(winner_text, winner_rect)
    pygame.display.flip()
    pygame.time.delay(3000)


def main():
    player_suit = get_player_suit(screen, font, 1)
    computer_suit = computer_choose_suit(player_suit)
    option1 = 1
    option2 = 1
    countdown(screen)
    if option2 < 2:
        main_game(screen, font, option1, option2, 0, player_suit.lower(), computer_suit.lower())
    else:
        main_game(screen, font, option1, 3, option2 - 2, player_suit.lower(), computer_suit.lower())

    pygame.quit()

if __name__ == "__main__":
    main()
