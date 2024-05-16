try:
    import matplotlib.pyplot as plt
    import pandas as pd
    from sklearn.linear_model import LinearRegression
    from pathlib import Path
    import pandas as pd
    # NAME = 'docker_new_debian_new'
    # NAME = 'docker_old_ubuntu_old'
    NAME = 'podman_new_ubuntu_new'
    NAME = 'logs_com_disco_1gb'
    PASTA_LOGS = f'./plotagem/registros de monitoramento dos testes de envelhecimento/virtualbox/{NAME}'
    NAME_FORMAT = 'frag_' + NAME.replace('/', '_')
    
except ImportError as e:
    print(f'Erro de importação: {e}')
    exit(1)

MINIMUM_PROCESS_OCCURRENCES :int = 1

dir1 = Path("plotagem/plot_images")
dir2 = Path("plotagem/registros de monitoramento dos testes de envelhecimento")

if not dir1.exists():
    dir1.mkdir()
    print("Diretório 1 criado com sucesso.")
else:
    print('verificação de diretorio 1 feita')
    
if not dir2.exists():
    dir2.mkdir()
    print("Diretório 2 criado com sucesso.")
    
else:
    print('verificação de diretorio 2 feita\n')
    

vbox = {
    'monitoring_cpu':
        f'{PASTA_LOGS}/machine_monitoring-cpu.csv',
        
    'monitoring_disks':
        f'{PASTA_LOGS}/machine_monitoring-disk.csv',
    
    'monitoring_zumbies':
        f'{PASTA_LOGS}/machine_monitoring-zombies.csv',
    
    'monitoring_mem':
        f'{PASTA_LOGS}/machine_monitoring-mem.csv',
        
    'machineHost_server_status':
        f'{PASTA_LOGS}/machineHost_server_status.csv',
        
    'reset_times':
        f'{PASTA_LOGS}/reset_times.csv',
    
    'server_response_time_monitoring':
        f'{PASTA_LOGS}/response_times.csv',
        
    'monitoring_VboxHeadless':
        f'{PASTA_LOGS}/vbox_monitoring-VBoxHeadless.csv',
    
    'monitoring_VboxSvc':
        f'{PASTA_LOGS}/vbox_monitoring-VBoxSVC.csv',
    
    'monitoring_VboxXPCOMIPCD':
        f'{PASTA_LOGS}/vbox_monitoring-VBoxXPCOMIPCD.csv'
}

kvm = {
    'monitoring_cpu':
        f'{PASTA_LOGS}/machine_monitoring-cpu.csv',
        
    'monitoring_disks':
        f'{PASTA_LOGS}/machine_monitoring-disk.csv',
    
    'monitoring_zumbies':
        f'{PASTA_LOGS}/machine_monitoring-zombies.csv',
    
    'monitoring_mem':
        f'{PASTA_LOGS}/machine_monitoring-mem.csv',
        
    'machineHost_server_status':
        f'{PASTA_LOGS}/machineHost_server_status.csv',
        
    'reset_times':
        f'{PASTA_LOGS}/reset_times.csv',
    
    'server_response_time_monitoring':
        f'{PASTA_LOGS}/response_times.csv',
        
    'kvm_Headless':
        f'{PASTA_LOGS}/kvm_Headless_monitoring.csv',
    
    'kvm_libvirtd_service':
        f'{PASTA_LOGS}/kvm_libvirtd_service_monitoring.csv'
}

