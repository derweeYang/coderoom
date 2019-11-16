#encoding=utf-8
'''
简单区块链
区块
简要说包括三部分信息
    --数据
    --指向下一个区块的指针
    --根据区块中所有信息，计算出来的hashcode

区块链
第一块，没有别的区块指向他，这个特殊区块叫 genesis block
其他区块有序连接起来构成一个大链表
从数据结构上说这是一个双向链表
'''

import datetime
import hashlib

class Block:
    #区块编码
    blockNo = 0
    #区块存储数据
    data = None
    #校验码，根据区块重要信息计算出来的，这里采用sha256 生成 256位校验码
    hash  = None
#指向下一个区块
    next = None
    #记录上一个区块的hash code
    previous_hash = None
    #唯一编码
    nonce = 0
    #时间戳
    timestamp = datetime.datetime.now()

#创建一个区块，初始化为需要负载的信息
    def __init__(self,data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.blockNo).encode("utf-8") +\
            str(self.data).encode("utf-8") +\
            str(self.nonce).encode("utf-8") +\
            str(self.previous_hash).encode("utf-8") +\
            str(self.timestamp).encode("utf-8") 
            
        )

        return h.hexdigest()
    def __str__(self):
        #打印区块信息
        return "Block hash:" + str(self.hash()) \
        + " \n BlockNo:" + str(self.blockNo) \
        + " \n data:" + str(self.data)\
        + " \n nonce:" + str(self.nonce) \
        + " \n previouse_hash:" + str(self.previous_hash) \
        + " \n timestamp:" + str(self.timestamp)


class Blockchain:
    '''
    由创建出来的区块组成信息链表
    '''
    #控制取值范围，表示挖矿难度
    diff = 20
    #尝试空间
    maxNonce = 2**20
    target = 2**(256 - diff)

#创建链表头，block 指向最近产生的区块
    block = Block("Genesis")
    head = block

    def add(self, block):
        #前一个校验信息
        block.previous_hash = self.block.hash
        #当前块编码
        block.blockNo = self.block.blockNo + 1
        #上一个块指向当前块
        self.block.next = block
        #移动block指向最新块
        self.block = self.block.next


    def mine(self,block):
        #假设在很大的空间尝试挖矿
       for i in range(self.maxNonce):
           #假设得到的块小于 taget是满足条件的块，加到链表中
            if int(block.hash(),16) < self.target:
                self.add(block)
                print(block)
                break;
            else:
                block.nonce  +=1

if __name__ == "__main__":
    blockchain = Blockchain()

    for i in range(10):
        blockchain.mine(Block("Block" + str(i)))

#遍历链表
    headNode = blockchain.head
    while headNode != None:
        print(headNode)
        headNode = headNode.next





