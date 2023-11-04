from TTFTree import TTFTree

tree = TTFTree()

# [33, 6, 42, 18, 31, 10, 90, 27, 0, 51, 67, 39, 58, 94, 70, 69, 28, 93, 12, 43, 88, 5, 15, 71, 97]; [6, 0, 88, 39, 42, 94, 51, 5, 43, 18, 90]
numbers_insert = [33, 6, 42, 18, 31, 10, 90, 27, 0, 51, 67, 39, 58, 94, 70, 69, 28, 93, 12, 43, 88, 5, 15, 71, 97]
numbers_remove = [6, 0, 88, 39, 42, 94, 51, 5, 43, 18, 90]

for x in numbers_insert:
    tree.insertTree(x)
    print("Percurso em pre-ordem")
    tree.tree_preorder()
    print("Percurso em nivel")
    tree.tree_levelorder()

for y in numbers_remove:
    tree.removeTree(y)
    print("Percurso em pre-ordem")
    tree.tree_preorder()
    print("Percurso em nivel")
    tree.tree_levelorder()

print("\nArvore 234 final")
tree.tree_visualize()

