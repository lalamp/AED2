from TTFNode import TTFNode
class TTFTree():
    def __init__(self):
        self.root = TTFNode()

    # Inserção
    def insertTree(self, key):
        print("\nInserindo: " + str(key))
        self.root.insert(key)

    # Remoção
    def removeTree(self, key):
        print("\n\nRemovendo: " + str(key))
        keyNode = self.root.searchNode(key)

        if keyNode == None:
            print("A chave " + str(key) + " não está na árvore")
            return

        keyIdx = keyNode.keys.index(key)

        # Casos com nós intermediários - busca o maior dos menores ou o menor dos maiores para trocar com a chave a ser removida
        if not keyNode.isLeaf():
            '''
                lowHighNode => pega o menor do maiores
                highLowNode => pega o maior do menores
            '''
            lowHighNode = keyNode.children[keyIdx+1].getLeafNode(0)
            if lowHighNode.getKeysNum() == 1:
                highLowNode = keyNode.children[keyIdx].getLeafNode(-1)
                if highLowNode.getKeysNum() == 1:
                    # Caso 2 - o maior dos menores e o menor dos maiores está sozinho no nó folha
                    if keyNode == self.root:
                        if keyNode == highLowNode.parent:
                            highLowNode.keys.append(lowHighNode.keys[0])
                            keyNode.children.remove(lowHighNode)
                            if keyNode.getKeysNum() == 1:
                                keyNode = highLowNode
                                self.root = keyNode
                                del highLowNode
                            else:
                                keyNode.removeKey(keyIdx)
                            print("Caso 2 1")
                        else:
                            keyNode.keys[keyIdx] = highLowNode.keys[0]
                            highLowNode.keys[0] = highLowNode.parent.keys[-1]
                            highLowNode.parent.removeKey(-1)
                            highLowNode.parent.children[-2].keys.append(highLowNode.keys[0])
                            highLowNode.parent.children.remove(highLowNode)
                            del highLowNode
                            print("Caso 2 2")

                    else:
                        parent = keyNode.parent
                        adjacentBrother = keyNode.adjacentBrother()
                        keyNodeIdx = parent.children.index(keyNode)

                        if keyNodeIdx == (parent.getChildrenNum() - 1):
                            if adjacentBrother.getKeysNum() != 1:
                                keyNode.keys[keyIdx] = parent.keys[keyIdx-1]
                                keyNode.keys.sort()
                                parent.keys[keyIdx-1] = adjacentBrother.keys[-1]
                                adjacentBrother.removeKey(-1)

                                if highLowNode.parent.getChildrenNum() == 2:
                                    highLowNode.parent.children[1].keys.append(highLowNode.keys[0])
                                    highLowNode.parent.children[1].keys.sort()
                                    highLowNode.keys = adjacentBrother.children[-1].keys
                                    adjacentBrother.children.remove(adjacentBrother.children[-1])

                                if highLowNode.parent.getChildrenNum() == 3:
                                    highLowNode.parent.children[2].keys.insert(0, highLowNode.parent.children[1].keys[0])
                                    highLowNode.parent.children[1] = highLowNode
                                    highLowNode = adjacentBrother.children[-1]
                                    adjacentBrother.children.remove(adjacentBrother.children[-1])

                                if highLowNode.parent.getChildrenNum() == 4:
                                    for key in highLowNode.parent.children[2]:
                                        highLowNode.parent.children[3].keys.append(key)
                                    highLowNode.parent.children[3].keys.sort()
                                    if highLowNode.parent.children[3].getChildrenNum() > 4:
                                        highLowNode.parent.children[3].split()

                                    highLowNode.parent.children[2] = highLowNode.parent.children[1]
                                    highLowNode.parent.children[1] = highLowNode
                                    highLowNode = adjacentBrother.children[-1]
                                    adjacentBrother.children.remove(adjacentBrother.children[-1])
                                print("Caso 2 3")

                            else:
                                keyNode.keys[keyIdx] = parent.keys[keyIdx-1]
                                keyNode.keys.append(adjacentBrother.keys[0])
                                keyNode.keys.sort()
                                keyNode.children.insert(0, adjacentBrother.children[0])
                                adjacentBrother.children[0].parent = keyNode
                                keyNode.children.insert(1, adjacentBrother.children[1])
                                adjacentBrother.children[1].parent = keyNode
                                keyNode.children[2].keys.append(keyNode.children[3].keys[0])
                                keyNode.children.remove(keyNode.children[3])

                                if keyNode.parent == self.root:
                                    self.root = keyNode
                                else:
                                    parent.children.remove(adjacentBrother)
                                print("Caso 2 4")

                        else: #keyNodeIdx != (parent.getChildrenNum() - 1)
                            if adjacentBrother.getKeysNum() == 1:
                                keyNode.keys[keyIdx] = parent.keys[keyIdx]
                                keyNode.keys.append(adjacentBrother.keys[0])
                                keyNode.keys.sort()
                                keyNode.children[0].keys.append(keyNode.children[1].keys[0])
                                keyNode.children[0].keys.sort()
                                keyNode.children.remove(keyNode.children[1])
                                keyNode.children.append(adjacentBrother.children[0])
                                keyNode.children.append(adjacentBrother.children[1])
                                adjacentBrother.children[0].parent = keyNode
                                adjacentBrother.children[1].parent = keyNode

                                if keyNode.parent == self.root:
                                    self.root = keyNode
                                else:
                                    parent.children.remove(adjacentBrother)
                                print("Caso 2 5")
                else:
                    # Caso 1 - buscando o maior dos menores
                    keyNode.keys[keyIdx] = highLowNode.keys[-1]
                    keyNode.keys.sort()
                    highLowNode.removeKey(-1)
                    print("Caso 1")
            else:
                # Caso 1 - buscando o menor dos maiores
                keyNode.keys[keyIdx] = lowHighNode.keys[0]
                keyNode.keys.sort()
                lowHighNode.removeKey(0)
                print("Caso 1")

        # Casos com nós folhas
        else:
            # Caso 3 - nó folha (raiz ou não) com mais de uma chave
            if keyNode.getKeysNum() != 1:
                keyNode.removeKey(keyIdx)
                print("Caso 3")

            # Casos com nós folhas com apenas uma chave
            else:
                # Caso 4 - nó raiz
                if keyNode == self.root:
                    keyNode.removeKey(0)
                    del self
                    print("Caso 4")
                    return

                # Casos 5, 6 e 7
                parent = keyNode.parent
                keyNodeIdx = parent.children.index(keyNode)
                adjacentBrother = keyNode.adjacentBrother()

                # Caso 5 - nó folha com apenas uma chave e irmão adjacente tem mais de uma chave
                if adjacentBrother.getKeysNum() > 1:
                    if keyNodeIdx == (parent.getChildrenNum() - 1):
                        keyNode.keys[0] = parent.keys[keyNodeIdx - 1]
                        parent.keys[keyNodeIdx - 1] = adjacentBrother.keys[-1]
                        adjacentBrother.removeKey(-1)
                    else:
                        keyNode.keys[0] = parent.keys[keyNodeIdx]
                        parent.keys[keyNodeIdx] = adjacentBrother.keys[0]
                        adjacentBrother.removeKey(0)

                    parent.keys.sort()
                    print("Caso 5")

                # Caso 6 - nó folha com apenas uma chave, pai e irmão com apenas uma chave ou o irmão não existe
                elif parent.getKeysNum() == 1 and adjacentBrother.getKeysNum() == 1:
                    if parent == self.root:
                        keyNode.keys = [parent.keys[0]]
                        keyNode.keys.append(adjacentBrother.keys[0])
                        keyNode.keys.sort()
                        self.root = keyNode

                        del adjacentBrother
                        del parent
                        print("Caso 6")

                    else:
                        uncle = parent.adjacentBrother()
                        grandparent = parent.parent
                        parentIdx = grandparent.children.index(parent)

                        keyNode.keys = [parent.keys[0]]
                        keyNode.keys.append(adjacentBrother.keys[0])
                        keyNode.keys.sort()

                        if grandparent.getKeysNum() == 1:
                            parent.keys[0] = grandparent.keys[0]

                            uncle.keys.append(parent.keys[0])
                            if parentIdx == (grandparent.getChildrenNum() - 1):
                                uncle.children.append(keyNode)
                            else:
                                uncle.children.insert(0, keyNode)
                            uncle.keys.sort()
                            keyNode.parent = uncle
                            self.root = uncle

                            del adjacentBrother
                            del parent
                            del grandparent

                        else:
                            if parentIdx == (grandparent.getChildrenNum() - 1):
                                parent.keys[0] = grandparent.keys[parentIdx - 1]
                                grandparent.keys.removeKey(parentIdx-1)
                            else:
                                parent.keys[0] = grandparent.keys[parentIdx]
                                grandparent.keys.removeKey(parentIdx)

                            uncle.keys.append(parent.keys[0])
                            if parentIdx == (grandparent.getChildrenNum() - 1):
                                uncle.children.append(keyNode)
                            else:
                                uncle.children.insert(0, keyNode)
                            uncle.keys.sort()
                            keyNode.parent = uncle

                            grandparent.children.remove(parent)
                            del parent

                        print("Caso 6")

                # Caso 7 - nó pai tem mais de uma chave e o irmão adjacente tem apenas uma chave
                elif parent.getKeysNum() != 1 and adjacentBrother.getKeysNum() == 1:
                    if keyNodeIdx == (parent.getChildrenNum() - 1):
                        adjacentBrother.keys.append(parent.keys[keyNodeIdx-1])
                        adjacentBrother.keys.sort()
                        parent.removeKey(keyNodeIdx-1)
                    else:
                        adjacentBrother.keys.append(parent.keys[keyNodeIdx])
                        adjacentBrother.keys.sort()
                        parent.removeKey(keyNodeIdx)

                    parent.children.pop(keyNodeIdx)
                    print("Caso 7")

    # Visualização
    def tree_preorder(self):
        self.root.preorder()

    def tree_levelorder(self):
        self.root.levelorder()

    def tree_visualize(self):
        this_level = [self.root]

        while this_level:
            next_level = []
            for nodes in this_level:
                print(str(nodes.keys), end = ' ')
                for child in nodes.children:
                    next_level.append(child)

            this_level = next_level
            print("\n")