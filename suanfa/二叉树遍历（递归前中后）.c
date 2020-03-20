2.二叉树（前、中、后序遍历）


/*
递归遍历
*/
typedef struct BiTree
{
	ElemType data;
	struct BiTree *lchild, *rchild;
}BiTree, *BiTree

//前序    根左右
void PreOrderTraverse(BiTree t, int level)       //t是一个二叉树， level表示层数
{
	if (t == NULL)   // 如果是一颗空树
	{
		return 
	}

	printf("data = %s, level = %d\n", t->data, level);    //输出根节点
	PreOrderTraverse(t->lchild, level+1);      //遍历做孩子节点
	PreOrderTraverse(t->rchild, level+1);     //遍历右孩子节点
}

//中序   左根右
void PreOrderTraverse(BiTree t, int level)       //t是一个二叉树， level表示层数
{
	if (t == NULL)   // 如果是一颗空树
	{
		return 
	}

	PreOrderTraverse(t->lchild, level+1);       //遍历做孩子节点
	printf("data = %s, level = %d\n", t->data, level);    //输出根节点   
	PreOrderTraverse(t->rchild, level+1);     //遍历右孩子节点
}

//后序遍历    左右根
void PreOrderTraverse(BiTree t, int level)       //t是一个二叉树， level表示层数
{
	if (t == NULL)   // 如果是一颗空树
	{
		return 
	}

	PreOrderTraverse(t->lchild, level+1);       //遍历做孩子节点
	PreOrderTraverse(t->rchild, level+1);     //遍历右孩子节点
	printf("data = %s, level = %d\n", t->data, level);    //输出根节点   
	
}



/*
非递归遍历
*/














































