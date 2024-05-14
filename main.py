from plotagem.plots import (
        vbox_plots,
        kvm_plots,
        xen_plots,
        lxc_plots,
        docker_antigo,
        docker_novo,
        podman
    )

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