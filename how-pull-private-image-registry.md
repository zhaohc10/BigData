### How config for pull image from hw registry
```
mkdir -p ~/.docker
vi config.json
# past the content of the file download from cce (like follow one)
{"auths":{"117.78.33.214":{"auth":"<***>==","email":""}}}
```
on ubuntu
```
vi /etc/default/docker
# modify following line
DOCKER_OPTS="--insecure-registry 172.**.**.**"
# restart docker service
service docker restart
```
on CentOS
```
vi /usr/lib/systemd/system/docker.service
# modify following line
ExecStart=/usr/bin/docker daemon -H fd:// --insecure-registry 172.**.**.**
# restart docker service
systemctl daemon-reload
service docker restart

```
on coreOS
```
vi /run/flannel_docker_opts.env
# add one line
DOCKER_OPTS="--insecure-registry 172.**.**.**"
# restart docker service
sudo systemctl daemon-reload
sudo systemctl restart docker

```
