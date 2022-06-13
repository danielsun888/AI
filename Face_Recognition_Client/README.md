### 客户端界面
![](http://ww1.sinaimg.cn/large/006IYRZEly1fsj1kkak90j30sd0lzjrs.jpg)
### 使用说明
1. 点击“打开本地摄像头”按钮，在“摄像头采集信息”栏目中即会显示摄像头采集到的信息。
2. 点击“打开网络摄像头”按钮，在“摄像头采集信息”栏目中即会显示通过WIFI传输到的视频信息。传输协议是UDP，目的是显示树莓派采集到的视频。
3. 在打开摄像头后，点击获取人脸，左边会显示对齐后的人脸图片，大小为96*96.第一次使用时，数据集为空，在获得人脸图片后，点击新建人脸数据按钮，输入姓名，此时人脸图片保存在faces文件夹下。
4. 当人脸图片上出现图片时，才可点击“人脸识别”按钮，点击后会在人脸图片下方显示预测的姓名和欧式距离。欧式距离，值越小，表示越相似。当距离大于一定阈值（默认为0.4），其姓名会显示为unknown。
5. 点击“报错”功能按钮，把误识的人脸存入对应的人脸数据集中。例如：数据集中有5种人脸，分别标号为1、2、3、4、5，采集人脸其实为5号，却被误识为1、2、3、4或者unknown，这时点击“报错”按钮，把采集人脸存为5号人脸文件夹中即可。
6. 阈值是影响人脸识别的关键因素，默认为0.4，可自行调整。
7. 有2种模型可供下载，在model文件夹中可得下载链接
    1. 此种模型在微软MS-Celeb-1M数据集上训练，在LFW上测试的准确率可达87%以上。
    2. 此种模型在模型1的基础上，在LFW上继续训练，在LFW上测试的准确率可达91%以上。
8. 可以自己训练模型，参考我的另一个项目：https://github.com/yeziyang1992/Python-Tensorflow-Face-v2.0

___
### 代码思路
1. 开发环境
   * 开发平台：win10
   * 开发软件：PyCharm
   * 界面开发：PyQt5
2. 文档说明
    1. face_lib文件夹
        * align_dlib.py文件：主要进行人脸对齐。
        * face_recg.py文件： 进行人脸识别，其中阈值为0.4，可根据相应情况进行修改。
        * my.api.py文件： 自己写的各种函数方法。
        * udp_recv.py文件：包含进行udp协议传输视频的类。
    2. faces文件夹
        每一个文件夹名字必须是英文字母，代表一个类，其每一个类别中可以有多张图片，但数量过多，识别过慢。图片必须是96*96大小的经过对齐的jpg格式图片。
    3. model文件夹
        存放你训练的模型。
    4. gui.py文件
        一些界面相关的函数。
    5. inference.py文件
        神经网络函数。
    6. main.py文件
