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


# <codecell>


# <codecell>


# <codecell>


# <markdowncell>

# #### 3. Finding the closest right sibling
# 
# How can we do this?

# <codecell>

def closestSib(tr):
    '''Crawl up the tree from tr and return the treeposition of the first right sibling.'''
    
    # Your code here
   
    return None #returns None if no closest sibling found

# <markdowncell>

# #### 4. Find the rightmost leaf
# 
# This part's quick

# <codecell>

def firstLeaf(sib):
    '''Given a tree sib, return the position of the leftmost leaf in sib'''
    
    return None # Return something else here

# <markdowncell>

# #### 5. Climb back up, checking as we go
# 
# Keep in mind: At the leaf we're checking a string against `elt`. At subtrees we're checking a node label.

# <codecell>

def right(t1, elt): 
    '''Given a tree t1 and a string elt, return True if t1 precedes elt'''
    
    # Your code here
    
    return False

# <codecell>


# <markdowncell>

# ## Putting it together
# 
# How can these methods be put together in the class definition?

# <codecell>

from nltk import ParentedTree

class myTree(ParentedTree):
    
    foo = "bar" #delete me
    
    # Add your method(s) here. Don't forget 'self' is always an argument.
    
    #At the very least, you'll need:
    
    def right(self, elt):
        
        #Your code here
        
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

print contract.right("for") # Should be true
print contract.right("IN")  # Should be true
print contract.right("PP")  # Should be true
print contract.right("NP")  # Should be false

# <markdowncell>

# ## We're done! Good luck on final projects.

