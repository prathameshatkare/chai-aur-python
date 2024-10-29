
---

### 2. Using the Python Program
#### 2.1 Starting the Python Program
If you have Python installed on your computer, you can open it by typing this command:
```
python3.13
```

This works if Python is installed in a place where the computer knows to look, usually a folder called `/usr/local/bin/` on some systems. On other computers, it might be in a different folder, so check with someone who knows about computers if you’re not sure.

If you have Windows, and installed Python from the Microsoft Store, the command `python3.13` should work. Or, if you have a special Python launcher called `py.exe`, you can just type:
```
py
```

To quit Python, you can do two things:
1. Type `quit()`.
2. Use a shortcut on the keyboard: **Control-D** (on some computers) or **Control-Z** (on Windows).

When using Python, it’s a bit like typing commands in a chat box. You can also use shortcuts to make things faster, like pressing **Control-P** to bring up past commands.

Python has two modes:
1. **Interactive Mode:** You can type commands one by one, and it does them right away.
2. **Script Mode:** You can write a list of commands in a file (a script), and Python will do everything in that file when you ask it to.

#### 2.1.1. Sending Information to Python
When you run a Python script (a list of commands in a file), you can add extra information to help it know what to do. Python puts this information in a list called `sys.argv` in the `sys` module, which is like a collection of tools Python comes with.

#### 2.1.2. Talking to Python
When you type commands straight into Python, it’s in **interactive mode**. This means you’ll see a prompt that looks like this:
```
>>>
```
If you need more space for a long command, you’ll see a continuation prompt like this:
```
...
```

Here’s an example:
```python
the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")
```
And Python would say:
```
Be careful not to fall off!
```

#### 2.2. Python’s World and Environment
Python works with text files saved in **UTF-8**, a type of text encoding that lets it understand letters and symbols from different languages. If you need a different encoding, you can add a special line at the start of your file to let Python know. It looks like this:
```python
# -*- coding: cp1252 -*-
```

If you’re also using a **shebang** (a line that tells the computer to use Python), it should look like this:
```python
#!/usr/bin/env python3
# -*- coding: cp1252 -*-
```

That’s it! Now you know the basics of opening, using, and closing the Python interpreter, and even how to work with different types of text files!
