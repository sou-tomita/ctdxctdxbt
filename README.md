# ctdxctdxbt

X-CTDのデータをcsvファイルに変換する

## Requirement
- Python
- Pandas

## Usage 
### 1. ```namelist.py```を設定
```namelist.py```を編集する。
| 変数名|説明|
|:---|:---|
|```field_book_path:Path```|```field_book.csv```のファイルパスを設定|
|```input_dir:Path```|入力データのディレクトリを指定|
|```output_dir:Path```|出力データのディレクトリを指定|

(例)
```
#!/usr/bin/env python3

from pathlib import Path

field_book_path = Path("./sample_Seisui2022/field_book_1m.txt")
input_dir = Path("./sample_Seisui2022")
output_dir = Path("./output")

fig_dir = Path("./fig")
```

### 2. ```qc.py```を実行
```qc.py```を実行すると、出力先データディレクトリに出力される。


### 6. T-Sダイアグラムの作図```ts_diagram.py```
```namelist.py```の```output_dir```内のすべてのデータについて、T-Sダイアグラムを描画する  
#### 必要ライブラリ
- [GSW-Python](https://teos-10.github.io/GSW-Python/index.html)  

```ts_diagram.py```を編集し実行する

|変数名|説明|
|:---|:---|
|```min_sp```,```max_sp```|横軸(実用塩分[psu])の最小・最大値|
|```sp_ticks```|横軸の目盛|
|```min_tmp```,```max_tmp```|縦軸(水温[deg])の最小・最大値|
|```tmp_ticks```|縦軸の目盛|
|```lat```,```lon```|観測点の緯度・経度[deg]|
|```p```|密度を計算する圧力(<=0)[dbar]|

```namelist.py```で指定した```fig_dir```直下の```tsdiagram```ディレクトリに出力される．