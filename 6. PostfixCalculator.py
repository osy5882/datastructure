class Stack():
    def __init__(self):
        self.s = []  # 빈 스텍 준비 -> 연산자들을 push해뒀다가 pop하기위한 용도(?)
        self.postEq = []  # 빈 리스트 준비 -> 후위연산을 위해 생성하는 리스트

    def isEmpty(self):
        if len(self.s) == 0:
            return True
        else:
            return False

    def push(self, item):
        return self.s.append(item)

    def pop(self):  # top에 있는 원소를 스택에서 삭제하고 반환하는 메소드
        if self.isEmpty() == False:
            return self.s.pop(-1)
        else:
            return None

    def delete(self):  # top에 있는 원소를 스택에서 삭제하는 메소드
        if self.isEmpty() == False:
            return self.s.pop()
        else:
            return None

    def peek(self):  # 삭제x 그냥 원소가 무엇인지 확인하기 위한 메소드
        if self.isEmpty() == False:
            return self.s[-1]
        else:
            return None

    def size(self):
        return len(self.s)


class PostfixAlgorithm(Stack):  # subclass라고하나,,? 이렇게 사용하는 거 맞나,,?

    def isOper(self, item):
        if item == '+' or item == '-' or item == '*' or item == '/':
            return True
        else:
            return False

    def isNum(self, item):
        try:
            float(str(item))
            return True
        except ValueError:
            return False

    def PostfixCalc(self, eqList):
        for item in eqList:
            if item == '(':
                self.push(item)  # stack에 push
            elif item == ')':
                # ')' 얘가 나오면 그 전에 무조건 '('가 나왔다는 뜻. '(' 얘 이후의 모든 연산자를 stack에서 eqList로 옮기기 위함.
                while True:
                    _tmp = self.pop()
                    if _tmp != '(':
                        self.postEq.append(_tmp)
                    else:
                        break
            elif item == '+' or item == '-':
                while self.isOper(self.peek()) == True:
                    # +,- 보다 *,/ 가 먼저 연산되므로 stack 안에 *,/ 가 있으면 먼저 postEq에 넣어야함.
                    # 그래서 *,/ 연산 때랑 함수가 다름.
                    self.postEq.append(self.pop())
                self.push(item)  # 있던 *,/ 모두 먼저 빼내고 자기를 push
            elif item == '*' or item == '/':
                while self.peek() == '*' or self.peek() == '/':
                    # *,/ 는 앞에서부터 연산되므로 먼저 stack안에 있던 *,/를 먼저 postEq에 넣어줘야함.
                    self.postEq.append(self.pop())
                self.push(item)
            elif self.isNum(item) == True:
                self.postEq.append(item)  # 숫자면 바로 postEq에 넣음.

        while self.isEmpty() != True:
            self.postEq.append(self.pop())
            # 수식 끝나면 stack에 남아있는 모든 것들 postEq에 추가.

        # 이제 다시 stack(self.s)은 빈 상태(다음 단계에서 사용 가능)

        for item in self.postEq:
            if self.isOper(item) == False:
                self.push(item)  # 숫자이면 stack에 넣음(stack에 들어가있는 숫자가 연산자 만나면 연산 될 것임.)
            else:
                num2 = float(self.pop())  # 상대적으로 최근에 들어간 수
                num1 = float(self.pop())  # 먼저 들어간 수 => -,/ 연산할때는 순서 중요하니까
                if item == '+':
                    self.push(str(num1 + num2))
                elif item == '-':
                    self.push(str(num1 - num2))
                elif item == '*':
                    self.push(str(num1 * num2))
                elif item == '/':
                    self.push(str(num1 / num2))
        result = self.pop()  # stack에 마지막을 남은 수가 결과값이 됨. 이를 pop해서 result에 저장하고 return 값으로 받자.
        return result


eq = "( 12.3 + 6 ) * 3 / 6"
A = PostfixAlgorithm()

print('연산하고자 하는 식: ', eq)
eqList = eq.split(" ")
print(eqList)
print('연산 결과: ', A.PostfixCalc(eqList))
