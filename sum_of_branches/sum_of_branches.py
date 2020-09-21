



class BinarySearchtree:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
        



def branch_sum(root):
    sum = []
    find_sum_of_branches(root,0,sum)        
    return sum

def find_sum_of_branches(tree,current_sum,sum):
    if tree is None:
        return
    current_sum = current_sum + tree.value
    if tree.right is None and tree.left is None:
        sum.append(current_sum)
        return
    
    
    find_sum_of_branches(tree.left,current_sum,sum)
    find_sum_of_branches(tree.right,current_sum,sum)

