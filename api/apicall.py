from jnpr.junos import Device
from pprint import pprint

dev = Device(host=None,
             user=None,
             passwd=None,
             port=None)

dev.open()
pprint(dev.facts)
dev.close()
