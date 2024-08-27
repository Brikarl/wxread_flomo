# 微信读书笔记同步工具

这是一个Python脚本，用于从本地文本文件中读取[微信读书](https://weread.qq.com/)笔记，并使用flomo
API将其同步至[flomo](https://flomoapp.com/)笔记应用。

## 功能

1. 读取本地文件 `wx_notes.txt`。
2. 提取文件内容并标记章节标题和笔记内容。
3. 将整理后的内容按章节和笔记通过flomo API同步至flomo。

## 安装

在运行此脚本之前，您需要确保已经安装了 `Python 3.x` 和 `pip`。

1. clone 本仓库：

```sh
git clone https://github.com/Brikarl/wxread_flomo.git
cd wxread_flomo
```

2. 安装依赖：

```sh
pip install -r requirements.txt
```

## 使用方法

1. 打开微信读书 App - 选择「我」 - 「笔记」，从其中选择想要的笔记内容，复制到剪贴板。
2. 将笔记内容粘贴到名为 [wx_notes.txt](wx_notes.txt) 的文件中，并且格式如下：

```
书名

作者
x个笔记

标题

◆ 内容

◆ 内容

标题

◆ 内容

-- 来自微信读书
```

2. 将 [wxread_flomo.py](wxread_flomo.py) 中的 `URL` 变量 `https://flomoapp.com/xxxx` 替换为您的 flomo API 地址。

3. 运行脚本：

```sh
python wxread_flomo.py
```

## 注意事项

- 该脚本假定您的微信读书笔记文件格式与上面示例一致。如果格式有所不同，请根据实际情况调整代码。
- 为了防止每日API调用次数达到上限（flomo对API调用次数有每日限制），当检测到限制时，脚本会自动停止上传。
- 确保您的flomo API URL正确无误。

通过这个脚本，您可以轻松将微信读书笔记同步到Flomo，使得笔记管理更加方便高效。