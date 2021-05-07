import sys

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if not root : return None # root가 null 이면 None를 return
        else :
            if root.val == val : # root의 val이 찾는 val 값이라면 root를 return
                return root
            elif root.val > val :
                return self.searchBST(root.left, val) # 왼쪽 자식노드에는 루트노드보다 작은 값,오른쪽 자식노드에는 루트노드보다 큰 값 대소 비교
            elif root.val < val :
                return self.searchBST(root.right, val)