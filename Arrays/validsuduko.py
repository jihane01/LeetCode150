#The code iterates through the list of lists, and for each row in the board, it iterates through all possible combinations of cells.
 #For each combination, it creates a new list with three elements: (i, x), (x, j), and (i // 3, j // 3).
 #The code then checks to see if there are any duplicates in this list.
 #If so, it adds them together into a single element that is an array containing two integers separated by a comma.
 #The code returns len(res) == len(set(res)) which means that the length of res equals the number of elements in set(res).
 #The code will return the length of the list in res.
 #The code above attempts to check if a Sudoku board has an invalid entry, and it does so by checking if each row has an invalid entry.
 #if the result is true, then there was an error in the Sudoku board that needs to be fixed.


def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x != '.':
                    res += [(i, x), (x, j), (i // 3, j // 3, x)]
        return len(res) == len(set(res))