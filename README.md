# BullShitGenerator2.0

基于 [BullshitGenerator](https://github.com/menzi11/BullshitGenerator/) 的狗屁不通文章生成器，加入了成语、古诗、励志句子等元素，支持自定义字数和导出 txt。

> 生成的文章仅供娱乐，请勿用于正规用途。

## 运行

```bash
pip install -r requirements.txt
python MakePassage.py
```

## 功能

- 自定义文章主题和字数
- 支持导出为 txt 文件
- 文章随机结尾
- 内容包含：成语、古诗、励志句子、网络名句

## 目录结构

```
MakePassage.py   主程序
read.py          JSON 读取工具
data.json        素材数据
cybash.txt       成语库
sentence.txt     句子库
poem.txt         古诗库
```

## 计划

- 加入更多句子与调侃
- 增加文章类型与语言风格
- 增加更多导出格式

欢迎开分支贡献内容。