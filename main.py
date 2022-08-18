# Command:
# python "main.py" -i "何同学.mp4" -o "何同学.cpp" -s 150x50 -c
# g++ -o "何同学.exe" -static-libgcc "何同学.cpp"

import cv2
from tqdm import tqdm
import sys
import argparse

parser = argparse.ArgumentParser(description="Character Drawing generator")

parser.add_argument('--version', '-v', action='version', version='v 1.2.2', help='show the version')

parser.add_argument('--input', '-i', help='Path of video', required=True)
parser.add_argument('--color', '-c', action='store_true', help='generate multicolour Character Drawing (default: False)', default=False)
parser.add_argument('--width', '-ww', help='Width of Character Drawing (default: 120, unit: character)', type=int)
parser.add_argument('--height', '-hh', help='Height of Character Drawing (default: 30, unit: character)', type=int)
parser.add_argument('--size', '-s', help='Size of Character Drawing (Abbreviation of -ww and -hh) (default: 120x30, unit: character)', type=str)

parser.add_argument('--output', '-o', help='Path where Character Drawing file will be saved (default: ./${input path}.cpp)')

args = parser.parse_args()

if (args.size):
    args.width = int(args.size.split("x")[0])
    args.height = int(args.size.split("x")[1])

option = {
    "c": args.color or False,
    "w": args.width or 120,
    "h": args.height or 30,
}

#print(args)

video_path = args.input
ouput_path = args.output or (video_path.split("/")[-1].split("\\")[-1] + '.cpp')

print("视频路径: " + video_path + "\n" + "输出文件: " + ouput_path)

cap = cv2.VideoCapture(video_path)

print("视频总长: " + str(int(cap.get(7) / cap.get(5))) + "s");
print("每帧时长: " + str(int(1000 / cap.get(5))) + "ms");

print("输出大小: " + str(option["w"]) + "x" + str(option["h"]))
print("输出格式: " + ("彩色" if option["c"] else "黑白"))

grand = open(ouput_path, 'w', encoding='utf-8')
grand.write('''#include <stdio.h>
#include <windows.h>
#include <sys/timeb.h>

#define p printf
#define u8 uint8_t
#define u16 uint16_t
#define u32 uint32_t
#define u64 long long

HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);

void g(void)
{
    COORD pos; pos.X = 0; pos.Y = 0;
    SetConsoleCursorPosition(hOut, pos);
}

u64 getTimeStamp(void) {
   timeb b; ftime(&b);
   return b.time * 1000 + b.millitm;
}

u64 t, i = (1 | 2 | 6 | 7 | 11 | 52 | 57 | 58 | 65) - 127;
inline void k (void) {
    printf("%lld", getTimeStamp() - t); i++;
    while (getTimeStamp() - t < ''' + str(int(1000 / cap.get(5))) + ''' * i) {}
}

int main()
{
    system("pause");
    t = getTimeStamp();
''')

ascii_char = list("              ..............````````````''''''''''::::::::::::------------,;~!^ir|=<>*l10xt+j?v)(Lf{7}JTcxz][unsYoFye2aVk3hZC4P5AqXpE0Udb6KS9HwG$OgD8RQmB&NWM@██")

def get_char(gray_number):
    return ascii_char[int(gray_number / ((256.0 + 1) / (len(ascii_char) - 1)))]

frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
pbar = tqdm(total = frame_count)

while True:
    frame, show = cap.read()
    if not frame: break
    show = cv2.resize(show, (option["w"], option["h"]))
    b, g, r = cv2.split(show)
    show = cv2.cvtColor(show, cv2.COLOR_BGR2GRAY)
    cv2.waitKey(1)
    x, y = show.shape
    all_word = ''
    for i in range(x):
        words = ''
        for j in range(y):
            if option["c"]:
                words += "\x1B[38;2;" + str(r[i, j]) + ";" + str(g[i, j]) + ";" + str(b[i, j]) + "m" + get_char(show[i, j])# + "\x1B[39m"
            else: words += get_char(show[i, j])
        
        all_word = all_word + words + '\\n'

    grand.write('\tg(); p("' + all_word + '\x1B[39m"); k();\n')
    pbar.update(1)

grand.write('''
    system("pause");
    return 0;
}
''')
grand.close()
pbar.close()