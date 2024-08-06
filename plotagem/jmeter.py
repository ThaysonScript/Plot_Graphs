import matplotlib.pyplot as plt
import pandas as pd
import re

# Função para extrair informações de resumo do log
def extract_summary_from_log(log_lines):
    summaries = []
    for line in log_lines:
        match = re.match(r'(\d+-\d+-\d+ \d+:\d+:\d+,\d+) INFO o\.a\.j\.r\.Summariser: summary \+ +(\d+) in \d+:\d+:\d+ = +([\d,]+/s) Avg: +(\d+) Min: +(\d+) Max: +(\d+) Err: +(\d+) \(([\d,]+%)\) Active: +(\d+) Started: +(\d+) Finished: +(\d+)', line)
        if match:
            timestamp, count, rate, avg, min_, max_, err, err_pct, active, started, finished = match.groups()
            summaries.append({
                'Timestamp': timestamp,
                'Count': int(count),
                'Rate': str(rate.replace(',', '.')),  # substitui vírgula por ponto para converter para float
                'Avg': int(avg),
                'Min': int(min_),
                'Max': int(max_),
                'Err': int(err),
                'Err_pct': str(err_pct.replace(',', '.')),  # substitui vírgula por ponto para converter para float
                'Active': int(active),
                'Started': int(started),
                'Finished': int(finished)
            })
    return summaries

# Caminho do arquivo de log
log_file_path = './registros de monitoramento dos testes de envelhecimento/logs-teastore/logs-jmeter-yes-wait/jmeter.log'

# Leitura do arquivo de log
with open(log_file_path, 'r') as file:
    log_lines = file.readlines()

# Extração das informações de resumo
summaries = extract_summary_from_log(log_lines)

# Conversão para DataFrame
df = pd.DataFrame(summaries)

# Exibição do DataFrame
print(df)





# Configurações de plotagem
plt.figure(figsize=(10, 6))

# Plotando Avg, Min, Max
plt.plot(df['timestamp'], df['avg'], label='Avg')
plt.plot(df['timestamp'], df['min'], label='Min')
plt.plot(df['timestamp'], df['max'], label='Max')

# Adicionando título e legendas
plt.title('JMeter Test Summary')
plt.xlabel('Timestamp')
plt.ylabel('Response Time (ms)')
plt.legend()

# Mostrar o gráfico
plt.show()
