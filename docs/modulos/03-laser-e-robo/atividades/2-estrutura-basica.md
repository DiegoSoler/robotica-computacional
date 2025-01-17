# Estrutura Básica de um Nó

Para facilitar o desenvolvimento de um nó, a fornecemos uma estrutura básica de um nó da ROS 2 em python. Também fornecemos uma estrutura básica de um nó que controla o robô, incluindo a definição da maquina de estados, a função de controle e o publisher do `cmd_vel`.

* Nó básico: [base.py](../util/base.py)

* Nó básico de controle: [main.py](../util/base_control.py)

Baixe os arquivos e coloque-os na em uma pasta de fácil acesso. 

Agora vamos entender o que cada parte do código faz.

## Nó Básico

Este script não tem nenhuma novidade em relação ao que já foi visto. Quando executado, ele chama a função `control()` a cada 0,25 segundos. Este script é útil para criar um nó que se inscreve em um tópico e executa uma função a cada nova mensagem recebid, publicando uma mensagem em outro tópico.

**Dica:** Será útil para desenvolver módulos de processamento de imagem, onde o nó se inscreve em um tópico de imagem, processa a imagem e publica o resultado em outro tópico.

## Nó Básico de Controle

Neste script, definimos a máquina de estados do robô (no dicionário `self.state_machine`), o estado inicial (no atributo `self.robot_state`) e a função de controle (no método `self.control()`), que a cada 0,25 segundos, executa a função `self.state_machine[self.robot_state]()` e publica a a ação de controle no tópico `cmd_vel` (`self.cmd_vel_pub.publish(self.twist)`).

**Dica:** Em uma máquina de estados bem definida, a função de controle não precisa ser alterada, sendo ela a única função que publica no tópico `cmd_vel`.