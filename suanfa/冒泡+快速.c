3.常见排序（冒泡、快速）

//  a.冒泡排序(从左到右，相邻元素进行比较，每比较一轮，就会找到序列中最大的或者最小的那一个)
for (i=0; i<n-1; ++i)    //一共比较n-1轮
{
	for (j=0; j<n-1-i; ++j)   //每轮比较n-1-i次
	{
		if (a[j] > a[j+1])
		{
			temp = a[j+1];
			a[j+1] = a[j];
			a[j] = temp;
		}
	}
}


//   b.快速排序   将第一个数作为基准，先从右向左找到第一个小于它的，再从左向右找到第一个大于它的，交换这两个数的位置，之后继续移动，直到这两个指针相遇，
// 将相遇下标对应的数与第一个数交换位置，之后以这个数为界，左边和右边都采用同样的方法排序
def quick_sort(list, start, end):
	mid = a[start];   //start表示列表的第一个数下标，end表示最后一个数的下标
	low = start;
	high = end;

	// 当low和high相遇时，要排的子数列就剩下一个数
	while low < high:
		// high先从右向左找到第一个小于或者等于mid的数，如果high的数比mid大，左移high
		// 找到之前，如果high和low碰面了，也不继续找了
		while low < high and a[high] < mid:
			high -= 1
		//跳出循环后，high下标对应的数就是比mid小的数
                a[i] = a[j]

		//low从左向右找到第一个大于mid的数，如果low的数比mid大，右移low
		while low < high and a[low] > mid:
			low += 1
		//跳出循环后，low下标对应的数就是比mid大的数
                a[j] = a[i]

	//当high和low相遇了，则将该位置的数与mid交换
	result = a[high]

	quick_sort(list, start, low-1)
	quick_sort(list, high+1, end)

