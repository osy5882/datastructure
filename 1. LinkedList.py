class Node:
  def __init__(self, item = None, link = None):
    self.item = item
    self.link = link

# root
class LinkedList:
  def __init__(self):
    self.root = None

# append method
  def append(self, item):
    NewNode = Node(item)
    CurNode = self.root
    if self.root == None:          # 'NoneType' object has no attribute 'item' 오류 안뜨게 하기 위해 None일 때와 아닐 때를 구분,, -> 안하는 방법,,
      self.root = NewNode
    else:
      while True:
        if CurNode.link == None:
          CurNode.link = NewNode
          break
        else:
          while True:
            CurNode = CurNode.link
            if CurNode.link == None:
              CurNode.link = NewNode
              break
          break

# print method
  def print(self):
    CurNode = self.root
    if CurNode == None:
      print('NONE')
    else:
      print(CurNode.item, end=', ')
      while True:
        CurNode = CurNode.link
        print(CurNode.item, end=', ')          # 맨 마지막에 ',' 안들어가게 하는 방법,,?
        if CurNode.link == None:
          break

# insert method
  def insert(self, idx, item):
    NewNode = Node(item)
    CurNode = self.root
    if idx == 0:
      tmp = self.root
      self.root = NewNode
      NewNode.link = tmp
    else:
      for i in range(idx-1):
        CurNode = CurNode.link
      tmp = CurNode.link
      CurNode.link = NewNode
      NewNode.link = tmp

# find method
  def find(self, item):
    CurNode = self.root
    if self.root == None:
      print("찾고자 하는 item이 없습니다.")
    else:
      idx = 1
      while True:
        if CurNode.item == item:
          print(idx)
          break
        elif CurNode.link == None:
          print("찾고자 하는 item이 없습니다.")
          break
        else:
          idx += 1
          CurNode = CurNode.link


# delete method
  def delete(self, item):
    CurNode = self.root
    PreNode = self.root
    if self.root == None:
      print('delete할 item이 없습니다')
    else:
      if CurNode.item == item:
        self.root = CurNode.link
      else:
        CurNode = CurNode.link
        while True:
          if CurNode.item == item:
            PreNode.link = CurNode.link
            break
          else:
            CurNode = CurNode.link
            PreNode = PreNode.link
            if PreNode.link == None:
              break

# listSize method
  def list_size(self):
    CurNode = self.root
    if self.root == None:
      print(0)
    else:
      n = 1
      while True:
        if CurNode.link != None:
          CurNode = CurNode.link
          n += 1
        else:
          break
      print(n)

# 실행 되는지 확인.
sports = LinkedList()
sports.append('축구')
sports.append('농구')
sports.append('야구')
sports.append('풋살')
sports.print()
sports.insert(3, '배드민턴')
sports.print()
sports.find('농구/')
sports.find('배드민턴')
sports.find('풋살')
sports.delete('야구')
sports.print()
sports.list_size()