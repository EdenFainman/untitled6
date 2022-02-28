"""
Eden Fainman ID 206796351
"""


class Tree(object):

    def __init__(self, val, children=[]):   #Tree[<12>][<8>[<3>,<4>];,<7>;,<10>;]

        self.val = val
        self.children = children


    def __str__(self):
        for child in self.children:
            length = 0

            if child is None:
                return ('<'+self.val+'>')

            else:
                for c in self.children:
                    length=length+1
                    result=str('<'+str(self.val)+'>[')
                for i in range (0,length):
                    ch=str(self.children[i])
                    result = result + str('<' +ch + '>;')
                result=str(result)+str(']')
                return(f'{result}')

    def __repr__(self):
        for child in self.children:
            length = 0
            if child is None:
                return ('<' + self.val + '>')
            else:
                for c in self.children:
                    length = length + 1


                result = str('<' + str(self.val) + '>[')
                for i in range(0, length):
                    result = result + str('<' + str(self.children[i]) + '>;')
                result = result + str(']')
                return f'Tree({result})'



    def setVal(self, val):
        self.val = val

    def getVal(self):
        return self.val


    def insert(self, val):
            # Compare the new value with the parent node
        if val < self.val:
            if self.children[0] is None:
                self.children[0] = Tree(self,int(val),[])
            else:
                self.children.insert(0,val)

        elif val > self.val:
            if self.children[1] is None:
                self.children[1] = Tree(self,val,[])
            else:
                self.children.append(val)

        else:
            self.children.append(val)

    def deleteValue(self,value):
        try:
            if value==self.val:
                self.children.remove(value)
            else:
                if value in self.children:
                    index=self.children.index(value)
                    self.children.remove(value)
                else:
                    print("the value isnt exist")

        except Exception:
            print("unexpected error please try again")






class BinaryTree(Tree):
    def __init__(self, val, left=None, right=None):
        super().__init__(val, [left, right])
        self.val = val;
        self.children = [left, right];

    def setLeft(self, left):
        if left is None:
            return
        if (len(self.children) == 2):
            self.children = [left, self.children[1]]
        else:
            self.children = [left]

    def setRight(self, right):
        if right is None:
            return;
        if (len(self.children) >= 1):
            self.children = [self.children[0], right]
        else:
            self.children = [None, right]

    def getLeft(self):
        if self.children is None or len(self.children) < 1:
            return None;
        return self.children[0]

    def getRight(self):
        if self.children is None or len(self.children) < 2:
            return None;
        return self.children[1]


if __name__ == "__main__":

    while (True):
        choise = input(
            "please enter your choise from 1-4\nfor create a tree type 1\n for insert value to tree type 2\n for delete value from tree type 3\n for print tree type 4\n to exit type 5")
        if (choise == '1'):
            root = input("enter tree values enter root")
            children=[]
            while True:

                temp= input("enter child to end type -1")
                if temp==str(-1):
                    break
                children.append(temp)

            t=Tree(root,children)

        elif (choise == '2'):
            try:
                value = input("enter value")
                t.insert(value)
            except UnboundLocalError:
                print("there is not tree existes")
        elif (choise == '3'):
            try:
                value = input("enter value")
                t.deleteValue(value)
            except UnboundLocalError:
                print("the value isnt existes")

        elif (choise == '4'):
            try:
                t.__str__()
            except UnboundLocalError:
                print("there is not tree existes")


        elif (choise == '5'):
            print("thank you,Bye")
            quit()


