try:
    import sys
    import pandas as pd
    from plotagem.logs import PASTA_LOGS, NAME_FORMAT
    pasta_logs = f'{PASTA_LOGS}/fragmentation.csv'
    
except ImportError as e:
    print(f'Erro de importação: {e}')
    sys.exit(1)


def definir_ciclos(df, col):
    indices_ciclo = df.index[df[f'{col}'] == '>>> Emptied array'].tolist()
    
    dataframes = list()

    for i in range(len(indices_ciclo)):
        if i == 0:         
            df1 = df.iloc[:indices_ciclo[0]].reset_index(drop=True)
            dataframes.append(df1)
            
        else:
            df2 = df.iloc[(indices_ciclo[i - 1] + 1):indices_ciclo[i]].reset_index(drop=True)
            dataframes.append(df2)
    
    df_final = df.iloc[(indices_ciclo[-1] + 1):].reset_index(drop=True)
    dataframes.append(df_final)

    return dataframes

def quantidade_processos_manual(dataframes, i, manual=False):
    if manual == False:
        return None
    
    docker_antigo = [150, 100, 100]
    docker_novo = [80, 40, 40]
    podman = [500, 500, 25]
    
    if i == 0:
        df_filtered = dataframes[dataframes['process_occurrences'] >= docker_antigo[0]]
    
    elif i == 1:
        df_filtered = dataframes[dataframes['process_occurrences'] >= docker_antigo[1]]
        
    else:
        df_filtered = dataframes[dataframes['process_occurrences'] >= docker_antigo[2]]
    
    df_pivot = df_filtered.pivot(columns='process', values='process_occurrences')

    ax = df_pivot.plot(ylabel=f'Process occurrences (qtt) - ciclo_{i + 1}', xlabel='Time(H)')

    # Save the figure
    fig = ax.get_figure()
    fig.savefig(f'./plotagem/plot_images/{NAME_FORMAT}_ciclo_{i + 1}.png')


def analisar_ciclos(df, minimum_process_occurrences, analisar=False, processo_manual=False):
    if analisar == False:
        return None
    
    dataframes = definir_ciclos(df, 'process')
    
    for i in range(len(dataframes)):
        dataframes[i]['datetime'] = pd.to_datetime(dataframes[i]['datetime'])
        
        dataframes[i] = dataframes[i].groupby([pd.Grouper(key='datetime', freq='H'), 'process']).agg({
            'parent': 'first',  
            'UID': 'first',     
            'process_occurrences': 'sum',  
            'fragmented': 'first',           
        }).reset_index()

        if not dataframes[i].empty:
            # Set the index to the datetime column
            dataframes[i] = dataframes[i].set_index('datetime')

            dataframes[i]['time_passed'] = (dataframes[i].index - dataframes[i].index[0]).total_seconds() / 3600

            # Resetting the index to use 'time_passed' as index
            dataframes[i] = dataframes[i].set_index('time_passed')

            df_filtered = dataframes[i][dataframes[i]['process_occurrences'] >= minimum_process_occurrences]

            if processo_manual == True:
                quantidade_processos_manual(dataframes[i], i, processo_manual)
                
            else:
                df_pivot = df_filtered.pivot(columns='process', values='process_occurrences')

                ax = df_pivot.plot(ylabel=f'Process occurrences (qtt) - ciclo_{i + 1}', xlabel='Time(H)')

                # Save the figure
                fig = ax.get_figure()
                fig.savefig(f'./plotagem/plot_images/{NAME_FORMAT}_ciclo_{i + 1}.png')

    sys.exit(1)