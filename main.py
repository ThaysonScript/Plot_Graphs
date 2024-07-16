from plotagem.plots import (
        vbox_plots,
        kvm_plots,
        xen_plots,
        lxc_plots,
        docker_antigo,
        docker_novo,
        podman
    )


plots_mapping = {
    1: vbox_plots,
    2: kvm_plots,
    3: xen_plots,
    4: lxc_plots,
    5: docker_antigo,
    6: docker_novo,
    7: podman
}


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
    

def get_user_choice():
    try:
        return int(input('Escolha: '))
    
    except ValueError as e:
        return print(f'erro gerado {e}')


def main():
    prints_usage()
    
    user_choice = get_user_choice()
    
    if user_choice in plots_mapping:
        plots_mapping[user_choice]
    else:
        print('Escolha uma opção válida!')

if __name__ == '__main__':
    main()