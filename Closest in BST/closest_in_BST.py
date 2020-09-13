
# Average : O(log(n)) time | O(log(n)) space
# Worst   : O(n) time | O(log(n)) space These is the worst case when the tree is a linear 

def findclosestinbst(tree,target):
    return findclosestinbsthelper(tree,target,float("inf"))

def findclosestinbsthelper(tree,target,closest):
    if tree is None:
        return closest
    elif abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    elif target > closest:
        return findclosestinbsthelper(tree.right,target,closest)
    elif target < closest: 
        return findclosestinbsthelper(tree.left,target,closest)
    else:
        return closest    


# Average : O(log(n)) time | O(1) space
# Worst   : O(n) time | O(1) space These is the worst case when the tree is a linear 

def findclosestinbst1(tree,target):
    return findclosestinbsthelper(tree,target,float("inf"))

def findclosestinbsthelper1(tree,target,closest):
    currentnode = tree
    while currentnode is None:
    
        if abs(target - closest) > abs(target - tree.value):
            closest = currentnode.value
        elif target > closest:
            currentnode=currentnode.right
        elif target < closest: 
            currentnode=currentnode.left
        else:
            break
   
    return closest