from turtle import Turtle
from pathlib import Path

ALIGN = 'center'
FONT = ('Courier', 20, 'normal')
HIGH_SCORE_FILE = Path.home() / '.snake_game_high_score.txt'

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()
        self.color('gold')
        self.penup()
        self.goto(0, 255)
        self.hideturtle()
        self.update_scoreboard()

    def load_high_score(self):
        try:
            return int(HIGH_SCORE_FILE.read_text())
        except (FileNotFoundError, ValueError):
            return 0

    def save_high_score(self):
        HIGH_SCORE_FILE.write_text(str(self.high_score))

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} - High Score: {self.high_score}', align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.update_scoreboard()

