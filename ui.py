# -*- coding: utf-8 -*-
"""ui.py"""

import pygame
import sys

BLACK = (0, 0, 0)  # Define BLACK color here
GREEN = (0, 100, 0)  # Define GREEN color here
WHITE = (255, 255, 255)  # Define WHITE color here
SCREEN_WIDTH = 1280  # Define SCREEN_WIDTH here

# Countdown function
def countdown(screen):
    font = pygame.font.SysFont(None, 100)
    for i in range(3, 0, -1):
        screen.fill(GREEN)
        text = font.render(str(i), True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(1000)


# Player suit function
def get_player_suit(screen, font, player):
    option = None
    selected_suit = None
    if player == 1:
        screen.fill(GREEN)
        player1_text = font.render("Select a Suit", True, WHITE)
        player1_rect = player1_text.get_rect(midtop=(640, 120))
        screen.blit(player1_text, player1_rect)
        suits = ['Spades', 'Clubs', 'Hearts']
        button_width = 200
        button_height = 50
        option1_buttons = [font.render(suit, True, BLACK) for suit in suits]
        option1_button_rects = []
        for i, button in enumerate(option1_buttons):
            button_rect = pygame.Rect((SCREEN_WIDTH // 2 - button_width // 2, 250 + i * 60), (button_width, button_height))
            option1_button_rects.append(button_rect)
            pygame.draw.rect(screen, WHITE, button_rect)
            button_text_rect = button.get_rect(center=button_rect.center)
            screen.blit(button, button_text_rect)

        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, button_rect in enumerate(option1_button_rects):
                        if button_rect.collidepoint(mouse_pos):
                            option = i
                            selected_suit = suits[option]
                            print("User suit:", selected_suit)  # Print user's selected suit
                            running = False
                            break

    else:
        # Computer chooses a suit from the remaining two
        selected_suit = computer_choose_suit(player)

    return selected_suit

# Player input functions
def get_player_options(screen, font, player):
    option = None
    if player == 1:
        screen.fill(GREEN)
        player1_text = font.render("Player 1 Options", True, WHITE)
        player1_rect = player1_text.get_rect(midtop=(640, 120))
        screen.blit(player1_text, player1_rect)
        opt = ['Adaptive', 'Balanced', 'Dynamic', 'Random', 'Equal']
        button_width = 200
        button_height = 50
        option1_buttons = [font.render(f"{opt[i]}", True, BLACK) for i in range(5)]
        for i, button in enumerate(option1_buttons):
                button_rect = pygame.Rect((SCREEN_WIDTH // 2 - button_width // 2, 250 + i * 60), (button_width, button_height))
                pygame.draw.rect(screen, WHITE, button_rect)
                button_text_rect = button.get_rect(center=button_rect.center)  # Get text rectangle
                screen.blit(button, button_text_rect)
    else:
        screen.fill(GREEN)
        player2_text = font.render("Player 2 Options", True, WHITE)
        player2_rect = player2_text.get_rect(midtop=(640, 120))
        screen.blit(player2_text, player2_rect)
        opt = ['Maximum', 'Minimum', 'Adaptive', 'Balanced', 'Dynamic', 'Random', 'Equal']
        button_width = 200
        button_height = 50
        option2_buttons = [font.render(f"{opt[i]}", True, BLACK) for i in range(7)]
        for i, button in enumerate(option2_buttons):
                button_rect = pygame.Rect((SCREEN_WIDTH // 2 - button_width // 2, 200 + i * 60), (button_width, button_height))
                pygame.draw.rect(screen, WHITE, button_rect)
                button_text_rect = button.get_rect(center=button_rect.center)  # Get text rectangle
                screen.blit(button, button_text_rect)
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if player == 1:
                    for i, option_text in enumerate(option1_buttons):
                        button_rect = pygame.Rect((SCREEN_WIDTH // 2 - button_width // 2, 250 + i * 60), (button_width, button_height))
                        if button_rect.collidepoint(mouse_pos):
                            option = i + 1  # Option numbers start from 1
                            running = False
                            break
                else:
                    for i, option_text in enumerate(option2_buttons):
                        button_rect = pygame.Rect((SCREEN_WIDTH // 2 - button_width // 2, 250 + i * 60), (button_width, button_height))
                        if button_rect.collidepoint(mouse_pos):
                            option = i + 1  # Option numbers start from 1
                            running = False
                            break

    return option
    # Player input function
def get_player_input(screen, font, player_cards, player_suit, opponent_cards, opponent_suit):
    screen.fill(GREEN)
    selected_card = None
    player_text = font.render("Select a Card", True, WHITE)
    screen.blit(player_text, (20, 20))
    button_width = 120
    button_height = 150
    player1_buttons = [font.render(str(card), True, BLACK) for card in player_cards]
    player1_button_rects = []
    for i, button in enumerate(player1_buttons):
        button_rect = pygame.Rect((20 + i * 150, 100), (button_width, button_height))
        player1_button_rects.append(button_rect)
        pygame.draw.rect(screen, WHITE, button_rect)
        button_text_rect = button.get_rect(center=button_rect.center)  # Get text rectangle
        screen.blit(button, button_text_rect)

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, button_rect in enumerate(player1_button_rects):
                    if button_rect.collidepoint(mouse_pos):
                        selected_card = player_cards[i]
                        running = False
                        break

    return selected_card

