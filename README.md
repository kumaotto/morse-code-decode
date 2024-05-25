# Morse Code Decoder

This project is a Morse code decoder implemented in Python. It uses the `pynput` library to detect key presses and releases, and translates Morse code input into English text.

## Features

- Detects short and long key presses to represent dots and dashes in Morse code.
- Interprets spaces between Morse code symbols and words.
- Stops listening for input when the `esc` key is pressed.

## Usage

1. Run the script in a Python environment where the `pynput` library is installed.
2. Input Morse code using the space bar (short press for dot, long press for dash).
3. Press the `esc` key to stop input and display the decoded message.

## Requirements

- Python 3.6 or later
- `pynput` library

## Mac Users

For Mac users, you may need to adjust your accessibility settings to allow the script to control your computer. Go to System Preferences > Security & Privacy > Privacy > Accessibility, and add your terminal application to the list of apps allowed to control your computer.

## Installation

1. Clone this repository.
2. Install the `pynput` library using pip: `pip install pynput`.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---
