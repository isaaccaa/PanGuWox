# PanGuWox
pangu的Wox插件，可用于自动在文本中的中英文之间插入空格
# 盘古自白

> 研究顯示，打字的時候不喜歡在中文和英文之間加空格的人，感情路都走得很辛苦，有七成的比例會在 34 歲的時候跟自己不愛的人結婚，而其餘三成的人最後只能把遺產留給自己的貓。畢竟愛情跟書寫都需要適時地留白。

本插件基于 [pangu.py](https://github.com/vinta/pangu.py) 制作，灵感来自于 [Alfred的pangu脚本](https://github.com/Norcy/alfred-workflow-pangu/)

# 安装方法

## Python 依赖

由于安装 Wox 时已经安装了 Python，仅需安装两个库即可实现

```bash
pip3 install pyperclip
pip3 install pangu
```

安装速度慢的情况下可以使用清华大学源进行安装

```bash
pip3 install pyperclip -i https://pypi.tuna.tsinghua.edu.cn/simple
pip3 install pangu -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 安装插件到Wox

1. 打开 Wox 的文件所在位置

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d81072b5-62cb-4849-9019-853587225ee6/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d81072b5-62cb-4849-9019-853587225ee6/Untitled.png)

2. 进入app-xxx/Plugins文件夹

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/81fa9b3e-d01c-4776-8c35-d0a37482fcda/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/81fa9b3e-d01c-4776-8c35-d0a37482fcda/Untitled.png)

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/226af5b8-085a-4646-badd-887dd685bbf7/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/226af5b8-085a-4646-badd-887dd685bbf7/Untitled.png)

3. 将解压得到的 PanGuWox 文件夹拷贝至此

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6a313099-1646-4737-bcfb-2630b33b214f/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6a313099-1646-4737-bcfb-2630b33b214f/Untitled.png)

4. 在插件中启用PanGuPython

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/18c00c91-96c0-43ed-a955-e9af36026e93/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/18c00c91-96c0-43ed-a955-e9af36026e93/Untitled.png)

5. 可以在热键中创建自定义查询热键

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6341895e-90cf-4903-b076-0e9f6ae72bfc/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6341895e-90cf-4903-b076-0e9f6ae72bfc/Untitled.png)

# 使用方法

选中文字——复制——调用插件——粘贴

调用插件推荐使用自定义查询热键，由于第一次接触 Wox，对其中的代码十分不熟悉，目前似乎没有找到类似 Alfred 中选中文字——按快捷键自动替换的功能。好像 Wox 的 Python 插件必须要输入内容，但本插件选择使用剪贴板的内容，这样更快。

以上图设置热键为例，整套流程为：鼠标选中文字——[Ctrl + C]——[Alt + P]——[Ctrl + V]