xen = {
    'monitoring_cpu':
        f'{PASTA_LOGS}/machine_monitoring-cpu.csv',
        
    'monitoring_disks':
        f'{PASTA_LOGS}/machine_monitoring-disk.csv',
    
    'monitoring_zumbies':
        f'{PASTA_LOGS}/machine_monitoring-zombies.csv',
    
    'monitoring_mem':
        f'{PASTA_LOGS}/machine_monitoring-mem.csv',
        
    'machineHost_server_status':
        f'{PASTA_LOGS}/machineHost_server_status.csv',
        
    'reset_times':
        f'{PASTA_LOGS}/reset_times.csv',
    
    'server_response_time_monitoring':
        f'{PASTA_LOGS}/response_times.csv',
        
    'xen_monitoring_oxenstored':
        f'{PASTA_LOGS}/xen_monitoring-oxenstored.csv',
    
    'xen_monitoring_xen_balloon':
        f'{PASTA_LOGS}/xen_monitoring-xen-balloon.csv',
        
        
    'xen_monitoring_xenbus':
        f'{PASTA_LOGS}/xen_monitoring-xenbus.csv',
    
    'xen_monitoring_xenconsoled':
        f'{PASTA_LOGS}/xen_monitoring-xenconsoled.csv'
}

# vs 20
dock_antigo = {
    # RUNS
    'runs':
        f'{PASTA_LOGS}/runs.csv',
        
    # --------------------- MACHINE PROCESS
    'cpu':
        f'{PASTA_LOGS}/cpu.csv',
        
    'memory':
        f'{PASTA_LOGS}/memory.csv',
        
    'disk':
        f'{PASTA_LOGS}/disk.csv',
        
    'process':
        f'{PASTA_LOGS}/process.csv',
        
    # ------------------- IMAGE PROCESS
    'nginx':
        f'{PASTA_LOGS}/nginx.csv',
        
    'postgres':
        f'{PASTA_LOGS}/postgres.csv',
        
    'rabbitmq':
        f'{PASTA_LOGS}/rabbitmq.csv',
        
    'redis':
        f'{PASTA_LOGS}/redis.csv',
        
    # ------------------- CONTAINER PROCESS
    'docker': 
        f'{PASTA_LOGS}/docker.csv',
        
    'dockerd': 
        f'{PASTA_LOGS}/dockerd.csv',
        
    'containerd': 
        f'{PASTA_LOGS}/containerd.csv',
        
    'containerd-shim': 
        f'{PASTA_LOGS}/containerd-shim.csv',
        
    'docker-proxy': 
        f'{PASTA_LOGS}/docker-proxy.csv',
        
    'runc': 
        f'{PASTA_LOGS}/runc.csv',
        
    'containerd': 
        f'{PASTA_LOGS}/containerd.csv',
        
    'containerd-shim': 
        f'{PASTA_LOGS}/containerd-shim.csv',
        
    'runc': 
        f'{PASTA_LOGS}/runc.csv',
        
    # -------------------- SERVICE PROCESS
    'java': 
        f'{PASTA_LOGS}/java.csv',
        
    'beam.smp': 
        f'{PASTA_LOGS}/beam.smp.csv',
        
    'initdb': 
        f'{PASTA_LOGS}/initdb.csv',
        
    'mysqld': 
        f'{PASTA_LOGS}/mysqld.csv',
        
    'postgres_process': 
        f'{PASTA_LOGS}/postgres_process.csv'
}

