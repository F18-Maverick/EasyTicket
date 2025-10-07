# EasyTicket
[![build](https://img.shields.io/badge/build-passing-green)](https://github.com/F18-Maverick/EasyTicket/actions)  [![lint](https://img.shields.io/badge/lint-passing-green)](https://github.com/F18-Maverick/EasyTicket/actions/workflows/pylint.yml)  [![Pypacket](https://img.shields.io/badge/PyPacket-passing-green)](https://github.com/F18-Maverick/EasyTicket/actions/workflows/publish.yml)  [![docs](https://img.shields.io/badge/docs-writing-blue)](https://github.com/F18-Maverick/EasyTicket/docs)  [![pypi](https://img.shields.io/badge/PyPI-testing_v0.0.1-red)](https://test.pypi.org/manage/project/easyticket)  [![version](https://img.shields.io/badge/Release-v0.0.1-green)](https://github.com/F18-Maverick/EasyTicket/releases/tag/v0.0.1-alpha)  [![PythonVersion](https://img.shields.io/badge/Python-3.8_|_3.9_|_3.10_|_3.11_|_3.12_|_3.13-blue)](https://github.com/F18-Maverick/EasyTicket)  [![lisence](https://img.shields.io/badge/Lisnece-GNU_GPL_v3.0_or_Later-red)](https://github.com/F18-Maverick/EasyTicket/blob/main/LICENSE)  [![Sponsor](https://img.shields.io/badge/%E2%9D%A4-Sponsor%20me-%23c96198?style=flat&logo=GitHub)](https://github.com/sponsors/F18-Maverick)  

<div align=center>
<img src="https://github.com/F18-Maverick/EasyTicket/blob/main/src/ticket_12306_prog_addition/download_photo.ico" width="120" height="120">
</div>  

票票通（EasyTicket）是基于12306的快速抢票工具，用爬虫和selenium等自动化技术调用系统浏览器实现。  
## 支持列表
* 操作系统：Windows | Linux | MacOS
* 浏览器：MicroSoft Edge (系列) | Google Chrome (系列) | FireFox (系列)  
(* 注：在使用该项目前请确保你的系统浏览器已经升级到最新，但是如果你不愿意升级你的浏览器，可以选择更改项目中的驱动版本，并确保和你的系统浏览器版本相匹即可。)
## 安装方式
票票通有多种安装方式。最简单的安装方式是通过python官方pypi的pip进行安装，或通过MakeFile的形式安装项目，或直接通过运行src/run.py（不推荐）。但是MakeFile的安装方式在本作者写该readme的时候还没有做出来，将在下一版中推出。
### 1, 通过pip安装：
&emsp; (* 注：当前pip仍然为测试版)
```sh
pip install -i https://test.pypi.org/simple/ EasyTicket==0.0.1.post1
```
### 2, 通过MakeFile安装：
&emsp; (* 注：正在制作中)
### 3, 通过run.py直接运行项目：
&emsp; 首先，请先克隆本项目仓库：
```sh
git clone https://github.com/F18-Maverick/EasyTicket.git
```
&emsp; 接着，进入项目的./src文件夹下，可以看到在该文件夹下有一个名为run.py的文件。我们直接运行他。  
```sh
python ./run.py
```  


