# delayed-string-typer
Script to type string in the active window with a delay

## Preparing

It's a python3 script.
Install dependencies:

```
python -m pip install -r requirements.txt
```

On MacOS, when running the first time, ensure that the permission for the terminal to gain control of the keyboard is enabled

![Allow keyboard control](media/permission_screen.png)

## Running
- By default, without any CLI arguments it will hide the string to type, and wait 5 seconds
- Optional args:
    - `--wait`, `-w` wait time before keypress emulation begins
    - `--kbstr`, `-s` string to emulate keypress on

<br/>

![running example](media/emulate_keypress__mk20230822.gif)

<sub>
** Note: A cython compiled binary is also included at `bin/emulateKeyPress_osx_bin`. If you have a macbook with M-series processor, you can skip the installation bit and use the binary as-is, out of the box.
</sub>