# vs 26
dock_novo = {
    # RUNS
    'runs':
        f'{PASTA_LOGS}/runs.csv',
        
    # --------------------- MACHINE PROCESS
    'cpu':
        f'{PASTA_LOGS}/cpu.csv',
        
    'memory':
        f'{PASTA_LOGS}/memory.csv',
        
    'disk':
        f'{PASTA_LOGS}/disk.csv',
        
    'process':
        f'{PASTA_LOGS}/process.csv',
        
    # ------------------- IMAGE PROCESS
    'nginx':
        f'{PASTA_LOGS}/nginx.csv',
        
    'postgres':
        f'{PASTA_LOGS}/postgres.csv',
        
    'rabbitmq':
        f'{PASTA_LOGS}/rabbitmq.csv',
        
    'redis':
        f'{PASTA_LOGS}/redis.csv',
        
    # ------------------- CONTAINER PROCESS
    'docker': 
        f'{PASTA_LOGS}/docker.csv',
        
    'dockerd': 
        f'{PASTA_LOGS}/dockerd.csv',
        
    'containerd': 
        f'{PASTA_LOGS}/containerd.csv',
        
    'containerd-shim': 
        f'{PASTA_LOGS}/containerd-shim.csv',
        
    'docker-proxy': 
        f'{PASTA_LOGS}/docker-proxy.csv',
        
    'runc': 
        f'{PASTA_LOGS}/runc.csv',
        
    'containerd': 
        f'{PASTA_LOGS}/containerd.csv',
        
    'containerd-shim': 
        f'{PASTA_LOGS}/containerd-shim.csv',
        
    'runc': 
        f'{PASTA_LOGS}/runc.csv',
        
    # -------------------- SERVICE PROCESS
    'java': 
        f'{PASTA_LOGS}/java.csv',
        
    'beam.smp': 
        f'{PASTA_LOGS}/beam.smp.csv',
        
    'initdb': 
        f'{PASTA_LOGS}/initdb.csv',
        
    'mysqld': 
        f'{PASTA_LOGS}/mysqld.csv',
        
    'postgres_process': 
        f'{PASTA_LOGS}/postgres_process.csv'
}

# vs 4.9
pod = {
    # RUNS
    'runs':
        f'{PASTA_LOGS}/runs.csv',
        
    # --------------------- MACHINE PROCESS
    'cpu':
        f'{PASTA_LOGS}/cpu.csv',
        
    'disk':
        f'{PASTA_LOGS}/disk.csv',
        
    'memory':
        f'{PASTA_LOGS}/memory.csv',
        
    'process':
        f'{PASTA_LOGS}/process.csv',
        
    # ------------------- IMAGE PROCESS
    'nginx':
        f'{PASTA_LOGS}/nginx.csv',
        
    'postgres':
        f'{PASTA_LOGS}/postgres.csv',
        
    'rabbitmq':
        f'{PASTA_LOGS}/rabbitmq.csv',
        
    'redis':
        f'{PASTA_LOGS}/redis.csv',
        
    # ------------------- CONTAINER PROCESS
    'podman':
        f'{PASTA_LOGS}/podman.csv',
        
    'conmon':
        f'{PASTA_LOGS}/conmon.csv',
        
    'cron':
        f'{PASTA_LOGS}/cron.csv',
        
    'crun':
        f'{PASTA_LOGS}/crun.csv',
        
    'systemd':
        f'{PASTA_LOGS}/systemd.csv',
    
    # -------------------- SERVICE PROCESS
    'java':
        f'{PASTA_LOGS}/java.csv',
        
    'postgres_process':
        f'{PASTA_LOGS}/postgres_process.csv',
        
    'mysqld':
        f'{PASTA_LOGS}/mysqld.csv',
        
    'initdb':
        f'{PASTA_LOGS}/initdb.csv',
        
    'beam.smp':
        f'{PASTA_LOGS}/beam.smp.csv'
}
    
    
def plot(
    filename, ylabel, datetime="date_time", title=None, separator=';', 
    decimal_separator=",", dayfirst=False, multiply=1, division=1, decimals_quantity=2, 
    includeColYlabel=False, cols_to_divide=[], cols_to_multiply=[]
):
    try:
        df = pd.read_csv(filename, sep=separator, decimal=decimal_separator, dayfirst=dayfirst, parse_dates=[datetime]).rename(columns={datetime: 'seconds'})
    
    except ValueError:
        try:
            df = pd.read_csv(filename, sep=separator, decimal=decimal_separator, dayfirst=dayfirst, parse_dates=['time']).rename(columns={'time': 'seconds'})        

        except Exception as e:
            print("Erro ao ler o arquivo CSV:", e)
            return None

    # df['seconds'] = pd.to_datetime(df['seconds'], format='%d-%m-%Y-%H:%M:%S')
    # df['seconds'] = df['seconds'].apply(lambda x: pd.to_datetime(x, format="%d-%m-%Y-%H:%M:%S"))

    df['seconds'] = (df['seconds'] - df['seconds'][0]).dt.total_seconds() / 3600
    df = df.set_index('seconds').replace(',', '.', regex=True).apply(lambda x: pd.to_numeric(x, errors='ignore'))
    
    # perform data multiplication
    cols_to_multiply = cols_to_multiply if len(cols_to_multiply) != 0 else df.columns
    df[cols_to_multiply] = df[cols_to_multiply].mul(multiply)
    
    # perform data division
    cols_to_divide = cols_to_divide if len(cols_to_divide) != 0 else df.columns
    df[cols_to_divide] = df[cols_to_divide].div(division)
        
    for col in df.columns:            
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
        
        ax.yaxis.set_major_formatter('{x:.2f}')

        # Adicionar a linha da regressão
        ax.plot(x, Y_pred, color='red')
        plt.show()
        
        fig = ax.get_figure()
        fig.savefig(f'./plotagem/plot_images/{title}-{col}.png')
        

