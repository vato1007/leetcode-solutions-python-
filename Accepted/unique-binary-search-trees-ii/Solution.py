class Solution:
    def generateTrees(self, n):
        def build(left, right):
            if left > right:
                return [None]

            trees = []

            for root in range(left, right + 1):
                left_trees = build(left, root - 1)
                right_trees = build(root + 1, right)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        node = TreeNode(root)
                        node.left = left_tree
                        node.right = right_tree
                        trees.append(node)

            return trees

        return build(1, n)