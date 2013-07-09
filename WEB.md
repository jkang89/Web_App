Going Online
============
A database is the last piece of technology we need before going online. In this segment, we'll take our database online, turning it into a web application using flask, our preferred web framework.

A State of Being
----------------
A database introduces an important concept to our programs. Until now, our programshave had no long-term memory. That is to say, if you ran our calculator from earlier, quit it, then ran it again, it would run exactly the same as if it were run for the first time: two plus two will always be four. 

The database changes all that. When we run our database-backed program, asking it for a student's grades will give different results over time as you add more data. This is called 'state', when the program reacts to input and responds differently. On top of that, the state is preserved when our program quits and restarts. This is called 'persistence'. Both of these things are provided by the database. 

It is of interest to note that our program is written as if it is stateless. Our database-backed application is fundamentally identical to our calculator in terms of program structure. We will abuse this fact as much as we can when writing web applications, as it makes our lives easier.

But First, A Detour Into VirtualEnv
-----------------------------------
Until now, we have not spent any time concerning ourselves with our 'environment'. On our machines, the appropriate version of python is already installed, we need only type the word to invoke it. Additionally, whenever we need a module, most of the time we can safely import it without question, as our machines have been prepared for these eventualities.

The thing is, even though it may seem like it, our computers are not our own. Modern unix-based operating systems are multi-user systems, which means multiple users can be logged in at the same time. In fact, every time you open a new terminal window, you're essentially logging in again, once in each terminal.

Given that there may be a multitude of users logged onto your system (over the network, most likely), we must generally be careful not to clobber other users' programs and settings. If you install python3 in a multi-user setting, you'll likely anger those who rely on python2.7.

In practice, the only other 'user' you need to worry about angering is your operating system. It relies on certain software packages to be installed to operate correctly. Currently, both linux and OSX are dependent on very specific versions of python. On top of that, it relies on very specific versions of certain modules, so we can't just go upgrading and installing things willy-nilly. (In python, installing certain modules sometimes forces an upgrade of others.)

Enter the virtual environment. Essentially, a virtualenv is a python sandbox. It gives you, the user, a way to cordon off whichever version of python you want to use along with whatever modules you need. This virtual environment is specific to you, and there's no need to ask permission of the operating system (or the super user) to install new modules.

Here are the steps to using virtual environments:

1. Create an environment.
This basically creates a copy of python and all of the essential modules and puts it in a directory of your choice. Creation of a virtual environment is _free_. This means you should make as many as you need, usually one per project. Each of your projects will have different requirements, so don't be stingy and try to use one env for all of them. The directory you put your environment in is usually named 'env' under the top level of your project.
2. Activate your environment.
Once an environment is created, you need to activate it. Unless you activate an environment, it simply sits there, sad and alone. But more importantly, unless you activate it, you'll continue to use the OS-specific versions of python and its modules.
3. Install your modules.
Even if you don't appreciate the utility of being able to cordon off your python configuration, at the very least, you'll now enjoy the ability to install modules without having to ask for permission. Once your environment is activated, you can install new python modules with impunity. Note: impunity is not the name of the python module installer, that program is actually called pip.
4. Work!
As you write and test your code, make sure to run it inside a terminal that has a virtualenv activated. It is very easy to forget this. If your program raises an ImportError when running, you're probably not inside the activated environment. When you activate an environment, it leaves a visual cue on your command prompt, make sure to check for it if things aren't going correctly.
5. Deactivate your environment
Just kidding, unless you're specifically going to activate another environment for a different project, don't worry about deactivating. Just open another window for that project.

### Your Mission, Should You Choose To Accept It
There exists a python module named 'howdoi'. Importing it from inside a python program does nothing, but it _does_ install a useful program that can answer programming questions from the command line.

First, verify that 'howdoi' is not installed on your machine:

    Meringue:sql_lesson chriszf$ howdoi
    -bash: /usr/local/bin/howdoi: No such file or directory

Your task is to create a new virtual environment, use pip to install howdoi, and ask howdoi a programming question:

    (env)Meringue:sql_lesson chriszf$ howdoi create a virtualenv
    pip freeze > env_modules.txt
    virtualenv my_env && cd my_env && source bin/activate
    pip install -r ../env_modules.txt


