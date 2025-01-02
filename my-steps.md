What I tried to do here was to implement a script that allows me to:
    1. Create scripts according to what I add to the function call

For that, I needed to:
    1. Check if there are directories where all custom commands are going to be stored (_/.custom-commands/bin_). If not, create them.
    2. Check if the system variable **Path** has a path leading to */.custom-commands/bin*. If not, store that variable in the system's Path

When attempting step 2, I could not proceed as I did not have admin privileges when running the script. Therefore, I installed win32security with the following command:

```bash
$ pip install win32security ❌
```

It did not change the outcome. By googling some more, I found [this Stack Overflow answer](https://stackoverflow.com/questions/27547435/how-to-find-import-the-win32security-in-python), which pointed me to [PyWin32](https://pypi.org/project/pywin32/), which effectively fixed my problem. I ran the following command:

```bash
$ pip install pywin32 ✅
```

It worked. When I ran the script, it worked as expected, and when I checked the system variables, a new variable was stored there.