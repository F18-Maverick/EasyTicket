首先，感谢所有希望给票票通 (EasyTicket) 开源代码仓库做出贡献的每个人。希望各位都能顺利的买到回家的火车票！

## 在做出贡献之前：
&emsp; -- 本分支或是本版本尚未拥有完整的功能，如果您想参与开发，我们也十分感谢!
&emsp; -- 我们非常欢迎任何形式的贡献，包括但不限于提出[issues](https://github.com/F18-Maverick/EasyTicket/issues)、
[Pull requests](https://github.com/F18-Maverick/EasyTicket/pulls)。  
&emsp; -- issues中可以包括[readme](https://github.com/F18-Maverick/EasyTicket/blob/main/README.md)、
[文档](https://github.com/F18-Maverick/EasyTicket/tree/main/Doc)、
[代码](https://github.com/F18-Maverick/EasyTicket)等中的任何问题(如标点符号问题, bug等)或关于新功能或特性的好想法，
只要能让本项目更加完美。  
&emsp; -- Pull requests中可以在任何符合标准的情况下修改你遇到的任何问题或增加任何的新功能、特性等。
但是请一定要在Pull request标题以及commit信息中包含对应的issues号（无issues除外）。  
&emsp; -- 但是我们仍然强烈您在修改任何内容前（除了文档和Readme）在[issues区](https://github.com/F18-Maverick/EasyTicket/issues)
和我们进行友好的沟通。否则尽管您有可能确实做了非常大的努力，但是最后的修改仍然不被合并到我们的主分支中。

## 贡献内容：
### 代码部分：
为了让本项目的代码更容易维护，我们只要求贡献的代码尽可能的可读并有实际使用价值。
### 测试代码：
本项目暂时并没有写任何的测试代码，所以这里的测试代码如果你希望做出贡献，标准可自行决定。
但是请说明测试代码中测试的部分并在有需要的情况下说明用途。
### 文档&Readme部分：
任何语法，标点，语句不通顺等问题都可以修改。

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
接下来，您就可以在您创建的分支中修改任何问题或增加新功能、特性了。在修改结束后，请将修改内容push进您fork的项目对应分支中，
然后通过加Pull requests的方式提交PR！  
最后再次非常感谢您的任何贡献，我们会在最快的时间内给您的贡献回应！
