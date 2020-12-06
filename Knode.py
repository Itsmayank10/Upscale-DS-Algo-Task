class Node: 
    # A constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
      
def kDistanceNodeDown(root, k): 
      
    if root is None or k< 0 : 
        return 
      
    if k == 0 : 
        print(root.data)  
        return 
      
    kDistanceNodeDown(root.left, k-1) 
    kDistanceNodeDown(root.right, k-1) 
  
  
def kDistanceNode(root, target, k): 
      
    if root is None: 
        return -1
  
    if root == target: 
        kDistanceNodeDown(root, k) 
        return 0 
      
    dleft = kDistanceNode(root.left, target, k) 
      
    if dleft != -1: 
           
        if dleft +1 == k : 
            print(root.data) 
        else: 
            printkDistanceNodeDown(root.right, k-dleft-2)   
        return 1 + dleft
  

    dright = kDistanceNode(root.right, target, k) 
    if dright != -1: 
        if (dright+1 == k): 
            print(root.data) 
        else: 
            kDistanceNodeDown(root.left, k-dright-2) 
        return 1 + dright 
  
    # If target was neither present in left nor in right subtree 
    return -1
  
# Driver program to test above function 
root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14) 
target = root.left.right 
kDistanceNode(root, target, 2)