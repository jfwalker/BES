'''
Code adapted from code written by Stephen A. Smith
'''
class Quartet:
    def __init__ (self,lfs,rts,length):
        self.left = set()
        self.right = set()
        for i in lfs:
            self.left = self.left.union(i)
        self.lefts = lfs
        for i in rts:
            self.right = self.right.union(i)
        self.rights = rts
        self.length = length

    def __str__(self):
        t = []
        for i in self.lefts:
            t.append(",".join([j for j in i]))
        x = " | ".join(t)
        t = []
        for i in self.rights:
            t.append(",".join([j for j in i]))
        y = " | ".join(t)
        return x+" === "+y+" ("+str(self.length)+")"
    
    def conflict(self, inbp):
        if len(inbp.right.intersection(self.right)) > 0 and len(inbp.right.intersection(self.left)) > 0:
            if len(inbp.left.intersection(self.right)) > 0 and len(inbp.left.intersection(self.left)) > 0 :
                return True
        if len(inbp.left.intersection(self.left)) > 0 and len(inbp.left.intersection(self.right)) > 0:
            if len(inbp.right.intersection(self.left)) > 0 and len(inbp.right.intersection(self.right)) > 0:
                return True
        return False

    def same(self, inbp):
        if len(inbp.right) != len(self.right) and len(inbp.right) != len(self.left):
            return False
        if inbp.right == self.right and inbp.left == self.left:
            return True
        if inbp.right == self.left and inbp.left == self.right:
            return True
        return False
    
    def match(self,inq):
        if self.conflict(inq):
            return False
        lmatchedl = set()
        lmatchedr = set()
        for i in self.lefts:
            tl = 0
            for j in range(len(inq.lefts)):
                if i.intersection(inq.lefts[j]):
                    tl += 1
                    lmatchedl.add(j)
            for j in range(len(inq.rights)):
                if i.intersection(inq.rights[j]):
                    tl += 1
                    lmatchedr.add(j)
            if tl > 1:
                return False
        samed = True
        lmatched = lmatchedl
        if len(lmatchedl) > 0 and len(lmatchedr) > 0:
            return False
        if len(lmatchedr) > 0:
            samed = False
            lmatched = lmatchedr
        if len(lmatched) < 2:
            return False
        rmatchedl = set()
        rmatchedr = set()
        for i in self.rights:
            tl = 0
            for j in range(len(inq.lefts)):
                if i.intersection(inq.lefts[j]):
                    tl += 1
                    rmatchedl.add(j)
            for j in range(len(inq.rights)):
                if i.intersection(inq.rights[j]):
                    tl += 1
                    rmatchedr.add(j)
            if tl > 1:
                return False
        if len(rmatchedl) > 0 and len(rmatchedr) > 0:
            return False
        rmatched = rmatchedr
        if samed and len(rmatchedl) > 0:
            return False
        if samed == False and len(rmatchedr) > 0:
            return False
        if samed == False:
            rmatched = rmatchedl
        if len(rmatched) < 2:
            return False
        return True
            

"""
return one bipart for the node
"""
def get_quartet(nd,rt):
    if len(nd.children) == 0 or nd == rt:
        return None
    length = nd.length
    rights = []
    lefts = []
    right = set()
    for i in nd.children:
        r = set(i.lvsnms())
        rights.append(r)
        right = right.union(r)
    p = nd.parent
    for i in p.children:
        if len(set(i.lvsnms()).intersection(right)) > 0:
            continue
        else:
            lefts.append(set(i.lvsnms()))
    if p != rt:
        out = set(rt.lvsnms())
        lefts.append(out-set(p.lvsnms()))
    bp = Quartet(lefts,rights,length)
    return bp

"""
get all the biparts for a tree
"""
def get_quartets(rt):
    bps = []
    for i in rt.iternodes():
        q = get_quartet(i,rt)
        if q != None:
            bps.append(q)
    return bps

if __name__ == "__main__":
    """
    needs to be unrooted
    """
    import ctree as tree_stuff
    t = tree_stuff.build("(((a:0.1,b:0.1):0.1,c:0.2):0.1,(d:0.2,(e:0.1,f:0.1):0.1):0.1);")    
    t2 = tree_stuff.build("((a:0.1,b:0.1):0.1,c:0.1,f:0.1);")
    q1 = get_quartets(t)
    for i in q1:
        print(i)
    print("----")

    q2 = get_quartets(t2)
    for i in q2:
        print(i)

    for i in q1:
        if i.match(q2[0]):
            print "MATCHED:  ",i,"    ",q2[0] 
