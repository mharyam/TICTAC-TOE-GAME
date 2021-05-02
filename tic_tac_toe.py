class XandO:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        # Player X always plays first
        self.current_state = [['*','*','*'],
                              ['*','X','*'],
                              ['*','*','*']]

        self.next_player = 'O'

    def draw_board(self):
        for m in range(0, 3):
            for n in range(0, 3):
                print('{}|'.format(self.current_state[m][n]), end=" ")
            print()
        print()


# Validate the move 
    def is_valid(self, x, y):
        if x < 0 or y > 2 or x < 0 or y > 2:
            return False
        elif self.current_state[x][y] != '*':
            return False
        else:
            return True

# Check for the winner of the game and also check if there is no availabe space to play the game
    def game_has_ended(self):

        #check for vertical win 
        for i in range(0, 3):
            if (self.current_state[0][i] != '*' and
                self.current_state[0][i] == self.current_state[1][i] and
                self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]

        # check for horizontal win
        for i in range(0, 3):
            if (self.current_state[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.current_state[i] == ['O', 'O', 'O']):
                return 'O'

        # check for first diagonal win 
        if (self.current_state[0][0] != '*' and
            self.current_state[0][0] == self.current_state[1][1] and
            self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]

        # check for second diagonal win 
        if (self.current_state[0][2] != '*' and
            self.current_state[0][2] == self.current_state[1][1] and
            self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]

        # check if the game has ended, if it has it retrun an empty result 
        for i in range(0, 3):
            for j in range(0, 3):
                # There's an empty field, we continue the game
                if (self.current_state[i][j] == '*'):
                    return None

        # this is the last check, if all the above conditions are not met, it is definitely a tie.
        return '*'

    # This is the Algortihm that checks for the best score point for X
    def max(self):

        # Possible values for maxv are:
        # -1 - loss
        # 0  - a tie
        # 1  - win

        # We're initially setting it to -2 as worse than the worst case:
        maxv = -2

        px = None
        py = None

        result = self.game_has_ended()

        if result == 'O':
            return (-1, 0, 0)
        elif result == 'X':
            return (1, 0, 0)
        elif result == '*':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '*':
                    self.current_state[i][j] = 'O'
                    (m, min_i, min_j) = self.min()
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    # Setting back the field to empty
                    self.current_state[i][j] = '*'
        return (maxv, px, py)

        # Player 'X' is min, in this case human
    def min(self):

        #set worst case for min value:
        minv = 2

        qx = None
        qy = None

        result = self.game_has_ended()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '*':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '*':
                    self.current_state[i][j] = 'X'
                    (m, max_i, max_j) = self.max()
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = '*'

        return (minv, qx, qy)

    def play(self):
        while True:
            self.draw_board()
            self.result = self.game_has_ended()

            if self.result != None:
                if self.result == 'X':
                    print('The winner is X!')
                elif self.result == 'O':
                    print('The winner is O!')
                elif self.result == '*':
                    print("It's a tie!")

                self.initialize_game()
                return

            # If it's player's turn
            if self.next_player == 'O':

                while True:
                    px = int(input('Insert the X coordinate: '))
                    py = int(input('Insert the Y coordinate: '))


                    if self.is_valid(px, py):
                        self.current_state[px][py] = 'O'
                        self.next_player = 'X'
                        break
                    else:
                        print('The move is not valid! Try again.')

           # X turn (the computer) 
            else:
                (m, px, py) = self.max()
                self.current_state[px][py] = 'X'
                self.next_player = 'O'


def main():
    g = XandO()
    g.play()

if __name__ == "__main__":
    main()