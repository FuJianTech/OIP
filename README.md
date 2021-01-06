# OIP
🌍
*[English](/docs/README-en.md) ∙ [简体中文](README.md)*

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

(![红尘](http://dorians.top/usr/uploads/2021/0105/红尘.jpg)

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