def fragmentacao(minimum_process_occurrences=1):   
    pasta_logs = f'{PASTA_LOGS}/fragmentation.csv'     
    df = pd.read_csv(pasta_logs, delimiter=';')     # Read the CSV file into a DataFrame
    
    df = df.dropna()        # drop nan column values and emptieds array
    
    # Convert the datetime column to a datetime object
    df['datetime'] = pd.to_datetime(df['datetime'])

    # Set the index to the datetime column
    df = df.set_index('datetime')

    df['time_passed'] = (df.index - df.index[0]).total_seconds() / 3600

    # Resetting the index to use 'time_passed' as index
    df = df.set_index('time_passed')

    df_filtered = df[df['process_occurrences'] >= minimum_process_occurrences]

    df_pivot = df_filtered.pivot(columns='process', values='process_occurrences')
    
    ax = df_pivot.plot(ylabel='Process occurrences (qtt)', xlabel='Time(H)')

    # Save the figure
    fig = ax.get_figure()
    fig.savefig(f'./plotagem/plot_images/{NAME_FORMAT}.png')

# ------------------------------------------------ VIRTUALIZADORES ------------------------------------------- #
def vbox_plots():
    fragmentacao(MINIMUM_PROCESS_OCCURRENCES)
    
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
        dayfirst=True, division=(1024**2)
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
        multiply=1000, dayfirst=True
    )
    
    
def kvm_plots():
    fragmentacao(MINIMUM_PROCESS_OCCURRENCES)
    
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
        dayfirst=True, division=(1024**2)
    )

    plot(
        title="Zumbis", 
        filename=kvm['monitoring_zumbies'], 
        ylabel='Zumbies processes(qtt)', 
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
        cols_to_divide=["rss","vsz","swap"],
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
        filename=kvm['server_response_time_monitoring'], 
        ylabel='Response time (seconds)', 
        multiply=1000, dayfirst=True
    )


def xen_plots():
    fragmentacao(MINIMUM_PROCESS_OCCURRENCES)
    
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
        dayfirst=True, division=(1024**2)
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

    plot(
        title="Server response time", 
        filename=xen['server_response_time_monitoring'], 
        ylabel='Response time (seconds)', 
        multiply=1000, dayfirst=True
    ) 


def lxc_plots():
    fragmentacao(MINIMUM_PROCESS_OCCURRENCES)
    pass


