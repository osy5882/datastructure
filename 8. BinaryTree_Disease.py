class BinaryTree:
    def __init__(self):
        self.t = [None]

    def append(self, item):
        self.t.append(item)

    def getChild(self, item):
        if item in self.t:
            idx = self.t.index(item)
            lidx = idx * 2
            ridx = idx * 2 + 1
            if lidx <= len(self.t)-1:
                lnode = self.t[lidx]
            else:
                lnode = None
            if ridx <= len(self.t)-1:
                rnode = self.t[ridx]
            else:
                rnode = None
        else:
            print("찾는 item이 없습니다.")
        return lnode, rnode

    def getParent(self, item):
        if item in self.t:
            idx = self.t.index(item)
            pidx = idx // 2
            if pidx > 0:
                pnode = self.t[pidx]
            else:
                pnode = None
        else:
            print("찾는 item이 없습니다")
        return pnode


    def TotalLevel(self, DiseaseTree):   # 거리를 표현하기 위해서는 먼저 전체 단계가 몇단계인지 알아아함.
        idx_maxnode = len(DiseaseTree.t) - 1
        k = 0
        while 2**k < idx_maxnode:
            k += 1
        return k-1

    def find_distance(self, a, b):   # 두 질병 사이의 거리는 '거슬러올라가야하는 단계 수/전체 단계 수' 로 나타난다.
        a_pnode, b_pnode = a, b
        n = 0
        while a_pnode != b_pnode:
            a_pnode = self.getParent(a_pnode)
            b_pnode = self.getParent(b_pnode)
            n += 1
        print("{}와 {} 사이의 거리는 {}/{}이다.".format(a, b, n, self.TotalLevel(DiseaseTree)))



Disease_list = ['호흡기/소화기병', '호흡기병', '소화기병','호흡기감염', '폐질환', '위질환', '결장질환',
                '독감', '기관지염', '폐부종', '폐색전증', '위궤양', '위암', '대장염', '대장암']

DiseaseTree = BinaryTree()
for i in Disease_list:
    DiseaseTree.append(i)

DiseaseTree.find_distance('독감', '대장암')
DiseaseTree.find_distance('대장염', '대장암')
DiseaseTree.find_distance('위암', '대장암')

