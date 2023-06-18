## Project: Logger

## Overview
---
LoggerはPythonのコードを作成時に、作成した関数やクラスメソッドの呼び出し回数や処理時間を簡単に測定するためのツールです。  

## Description
---
Loggerクラスは単純にインポートして使用することができます。また、運用中にはOFFに設定してパフォーマンスへの影響を最小限にすることも可能です。

スレッドセーフを確保するためのLoggerのサブクラスであるThreadSafeLoggerクラスも提供しています。ThreadSafeLoggerはLoggerクラスと同じように使用しますが、スレッドセーフなロギングを提供します。

このプロジェクトは主に以下の四つの部分で構成されています:

- Logger.py: Loggerクラスを提供します。  
    'log_calls'メソッドは関数の呼び出し回数をカウントし、'timer'メソッドは関数の実行時間を計測します。  

- ThreadSafeLogger.py: ThreadSafeLoggerクラスを提供します。  
    これはLoggerクラスのスレッドセーフなバージョンで、同じ方法で使用できます。  

- analyze.py: ログデータを分析する'analyze_logs'関数を提供します。  

- demo.py: 上記のクラスと関数の使用例をデモンストレーションします。  
## USAGE
---
### ログ埋め込み
関数やメソッドにログ機能を追加するために、Loggerのメソッドをデコレータとして使用します。ThreadSafeLoggerにも同じことが適用されます。  
```py
@Logger.timer
@Logger.log_calls
def slow_function():
    time.sleep(1)
```

### 開発時
LoggerのenabledをTrueに設定し、modeを'memory'に設定すると、ログ情報はメモリ内に保存されます。ThreadSafeLoggerにも同じ設定が適用されます。必要に応じて、ログ情報をテキストファイルに出力することもできます。  

```py
Logger.enabled = True
Logger.mode = 'memory'  # ログをテキストに出力
slow_function()
Logger.write_logs()
```

### ログ解析
ログファイルの解析はanalyzeモジュールの'analyze_logs'関数を用いて行います。  

```py
import analyze
analyze.analyze_logs(filename)
```

### 運用時
運用環境では、LoggerまたはThreadSafeLoggerはOFFに設定してパフォーマンスへの影響を最小限にします。その後は、Loggerのメソッドは何も出力しません。  
```py
Logger.enabled = False
# これ以降はログは作成されない
```

## Latest Version
v1.0 (2023-06-18)

新たなデータ分析機能の追加、ロギング機能の改善、新しいデモンストレーション例の追加が行われました。詳細については、[リリースノート](RELEASE_NOTES.md)をご確認ください。


## Requirement
---
このプロジェクトを実行するためにはPython 3.11.2と次のPythonライブラリが必要です:

- matplotlib 3.7.1

## Licence
---
このプロジェクトは[MIT](LICENSE)ライセンスに基づいて利用できます。

## Author
---
[kumab2221](https://github.com/kumab2221)

## Acknowledgements
---
このプロジェクトはオープンソースコミュニティに感謝の意を表しています。その中でも特にPython言語とその素晴らしいエコシステムに対して感謝します。