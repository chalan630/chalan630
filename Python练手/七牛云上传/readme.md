# 七牛云上传图片脚本

## 预期目标
- [x] 将图片拖拽到图标上，实现将图片上传到七牛云，并返回图片外链。
- [x] 封装为类

## 知识点
### sys.argv[]的用法
对图片拖拽所使用的sys.argv[]的测试  
简单测试实例  
```python
import sys,os  
print('1.' + sys.argv[0])
print('2.' + sys.argv[1])
os.system(sys.argv[1])
```

> 结论：  
sys.argv[0] 为可执行文件的绝对路径  
sys.argv[1:] 为所有输入文件的绝对路径组成的列表  
输入文件可有多个

![argv1.png](http://okt3vzszu.bkt.clouddn.com/img/argv1)
![argv2.png](http://okt3vzszu.bkt.clouddn.com/img/argv2)


### sys.exit()和os._exit()的选择

**os._exit()** 会直接将python程序终止，之后的所有代码都不会继续执行。

**sys.exit()** 会引发一个异常：SystemExit，如果这个异常没有被捕获，那么python解释器将会退出。  
如果有捕获此异常的代码，那么这些代码还是会执行。捕获这个异常可以做一些额外的清理工作。  
0为正常退出，其他数值（1-127）为不正常，可抛异常事件供捕获。

> sys.exit()的退出比较优雅，调用后会引发SystemExit异常，可以捕获此异常做清理工作。os._exit()直接将python解释器退出，余下的语句不会执行。

## 参考资料
[七牛云PythonSDK](https://developer.qiniu.com/kodo/sdk/1242/python)  
[七牛云PythonAPI源码](https://github.com/qiniu/python-sdk)

