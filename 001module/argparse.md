argument[实参，调用方法/函数时括号里的参数]；
parameter[形参，方法/函数定义时在括号里的参数]

## Positional arguments
```
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.foo)
```
输出:
```
$ python3 1.py
usage: 1.py [-h] echo
1.py: error: the following arguments are required: echo

## 
$ python3 1.py foo
foo

## 位置参数
$ python3 1.py -h
usage: 1.py [-h] echo
positional arguments:
  echo        echo it
optional arguments:
  -h, --help  show this help message and exit

```

```
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number", type = int)
args = parser.parse_args()
print(args.square**2)

```

## Optional arguments
```
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")
```
当不使用--verbosity的时候是不会报错的. args.verbosity的值也是None;
当使用--verbosity的时候, 就要给它赋值, 否则会报错；

```
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", --verbosity", help="increase output verbosity",
                     action="store_true")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")
```
注意Short options和关键字action；

## Combining Positional and Optional arguments
```
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
parser.add_argument("-v0", "--verbosity", type = int, choices=[0, 1, 2],
                    help="increase output verbosity")
args = parser.parse_args()

answer = args.square**2
if args.verbose:
    print("verbosity turned on")
    if args.verbosity == 2:
        print("the square of {} equals {}".format(args.square, answer))
    elif args.verbosity == 1:
        print("{}^2 == {}".format(args.square, answer))
    else:
        print(answer)
else:
    print("verbosity turned off")
    print(answer)


```
关键字choices

```
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
       help="display a square of a given number")
parser.add_argument("-v", "--verbosity",
       action="count", default=0, help="increase output verbosity")
args = parser.parse_args()
answer = args.square ** 2
if args.verbosity >= 2:
       print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity >= 1:
       print("{}^2 == {}".format(args.square, answer))
else:
       print(answer)


##输出
$ python3 3.py 111 -vvvvv
the square of 111 equals 12321

$ python3 3.py 111
12321
```
例子：
```
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
parser.add_argument("-v", "--verbosity", action="count", default=0)
args = parser.parse_args()
answer = args.x ** args.y
if args.verbosity >= 2:
     print("Running '{}'".format(__file__))
if args.verbosity >= 1:
     print "{}^{} == {}".format(args.x, args.y, answer)
print(answer)
```

## Reference_Info
http://www.cnblogs.com/nkwy2012/p/6272567.html
https://docs.python.org/2.7/howto/argparse.html#