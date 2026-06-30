class textEditor:
    def __init__(self):
        self.l = []
    def type(self, ch):
        for i in ch:
            self.l.append(i)
    def undo(self):
        self.l.pop()
        t.disp()
    def disp(self):
        for i in self.l:
            print(i, end="")

t = textEditor()
while True:
    ch = input()
    if ch=="exit":
        break
    elif ch=="undo":
        t.undo()
    elif ch=="disp":
        t.disp()
    else:
        t.type(ch)