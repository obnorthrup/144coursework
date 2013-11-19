# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # Welcome to Week 8
# 
# Today's notebook can be found in the usual place: https://github.com/obnorthrup/144coursework
# 
# #### Plan for today:
# 
# 1. Setting up the Tregex wrapper
# 2. Reviewing how to use the wrapper
# 3. Extending the wrapper (to check for dominance)
# 
# ---
# 
# ## 1. Setting up the tools
# 
# 1. The [course website](https://github.com/panand/ComputationalMethods) has everything you need in the `scripts` directory
# 2. Open up runTregex.py and change the directories to match the locations on your computer
# 3. If you're going to use an iPython Notebook, put the notebook in the same folder as runTregex.py
# 
# ---
# 
# ## 2. How to use the wrapper
# 
# Here's a basic example. Import the Treebank class, name a pattern and a search directory, save the search, and run it.

# <codecell>

from runTregex import Treebank

pattern = "NP=np . NP=np2"
dir = "/Users/obn/Dropbox/Linguistics/Tools/treebank_3/parsed/mrg/wsj/24/"

t = Treebank(dir,pattern)
t.run()

# <markdowncell>

# `t` contains all the results in t.trees

# <codecell>

print len(t)
print t[8]

# <markdowncell>

# What kind of object is each tree?

# <codecell>


# <codecell>


# <codecell>


# <markdowncell>

# ---
# 
# ## 3. Determining dominance
# 
# Here's **Problem 3** on HW6:
# 
# >Build a subclass of the `SearchTree` class in `runTregex.py` that contains a method `adjacent(self, elt)`, which checks whether adjacent to `self` is a treelet bearing the `elt` as node label (for non-terminals) or value (in the case of leaves).
# 
# Let's do a similar kind of problem: Write a function `dominates(tree, elt)` that checks whether `elt` is within `tree`. (Then we'll make it a method if there's time. Most likely, we won't get that far.)

# <codecell>

t[1]

# <markdowncell>

# We can use whether or not an object is unicode to split the subtree cases from the terminals

# <codecell>


