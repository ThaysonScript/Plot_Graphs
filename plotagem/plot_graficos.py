try:
    from logs import vbox, kvm, xen, pod
    from plot_fragmentacao import fragmentacao
    import matplotlib.pyplot as plt
    import pandas as pd
    import scipy.stats as stats
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


def vbox_plots():
    fragmentacao()
    
    plot(
    title="CPU",
    filename=vbox['monitoring_cpu'], 
    ylabel='(percentage)', 
    dayfirst=True, includeColYlabel=True
    )

    plot(
        title="Disk", 
        filename=vbox['monitoring_disks'], 
        ylabel='Disk usage (GB)', 
        dayfirst=True, division=1048576
    )

    plot(
        title="Zumbis", 
        filename=vbox['monitoring_zumbies'], 
        ylabel='Zumbis processes(qtt)', 
        dayfirst=True
    )

    plot(
        title="Memory", 
        filename=vbox['monitoring_mem'], 
        ylabel='(MB)', 
        dayfirst=True, 
        division=1024, includeColYlabel=True
    )

    plot(
        title="Process - VBoxHeadless", 
        filename=vbox['monitoring_VboxHeadless'], 
        cols_to_divide=["vmrss","vsz","swap"],
        ylabel={
            'cpu': 'CPU usage (percentage)',
            "vmrss": "Physical memory usage(MB)",
            "vsz": "Virtual memory usage (MB)",
            "swap": "Swap used(MB)",
            'mem': 'Memory usage (percentage)',
            "thread": "Number of threads(qtt)"
        },
        division=1024, dayfirst=True
    )

    plot(
        title="Process - VBoxSVC", 
        filename=vbox['monitoring_VboxSvc'], 
        cols_to_divide=["vmrss","vsz","swap"],
        ylabel={
            'cpu': 'CPU usage (percentage)',
            "vmrss": "Physical memory usage(MB)",
            "vsz": "Virtual memory usage (MB)",
            "swap": "Swap used(MB)",
            'mem': 'Memory usage (percentage)'
        },
        division=1024, dayfirst=True
    )

    plot(
        title="Process - VBoxXPCOMIPCD", 
        filename=vbox['monitoring_VboxXPCOMIPCD'], 
        cols_to_divide=["vmrss", "vsz", "swap"],
        ylabel={
            'cpu': 'CPU usage (percentage)',
            "vmrss": "Physical memory usage(MB)",
            "vsz": "Virtual memory usage (MB)",
            "swap": "Swap used(MB)",
            'mem': 'Memory usage (percentage)'
        },
        division=1024, dayfirst=True
    )

    plot(
        title="Server response time", 
        filename=vbox['server_response_time_monitoring'], 
        ylabel='Response time(s)', 
        division=1000, dayfirst=True
    )
    
    
def kvm_plots():
    fragmentacao()
    
    plot(
    title="CPU",
    filename=kvm['monitoring_cpu'], 
    ylabel='(percentage)', 
    dayfirst=True, includeColYlabel=True
    )

    plot(
        title="Disk", 
        filename=kvm['monitoring_disks'], 
        ylabel='Disk usage (GB)', 
        dayfirst=True, division=1048576
    )

    plot(
        title="Zumbis", 
        filename=kvm['monitoring_zumbies'], 
        ylabel='Zumbis processes(qtt)', 
        dayfirst=True
    )

    plot(
        title="Memory", 
        filename=kvm['monitoring_mem'], 
        ylabel='(MB)', 
        dayfirst=True, 
        division=1024, includeColYlabel=True
    )

    plot(
        title="Server response time", 
        filename=kvm['server_response_time_monitoring'], 
        ylabel='Response time(s)', 
        division=1000, dayfirst=True
    )
    
    plot(
        title="Process - kvmHeadless", 
        filename=kvm['kvm_Headless'], 
        cols_to_divide=["vmrss","vsz","swap"],
        ylabel={
            'cpu': 'CPU usage (percentage)',
            "vmrss": "Physical memory usage(MB)",
            "vsz": "Virtual memory usage (MB)",
            "swap": "Swap used(MB)",
            'mem': 'Memory usage (percentage)',
            "thread": "Number of threads(qtt)"
        },
        division=1024, dayfirst=True
    )

    plot(
        title="Process - kvm_libvirt_service", 
        filename=kvm['kvm_libvirtd_service'], 
        cols_to_divide=["vmrss","vsz","swap"],
        ylabel={
            'cpu': 'CPU usage (percentage)',
            "vmrss": "Physical memory usage(MB)",
            "vsz": "Virtual memory usage (MB)",
            "swap": "Swap used(MB)",
            'mem': 'Memory usage (percentage)'
        },
        division=1024, dayfirst=True
    )

    

