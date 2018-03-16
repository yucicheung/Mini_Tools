I've got three solutions from the Internet.
1. PyQt
2. PIL
Why not pillow(PIL)? Because it's only useful for windows and MacOS.
3. `dll`file from weixin or qq.
Same for way like call `.dll`.
## easy way 
PyQt有两个主要版本：PyQt 4.x和PyQt 5.x，两者不兼容，且前者基于Python 2和Python 3，后者仅基于Python 3。
```bash
sudo apt install python-qt4
```

## SIP
1. 下载sip
SIP must be installed before building and using PyQt4. You can get the latest release of the SIP source code from http://www.riverbankcomputing.com/software/sip/download.

2. 配置sip
```bash
python configure.py
```

3. 编译(build)sip
```bash
make
```

4. 安装SIP
```bash
sudo make install
```

5. 检查安装成功
```bash
sip -V
```

## 依赖包
```bash
sudo apt-get install libqwt5-qt4 libqwt5-qt4-dev
sudo apt-get install qt4-dev-tools qt4-doc qt4-qtconfig qt4-demos qt4-designer
```

##PyQt4
In order to configure the build of PyQt4 you need to run either the configure-ng.py or the configure.py script.

configure.py is the original configuration script that uses the build system of SIP v4 (i.e. the sip.sipconfig module). It will be supported for the life of PyQt4.

configure-ng.py is the new configuration script that uses Qt’s qmake program to do all the heavy lifting. It has the following advantages:

it supports cross-compilation
it is the basis of PyQt5’s configuration script
generated Makefiles have an uninstall target
it will work with SIP v5 (which will have no build system).

```bash
$ mkdir pyqt4
$ tar -xzvf package.tar.gz -C /home/yucicheung/pyqt4 #会在pyqt4文件夹中生成一个压缩文件名字一致的文件夹
```

### use configure-ng.py(If you are sure u r using the v4,run configure.py instead of this one)
```bash
sudo python configure-ng.py #之后要输入yes
```
### build pyqt4
```bash
$ sudo make -j4
$ sudo make install -j4
```
