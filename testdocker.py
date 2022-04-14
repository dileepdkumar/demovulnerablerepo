import docker
import os
import time
pwd = os.getcwd()
client = docker.from_env()
client.images.pull('dops-registry.fortinet-us.com/fortidevsecops/fdevsec_sast:latest')

container=client.containers.run('dops-registry.fortinet-us.com/fortidevsecops/fdevsec_sast:latest',remove=False,extra_hosts={'qa.fortidevsec.forticloud.com':'10.34.160.14'},volumes={pwd : {'bind': '/scan', 'mode': 'rw'}},detach=True)

#str1=container.logs();
#print(str1)
for line in container.logs(stdout=True,stderr=True,follow=True,stream=True):
    line=line.decode("utf-8")
    print(line.strip())

#print(container.attrs)

container.stop()
container.remove(force=True)
