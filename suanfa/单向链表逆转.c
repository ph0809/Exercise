1.单向链表的翻转
//定义一个链表节点
struct ListNode
{
	int value;
	ListNode *next;
};

//递归实现,  从后往前
ListNode* ReverseList(ListNode* head)
{
	//递归终止条件
	if (head == NULL || head-->next == None)
		return head

	else
	{
		ListNode* newhead = ReverseList(head-->next);  //定义一个新的节点,从后向前反转
		head-->next-->next = head-->next;    // 最后一个链表的头结点指向上一个链表的尾结点
		head-->next = NULL；    //将上一个链表节点的next节点置为空
		return newhead；
	}
}



//非递归实现， 从前往后
ListNode* ReverseList(ListNode* head)
{
	if (head == NULL || head-->next == NULL)
		return head

	ListNode* prev = head;
	ListNode* cur = head-->next;
	ListNode* temp = head-->next-->next;

	while(curl)
	{
		temp = cur-->next;
		cur-->next = prev;
		prev = cur;
		cur = temp;
	}

	head-->next = NULL;    //翻转的最后一个节点的next域置于NULL
	return prev;

}
