## Python Virtual Environment Setup

The dependancy tool `uv` [uv documentation here](https://docs.astral.sh/uv/getting-started/)
is used to control the python virtual environment. This can be installed with

```
pip install uv
```

Once it has completed you can then run `uv sync` to install everything.

The script can then be run by using `uv run transmit_and_receive.py` or by configuring vscode to use
the newly created virtual environment.

## Teensy Code

The teensy software was written using the PlatformIO extension for VSCode. The code is retained in
the Teensy memory between power cycles. If requried PlatformIO can be used to rebuild the code and
reflash.

The device used is a Teensy 4.1 [see link here for pinout and details](https://www.pjrc.com/teensy/)
