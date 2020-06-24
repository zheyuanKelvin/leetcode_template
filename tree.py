##go through tree

#Recursive Approach
'''
change the order of left, right, append when you need different traversal order
'''
def recursive_inorder_Traversal(self, root: TreeNode) -> List[int]:
    res = []
    def helper(root):
        if root.left: helper(root.left)
        res.append(root.val)
        if root.right: helper(root.right)
    if root: helper(root)
    return res

#Stack Approach
def stack_preorder_Traversal(self, root: TreeNode) -> List[int]:
    if root is None:
        return []
        
    stack, res = [root, ], []
    while stack:
        root = stack.pop()
        if root is not None:
            res.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)        
    return res

def stack_inorder_Traversal(self, root: TreeNode) -> List[int]:
    res, stack = [], []
    if root is None: return []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)           
        curr = curr.right
    return res
   
def stack_postorder_Traversal(self, root: TreeNode) -> List[int]:
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            if type(node) is int:
                result.append(node)
            else:
                stack.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
    return result


## BFS

# stack
def stack_levelOrder(self, root: TreeNode) -> List[List[int]]:
    result = []
    if not root:
        return result

    level = 0
    queue = deque([root])
    print(queue)

    while queue:
        result.append([])
        l = len(queue)

        for i in range(len(queue)):
            node = queue.popleft()
            # fulfill the current level
            result[level].append(node.val)

            # add child nodes of the current level
            # in the queue for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1

    return result

# recursive
def recursive_levelOrder(self, root: TreeNode) -> List[List[int]]:
    result = []
    if not root:
        return result

    def helper(node, level):
        if len(result) < level+1:
            result.append([])
        result[level].append(node.val)
        if node.left: helper(node.left, level+1)
        if node.right: helper(node.right, level+1)

    helper(root,0)
    return result

##DFS
#recursive
def recursive_DFS(self, root: TreeNode):
    if not root: return False
    #opeartions
    if (root.left or root.right) == None: #reach leaves
        #return something or do nothing
    #go to left subtree or right subtree
    return self.recursive_DFS(root.left) or self.recursive_DFS(root.right)

#stack
def stack_DFS(self, root: TreeNode):
    if not root:
        return False
    de = [root, ] #(root, #something needed) instead of root
    while de:
        node = de.pop()
        if not node.left and not node.right:  #reach leaves
            # retrue something
        if node.right:
            de.append(node.right) #append right subtree
        if node.left:
            de.append(node.left) #append left subtree
    
