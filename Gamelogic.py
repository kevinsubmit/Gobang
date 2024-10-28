from .board import Board
class GameLogic:
    def __init__(self):
        self.board = Board()
        self.row = 0
        self.col = 0
        self.cpuRow = 0
        self.cpuCol = 0

    def showBoard(self):
        self.board.showBoard()

    def playerWin(self):
        count = 1
        for i in range(1, 5):  # 纵向向下计算
            if self.row + i < 9 and self.board.Black(self.row + i, self.col):
                count += 1
            else:
                break
        for i in range(-1, -5, -1):  # 纵向向上计算
            if self.row + i > 0 and self.board.Black(self.row + i, self.col):
                count += 1
            else:
                break
        if count >= 5:
            return True

        count = 1
        for i in range(1, 5):  # 横向向右计算
            if self.col + i < 9 and self.board.Black(self.row, self.col + i):
                count += 1
            else:
                break
        for i in range(-1, -5, -1):  # 横向向左计算
            if self.col + i > 0 and self.board.Black(self.row, self.col + i):
                count += 1
            else:
                break
        if count >= 5:
            return True

        count = 1
        for i in range(-1, -5, -1):  # 10点方向计算
            if self.row + i > 0 and self.col + i > 0 and self.board.Black(self.row + i,
                                                                          self.col + i):
                count += 1
            else:
                break
        for i in range(1, 5):  # 5点方向计算
            if self.row + i < 9 and self.col + i < 9 and self.board.Black(self.row + i,
                                                                          self.col + i):
                count += 1
            else:
                break
        if count >= 5:
            return True

        count = 1
        for i in range(1, 5):  # 2点方向计算
            if self.row + i > 0 and self.col + i < 9 and self.board.Black(self.row + i,
                                                                          self.col + i):
                count += 1
            else:
                break
        for i in range(-1, -5, -1):  # 7点方向计算
            if self.row + i < 9 and self.col + i > 0 and self.board.Black(self.row + i,
                                                                          self.col + i):
                count += 1
            else:
                break
        if count >= 5:
            return True
        return False

    def cpuWin(self):
        count = 1
        for i in range(1, 5):  # 横向向右计算
            if self.cpuRow + i < 9 and self.board.White(self.cpuRow + i, self.cpuCol):
                count += 1
            else:
                break
        for i in range(-1, -5, -1):  # 横向向左计算
            if self.cpuRow + i > 0 and self.board.White(self.cpuRow + i, self.cpuCol):
                count += 1
            else:
                break
        if count >= 5:
            return True

        count = 1
        for i in range(1, 5):  # 纵向向上计算
            if self.cpuCol + i < 9 and self.board.White(self.cpuRow, self.cpuCol + i):
                count += 1
            else:
                break
        for i in range(-1, -5, -1):  # 纵向向下计算
            if self.cpuCol + i > 0 and self.board.White(self.cpuRow, self.cpuCol + i):
                count += 1
            else:
                break
        if count >= 5:
            return True

        count = 1
        for i in range(-1, -5, -1):  # 7点方向计算
            if self.cpuRow + i > 0 and self.cpuCol + i > 0 and self.board.White(self.cpuRow + i, self.cpuCol + i):
                count += 1
            else:
                break
        for i in range(1, 5):  # 2点方向计算
            if self.cpuRow + i < 9 and self.cpuCol + i < 9 and self.board.White(self.cpuRow + i, self.cpuCol + i):
                count += 1
            else:
                break
        if count >= 5:
            return True

        count = 1
        for i in range(1, 5):  # 5点方向计算
            if self.cpuRow + i > 0 and self.cpuCol + i < 9 and self.board.White(self.cpuRow + i, self.cpuCol + i):
                count += 1
            else:
                break
        for i in range(-1, -5, -1):  # 10点方向计算
            if self.cpuRow + i < 9 and self.cpuCol + i > 0 and self.board.White(self.cpuRow + i, self.cpuCol + i):
                count += 1
            else:
                break
        if count >= 5:
            return True
        return False

    def playerRound(self):
        playerInPut = input('请落子以行列的方式，如28即在第2行，第8列落子')
        self.row = int(playerInPut[0])-1
        self.col = int(playerInPut[1])-1
        if 0 <= self.row < 9 and 0 <= self.col < 9:
            self.board.Move(self.row,self.col,True)
        else:
            print("输入的行列超出范围，请重新输入。")

    def cpuRound(self):
        Hlink1 = -1
        Hlink2 = 1
        linkCount = 1
        maxLinkCount = 1
        defendRow = 0
        defendCol = 0
        while self.col + Hlink1 > 0 and self.board.Black(self.row, self.col + Hlink1):
            linkCount += 1
            Hlink1 -= 1

        while self.col + Hlink2 < 9 and self.board.Black(self.row, self.col + Hlink2):
            linkCount += 1
            Hlink2 += 1

        if linkCount >= maxLinkCount:
            if self.board.Black(self.row, self.col + Hlink1):
                maxLinkCount = linkCount
                defendRow = self.row
                defendCol = self.col + Hlink1
            elif self.board.Black(self.row, self.col + Hlink2):
                maxLinkCount = linkCount
                defendRow = self.row
                defendCol = self.col + Hlink2

        # 纵向判断

        Vlink1 = -1
        Vlink2 = 1
        linkCount = 1
        while self.row + Vlink1 > 0 and self.board.Black(self.row + Vlink1, self.col):
            linkCount += 1
            Vlink1 -= 1

        while self.row + Vlink2 < 9 and self.board.Black(self.row + Vlink2, self.col):
            linkCount += 1
            Vlink2 += 1

        if linkCount >= maxLinkCount:
            if self.board.Black(self.row + Vlink1, self.col):
                maxLinkCount = linkCount
                defendRow = self.row + Vlink1
                defendCol = self.col
            elif self.board.Black(self.row + Vlink2, self.col):
                maxLinkCount = linkCount
                defendRow = self.row + Vlink2
                defendCol = self.col

        # 10点判断
        link10 = -1  # row
        link11 = -1  # col
        link4 = 1  # row
        link5 = 1  # col
        linkCount = 1
        while self.row + link10 > 0 and self.col + link11 > 0 and self.board.Black(self.row + link10,
                                                                                   self.col + link11):
            linkCount += 1
            link10 -= 1
            link11 -= 1
        while self.row + link4 < 9 and self.col + link5 < 9 and self.board.Black(self.row + link4,
                                                                                 self.col + link5):
            linkCount += 1
            link4 += 1
            link5 += 1
        if linkCount >= maxLinkCount:
            if self.board.Black(self.row + link10, self.col + link11):
                maxlinkCount = linkCount
                defendRow = self.row + link10
                defendCol = self.col + link11
            elif self.board.Black(self.row + link4, self.col + link5):
                maxLinkCount = linkCount
                defendRow = self.row + link4
                defendCol = self.col + link5

        link8 = 1  # row
        link7 = -1  # col
        link1 = -1  # row
        link2 = 1  # col
        linkCount = 1
        while self.row + link8 < 9 and self.col + link7 > 0 and self.board.Black(self.row + link8,
                                                                                 self.col + link7):
            linkCount += 1
            link8 += 1
            link7 -= 1
        while self.row + link1 > 0 and self.col + link2 < 9 and self.board.Black(self.row + link1,
                                                                                 self.col + link2):
            linkCount += 1
            link1 -= 1
            link2 += 1

        if linkCount >= maxLinkCount:
            if self.board.Black(self.row + link8, self.col + link7):
                maxlinkCount = linkCount
                defendRow = self.row + link8
                defendCol = self.col + link7
            elif self.board.Black(self.row + link1, self.col + link2):
                maxLinkCount = linkCount
                defendRow = self.row + link1
                defendCol = self.col + link2

        self.board.Move(defendRow, defendCol,False)

# gameloop():
# while True:
# Board.showboard()
# playerRound():
# if game.playerWin():
# print("好厉害，你赢了！")
# break
# cpuRound():
# if game.cpuWin():
# print("很遗憾，你输了！")
# break
