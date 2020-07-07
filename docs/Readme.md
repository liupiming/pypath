

# 算法alg

1. [git 参考](https://github.com/TheAlgorithms/Python)



## arithmetic_analysis

1. 算术分析
2. 





# sorts

### bead sort

1. 珠排序
2. 个数字9用9个1来表示,珠排序中的珠指的是每一个1,它把每一个1想像成一个珠子,这些珠子被串在一起

![Image(7)](https://images.cnblogs.com/cnblogs_com/kkun/201111/201111231440229963.png)

### bitonic
1. 双调排序

### Bogo 排序
1. 又被称为猴子排序，是一种恶搞排序算法，其算法就是坑爹的将元素随机打乱，然后紧紧检查其是否符合排列顺序，若否，则继续进行随机打乱，继续检查结果，直到符合排列顺序。
2. 是个既不实用又原始的排序算法，其原理等同将一堆卡片抛起，落在桌上后检查卡片是否已整齐排列好，若非就再抛一次。



### 堆排序

![img](https://img-blog.csdn.net/20180801211245720?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTA0NTIzODg=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)



![img](https://img-blog.csdn.net/20180801213938728?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTA0NTIzODg=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

1. 每个结点的值都大于其左孩子和右孩子结点的值，称之为大根堆；
2. 每个结点的值都小于其左孩子和右孩子结点的值，称之为小根堆。
3. ==堆的结构可以分为大根堆和小根堆，是一个完全二叉树==



**基本思想：**

   1.首先将待排序的数组构造成一个大根堆，此时，整个数组的最大值就是堆结构的顶端
   2.将顶端的数与末尾的数交换，此时，末尾的数为最大值，剩余待排序数组个数为n-1
   3.将剩余的n-1个数再构造成大根堆，再将顶端数与n-1位置的数交换，如此反复执行，便能得到有序数组

**构造堆：**

1. 保证0~1位置大根堆结构，
2. 保证0~2位置大根堆结构...直到保证0~n-1位置大根堆结构（每次新插入的数据都与其父结点进行比较，如果插入的数比父结点大，则与父结点交换，否则一直向上交换，直到小于等于父结点，或者来到了顶端）
3. 后面的是将顶节点去掉后，下面的子节点比较，继续构建大根堆



# 爬虫

1. [git 参考](https://github.com/geekcomputers/Python)
2. https://github.com/gxcuizy/Python/tree/master/12306%E6%8A%A2%E7%A5%A8
3. https://github.com/wkunzhi/Python3-Spider/tree/master/%E5%8E%9F%E5%88%9B%E7%88%AC%E8%99%AB%E5%B7%A5%E5%85%B7





