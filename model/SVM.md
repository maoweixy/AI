支持向量机(Support Vector Machine,SVM)是用于分类的一种算法，也属于有监督学习的范畴。

让我们先从一个大侠与反派的故事开始吧~

【该故事来源于https://www.reddit.com上的一个话题讨论:让5岁小孩也能看懂的SVM】

在很久以前，大侠的心上人被反派囚禁，大侠想要去救出他的心上人，于是便去和反派谈判。反派说只要你能顺利

通过三关，我就放了你的心上人。

现在大侠的闯关正式开始:

第一关:反派在桌子上似乎有规律地放了两种颜色的球，说:你用一根棍子分离开他们，要求是尽量再放更多的球

之后，仍然适用。

![image-20200501221424461](https://tva1.sinaimg.cn/large/007S8ZIlgy1gedb4p18jqj30d308c752.jpg)

大侠很干净利索的放了一根棍子如下:

![image-20200501221529224](https://tva1.sinaimg.cn/large/007S8ZIlgy1gedb5iqmeyj30ay07st9i.jpg)

 第二关:反派在桌子放上了更多的球，似乎有一个红球站错了阵营。

![image-20200501221543597](https://tva1.sinaimg.cn/large/007S8ZIlgy1gedb5xd2bzj30cc085myc.jpg)

SVM就是试图把棍放在最佳位置，好让在棍的两边有尽可能大的间隙。

![image-20200501221604187](https://tva1.sinaimg.cn/large/007S8ZIlgy1gedb64bkbkj309507njsg.jpg)

于是大侠将棍子调整如下，现在即使反派放入更多的球，棍子仍然是一个很好的分界线。


![image-20200501221613321](https://tva1.sinaimg.cn/large/007S8ZIlgy1gedb69ygubj309v07nabd.jpg)

反派看到大侠已经学会了一个trick，于是心生一计，给大侠更 难的一个挑战。

第三关:反派将球散乱地放在桌子上。

![image-20200501221745591](https://tva1.sinaimg.cn/large/007S8ZIlgy1gedb7w0qzrj309p06wt98.jpg)

现在大侠已经没有方法用一根棍子将这些球分开了，怎么办呢?大侠灵机一动，使出三成内力拍向桌子，然后桌子上的球就被震到空中，说时迟那时快，大侠瞬间抓起一张纸，插到了两种球的中间。

![image-20200501221833955](https://tva1.sinaimg.cn/large/007S8ZIlgy1gedb8px77uj30f507i3zv.jpg)

现在从反派的角度看这些球，这些球像是被一条曲线分开了。于是反派乖乖地放了大侠的心上人。

![image-20200501221843919](https://tva1.sinaimg.cn/large/007S8ZIlgy1gedb8vyn1wj309q06zdgs.jpg)

 从此之后，江湖人便给这些分别起了名字，把这些球叫做 「data」，把棍子叫做 「classifier」, 最大间隙trick 叫 做「optimization」， 拍桌子叫做「kernelling」, 那张纸叫做「hyperplane」



总结一下:

当一个分类问题，数据是线性可分(linearly separable)的，也就是用一根棍就可以将两种小球分开的时候，我们 只要将棍的位置放在让小球距离棍的距离最大化的位置即可，寻找这个最大间隔的过程，就叫做最优化。但是，现 实往往是很残酷的，一般的数据是线性不可分的，也就是找不到一个棍将两种小球很好的分类。这个时候，我们就 需要像大侠一样，将小球拍起，用一张纸代替小棍将小球进行分类。想要让数据飞起，我们需要的东西就是核函数 (kernel)，用于切分小球的纸，就是超平面(hyperplane)。如果数据集是N维的，那么超平面就是N-1维的。

![image-20200501221948770](https://tva1.sinaimg.cn/large/007S8ZIlgy1gedba0uhgbj30ao083myg.jpg)

把一个数据集正确分开的超平面可能有多个(如下图)，而那个具有“最大间隔”的超平面就是SVM要寻找的最优 解。而这个真正的最优解对应的两侧虚线所穿过的样本点，就是SVM中的支持样本点，称为“支持向量(support vector)”。支持向量到超平面的距离被称为间隔(margin)。

![image-20200501221956810](https://tva1.sinaimg.cn/large/007S8ZIlgy1gedba5ywzuj30om083tcc.jpg)