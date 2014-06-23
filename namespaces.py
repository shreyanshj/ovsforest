#!/usr/bin/python

from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def ovsns():

    "Create an empty network and add nodes to it."

    net = Mininet( topo=None,
                   build=False)

    h1 = net.addHost( 'h1')
    s11 = net.addSwitch( 's11')
    s22 = net.addSwitch( 's22' )
    h2 = net.addHost( 'h2' )

#    net.addLink( h1, s1 )
#    net.addLink( s1, s2 )
#    net.addLink( h2, s2 )

    net.start()
    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'debug' )
    ovsns()
