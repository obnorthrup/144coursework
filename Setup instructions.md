Tags: #ling #x44  
Date: 2013-10-03

# How to get GitHub and Anaconda working (on Mac OS  X 10.7+) so you can do your homework

This guide will lead you through the setup process step by step. The GitHub for Mac app only works with Mac OS X Lion or newer (10.7+). If you're using Windows, Linux, or an older version of Mac OS X, you'll need to use a [different client](http://git-scm.com/downloads/guis) or the command line tool, but the general steps remain the same. 

## Github Part 1: Cloning the class repository

The end goals here are A) that you have a folder on your computer called ComputationalMethods that mirrors what Pranav's put on the web, and B) that by using the GitHub for Mac app, you can update your copy (called your "local repository") to mirror any changes Pranav has made, plus see a list of what those changes are. Think Dropbox, but with manual sync and a list of what changed each time. Here's what I did to get this working:


1. Make an account on [GitHub.com](http://github.com/)

2. Download GitHub for Mac, open it up, and log in. You have no repositories, but that's okay.  
    - _FYI: **GitHub for Mac** is a "Git client." This means it gives you a native (graphical) interface for using **Git**, the program that's actually doing all the syncing stuff. When Pranav was doing things in the terminal in class Wednesday, that was Git. GitHub for Mac lets you do all the same things in a more familiar way._

3. On the class website, click the "Clone in Desktop" button, or go to this link directly:  
    `github-mac://openRepo/https://github.com/panand/ComputationalMethods`  
The above tells GitHub for Mac to open on your computer and prompts you to pick a place to save your new local clone.

4. Pick a place and save it. It'll download and now it's like any other folder on your computer.

5. Whenever you want to update your local copy, click on ComputationalMethods in GitHub for Mac. You'll see a list of previous updates, and clicking each will show you what changed. If you click "Pull" under the ""Repository" menu, you'll get the latest version.

6. Optional: If you want to get notified when there's a new version, click "Watch" in the mid-upper right on the class website.


At this stage, the homework assignment is sitting in the directory `[whatever you picked]/ComputationalMethods/homework/`.
Mine's in a folder called `x44`, inside my `Linguistics` folder, inside my `Documents` folder, inside my home (`~`) directory. So that's:

`~/Documents/Linguistics/x44/ComputationalMethods/homework/`

Since the homework file is an IPython notebook, you'll have to open it with that program, otherwise it'll just be text. So to use it, you'll have to get the notebook software working. First though, remember that you have to submit your assignment through GitHub too. The next step is to make your own repository for this purpose.


## GitHub Part 2: Making your own repository

You can't upload to the course repository, because it belongs to Pranav. What you need now is your own place to upload files on GitHub. In this part, you'll make a new repository and put a copy of `Homework 1.ipynb` in it.

1. In GitHub for Mac, go to `File > Create New Repository`

2. Name and describe your repository. Mine's called "144coursework" with the description "My repo for Computational Methods."

3. For the local path (i.e., where the repo's stored on your computer), you can choose whatever you want. I recommend putting it near the course repo, though. In my case, my `x44` folder contains Pranav's `ComputationalMethods`, my new `144coursework` repo, and a few other folders like `Notes` that I don't want to publish online, but that I want to keep together with the other course materials.

4. Make sure the checkbox is checked (so that it syncs with GitHub), then click "Make Repository"

Alright, now you have a folder on your computer (mine's `144coursework`), and whatever you put in it will appear on GitHub.com the next time you "push" changes. If you open your repo online at GitHub.com, you'll see it's empty. Why not do your first push now? Here's how:

1. Remember how the homework assignment is in `[wherever you downloaded the course repo to]/ComputationalMethods/homework/`? Go find `Homework 1.ipynb` in there, and put a copy of it in your new repository's folder. (I renamed my copy "Homework 1 - northrup.ipynb" and put it in a new subfolder called "homework" inside my repo folder, because that's tidier.)

2. If you go back to GitHub for Mac and click the "Changes" side tab, you'll see that it noticed you added some files to your new repo. Crucially, these changes won't get mirrored online until you "commit" them and "push" them to GitHub.com. Let's do that now:

3. Write a short summary of what you've done in the "commit summary" field. Mine says "Started HW1."

4. Look through the list of proposed changes and make sure everything seems right. At this stage, the answer's almost certainly "yes," but it's a good habit.

5. Click "Commit." This means you're confident that the changes you've made to the local folder are ones you want to keep. It's like saving your game.

6. Go to the menu bar and click `Repository > Push`. This means you want the version of your repo that's online to match the latest saved version on your computer.

7. Check out your repo on GitHub. There's your homework file!

Remember: **Commit saves changes locally, and Push publishes them.** You should commit after every milestone in your project. Git remembers your changes, so you can always go back to old versions if you need to. Until you hit Push, no changes will be reflected online. So if you don't want your homework up there half-done, just don't push it again until you've finished the assignment.

Ok, now all that's left is to open that homework file and do the homework. Hang in there!

## Anaconda + IPython Notebook

Anaconda is a self-contained version of Python with a bunch of extra things we'll use in this course. You can install Anaconda by following [these instructions](http://docs.continuum.io/anaconda/install.html#mac-install).

Once it's installed, there'll be a folder in your home directory called `anaconda` that contains the whole Python installation with all of Anaconda's bells and whistles. If you poke around in there, you'll see a `bin` folder, which contains all the programs that make up the Anaconda installation. One of these is called `iphython`, and all the Launcher does (or is supposed to do) is launch that program for you.

But you don't want the Launcher. It's bad. You can do everything you need, more easily, with two commands in the terminal. Here's how:

1. Open the Terminal app (in your Utilities folder). Eventually, you're going to start the IPython notebook, but you have to do so from the folder where your homework file is, otherwise it won't see it. So the next step is to get to the right folder in the terminal.

2. Navigate the terminal to the folder where your copy of Homework 1 is. If you know how to do this, great. If you don't, I'll give you a workaround, but try to ask someone to show you how to navigate through the terminal because it's a very useful skill. Anyway, the trick way is:

    1. Type `cd` in the terminal, followed by a space. _Note: cd means "change directory."_

    2. In the Finder, get to where you can see the folder your homework file is in. For me, that's `~/Documents/Linguistics/x44/144coursework/homework/`.

    3. Drag the `homework` folder (or your equivalent) to the terminal. When you release, the folder's path should appear after `cd  ` .

    4. Hit return. You're now in the homework folder. You can check this by typing the command `ls` to list the folder's content. If you see your homework file, you're golden.

3. Paste or type the command `ipython notebook` and hit return. The notebook interface will load in your browser, and you're good to go. If the terminal instead says "command not found," try `~/anaconda/bin/ipython notebook` instead.

4. The terminal stays open while the notebook is running. When you're done working, type `Control-c` to turn off the notebook.


**The End.** (Or just the beginning?)