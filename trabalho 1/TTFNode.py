class TTFNode():
    def __init__(self):
        self.keys = []
        self.children = []
        self.parent = None

    def getKeysNum(self):
        return len(self.keys)

    def getChildrenNum(self):
        return len(self.children)

    def isLeaf(self):
        return self.getChildrenNum() == 0

    # Busca (retorna o nó que possui a chave)
    def searchNode(self, key):
        if key in self.keys:
            return self
        elif self.isLeaf():
            return None
        else:
            if key < self.keys[0]:
                return self.children[0].searchNode(key)
            for idx, i in enumerate(self.keys):
                if key < i:
                    return self.children[idx].searchNode(key)
                elif idx == (self.getKeysNum() - 1):
                    return self.children[idx + 1].searchNode(key)

    # Inserção
    def insert(self, key):
        if self.isLeaf() and self.getKeysNum() < 3:
            self.keys.append(key)
            self.keys.sort()

        elif self.isLeaf() and self.getKeysNum() == 3:
            self.keys.append(key)
            self.keys.sort()
            self.split()

        else:
            if self.getChildrenNum() == 2:
                if key < self.keys[0]:
                    self.children[0].insert(key)
                else:
                    self.children[1].insert(key)

            elif self.getChildrenNum() == 3:
                if key < self.keys[0]:
                    self.children[0].insert(key)
                elif key > self.keys[0] and key < self.keys[1]:
                    self.children[1].insert(key)
                else:
                    self.children[2].insert(key)

            else:
                if key < self.keys[0]:
                    self.children[0].insert(key)
                elif key > self.keys[0] and key < self.keys[1]:
                    self.children[1].insert(key)
                elif key > self.keys[0] and key > self.keys[1] and key < self.keys[2]:
                    self.children[2].insert(key)
                else:
                    self.children[3].insert(key)


    def split(self):
        left_child = TTFNode()
        left_child.keys = [self.keys[0], self.keys[1]]
        right_child = TTFNode()
        right_child.keys = [self.keys[3]]
        self.keys = [self.keys[2]]

        if self.children:
            self.children[0].parent = left_child
            self.children[1].parent = left_child
            self.children[2].parent = left_child
            self.children[3].parent = right_child
            self.children[4].parent = right_child
            left_child.children = [self.children[0], self.children[1], self.children[2]]
            right_child.children = [self.children[3], self.children[4]]

        self.children = [left_child]
        self.children.append(right_child)

        if self.parent:
            if self in self.parent.children:
                self.parent.children.remove(self)
            self.parent.insertIntoNode(self)
        else:
            left_child.parent = self
            right_child.parent = self


    def insertIntoNode(self, node):
        self.keys.extend(node.keys)
        self.keys.sort()

        for child in node.children:
            child.parent = self
        self.children.extend(node.children)

        if self.getChildrenNum() > 1:
            if self.getChildrenNum() == 3:
                aux = self.children[0]
                if self.children[0].keys[0] > self.children[1].keys[-1]:
                    # 1 2 0
                    if self.children[0].keys[0] > self.children[2].keys[-1]:
                        self.children[0] = self.children[1]
                        self.children[1] = self.children[2]
                        self.children[2] = aux

                    # 1 0 2
                    else:
                        self.children[0] = self.children[1]
                        self.children[1] = aux

            elif self.getChildrenNum() == 4:
                aux0 = self.children[0]
                aux1 = self.children[1]
                aux2 = self.children[2]
                aux3 = self.children[3]

                # 2 3 0 1
                if self.children[0].keys[0] > self.children[3].keys[-1]:
                    self.children[0] = aux2
                    self.children[1] = aux3
                    self.children[2] = aux0
                    self.children[3] = aux1

                # 2 0 1 3
                elif self.children[1].keys[-1] < self.children[3].keys[0] and self.children[0].keys[0] > self.children[2].keys[-1]:
                    self.children[0] = aux2
                    self.children[1] = aux0
                    self.children[2] = aux1
                    self.children[3] = aux3

                # 2 0 3 1
                elif self.children[1].keys[0] > self.children[3].keys[-1] and self.children[0].keys[0] > self.children[2].keys[-1] and self.children[0].keys[-1] < self.children[3].keys[0]:
                    self.children[0] = aux2
                    self.children[1] = aux0
                    self.children[2] = aux3
                    self.children[3] = aux1

                # 0 2 3 1
                elif self.children[0].keys[-1] < self.children[2].keys[0] and self.children[3].keys[-1] < self.children[1].keys[0]:
                    self.children[0] = aux0
                    self.children[1] = aux2
                    self.children[2] = aux3
                    self.children[3] = aux1

                # 0 2 1 3
                elif self.children[0].keys[-1] < self.children[2].keys[0] and self.children[1].keys[0] > self.children[2].keys[-1] and self.children[1].keys[-1] < self.children[3].keys[0]:
                    self.children[0] = aux0
                    self.children[1] = aux2
                    self.children[2] = aux1
                    self.children[3] = aux3

            elif self.getChildrenNum() == 5:
                aux = self.children[0]
                aux1 = self.children[1]
                aux2 = self.children[2]
                aux3 = self.children[3]
                aux4 = self.children[4]

                # 0 1 3 4 2
                if self.children[1].keys[-1] < self.children[3].keys[0] and self.children[4].keys[-1] < self.children[2].keys[0]:
                    self.children[0] = aux
                    self.children[1] = aux1
                    self.children[2] = aux3
                    self.children[3] = aux4
                    self.children[4] = aux2

                # 0 3 4 1 2
                elif self.children[0].keys[-1] < self.children[3].keys[0] and self.children[4].keys[0] < self.children[1].keys[-1]:
                    self.children[0] = aux
                    self.children[1] = aux3
                    self.children[2] = aux4
                    self.children[3] = aux1
                    self.children[4] = aux2

                # 3 4 0 1 2
                elif self.children[0].keys[0] > self.children[4].keys[-1]:
                    self.children[0] = aux3
                    self.children[1] = aux4
                    self.children[2] = aux
                    self.children[3] = aux1
                    self.children[4] = aux2

                # 0 1 3 2 4
                elif self.children[1].keys[-1] < self.children[3].keys[0] and self.children[3].keys[-1] < self.children[2].keys[0] and self.children[2].keys[-1] < self.children[4].keys[0]:
                    self.children[0] = aux
                    self.children[1] = aux1
                    self.children[2] = aux3
                    self.children[3] = aux2
                    self.children[4] = aux4

                # 0 3 1 2 4
                elif self.children[0].keys[-1] < self.children[3].keys[0] and self.children[3].keys[-1] < self.children[1].keys[0] and self.children[1].keys[-1] < self.children[4].keys[0] and self.children[2].keys[-1] < self.children[4].keys[0]:
                    self.children[0] = aux
                    self.children[1] = aux3
                    self.children[2] = aux1
                    self.children[3] = aux2
                    self.children[4] = aux4

                # 3 0 1 2 4
                elif self.children[3].keys[-1] < self.children[0].keys[0] and self.children[2].keys[-1] < self.children[4].keys[0]:
                    self.children[0] = aux3
                    self.children[1] = aux
                    self.children[2] = aux1
                    self.children[3] = aux2
                    self.children[4] = aux4

                # 0 3 1 4 2
                elif self.children[0].keys[-1] < self.children[3].keys[0] and self.children[3].keys[-1] < self.children[1].keys[0] and self.children[1].keys[-1] < self.children[4].keys[0] and self.children[4].keys[-1] < self.children[2].keys[0]:
                    self.children[0] = aux
                    self.children[1] = aux3
                    self.children[2] = aux1
                    self.children[3] = aux4
                    self.children[4] = aux2

                # 3 0 1 4 2
                elif self.children[3].keys[-1] < self.children[0].keys[0] and self.children[1].keys[-1] < self.children[4].keys[0] and self.children[4].keys[-1] < self.children[2].keys[0]:
                    self.children[0] = aux3
                    self.children[1] = aux
                    self.children[2] = aux1
                    self.children[3] = aux4
                    self.children[4] = aux2

                # 3 0 4 1 2
                elif self.children[3].keys[-1] < self.children[0].keys[0] and self.children[0].keys[-1] < self.children[4].keys[0] and self.children[4].keys[-1] < self.children[1].keys[0]:
                    self.children[0] = aux3
                    self.children[1] = aux
                    self.children[2] = aux4
                    self.children[3] = aux1
                    self.children[4] = aux2

        if self.getChildrenNum() > 4:
            self.split()

    # Remoção
    def removeKey(self, keyIdx):
        self.keys.pop(keyIdx)

    def getLeafNode(self, idx):
        if self.isLeaf():
            return self

        tempNode = self.children[idx]
        while not tempNode.isLeaf():
            tempNode = tempNode.children[idx]
        return tempNode

    def adjacentBrother(self):
        parent = self.parent
        selfIdx = parent.children.index(self)

        if selfIdx == parent.getChildrenNum() - 1:
            return parent.children[selfIdx - 1]
        else:
            return parent.children[selfIdx + 1]

    # Visualização
    def preorder(self):
        print(self.keys)
        for child in self.children:
            child.preorder()
    
    def levelorder(self):
        this_level = [self]

        while this_level:
            next_level = []
            for nodes in this_level:
                print(str(nodes.keys), end = '\n')
                for child in nodes.children:
                    next_level.append(child)

            this_level = next_level