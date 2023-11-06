from TTFTree import TTFTree

tree = TTFTree()

'''
Exemplos:
    insert = [33, 6, 42, 18, 31, 10, 90, 27, 0, 51, 67, 39, 58, 94, 70, 69, 28, 93, 12, 43, 88, 5, 15, 71, 97]; remove = [6, 0, 88, 39, 42, 94, 51, 5, 43, 18, 90]
    insert = [33, 6, 42, 18, 31, 10, 90, 27, 0, 51, 67, 39, 58]; remove = [18, 67, 6, 10, 27, 0, 33, 39, 58, 90, 51, 31, 42]
    insert = [8, 26, 45, 30, 72, 16, 89, 55, 0, 1, 99, 34, 46, 20, 15]; remove = [45, 16, 8, 0, 34, 20]
'''
numbers_insert = [33, 6, 42, 18, 31, 10, 90, 27, 0, 51, 67, 39, 58]
numbers_remove = [18, 67, 6, 10, 27, 0, 33, 39, 58, 90, 51, 31, 42]

for x in numbers_insert:
    tree.insertTree(x)
    print("Percurso em pré-ordem")
    tree.tree_preorder()
    print("Percurso em nível")
    tree.tree_levelorder()

for y in numbers_remove:
    tree.removeTree(y)
    print("Percurso em pré-ordem")
    tree.tree_preorder()
    print("Percurso em nível")
    tree.tree_levelorder()

print("\nÁrvore 234 final")
tree.tree_visualize()