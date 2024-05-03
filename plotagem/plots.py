from plotagem.logs import (
    vbox,
    kvm,
    xen,
    dock_antigo,
    dock_novo,
    pod
)
from plotagem.plot_graficos import plot
from plotagem.plot_fragmentacao import fragmentacao


# ------------------------------------------------ VIRTUALIZADORES ------------------------------------------- #
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


# ------------------------------------------------ CONTAINERS ------------------------------------------- #
def docker_antigo():
    fragmentacao()
    
    # plot(
    #     title="runs",
    #     filename=dock_antigo['runs'], 
    #     ylabel='(stats)',
    #     dayfirst=True, includeColYlabel=True
    # )
    
    plot(
        title="CPU",
        filename=dock_antigo['cpu'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )

    plot(
        title="Disk", 
        filename=dock_antigo['disk'], 
        ylabel='Disk usage (GB)', 
        dayfirst=True, division=1048576
    )

    plot(
        title="Zumbis", 
        filename=dock_antigo['process'], 
        ylabel='Zumbis processes(qtt)', 
        dayfirst=True
    )

    plot(
        title="Memory", 
        filename=dock_antigo['memory'], 
        ylabel='(MB)', 
        dayfirst=True, 
        division=1024, includeColYlabel=True
    )
    
    plot(
        title="nginx",
        filename=dock_antigo['nginx'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )
    
    plot(
        title="postgres",
        filename=dock_antigo['postgres'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )
    
    plot(
        title="rabbitmq",
        filename=dock_antigo['rabbitmq'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )
    
    plot(
        title="redis",
        filename=dock_antigo['redis'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )
    
    plot(
        title="docker_antigo",
        filename=dock_antigo['docker_antigo'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )


def docker_novo():
    fragmentacao()
    
    plot(
        title="runs",
        filename=dock_novo['runs'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )
    
    plot(
        title="CPU",
        filename=dock_novo['cpu'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )

    plot(
        title="Disk", 
        filename=dock_novo['disk'], 
        ylabel='Disk usage (GB)', 
        dayfirst=True, division=1048576
    )

    plot(
        title="Zumbis", 
        filename=dock_novo['process'], 
        ylabel='Zumbis processes(qtt)', 
        dayfirst=True
    )

    plot(
        title="Memory", 
        filename=dock_novo['memory'], 
        ylabel='(MB)', 
        dayfirst=True, 
        division=1024, includeColYlabel=True
    )
    
    plot(
        title="nginx",
        filename=dock_novo['nginx'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )
    
    plot(
        title="postgres",
        filename=dock_novo['postgres'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )
    
    plot(
        title="rabbitmq",
        filename=dock_novo['rabbitmq'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )
    
    plot(
        title="redis",
        filename=dock_novo['redis'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )
    
    plot(
        title="docker_novo",
        filename=dock_novo['docker_novo'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )


def podman():
    fragmentacao()
    
    plot(
        title="runs",
        filename=pod['runs'], 
        ylabel='(percentage)', 
        dayfirst=True, includeColYlabel=True
    )
    
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