# ------------------------------------------------ CONTAINERS ------------------------------------------- #
def docker_antigo():
    fragmentacao(MINIMUM_PROCESS_OCCURRENCES)
    
    # sys.exit(0)    
    # plot(
    #     title="runs",
    #     filename=dock_novo['runs'], 
    #     ylabel='(percentage)', 
    #     dayfirst=True, includeColYlabel=True
    # )
    
    # --------------------- MACHINE RESOURCES
    plot(
        title="CPU",
        filename=dock_antigo['cpu'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )

    plot(
        title="Memory", 
        filename=dock_antigo['memory'], 
        ylabel='(MB)', 
        dayfirst=True, 
        division=1024, includeColYlabel=True
    )
    
    plot(
        title="Disk", 
        filename=dock_antigo['disk'], 
        ylabel='Disk usage (GB)', 
        dayfirst=True, division=(1024**2)
    )

    plot(
        title="Zumbis", 
        filename=dock_antigo['process'], 
        ylabel='Zumbis processes(qtt)', 
        dayfirst=True
    )

    # -------------------------- CONTAINER PROCESS
    plot(
        title="nginx",
        filename=dock_antigo['nginx'], 
        ylabel='(seconds)', 
        dayfirst=True, includeColYlabel=True,
        division=1e+9
    )
    
    # plot(
    #     title="postgres",
    #     filename=dock_antigo['postgres'], 
    #     ylabel='(seconds)', 
    #     dayfirst=True, includeColYlabel=True,
    #     division=1e+9
    # )
    
    plot(
        title="rabbitmq",
        filename=dock_antigo['rabbitmq'], 
        ylabel='(seconds)', 
        dayfirst=True, includeColYlabel=True,
        division=1e+9
    )
    
    plot(
        title="redis",
        filename=dock_antigo['redis'], 
        ylabel='(seconds)', 
        dayfirst=True, includeColYlabel=True,
        division=1e+9
    )
    
    # ----------------------------- DOCKER PROCESS
    plot(
        title="docker_antigo - process",
        filename=dock_antigo['docker'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    plot(
        title="dockerd_antigo - process",
        filename=dock_antigo['dockerd'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    plot(
        title="containerd_antigo - process",
        filename=dock_antigo['containerd'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    plot(
        title="containerd-shim_antigo - process",
        filename=dock_antigo['containerd-shim'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    plot(
        title="docker-proxy_antigo - process",
        filename=dock_antigo['docker-proxy'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    plot(
        title="runc_novo - process",
        filename=dock_antigo['runc'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    # -------------------------- IMAGE PROCESS
    plot(
        title="java",
        filename=dock_antigo['java'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    # plot(
    #     title="postgres_process",
    #     filename=dock_antigo['postgres_process'], 
    #     ylabel=labels(L_name=GRAPH_NAMES['postgres_process'], metrics='MB'),
    #     dayfirst=True, includeColYlabel=True,
    #     cols_to_divide=['rss', 'vsz', 'swap'],
    #     division=1024
    # )
    
    plot(
        title="beam.smp",
        filename=dock_antigo['beam.smp'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    plot(
        title="mysqld",
        filename=dock_antigo['mysqld'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    # plot(
    #     title="initdb",
    #     filename=dock_antigo['initdb'], 
    #     ylabel=labels(L_name=GRAPH_NAMES['initdb'], metrics='MB'),
    #     dayfirst=True, includeColYlabel=True,
    #     cols_to_divide=['rss', 'vsz', 'swap'],
    #     division=1024
    # )


def docker_novo():
    fragmentacao(MINIMUM_PROCESS_OCCURRENCES)
    
    # sys.exit(0)
    
    # plot(
    #     title="runs",
    #     filename=dock_novo['runs'], 
    #     ylabel='(percentage)', 
    #     dayfirst=True, includeColYlabel=True
    # )
    
    # --------------------- MACHINE RESOURCES
    plot(
        title="CPU",
        filename=dock_novo['cpu'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )

    plot(
        title="Memory", 
        filename=dock_novo['memory'], 
        ylabel='(MB)', 
        dayfirst=True, 
        division=1024, includeColYlabel=True
    )
    
    plot(
        title="Disk", 
        filename=dock_novo['disk'], 
        ylabel='Disk usage (GB)', 
        dayfirst=True, division=(1024**2)
    )

    plot(
        title="Zumbis", 
        filename=dock_novo['process'], 
        ylabel='Zumbis processes(qtt)', 
        dayfirst=True
    )

    # -------------------------- CONTAINER PROCESS
    plot(
        title="nginx",
        filename=dock_novo['nginx'], 
        ylabel='(seconds)', 
        dayfirst=True, includeColYlabel=True,
        division=1e+9
    )
    
    # plot(
    #     title="postgres",
    #     filename=dock_novo['postgres'], 
    #     ylabel='(seconds)', 
    #     dayfirst=True, includeColYlabel=True,
    #     division=1e+9
    # )
    
    plot(
        title="rabbitmq",
        filename=dock_novo['rabbitmq'], 
        ylabel='(seconds)', 
        dayfirst=True, includeColYlabel=True,
        division=1e+9
    )
    
    plot(
        title="redis",
        filename=dock_novo['redis'], 
        ylabel='(seconds)', 
        dayfirst=True, includeColYlabel=True,
        division=1e+9
    )
    
    # ----------------------------- DOCKER PROCESS
    plot(
        title="docker_novo - process",
        filename=dock_novo['docker'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    plot(
        title="dockerd_novo - process",
        filename=dock_novo['dockerd'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    plot(
        title="containerd_novo - process",
        filename=dock_novo['containerd'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    plot(
        title="containerd-shim_novo - process",
        filename=dock_novo['containerd-shim'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    plot(
        title="docker-proxy_novo - process",
        filename=dock_novo['docker-proxy'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    plot(
        title="runc_novo - process",
        filename=dock_novo['runc'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    # -------------------------- IMAGE PROCESS
    plot(
        title="java",
        filename=dock_novo['java'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    # plot(
    #     title="postgres_process",
    #     filename=dock_novo['postgres_process'], 
    #     ylabel=labels(L_name=GRAPH_NAMES['postgres_process'], metrics='MB'),
    #     dayfirst=True, includeColYlabel=True,
    #     cols_to_divide=['rss', 'vsz', 'swap'],
    #     division=1024
    # )
    
    plot(
        title="beam.smp",
        filename=dock_novo['beam.smp'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    plot(
        title="mysqld",
        filename=dock_novo['mysqld'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    # plot(
    #     title="initdb",
    #     filename=dock_novo['initdb'], 
    #     ylabel=labels(L_name=GRAPH_NAMES['initdb'], metrics='MB'),
    #     dayfirst=True, includeColYlabel=True,
    #     cols_to_divide=['rss', 'vsz', 'swap'],
    #     division=1024
    # )


def podman():
    fragmentacao(MINIMUM_PROCESS_OCCURRENCES)
    
    # sys.exit(0)
    
    # plot(
    #     title="runs",
    #     filename=pod['runs'], 
    #     ylabel='(percentage)', 
    #     dayfirst=True, includeColYlabel=True
    # )
    
    # --------------------- MACHINE RESOURCES
    plot(
        title="CPU",
        filename=pod['cpu'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )

    plot(
        title="Memory", 
        filename=pod['memory'], 
        ylabel='(GB)',
        dayfirst=True, 
        division=(1024**2), includeColYlabel=True
    )
    
    plot(
        title="Disk", 
        filename=pod['disk'], 
        ylabel='Disk usage (GB)', 
        dayfirst=True, division=(1024**2)
    )
    
    plot(
        title="Zumbis", 
        filename=pod['process'], 
        ylabel='Zumbis processes(qtt)', 
        dayfirst=True
    )
    
    # -------------------------- CONTAINER PROCESS
    plot(
        title="nginx",
        filename=pod['nginx'], 
        ylabel='(seconds)', 
        dayfirst=True, includeColYlabel=True,
        division=1e+9
    )
    
    # plot(
    #     title="postgres",
    #     filename=pod['postgres'], 
    #     ylabel='(seconds)', 
    #     dayfirst=True, includeColYlabel=True,
    #     division=1e+9
    # )
    
    plot(
        title="rabbitmq",
        filename=pod['rabbitmq'], 
        ylabel='(seconds)', 
        dayfirst=True, includeColYlabel=True,
        division=1e+9
    )
    
    plot(
        title="redis",
        filename=pod['redis'], 
        ylabel='(seconds)', 
        dayfirst=True, includeColYlabel=True,
        division=1e+9
    )
    
    # ----------------------------- PODMAN PROCESS
    plot(
        title="podman",
        filename=pod['podman'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    plot(
        title="conmon",
        filename=pod['conmon'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    # plot(
    #     title="cron",
    #     filename=pod['cron'], 
    #     ylabel=labels(L_name=GRAPH_NAMES['cron'], metrics='MB'),
    #     dayfirst=True, includeColYlabel=True,
    #     cols_to_divide=['rss', 'vsz', 'swap'],
    #     division=1024
    # )
    
    plot(
        title="crun",
        filename=pod['crun'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    plot(
        title="systemd",
        filename=pod['systemd'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    # -------------------------- IMAGE PROCESS
    plot(
        title="java",
        filename=pod['java'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    # plot(
    #     title="postgres_process",
    #     filename=pod['postgres_process'], 
    #     ylabel=labels(L_name=GRAPH_NAMES['postgres_process'], metrics='MB'),
    #     dayfirst=True, includeColYlabel=True,
    #     cols_to_divide=['rss', 'vsz', 'swap'],
    #     division=1024
    # )
    
    plot(
        title="beam.smp",
        filename=pod['beam.smp'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    plot(
        title="mysqld",
        filename=pod['mysqld'], 
        ylabel={
            'cpu': 'CPU usage (percentage)',
            'mem': 'Memory usage (percentage)',
            'rss': 'Physical memory usage(MB)',
            'vsz': 'Virtual memory usage (MB)',
            'threads': 'Number of threads(qtt)',
            'swap': 'Swap used(MB)',
        },
        dayfirst=True, includeColYlabel=True,
        cols_to_divide=['rss', 'vsz', 'swap'],
        division=1024
    )
    
    # plot(
    #     title="initdb",
    #     filename=pod['initdb'], 
    #     ylabel=labels(L_name=GRAPH_NAMES['initdb'], metrics='MB'),
    #     dayfirst=True, includeColYlabel=True,
    #     cols_to_divide=['rss', 'vsz', 'swap'],
    #     division=1024
    # )
    
    
def prints_usage():
    print('Altere primeiro o arquivo logs.py\n')
    input('Digite qualquer coisa para continuar _')
    print('---------------- VIRTUALIZADORES ----------------')
    print('Digite [1] para vbox')
    print('Digite [2] para kvm')
    print('Digite [3] para xen')
    print('Digite [4] para lxc')
    print('\n----------------- CONTAINERS --------------------')
    print('Digite [5] para docker antigo')
    print('Digite [6] para docker novo')
    print('Digite [7] para podman')
    
    return int(input('Escolha: '))

def main():
    tipo_virtualizador_plots = prints_usage()

    if tipo_virtualizador_plots == 1:
        vbox_plots()
        
    elif tipo_virtualizador_plots == 2:
        kvm_plots()
        
    elif tipo_virtualizador_plots == 3:
        xen_plots()
        
    elif tipo_virtualizador_plots == 4:
        lxc_plots()
        
    elif tipo_virtualizador_plots == 5:
        docker_antigo()
        
    elif tipo_virtualizador_plots == 6:
        docker_novo()
        
    elif tipo_virtualizador_plots == 7:
        podman()
        
    else:
        print('Escolha uma opção válida!')

if __name__ == '__main__':
    main()