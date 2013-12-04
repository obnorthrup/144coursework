# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # Welcome to Week 10!
# 
# Today's project: Homework 6 Problem 3 (the `adjacent` method).
# 
# You can find this notebook in the usual place: https://github.com/obnorthrup/144coursework

# <markdowncell>

# ## Framing the problem
# 
# Here was Problem 3:
#     
# > Build a subclass of the `SearchTree` class in `runTregex.py` that contains a method `adjacent(self, elt)`, which checks whether adjacent to `self` is a treelet bearing `elt` as node label (for non-terminals) or value (in the case of leaves).
# 
# What is this asking of you?

# <markdowncell>

# ## Breaking it down
# 
# #### 1. Setting up the subclass
# 
# Let's make a subclass of `ParentedTree` instead of SearchTree so we don't have to worry about `RunTregex.py`

# <codecell>

from nltk import ParentedTree

class myTree(ParentedTree):
    
    foo = "bar"

# <markdowncell>

# Now let's instantiate this, so we have a tree to play with

# <codecell>

tree = myTree("""(VP (VBD got)
  (NP
    (NP (DT a)
      (ADJP
        (QP ($ $) (CD 29.4) (CD million))
        (-NONE- *U*))
      (NNP Air) (NNP Force) (NN contract))
    (PP (IN for)
      (NP (NN intelligence) (NNS data) (NN handling)))))""")

# <codecell>

tree.draw()

# <markdowncell>

# #### 2. Moving around the tree
# 
# Subtrees keep track of where they sit in larger trees. We can move around with methods like `parent()` and `root()`, and we can see where we are with `treeposition()`

# <codecell>

print tree[0]
print tree[1]

# <codecell>

print tree[1][1]
print tree[1,1]
print tree[1,1,1,0,0]

# <codecell>

pp = tree[1][1]
intel = pp[1][0]
print pp[0]
print intel

print pp[0].right_sibling()
print pp[0].right_sibling()[0]

# <codecell>

contract = tree.root()[1,0,4]

# <codecell>

tree[1,1,1].leaf_treeposition(0)

# <codecell>

tree[1,1,1].leaves()

# <codecell>

tree[1,1,1].leaf_treeposition(0)

# <codecell>

tree[1,0,4]

# <markdowncell>

# #### 3. Finding the closest right sibling
# 
# How can we do this?

# <codecell>

def closestSib(tr):
    '''Crawl up the tree from tr and return the treeposition of the first right sibling.'''
    
    depth = len(tr.treeposition())
    searcher = tr # searcher will crawl up the tree until a node with a right sibling is found

    for i in range(0,depth): # only crawl up until the root
        tr_sib = searcher.right_sibling() # get the right sibling; if there's isn't one, it's None
        if tr_sib != None:
            return tr_sib
        searcher = searcher.parent() # otherwise, climb up a level and try again
   
    return None #returns None if no closest sibling found

# <markdowncell>

# #### 4. Find the rightmost leaf
# 
# This part's quick

# <codecell>

def firstLeaf(sib):
    '''Given a tree sib, return the position of the leftmost leaf in sib'''
    
    leafPos = sib.treeposition() + sib.leaf_treeposition(0)
    return leafPos

# <markdowncell>

# #### 5. Climb back up, checking as we go
# 
# Keep in mind: At the leaf we're checking a string against `elt`. At subtrees we're checking a node label.

# <codecell>

def right(t1, elt): 
    '''Given a tree t1 and a string elt, return True if t1 precedes elt'''
    
    sibling = closestSib(t1) # set sibling to the closest righthand sibling, or None
    if sibling == None:
        return False
    
    leafPos = firstLeaf(sibling) # if there's a sibling, leafPos is the position of leftmost leaf in it
    
    leaf = t1.root()[leafPos] # leaf is the leaf's content (a string), to be checked against elt
    if leaf == elt:
        return True
    
    # assuming there's a leaf but it isn't elt, walk up from leaf and check every node label
    pointer = t1.root()[leafPos[:-1]] # start at the subtree immediately above the leaf
    depth = len(sibling) # continue only up to the level of the closest sibling
    
    for i in range(depth):
        if pointer.node == elt:
            return True
        else:
            pointer = pointer.parent()
    
    # There's a sibling, but neither the leaf nor any nodes up to sibling match elt
    return False

# <codecell>

print right(contract, "PP")

# <markdowncell>

# ## Putting it together
# 
# How can these methods be put together in the class definition?

# <codecell>

from nltk import ParentedTree

class myTree(ParentedTree):
    
    def closestSib(self):
        '''Crawl up the tree from self and return the treeposition of the first right sibling.'''
        
        depth = len(self.treeposition())
        searcher = self # searcher will crawl up the tree until a node with a right sibling is found

        for i in range(0,depth): # only crawl up until the root
            tr_sib = searcher.right_sibling() # get the right sibling; if there's isn't one, it's None
            if tr_sib != None:
                return tr_sib
            searcher = searcher.parent() # otherwise, climb up a level and try again
   
        return None #returns None if no closest sibling found
    
    
    
    def firstLeaf(self):
        '''Given self, return the position of the leftmost leaf in self'''
    
        leafPos = self.treeposition() + self.leaf_treeposition(0)
        return leafPos
    
    
    
    def right(self, elt): 
        '''Given a tree t1 and a string elt, return True if t1 precedes elt'''
        
        sibling = self.closestSib() # set sibling to the closest righthand sibling, or None
        if sibling == None:
            return False
    
        leafPos = sibling.firstLeaf() # if there's a sibling, leafPos is the position of leftmost leaf in it
        
        leaf = self.root()[leafPos] # leaf is the leaf's content (a string), to be checked against elt
        if leaf == elt:
            return True
    
        # assuming there's a leaf but it isn't elt, walk up from leaf and check every node label
        pointer = self.root()[leafPos[:-1]] # start at the subtree immediately above the leaf
        depth = len(sibling) # continue only up to the level of the closest sibling
    
        for i in range(depth):
            if pointer.node == elt:
                return True
            else:
                pointer = pointer.parent()
    
        # There's a sibling, but neither the leaf nor any nodes up to sibling match elt
        return False

# <codecell>

tree = myTree("""(VP (VBD got)
  (NP
    (NP (DT a)
      (ADJP
        (QP ($ $) (CD 29.4) (CD million))
        (-NONE- *U*))
      (NNP Air) (NNP Force) (NN contract))
    (PP (IN for)
      (NP (NN intelligence) (NNS data) (NN handling)))))""")

contract = tree[1,0,4]

print contract.right("PP")

# <codecell>


