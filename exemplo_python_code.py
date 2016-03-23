#!/usr/bin/env python
# -*- coding:utf-8 -*- 

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from math import fabs


velocidade_objetivo = Twist();
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=3)

def notificacao(data):
    global velocidade_objetivo
    """
        Codigo de notificacao executado sempre que chega uma leitura da odometria

        Esta leitura chega na variavel data e e'  um objeto do tipo odometria
    """
    # Todo: a partir de uma leitura da odometria faça
    # um publish na velocidade até que o robô tenha andado 2 metros
    
    velocidade_objetivo = Twist()
    distancia = data.ranges[0]
    if distancia > 0.4:
        velocidade_objetivo.linear.x = distancia/5
        velocidade_objetivo.linear.y = 0
        velocidade_objetivo.linear.z = 0


def controle():
    """
        Função inicial do programa
    """
    rospy.init_node('Exemplo_Python')
    rospy.Subscriber("/stable_scan", LaserScan, notificacao)
    # Initial movement.    
    #pub.publish(velocidade_objetivo)
    while not rospy.is_shutdown():
        pub.publish(velocidade_objetivo)
        rospy.sleep(0.2)


if __name__ == '__main__':
    try:
        controle()
    except rospy.ROSInterruptException:
        pass
