![图片描述](misc/pdf2mind.png)


| [中文](README.CN.md) | [English](README.md) |

# pdf2mind
pdf2mind是一款由大语言模型驱动的智能工具，只需一键操作，即可将长篇PDF文档自动转换为结构清晰的思维导图。可以支持[XMind]("https://xmind.cn/")，[FreeMind]("https://freemind.sourceforge.io/wiki/index.php/Main_Page")和直接**SVG**格式输出。

# 演示
- [视频演示](https://www.youtube.com/watch?v=3JGv0MA77Qs)
- [功能展示](testdata/GreenAI-13Page.pdf_20250413151347.svg)
# 环境依赖
支持在Windows，Linux下运行。尚未尝试过MacOS。
需要安装如下依赖：
``` bash
conda create --name pdf2mind python=3.12
conda activate pdf2mind
pip install -r requirements.txt -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
```
其它依赖：
- [Graphviz](https://graphviz.org/)

对于linux操作系统:
``` bash
$ apt install graphviz
```
对于Mac操作系统:
``` bash
$ brew install graphviz
```
对于Windows操作系统

Please refer to https://graphviz.org/download/

# 帮助
```
$ python pdf2mind.py -h
usage: pdf2mind.py [-h] --pdf PDF --model MODEL --language LANGUAGE (--use-doubao | --use-qwen | --use-openai) [--chunk-size CHUNK_SIZE]
                   [--overlap-size OVERLAP_SIZE] [--max-level MAX_LEVEL] [--temperature TEMPERATURE]
                   [--only-freemind | --only-xmind | --only-svg]

Command-line parser: PDF filename + Model selection

options:
  -h, --help            show this help message and exit
  --pdf PDF             PDF filename
  --model MODEL         model name
  --language LANGUAGE   Target language (e.g., 'English', 'Chinese', 'France', etc.)
  --use-doubao          Use Doubao model
  --use-qwen            Use Qwen model
  --use-openai          Use OpenAI model
  --chunk-size CHUNK_SIZE
                        chunk size of PDF (optional, default 30000)
  --overlap-size OVERLAP_SIZE
                        overlap size of PDF (optional, default 1000)
  --max-level MAX_LEVEL
                        maximum level for mind maps (optional, default: 4)
  --temperature TEMPERATURE
                        LLM temperature (optional, default: 0.7)
  --only-freemind       Only generate FreeMind (.mm) format
  --only-xmind          Only generate XMind (.md) format
  --only-svg            Only generate SVG (.svg) format

```
# 支持度
## 支持的模型

| 厂商 | 必要的环境变量 |
| --- | --- |
| Openai | OPENAI_API_KEY |
| Qwen | DASHSCOPE_API_KEY |
| Doubao | ARK_API_KEY |

## 支持的思维导图
| 软件 | 所需格式 |
| --- | --- |
| Xmind | .md |
| Freemind | .mm |
| SVG | .svg |

# 使用方式
以使用Doubao大模型为例子：
```
$ setx ARK_API_KEY ***key*** or export ARK_API_KEY=***key***
$ python main.py --pdf testdata/GreenAI-2page.pdf --language Chinese --use-doubao --model doubao-1-5-lite-32k-250115
```
执行成功后可以在源目录下生成3种格式的思维导图。

# TODO清单

- **最高优先级别**
    * [ ] 完成async模式的IO
    * ✅ 更完善的类设计
    * [ ] 增加logging
    * ✅ 增加gitignore
    * ✅ 优化配置参数，包括：模型温度，pdf分片/重叠长度，思维导图最大深度，等
- **低优先级**
    * [ ] 改用poetry管理依赖
    * [ ] Docker部署
    * [ ] Flask提供接口服务到前端
    * [ ] 增加pytest
    * [ ] 增加github workflow
    * [ ] 更多的模型和格式支持

太多想做的事儿了，做完这些就能把大模型和python项目的知识顺一遍了。

# 致谢
- 我从[yihong0618](https://github.com/yihong0618/)的[xiaogpt](https://github.com/yihong0618/xiaogpt)和[bilingual_book_maker](https://github.com/yihong0618/bilingual_book_maker)学到了很多知识。
- [ChatPaper2Xmind](https://github.com/MasterYip/ChatPaper2Xmind)这个项目对我很有帮助。
