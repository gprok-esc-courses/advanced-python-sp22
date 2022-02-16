import requests


class Hangman:
    def __init__(self):
        self.word = ''
        self.secret = ''
        self.error = ''
        self.correct = []
        self.wrong = []

    def get_random_word(self):
        response = requests.get('https://random-word-api.herokuapp.com/word?number=1')
        if response.status_code != 200:
            self.error = 'Server error, try again'
        else:
            word_list = response.json()
            self.word = word_list[0]
            self.generate_secret_word()

    def generate_secret_word(self):
        self.secret = self.word[0] + ('_'*(len(self.word)-2)) + self.word[-1]

    def update_secret_word(self):
        self.secret = self.word[0]
        for i in range(1, len(self.word) - 1):
            if self.word[i] in self.correct:
                self.secret += self.word[i]
            else:
                self.secret += '-'
        self.secret += self.word[-1]

    def game_over(self):
        return self.word == self.secret or len(self.wrong) == 6

    def play(self, ch):
        if ch in self.correct or ch in self.wrong:
            print('Character ', ch, ' already played')
        else:
            if ch in self.word:
                self.correct.append(ch)
                self.update_secret_word()
                if self.word == self.secret:
                    print("Game Over, you WIN!")
            else:
                self.wrong.append(ch)
                if len(self.wrong) == 6:
                    print("Game Over, You are Hanged!")


if __name__ == '__main__':
    hangman = Hangman()
    hangman.get_random_word()
    print(hangman.word)
    while True:
        print(hangman.secret)
        ch = input('Give character: ')
        hangman.play(ch)
        if hangman.game_over():
            print(hangman.word)
            break