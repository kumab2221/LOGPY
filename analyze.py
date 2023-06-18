import matplotlib.pyplot as plt
from collections import defaultdict
import re
from itertools import cycle

# 利用可能なマーカースタイル
markers = cycle(('o', 'v', '^', '<', '>', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X'))

def analyze_logs(filename):
    # データを格納するディクショナリを初期化
    call_counts = defaultdict(int)
    execution_times = defaultdict(list)

    with open(filename, 'r') as f:
        for line in f:
            # 呼び出しのログを見つける
            call_match = re.match(r'(\w+) was called.', line)
            if call_match:
                function_name = call_match.group(1)
                call_counts[function_name] += 1
            # 実行時間のログを見つける
            time_match = re.match(r'(\w+) took (\d+\.\d+) milliseconds to run.', line)
            if time_match:
                function_name, exec_time = time_match.groups()
                execution_times[function_name].append(float(exec_time))

    # 呼び出し回数のグラフを作成
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.bar(call_counts.keys(), call_counts.values())
    plt.title('Function call counts')
    plt.xlabel('Function name')
    plt.ylabel('Count')
    
    # 実行時間のグラフを作成
    plt.subplot(1, 2, 2)
    for function_name, times in execution_times.items():
        plt.plot(times, label=function_name, marker=next(markers))
    plt.title('Function execution times')
    plt.xlabel('Call number')
    plt.ylabel('Execution time (ms)')
    plt.legend()

    plt.tight_layout()
    plt.show()
