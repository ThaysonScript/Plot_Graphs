try:
    import pandas as pd
    from plotagem.logs import PASTA_LOGS, NAME_FORMAT
    
except ImportError as e:
    print(f'Erro de importação: {e}')
    exit(1)

pasta_logs = f'{PASTA_LOGS}/fragmentation.csv'
minimum_process_occurrences = 15

def fragmentacao():        
    # Read the CSV file into a DataFrame
    df = pd.read_csv(pasta_logs, delimiter=';')

    # Convert the datetime column to a datetime object
    df['datetime'] = pd.to_datetime(df['datetime'])

    # Set the index to the datetime column
    df = df.set_index('datetime')

    df['time_passed'] = (df.index - df.index[0]).total_seconds() / 3600

    # Resetting the index to use 'time_passed' as index
    df = df.set_index('time_passed')

    df_filtered = df[df['process_occurrences'] >= minimum_process_occurrences]

    df_pivot = df_filtered.pivot(columns='process', values='process_occurrences')
    ax = df_pivot.plot(ylabel='Process occurrences', xlabel='Time(H)')

    # Save the figure
    fig = ax.get_figure()
    # fig.savefig(f'./plot_images/fragmentation.png')
    fig.savefig(f'./plotagem/plot_images/{NAME_FORMAT}.png')
