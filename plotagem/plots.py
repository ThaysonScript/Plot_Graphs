import sys
from plotagem.plot_graficos import plot
from plotagem.plot_fragmentacao import fragmentacao
from pathlib import Path
from plotagem.logs import (
    vbox,
    kvm,
    xen,
    dock_antigo,
    dock_novo,
    pod
)

MINIMUM_PROCESS_OCCURRENCES :int = 10

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
    
    # sys.exit(1)
    
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
    
    # sys.exit(1)
    
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