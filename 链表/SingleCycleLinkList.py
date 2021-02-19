"""
__project_ = 'algorithm-python'
__file_name__ = 'SingleCycleLinkList'
__author__ = 'Administrator'
__time__ = '2021/2/19 22:22'
__product_name = PyCharm
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃        ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""


class Node(object):
    """链表的结点"""

    def __init__(self, item):
        # item存放数据元素
        self.item = item
        # next是下一个节点的标识
        self.next = None


class SingleCycleLinkList(object):

    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        # 链表为空
        if self.is_empty():
            return 0
        # 链表不为空
        count = 1
        cur = self._head
        while cur.next != self._head:
            count += 1
            # 指针下移
            cur = cur.next
        return count

    def items(self):
        """ 遍历链表 """
        # 链表为空
        if self.is_empty():
            return
        # 链表不为空
        cur = self._head
        while cur.next != self._head:
            yield cur.item
            cur = cur.next
        yield cur.item

    def add(self, item):
        """ 头部添加结点"""
        node = Node(item)
        if self.is_empty():  # 为空
            self._head = node
            node.next = self._head
        else:
            # 添加结点指向head
            node.next = self._head
            cur = self._head
            # 移动结点，将末尾的结点指向node
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
        # 修改 head 指向新结点
        self._head = node

    def append(self, item):
        """尾部添加结点"""
        node = Node(item)
        if self.is_empty():  # 为空
            self._head = node
            node.next = self._head
        else:
            # 寻找尾部
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            # 尾部指针指向新结点
            cur.next = node
            # 新结点指针指向head
            node.next = self._head

    def insert(self, index, item):
        """ 指定位置添加结点"""
        if index <= 0:  # 指定位置小于等于0，头部添加
            self.add(item)
        # 指定位置大于链表长度，尾部添加
        elif index > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            # 移动到添加结点位置
            for i in range(index - 1):
                cur = cur.next
            # 新结点指针指向旧结点
            node.next = cur.next
            # 旧结点指针 指向 新结点
            cur.next = node

    def remove(self, item):
        """ 删除一个结点 """
        if self.is_empty():
            return
        cur = self._head
        pre = Node
        # 第一个元素为需要删除的元素
        if cur.item == item:
            # 链表不止一个元素
            if cur.next != self._head:
                while cur.next != self._head:
                    cur = cur.next
                # 尾结点指向 头部结点的下一结点
                cur.next = self._head.next
                # 调整头部结点
                self._head = self._head.next
            else:
                # 只有一个元素
                self._head = None
        else:
            # 不是第一个元素
            pre = self._head
            while cur.next != self._head:
                if cur.item == item:
                    # 删除
                    pre.next = cur.next
                    return True
                else:

                    pre = cur  # 记录前一个指针
                    cur = cur.next  # 调整指针位置
        # 当删除元素在末尾
        if cur.item == item:
            pre.next = self._head
            return True

    def find(self, item):
        """ 查找元素是否存在"""
        return item in self.items()
