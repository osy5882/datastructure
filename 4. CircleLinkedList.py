class Node:
    def __init__(self, item=None):
        self.item = item
        self.link = None


class CircleLinkedList:
    def __init__(self):
        self.root = Node()
        self.tail = self.root  # tail을 정의해 관리하는 이유는 루트가 삭제될 경우 tail.link를 갱신하기 위함.
        self.current = self.root

    def append(self, item):
        NewNode = Node(item)
        if self.root == None:
            self.root = NewNode
            self.tail = NewNode
            NewNode.link = self.root
        else:
            self.tail.link = NewNode
            self.tail = NewNode
            NewNode.link = self.root

    def setCurrent(self, item):
        CurNode = self.root
        while True:
            if CurNode.item != item:
                CurNode = CurNode.link
            else:
                self.current = CurNode
            if CurNode.link == self.root:
                print('찾는 item이 없습니다.')
                break

    def moveNext(self):
        self.current = self.current.link

    def insert(self, item):
        NewNode = Node(item)
        tmp = self.current.link
        self.current.link = NewNode
        NewNode.link = tmp
        # 여기서 self.current가 self.tail이었다면, insert한 NewNode를 tail로 지정해줘야함.
        if tmp == self.root:
            self.tail = NewNode
        # 여기서 NewNode를 self.current로 해줄 필요는 없나,,?

    # def delete(self, item):
    #     CurNode = PreNode = self.root
    #     if CurNode.item == item:
    #         #여기서 맨 앞에 건 짚고 넘어감.
    #         #아니었으면 그 다음부터 진행
    #     else:
    #         while CurNode.item != item:
    #             PreNode = CurNode
    #             CurNode = CurNode.link
    #             if CurNode == self.tail:
    #                 break
    #         #여기로 나온 거면 끝까지 갔거나/CurNode.item 이 item 인 노드를 찾은 것
    #         PreNode.link = CurNode.link


    def listSize(self):
        CurNode = self.root
        size = 1
        while CurNode.link != self.root:
            CurNode = CurNode.link
            size += 1
        return size

    def print(self):
        CurNode = self.root
        while CurNode.link != self.root:
            CurNode = CurNode.link
            print(CurNode.item, end=', ')

sports = CircleLinkedList()
sports.append('축구')
sports.append('농구')
sports.print()

print(sports.listSize())
