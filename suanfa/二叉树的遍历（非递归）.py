”“”
非递归 二叉树的各种遍历算法
“”“


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:

	def PreOrderTraverse(self, root):	
		"""先序遍历"""
		ret = []     # 返回的数据列表
		stack = [root]    # 栈，先把根放进去
		while stack:
			node = stack.pop()     # 将二叉树的根pop出来
			if node:
				ret.append(node.val)
				stack.append(node.right)    # 先压入右孩子
				stack.append(node.left)     # 后压入左孩子
		return ret


	def InOrderTraverse(self, root):
		"""中序遍历"""
		ret = []
		stack = []
		while stack or root:
			if root:
				stack.append(root)
				root = root.left    # 一直往左找，找到最左边的节点
			else:       # 找到了最左的节点
				temNode = stack.pop()         # pop出最左边的节点
				ret.append(temNode.val)
				root = temNode.right
		return ret

	def PostOrderTraverse(self, root):
		"""后序遍历"""
		ret = []
		stack = []
		while stack or root:
			if root:
				stack.append(root) 
				ret.insert(0, root.val)      # 从后往前插入，最上面的根是最先插入的
				root = root.right       # 一直向右找，找到最右的一个节点，开始pop出来
			else:
				stack.pop()
				root = root.left      # pop到某个根节点，判断是否有左孩子，有的话还是跟上面的规律一样，一直往下找
		return ret


	def LevelOrderTraverse(self, root):
		"""层序遍历"""
		ans = []
		level = [root]
		while any(level):
			ans.append([node.val for node in level])
			level = [kid for n in level for kid in (n.left, n.right) if kid]
		return ans

	def MulLevelOrderTraverse(self, root):
		"""多叉树的层序遍历"""
		ret = []
		level = [root]
		while any(level):
			ret.append([node.val for node in level])
			level = [child for n in level for child in n.children if child]
		return ret





































