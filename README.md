# OIP
🌍
*[English](/docs/README-en.md) ∙ [简体中文](README-en.md)*

`python 3.9.0` `Flask 1.1.2`

`OpenInterfacePlatform`(开放接口平台),简称`OIP`

`Operational Improvement Plan`(作战改进计划),简称`OIP`

`Optical Image Processor`(光图像处理机),简称`OIP`



[![Requirements Status](https://requires.io/github/liangliangyy/DjangoBlog/requirements.svg?branch=master)](https://requires.io/github/liangliangyy/DjangoBlog/requirements/?branch=master)  [![license](https://img.shields.io/github/license/liangliangyy/djangoblog.svg)]()

## 主要功能：

- Flask 多蓝本注册

## 主要功能：

- [x] 测试接口连通性
- [x] py版本对应tf版本脚本
-  [ ] mysql 类编写

## 安装

- 终端下执行:
    ```
   git clone  https://github.com/FuJianTech/OIP.git
    ```

- pip安装:

    ```
  pip install -Ur requirements.txt
    ```


## 配置
大配置 `apps/etc/config.cfg `（主要配置项目名称）

小配置 `apps/etc/xxx/config.cfg `(主要配置项目端口号和引入其他蓝本)


## 代码目录

Home directory 🙋‍♀️🙋‍♂️

        --- apps    Main Folder
            --- etc Configuration Folder
            --- example Example Folder
                --- __init__.py
                --- config.cfg  BluePrint Config File
            --- test    Test Folder
                --- __init__.py
                --- config.cfg  BluePrint Config File
            --- config.cfg  Project Config File

        --- logic   Logic Folder
           --- applocations Applocations Folder
               --- applocations_base_blueprint   Index.html show
                    --- __init__py  Register BluePrint File
                       --- views.py View Function
               --- applocations_examples   Project Folder
                    --- __init__py  Register BluePrint File
                       --- views.py View Function
                       --- fun.py  Logic Function To Views Function Simple
               --- applocations_test   Project Folder
                    --- __init__py  Register BluePrint File
                       --- views.py View Function
                       --- fun.py  Logic Function To Views Function Simple

        --- static Static Folder
            --- images Images Folder
                --- favicon.ico
                --- bg.jpg Background

        --- templates   Templates Folder
            --- index.html

        --- __init__.py  Use little_config Function

        --- manger.py Run Flask

        --- readme.md Read Me


## 运行

**注意：** 在使用`python manger.py`之前,确定系统中的 `python`环境是否正确:

如果使用了虚拟环境,请切换到`python=3.9.0`(非必须选项)

 终端下执行:
```
python manger.py
```

默认配置 `example`

默认端口 `5021`

浏览器打开: http://127.0.0.1:5021/  就可以看到效果了。


## 问题相关

有任何问题欢迎提Issue,或者将问题描述发送至我邮箱 `dorians5689@gmail.com`.我会尽快解答.推荐提交Issue方式.

感谢



初代，佐非，赛文，杰克，艾斯，奥特之父，泰罗，奥特之母，雷欧，阿斯特拉，乔亚尼斯，爱迪，尤里安，察克，贝斯，史考特，葛雷，帕瓦特，哉阿斯，迪加，戴拿，盖亚，阿古茹，奈伊斯，奈欧斯，赛文，高斯，杰斯迪斯，雷杰多，博伊，黄金博伊，诺亚，奈科斯特，奈克伊斯，麦克斯，杰诺，梦比优斯，希卡利，赛文等家族成员支持

![红尘](http://dorians.top/usr/uploads/2021/0105/红尘.jpg)

特别鸣谢

Agnes Obel

## CHANGELOG

### [v1.0] 2021.01.06
- 添加文件夹TS
- tools (工具类/脚本)
- 编写py版本对应tf版本脚本
- 主要涵盖于py3.5 py3.6 py3.7 py3.8
- 3.9 暂时pypi未更新  
- 进度条包 tqdm 
- 数据来源: https://pypi.org/project/tensorflow/#history  
- 更新MIT许可证

### [1.7] 2021.01.07
- 添加文件夹DB/database
- 添加文件DB/database/model.py
- model.py 初始化数据库
- init_data.db 初始化数据库指定路径
- sql_orm.py sqlalchemy 封装sqlite数据库
- 添加一条或多条数据
- 筛选一条或多条数据
- ORM 对应的原生SQL
- 删除表  


### [1.12] 2021.01.12
- sql_orm.py sqlalchemy 封装sqlite数据库
- 更新语句分类
- 更新指定字段 
- 更新字符串拼接
- 更新数值运,支持加减操作
- 初始化模型,添加num数值字段
- 优化函数


### [1.19] 2021.01.19
- 学习vue
- 更新static文件夹 axios.min.js/vue.js
- 更新templates文件夹 vue_demo.html
- 添加蓝图 application_vue_demo
- vue 界面展示 如下:
![无痕](http://dorians.top/usr/uploads/2021/0119/无痕.png)


### [1.21] 2021.01.21
- 更新static文件夹uoloads
- 重构application_vue_demo文件夹
- 新增函数uppload 修改update函数
- 修改vue_demo.html
- 增减文件增删等按钮
![上传测试文件](http://dorians.top/usr/uploads/2021/0121/balck_eys.png)



### [1.22] 2021.01.22
- 更新上传文件到static文件夹
- 更新上传文件函数
- 主页面添加上传文件按钮等
- 修改vue_demo.html
- 数据库新增pic_path字段
![上传](http://dorians.top/usr/uploads/2021/0122/上传文件.png)


  
### [1.22] 2021.01.22
- 图片预览功能实现
- 数据库存储显示路径
- vue函数绑定事件
- 看我的卡姿兰大眼圈
- (⓿_⓿) 
(⓿_⓿)
(⓿_⓿)
(⓿_⓿)
![图片预览](http://dorians.top/usr/uploads/2021/0123/图片添加成功.png)

### [2.01] 2021.02.01

- 晨出郡舍林下
- 作者：张九龄
- 晨兴步北林，萧散一开襟。
- 复见林上月，娟娟犹未沉。
- 片云自孤远，丛筱亦清深。
- 无事由来贵，方知物外心

### [2.01] 2021.02.08

- 更新文件夹FO(文件操作)File operation
- 更新 file_operate.py
- 将文件夹下的文件已后缀名的方式移动到各自的文件夹
- 待做,判断文件是否存在目标文件
- 待做,剪切文件
- 说明: 如我有一个老师.doc
  - 新建文件夹doc 
  - 我有一个老师.doc 放到doc文件夹
  
- 代码
![代码](http://dorians.top/usr/uploads/2021/0208/代码.jpg)
  
图前
![图前](http://dorians.top/usr/uploads/2021/0208/图前.jpg)

图后1
![图后1](http://dorians.top/usr/uploads/2021/0208/图后1.jpg)
图后2
![图后2](http://dorians.top/usr/uploads/2021/0208/图后2.jpg)

- 主要用途
  - 将个人硬盘视频文本音乐等分类
  - 个人文档 txt excel pdf 按文件夹分类
  - 目前还未打算做带时间分类文件夹
  - 后续会考虑将图片添加日期 如 华山树木202002081518.png


### [2.01] 2021.02.18

- 文件分类
  - 支持多种后缀名
  - 软件链接 http://www.dropitproject.com/
  - 自动分类包 详情解释 https://zhuanlan.zhihu.com/p/45275359
  - 自动分类包 详情解释1 https://zhuanlan.zhihu.com/p/90621173
  - 软件来源于网络 