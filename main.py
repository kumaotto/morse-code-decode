import time
from pynput import keyboard

# 入力設定
DOT_DURATION = 0.2
DASH_DURATION = 0.6
WORD_BREAK_TIME = 1.5

# キー入力の開始時間
press_start_time = None
# モールス信号のバッファ
morse_code_buffer = ''
# 最後の入力時間
last_input_time = time.time()


# キー入力の開始時間を記録
def on_press(key):
    global press_start_time

    # キーがescの場合、リスナーを停止する
    if key == keyboard.Key.esc:
        print('the messages is:', morse_code_buffer)
        return False

    if (key == keyboard.Key.space) and (press_start_time is None):
        press_start_time = time.time()


def on_release(key):
    global press_start_time, morse_code_buffer, last_input_time

    # キーがスペースの場合、デコードを実行する
    if key == keyboard.Key.space:
        
        last_input_time = time.time()
        press_duration = last_input_time - press_start_time

        if press_duration < DOT_DURATION:
            print('.')
            morse_code_buffer += '.'
        elif press_duration >= DASH_DURATION:
            print('-')
            morse_code_buffer += '-'

        # 次の入力のために初期化
        press_start_time = None

        print('morse_code_buffer:', morse_code_buffer)


def check_word_break_needed():
    global morse_code_buffer, last_input_time
    current_time = time.time()

    if (current_time - last_input_time) > WORD_BREAK_TIME:
        print(' ')
        morse_code_buffer += ' '
        last_input_time = current_time


# get key info by pressing key
def get_key_info():

    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    try:
        while listener.running:
            check_word_break_needed()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('exit morse code decoder...')


if __name__ == '__main__':
    print('start morse code decoder...')
    get_key_info()
