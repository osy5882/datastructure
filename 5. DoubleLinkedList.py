class DNode:
    def __init__(self, item=None):
        self.item = item
        self.right = None
        self.left = None


class DoubleLinkedList():
    def __init__(self):
        self.root = None

    def append(self, item):
        NewNode = DNode(item)
        CurNode = self.root
        if self.root == None:
            self.root = NewNode
        else:
            while CurNode.right != None:
                CurNode = CurNode.right
            CurNode.right = NewNode
            NewNode.left = CurNode

    def listSize(self):
        CurNode = self.root
        if self.root != None:
            size = 1
            while CurNode.right != None:
                CurNode = CurNode.right
                size += 1
        else:
            size = 0
        return(size)


    def insert(self, item, idx):
        NewNode = DNode(item)
        CurNode = self.root
        if idx < 0 or idx > self.listSize():
            print('index가 리스트 사이즈 범위에서 벗어났습니다.')
            return(-1)
        elif idx == 0:
            _tmp1 = self.root
            self.root = NewNode
            NewNode.right = _tmp1
            CurNode.left = NewNode
        else:
            cur_idx = 0
            while cur_idx != idx-1:
                CurNode = CurNode.right
                cur_idx += 1
            NextNode = CurNode.right
            _tmp = CurNode.right
            CurNode.right = NewNode
            NewNode.left = CurNode
            NewNode.right = _tmp
            NextNode.left = NewNode

    def delete(self, item):
        CurNode = self.root
        if self.root == None:
            print('삭제할 item이 없습니다.')
        else:
            while CurNode.right != None:
                CurNode = CurNode.right
                if CurNode.item == item:
                    if CurNode.right == None:
                        CurNode.left.right = None
                    else:
                        CurNode.left.right = CurNode.right
                        CurNode.right.left = CurNode.left


    def print(self):
        CurNode = self.root
        if self.root == None:
            print("None")
        else:
            while CurNode.right != None:
                print(CurNode.item, end=', ')
                CurNode = CurNode.right
            print(CurNode.item)



sports = DoubleLinkedList()

sports.append('축구')
sports.append('야구')
sports.insert('농구', 1)
sports.insert('배드민턴', 1)
sports.print()
sports.delete('농구')
sports.print()
sports.delete('야구')
sports.print()






