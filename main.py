# Creates a Tkinter application that shows the current time as a word clock format

#   0123456789ABC
# 0 ITRISUHALFTEN
# 1 QUARTERTWENTY
# 2 FIVEQMINUTEST
# 3 PASTMTOSAMOPM
# 4 ONENTWOZTHREE
# 5 FOURFIVESEVEN
# 6 SIXEIGHTYNINE
# 7 TENELEVENPHIL
# 8 TWELVELOCLOCK


import tkinter as tk
import time

class SentenceClock(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("What time is it?")
        
        self.letters = [
            ['I','T','R','I','S','U','H','A','L','F','T','E','N'],
            ['Q','U','A','R','T','E','R','T','W','E','N','T','Y'],
            ['F','I','V','E','Q','M','I','N','U','T','E','S','T'],
            ['P','A','S','T','M','T','O','S','A','M','O','P','M'],
            ['O','N','E','N','T','W','O','Z','T','H','R','E','E'],
            ['F','O','U','R','F','I','V','E','S','E','V','E','N'],
            ['S','I','X','E','I','G','H','T','Y','N','I','N','E'],
            ['T','E','N','E','L','E','V','E','N','P','H','I','L'],
            ['T','W','E','L','V','E','L','O','C','L','O','C','K'],
        ]

        self.labels = {}

        for i in range(0, len(self.letters)):
            for j in range(0, len(self.letters[i])):
                self.labels['label_' + str(i) + '_' + str(j)] = tk.Label(self, fg="black", text=self.letters[i][j], font="Helvetica 20")
                self.labels['label_' + str(i) + '_' + str(j)].grid(column=j, row=i)

        self.after(1000, self.update_time)

    def update_time(self):
        for i in range(0, len(self.letters)):
            for j in range(0, len(self.letters[i])):
                self.labels['label_' + str(i) + '_' + str(j)].config(fg="light pink", font="Helvetica 20")

        current_time = time.localtime()

        hour = int(time.strftime("%I", current_time))
        minute = int(time.strftime("%M", current_time))
        am_or_pm = time.strftime("%p", current_time)

        letters = self.translate_time(hour, minute, am_or_pm)

        for letter in letters:
            self.labels['label_' + str(letter[0]) + '_' + str(letter[1])].config(fg="black", font="Helvetica 25 bold italic")
        
        self.after(1000, self.update_time)

    def translate_to_or_past(self, minute):
        to_or_past = []
        if 3 <= minute < 33:
            to_or_past = [[3,0],[3,1],[3,2],[3,3]] # PAST
        elif 33 <= minute <= 57:
            to_or_past = [[3,5],[3,6]] # TO
        return to_or_past

    def translate_minute(self, minute):
        if (minute > 30):
            minute = 60 - minute

        if minute >= 3:
            minute_blocks = [
                [[2,0],[2,1],[2,2],[2,3],[2,5],[2,6],[2,7],[2,8],[2,9],[2,10],[2,11]], # FIVE
                [[0,10],[0,11],[0,12],[2,5],[2,6],[2,7],[2,8],[2,9],[2,10],[2,11]], # TEN
                [[0,7],[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6]], # A QUARTER
                [[1,7],[1,8],[1,9],[1,10],[1,11],[1,12],[2,5],[2,6],[2,7],[2,8],[2,9],[2,10],[2,11]], # TWENTY
                [[1,7],[1,8],[1,9],[1,10],[1,11],[1,12],[2,0],[2,1],[2,2],[2,3],[2,5],[2,6],[2,7],[2,8],[2,9],[2,10],[2,11]], # TWENTYFIVE
                [[0,6],[0,7],[0,8],[0,9]], # HALF
            ]
            mapped_minute_value = round((0 + (5 - 0) * ((minute - 3) / (28 - 3))) - 0.4)
            minute_name = minute_blocks[mapped_minute_value]
        else:
            minute_name = ''
        return minute_name

    def translate_hour(self, hour, minute):
        hours = [
            [[4,0],[4,1],[4,2]], #ONE
            [[4,4],[4,5],[4,6]], # TWO
            [[4,8],[4,9],[4,10],[4,11]], # THREE
            [[5,0],[5,1],[5,2],[5,3]], # FOUR
            [[5,4],[5,5],[5,6],[5,7]], # FIVE
            [[6,0],[6,1],[6,2]], # SIX
            [[5,8],[5,9],[5,10],[5,11],[5,12]], # SEVEN
            [[6,3],[6,4],[6,5],[6,6],[6,7]], # EIGHT
            [[6,9],[6,10],[6,11],[6,12]], # NINE
            [[7,0],[7,1],[7,2]], # TEN
            [[7,3],[7,4],[7,5],[7,6],[7,7],[7,8]], # ELEVEN
            [[8,0],[8,1],[8,2],[8,3],[8,4],[8,5]], # TWELVE'
            [[4,0],[4,1],[4,2]], #ONE
        ]
        if minute > 33:
            return hours[hour]
        else:
            return hours[hour - 1]

    def translate_time(self, hour, minute, am_or_pm):
        letters = [
            [0,0], [0,1], [0,3], [0,4] # IT IS
        ]

        letters.extend(self.translate_hour(hour, minute))
        letters.extend(self.translate_to_or_past(minute))
        letters.extend(self.translate_minute(minute))

        # if (am_or_pm == 'PM'):
        #     letters.extend([[3,11],[3,12]]) # PM
        # else:
        #     letters.extend([[3,8],[3,9]]) # AM

        if (0 <= minute < 1) or (5 < minute <= 60):
            letters.extend([[8,7],[8,8],[8,9],[8,10],[8,11],[8,12]]) # OCLOCK

        return letters

if __name__ == "__main__":
    sentence_clock = SentenceClock()
    sentence_clock.mainloop()