def xen_plots():
    fragmentacao()
    
    plot(
    title="CPU",
    filename=xen['monitoring_cpu'], 
    ylabel='(percentage)', 
    dayfirst=True, includeColYlabel=True
    )

    plot(
        title="Disk", 
        filename=xen['monitoring_disks'], 
        ylabel='Disk usage (GB)', 
        dayfirst=True, division=1048576
    )

    plot(
        title="Zumbis", 
        filename=xen['monitoring_zumbies'], 
        ylabel='Zumbis processes(qtt)', 
        dayfirst=True
    )

    plot(
        title="Memory", 
        filename=xen['monitoring_mem'], 
        ylabel='(MB)', 
        dayfirst=True, 
        division=1024, includeColYlabel=True
    )

    plot(
        title="Server response time", 
        filename=xen['server_response_time_monitoring'], 
        ylabel='Response time(s)', 
        division=1000, dayfirst=True
    ) 
    
    plot(
        title="Process - xen_monitoring_oxenstored", 
        filename=xen['xen_monitoring_oxenstored'], 
        cols_to_divide=["rss","vsz","swap"],
        ylabel={
            'cpu': 'CPU usage (percentage)',
            "rss": "Physical memory usage(MB)",
            "vsz": "Virtual memory usage (MB)",
            "swap": "Swap used(MB)",
            'mem': 'Memory usage (percentage)',
            "thread": "Number of threads(qtt)"
        },
        division=1024, dayfirst=True
    )

    plot(
        title="Process - xen_monitoring_xen_balloon", 
        filename=xen['xen_monitoring_xen_balloon'], 
        cols_to_divide=["rss","vsz","swap"],
        ylabel={
            'cpu': 'CPU usage (percentage)',
            "rss": "Physical memory usage(MB)",
            "vsz": "Virtual memory usage (MB)",
            "swap": "Swap used(MB)",
            'mem': 'Memory usage (percentage)'
        },
        division=1024, dayfirst=True
    )
    
    plot(
        title="Process - xen_monitoring_xenbus", 
        filename=xen['xen_monitoring_xenbus'], 
        cols_to_divide=["rss","vsz","swap"],
        ylabel={
            'cpu': 'CPU usage (percentage)',
            "rss": "Physical memory usage(MB)",
            "vsz": "Virtual memory usage (MB)",
            "swap": "Swap used(MB)",
            'mem': 'Memory usage (percentage)',
            "thread": "Number of threads(qtt)"
        },
        division=1024, dayfirst=True
    )

    plot(
        title="Process - xen_monitoring_xenconsoled", 
        filename=xen['xen_monitoring_xenconsoled'], 
        cols_to_divide=["rss","vsz","swap"],
        ylabel={
            'cpu': 'CPU usage (percentage)',
            "rss": "Physical memory usage(MB)",
            "vsz": "Virtual memory usage (MB)",
            "swap": "Swap used(MB)",
            'mem': 'Memory usage (percentage)'
        },
        division=1024, dayfirst=True
    )

def lxc_plots():
    fragmentacao()
    pass

def docker():
    fragmentacao()
    pass

def podman():
    fragmentacao()
    
    plot(
        title="CPU",
        filename=pod['cpu'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )

    plot(
        title="Disk", 
        filename=pod['disk'], 
        ylabel='Disk usage (GB)', 
        dayfirst=True, division=1048576
    )

    plot(
        title="Zumbis", 
        filename=pod['process'], 
        ylabel='Zumbis processes(qtt)', 
        dayfirst=True
    )

    plot(
        title="Memory", 
        filename=pod['memory'], 
        ylabel='(MB)', 
        dayfirst=True, 
        division=1024, includeColYlabel=True
    )
    
    plot(
        title="nginx",
        filename=pod['nginx'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )
    
    plot(
        title="postgres",
        filename=pod['postgres'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )
    
    plot(
        title="rabbitmq",
        filename=pod['rabbitmq'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )
    
    plot(
        title="redis",
        filename=pod['redis'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )
    
    plot(
        title="runs",
        filename=pod['runs'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )
    
    plot(
        title="conmon",
        filename=pod['conmon'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )
    
    plot(
        title="podman",
        filename=pod['podman'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )
    
    plot(
        title="java",
        filename=pod['java'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )    


def main():
    fragmentacao()
    
    # print('Altere primeiro o arquivo logs.py\n')
    # input('Digite qualquer coisa para continuar _')
    # print('---------------- VIRTUALIZADORES ----------------')
    # print('Digite [1] para vbox')
    # print('Digite [2] para kvm')
    # print('Digite [3] para xen')
    # print('Digite [4] para lxc')
    # print('----------------- CONTAINERS --------------------')
    # print('Digite [5] para docker')
    # print('Digite [6] para podman')
    
    tipo_virtualizador_plots = 7 # int(input('Escolha: '))

    if tipo_virtualizador_plots == 1:
        vbox_plots()
        
    elif tipo_virtualizador_plots == 2:
        kvm_plots()
        
    elif tipo_virtualizador_plots == 3:
        xen_plots()
        
    elif tipo_virtualizador_plots == 4:
        lxc_plots()
        
    elif tipo_virtualizador_plots == 5:
        docker()
        
    elif tipo_virtualizador_plots == 6:
        podman()
        
    else:
        print('Escolha uma opção válida!')
        
main()