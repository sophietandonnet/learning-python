class Tictactoe:
    def __init__(self):
        self.ttt = '012345678'
        self.line = ''
    
    def add_X(self, position):
        i = 0
        while i < 9:
            if self.ttt[i] == position and self.ttt[i]:
                self.ttt = self.ttt[:i] + 'X' + self.ttt[i+1:]
                
            i += 1
                
    def add_O(self, position):
        i = 0
        while i < 9:
            if self.ttt[i] == position and self.ttt[i]:
                self.ttt = self.ttt[:i] + 'O' + self.ttt[i+1:]
                
            i += 1
         
    def draw_ttt_no_numbers(self):
        print('+-+-+-+')
        i = 0
        j = 3
        while j <= 9:
            self.line = '|'
            while i < j:
                if self.ttt[i] in ['0','1','2','3','4','5','6','7','8']:
                    self.line += ' |'
                    
                if self.ttt[i] == 'O':
                    self.line += 'O|'
                    
                if self.ttt[i] == 'X':
                    self.line += 'X|'

                i += 1
                
            print(self.line)
            print('+-+-+-+')
            
            j += 3
           
    def draw_ttt(self):
        print('+-+-+-+')
        for i in range(0,9,3):
            print('|' + self.ttt[i] + '|' + self.ttt[i+1] + '|' + self.ttt[i+2] + '|')
            print('+-+-+-+')


    def check_lines(self):
        for i in range(0,9,3):
            if self.ttt[i] == self.ttt[i+1] == self.ttt[i+2]:
                return self.ttt[i] + ' won'
        return 'nobody won'               
    
    
    def check_columns(self):
        i = 0
        while i < 3:
            if self.ttt[i] == self.ttt[i+3] == self.ttt[i+6]:
                return self.ttt[i] + ' won'
                
            i += 1
        return 'nobody won'
        
    def check_dia(self):
        if self.ttt[0] == self.ttt[4] == self.ttt[8]:
            return self.ttt[0] + ' won'
        if self.ttt[2] == self.ttt[4] == self.ttt[6]:
            return self.ttt[0] + ' won'
        return 'nobody won'

    def result_ttt(self):
        l = self.check_lines()
        c = self.check_columns()
        d = self.check_dia()
        
        if l == c == d == 'nobody won':
            for i in range(0,8):
                if self.ttt[i] in ['0','1','2','3','4','5','6','7','8']:
                    return 'Game not finished'
            return 'O and X tie'
                    
        if l == 'O won' or l == 'X won':
            return l
            
        if c == 'O won' or c == 'X won':
            return c
            
        if d == 'O won' or d == 'X won':
            return d
            

my_ttt = Tictactoe()
#my_ttt.draw_ttt()
my_ttt.draw_ttt_no_numbers()

my_ttt.add_X('1')
my_ttt.add_X('3')
my_ttt.add_X('4')
my_ttt.add_X('6')
my_ttt.add_X('8')

my_ttt.add_O('0')
my_ttt.add_O('2')
my_ttt.add_O('5')
my_ttt.add_O('7')
my_ttt.add_X('7')

my_ttt.draw_ttt()
my_ttt.draw_ttt_no_numbers()

my_tt2 = Tictactoe()
my_tt2.add_O('0')
my_tt2.add_O('3')
my_tt2.add_O('6')
my_tt2.draw_ttt_no_numbers()
print(my_tt2.result_ttt())

#print(my_ttt.check_lines())
#print(my_ttt.check_columns())
#print(my_ttt.check_dia())
#print(my_ttt.result_ttt())
