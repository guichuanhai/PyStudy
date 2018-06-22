#-*-coding:utf-8-*-
class Game:
    def __init__(self):
        self.map = [[" ", " ", "O"], [" ", "O", " "], ["O", " ", "O"]];
        self.step = 0;
        self.finish=False;

    def draw(self):
        print(self.map[0]);
        print(self.map[1]);
        print(self.map[2]);

    def isWin(self,row,col):
        flag = self.map[row][col];
        total=0
        #纵
        if total<3:
            for i in range(min(0,row),max(2,row)+1):
                if self.map[i][col]==flag:
                    total +=1;
                else:
                    total=0;
            print(total);
        #横
        if total<3:
            for i in range(min(0,col),max(2,col)+1):
                if self.map[row][i]==flag:
                    total +=1;
                else:
                    total=0;
            print(total);
        if total<3:
            for i in range(min(0,col),max(2,col)+1):
                if self.map[row+col+i][i]==flag:
                    total +=1;
                else:
                    total=0;
            print(total);

        if total==3:
            print("win");
            self.finish=True;



    def play(self,row,col):
        if self.finish:
            return;
        self.step += 1;

        if(self.map[row][col]!=" "):
            print("error")
            return;

        if(self.step%2==0):
            flag = "X";
        else:
            flag = "O";
        self.map[row][col]=flag;
        self.isWin(row,col)

game = Game();
game.play(0,0)
# ga.play(1,1)
# ga.play(1,2)
# ga.play(1,0)
# ga.play(0,1)
# ga.play(2,0)
## ga.play(0,2)

game.draw();



