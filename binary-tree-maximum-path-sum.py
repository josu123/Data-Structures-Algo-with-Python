def solve(root,res):
    if root is None:
        return 0
    l=solve(root.left,res)
    r=solve(root.right,res)
    temp=max(max(l,r)+root.val,root.val)
    ans=max(temp,l+r+root.val)
    res[0]=max(res[0],ans)
    return temp
class Solution(object):
    def maxPathSum(self, root):
        l=[-1000000000]
        solve(root,l)
        return l[0]
       
