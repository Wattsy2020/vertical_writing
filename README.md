A small program to convert Japanese text into top-to-bottom, left-to-right format. It uses an NLP model to split up the text into words, to ensure that the words aren't split into different columns.

Installation: clone the repo and `pip install -r requirements.txt`

Usage:
```bash
> echo "これは日本語で書かれた文です。このプログラムはどの文を縦書きにできる機能を持っています" | python main.py
て で ど こ 書 こ 
い き の の か れ 
ま る 文 プ れ は 
す 機 を ロ た 日 
　 能 縦 グ 文 本 
　 を 書 ラ で 語 
　 持 き ム す で 
　 っ に は 。
```

You can also specify the text height, e.g. `python main.py 5`
```bash
> echo "これは日本語で書かれた文です。このプログラムはどの文を縦書きにできる機能を持っています" | python main.py 5
ま を で 縦 は プ で 書 日 こ 
す 持 き 書 ど ロ す か 本 れ 
　 っ る き の グ 。 れ 語 は 
　 て 機 に 文 ラ こ た で 　 
　 い 能 　 を ム の 文 　
```