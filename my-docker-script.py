import docker
from docker import Client
from docker import utils
from docker.utils import kwargs_from_env
import os, time, subprocess



def attach_to_docker_client():
    if os.getenv('DOCKER_HOST') == 'tcp://192.168.59.103:2376':
        c = Client(**kwargs_from_env(assert_hostname=False))
    else:
        c = Client()
    return c

c = attach_to_docker_client()

images = c.images()

#print(images)

# for image in images:
#     if image["RepoTags"] == ["twordpress:latest"]:
#         wp_image_id = image["Id"]
#         print(wp_image_id)



# container = c.create_container(image="twordpress:latest",
#                                volumes=['/mnt/vol1'],
#                                name="twordpress_foo7",
#                                ports=[80],
#                                host_config=docker.utils.create_host_config(port_bindings={
#                                    80:80,
#                                    },
#                                                                            binds={'/app/': {
#             'bind': '/app/',
#             'mode': 'rw',}}))



wp_container = c.create_container(image="twordpress:latest",
                               volumes=['mnt/vol1', '/mnt/vol2'],
                               name="twordpress_foo8",
                               ports=[80],
                               host_config=docker.utils.create_host_config(port_bindings={
                                   80:80,
                                   }))

container = c.create_container(image='thedhbox/seed:latest',
                               name='dhbox_container',
                               ports=[8080, 8787, 4444, 4200],
                               tty=True, stdin_open=True)

c.start('twordpress_foo8')
c.start('dhbox_container',volumes_from='twordpress_foo8')
