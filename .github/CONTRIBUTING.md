首先，感谢所有希望给票票通（EasyTicket）开源代码仓库做出贡献的每个人。希望各位都能顺利的买到回家的火车票！

## 在做出贡献之前：
&emsp; -- 我们非常欢迎任何形式的贡献，包括但不限于提出[issues](https://github.com/F18-Maverick/EasyTicket/issues)、[Pull requests](https://github.com/F18-Maverick/EasyTicket/pulls)。  
&emsp; -- 这里的issues可以包括[readme](https://github.com/F18-Maverick/EasyTicket/blob/main/README.md)、文档(正在写)、[代码](https://github.com/F18-Maverick/EasyTicket)中的任何问题，你甚至可以鸡蛋里挑骨头式的挑问题(如标点符号问题等)，只要能让本项目更加完美。  
&emsp; -- 至于Pull requests，你可以在任何符合标准的情况下修改你遇到的任何问题。
&emsp; -- 但是我仍然强烈您如果需要修改任何内容前（除了文档和Readme）请在issues区和我们进行友好的沟通，否则有可能您尽管确实做了非常大的努力但是最后的您的修改仍然不被合并到我们的主分支中。

## 贡献内容：
### 代码部分：
为了让本项目的代码更容易维护，我们只要求贡献的代码尽可能的可读并有实际使用价值。
### 测试代码：
本项目暂时并没有写任何的测试代码，所以这里的测试代码如果你希望做出贡献，标准可自行决定。但是请说明测试代码中测试的部分并在有需要的情况下说明用途。
### 文档&Readme部分：
只要按你认为对的改，人能看懂就行（awa!）

## 构建并测试项目：
在对本项目做任何贡献前，你需要先fork本项目至您自己的账户下。具体fork方式可在项目主页的左上角找到对应位置。  
在fork了本项目之后，请将源代码通过[Git](https://git-scm.com/downloads)克隆到本地。
```sh
git clone git@github.com:<Your_User_Name>/EasyTicket.git
```
在命令执行结束后，请进入项目目录
```sh
cd ~/src/EasyTicket
```
接着创建一个功能分支
```sh
git checkout -b <your_feature_branch>
```
然后配置开发环境(这里的requirements.txt在项目根目录下)
```sh
pip install -r requirements.txt
```
接下来，您就可以修改任何代码中的问题了。在修改结束后，请将修改内容push进您fork的项目分支中，然后通过加Pull requests的方式提交PR！
最后再次非常感谢您的任何贡献，我们会在最快的时间内给您的贡献回应！
