import matplotlib.pyplot as plt
import pandas as pd
import re
from itertools import cycle

# 利用可能なマーカースタイル
markers = cycle(('o', 'v', '^', '<', '>', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X'))

def analyze_logs(filename):
    # データを格納するデータフレームを初期化
    call_counts_df = pd.DataFrame(columns=['function_name', 'call_count'])
    execution_times_df = pd.DataFrame(columns=['function_name', 'execution_time'])

    with open(filename, 'r') as f:
        for line in f:
            # 呼び出しのログを見つける
            call_match = re.match(r'(\w+) was called.', line)
            if call_match:
                function_name = call_match.group(1)
                if function_name in call_counts_df['function_name'].values:
                    call_counts_df.loc[call_counts_df['function_name'] == function_name, 'call_count'] += 1
                else:
                    new_row = pd.DataFrame({'function_name': [function_name], 'call_count': [1]})
                    call_counts_df = pd.concat([call_counts_df, new_row], ignore_index=True)
            # 実行時間のログを見つける
            time_match = re.match(r'(\w+) took (\d+\.\d+) milliseconds to run.', line)
            if time_match:
                function_name, exec_time = time_match.groups()
                new_row = pd.DataFrame({'function_name': [function_name], 'execution_time': [float(exec_time)]})
                execution_times_df = pd.concat([execution_times_df, new_row], ignore_index=True)

    # 呼び出し回数のグラフを作成
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.bar(call_counts_df['function_name'], call_counts_df['call_count'])
    plt.title('Function call counts')
    plt.xlabel('Function name')
    plt.ylabel('Count')
    
    # 実行時間のグラフを作成
    plt.subplot(1, 2, 2)
    for function_name in execution_times_df['function_name'].unique():
        plt.plot(execution_times_df[execution_times_df['function_name'] == function_name]['execution_time'].values, 
                 label=function_name, marker=next(markers))
    plt.title('Function execution times')
    plt.xlabel('Call number')
    plt.ylabel('Execution time (ms)')
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    file_name = input()
    analyze_logs(filename=file_name)
