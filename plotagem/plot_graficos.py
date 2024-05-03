try:
    import matplotlib.pyplot as plt
    import pandas as pd
    from sklearn.linear_model import LinearRegression
    
except ImportError as e:
    print(f'Erro de importação: {e}')
    exit(1)

plt.close('all')


def plot(filename, ylabel, datetime="date_time", title=None, separator=';', decimal_separator=",", dayfirst=False, division=1, includeColYlabel=False, cols_to_divide=[]):
    try:
        df = pd.read_csv(filename, sep=separator, decimal=decimal_separator, dayfirst=dayfirst, parse_dates=[datetime]).rename(columns={datetime: 'seconds'})
        
        # df['seconds'] = pd.to_datetime(df['seconds'], format='%d-%m-%Y-%H:%M:%S')
        df['seconds'] = df['seconds'].apply(lambda x: pd.to_datetime(x, format="%d-%m-%Y-%H:%M:%S"))

        df['seconds'] = (df['seconds'] - df['seconds'][0]).dt.total_seconds() / 3600
        df = df.set_index('seconds').replace(',', '.', regex=True).apply(lambda x: pd.to_numeric(x, errors='ignore'))
        
        cols_to_divide = cols_to_divide if len(cols_to_divide) != 0 else df.columns
        df[cols_to_divide] = df[cols_to_divide].div(division)

    except ValueError:
        print("Ignorando linha devido a data incorreta.")

    for col in df.columns:
        
        try:
            col_mix = col + " " + ylabel if type(ylabel) is str and includeColYlabel else ylabel

            df[col] = df[col].fillna(0)

            x = df.index.to_numpy().reshape((-1, 1))
            y = df[col].to_numpy().reshape((-1, 1))

            model = LinearRegression()
            model.fit(x, y)

            Y_pred = model.predict(x)

            ax = df.plot(
                y=col,
                legend=0,
                xlabel='Time(h)',
                ylabel=col_mix if type(ylabel) is str else ylabel[col] if type(ylabel) is dict and col in ylabel else col,
                title=title if type(title) is str else title[col] if type(title) is dict and col in title else col,
                figsize=(10,5),
                style='k',
            )

            # Adicionar a linha da regressão
            ax.plot(x, Y_pred, color='red')
            plt.show()
            fig = ax.get_figure()
            fig.savefig(f'./plot_images/{title}-{col}.png')
            
        except ValueError:
            print(f"Ignorando coluna '{col}' devido a erro na conversão para float.")   