class Node:
  def __init__(self, data) -> None:
    self.data: int = data
    self.left: Node = None
    self.right: Node = None
  
def preorder(node: Node):
  if (node):
    print(node.data)
    preorder(node.left)
    preorder(node.right)

def inorder(node: Node):
   if (node):
    inorder(node.left)
    print(node.data)
    inorder(node.right)

def postorder(node: Node):
   if (node):
    postorder(node.left)
    postorder(node.right)
    print(node.data)
  
# MAIN
root = Node(10)

root.left = Node(34)
root.right = Node(89)
root.left.left = Node(45)
root.left.right = Node(50)

print("preorder")
preorder(root)
print("inorder")
inorder(root)
print("print")
postorder(root)



