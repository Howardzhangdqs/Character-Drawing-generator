# Character Drawing generator 字符画生成器

基于Python的视频生成字符画小工具，运行后生成C++程序

## Usage 使用

```
使用: main.py [-h] [--version] --input INPUT [--color] [--width WIDTH] [--height HEIGHT] [--size SIZE] [--output OUTPUT]

可选参数:
  -h, --help                 显示帮助信息并退出
  --version, -v              显示版本
  --input INPUT, -i INPUT
                             视频地址 (必填)
  --color, -c                是否生成彩色字符画 (默认值: False)
  --width WIDTH, -ww WIDTH
                             字符画宽 (默认值: 120, 单位: 字符)
  --height HEIGHT, -hh HEIGHT
                             字符画高 (默认值: 30, 单位: 字符)
  --size SIZE, -s SIZE       字符画大小 (-ww 和 -hh 的缩写) (默认值: 120x30, 单位: 字符)
  --output OUTPUT, -o OUTPUT
                             字符画输出地址 (默认值: ./${input path}.cpp)
```
样例：

```bash
python "main.py" -i "何同学.mp4" -o "何同学.cpp" -s 150x50 -c
```

输出为`何同学.cpp`，宽150字符，高50字符，彩色模式

再通过g++编译

```bash
g++ -o "何同学.exe" -static-libgcc "cheat2.mp4.cpp"
```

打开`何同学.exe`即可观看

## Features 特色

输出的C++程序内含何同学色特：
![未标题-1](https://user-images.githubusercontent.com/75195784/185288219-8a04e096-a4e7-492e-86b2-211568ae8a42.png)


