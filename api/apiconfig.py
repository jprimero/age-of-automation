from jnpr.junos import Device
from jnpr.junos.utils.config import Config

dev = Device(host=None,
             user=None,
             passwd=None,
             port=None)
    
dev.open()
print('configuring device:',dev.hostname)

with Config(dev) as conf:
    conf.load(template_path='configtemplate.set',
              template_vars={'interface':None,
                             'unit':'0',
                             'ip_address':None},
              merge=True)
    conf.pdiff()
    conf.commit()

dev.close()
