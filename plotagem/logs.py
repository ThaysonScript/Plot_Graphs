NAME = 'docker_antigo/ubuntu24/docker_new_debian_new'
PASTA_LOGS = f'./plotagem/registros de monitoramento dos testes de envelhecimento/testes_pre_finais/{NAME}'

NAME_FORMAT = 'frag_' + NAME.replace('/', '_')

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
        f'{PASTA_LOGS}/vbox_monitoring-VBoxXPCOMIPCD.csv',
    
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
        
    'disk':
        f'{PASTA_LOGS}/disk.csv',
        
    'memory':
        f'{PASTA_LOGS}/memory.csv',
        
    'process':
        f'{PASTA_LOGS}/process.csv',
        
    # ------------------- SERVICES PROCESS
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
}

# vs 26
dock_novo = {
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
        
    # ------------------- SERVICES PROCESS
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
        
    # ------------------- SERVICES PROCESS
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
    
    'java':
        f'{PASTA_LOGS}/java.csv'
}