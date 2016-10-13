### “Swarming” Up
[root@docker1]$ 
```
docker swarm init --advertise-addr 192.168.55.111
```
[docker1]$ 
```
docker swarm join-token manager
```
On docker2 and docker3, run the following command to register the node:
```
docker swarm join \
    --token SWMTKN-1-16kit6dksvrqilgptjg5pvu0tvo5qfs8uczjq458lf9mul41hc-7fd1an5iucy4poa4g1bnav0pt \
    192.168.55.111:2377
```
[docker1]$ 
```
docker node ls
```
### Overlay Network

[docker1]$
```
docker network create --driver overlay mynet
docker network ls
```
### Deploying Key-Value Store
```
curl -w "\n" 'https://discovery.etcd.io/new?size=1'
 # https://discovery.etcd.io/a293d6cc552a66e68f4b5e52ef163d68
docker service create \
--name etcd \
--replicas 1 \
--network mynet \
-p 2379:2379 \
-p 2380:2380 \
-p 4001:4001 \
-p 7001:7001 \
elcolio/etcd:latest \
-name etcd \
-discovery=https://discovery.etcd.io/a293d6cc552a66e68f4b5e52ef163d68

docker service inspect etcd -f "{{ .Endpoint.VirtualIPs }}"
```

### Deploying Database Cluster
```
docker service create \
--name mysql-galera \
--replicas 3 \
-p 3306:3306 \
--network mynet \
--env MYSQL_ROOT_PASSWORD=mypassword \
--env DISCOVERY_SERVICE=10.0.0.2:2379 \
--env XTRABACKUP_PASSWORD=mypassword \
--env CLUSTER_NAME=galera \
perconalab/percona-xtradb-cluster:5.6
```
Swarm mode has an internal DNS component that automatically assigns each service in the swarm a DNS entry. So you use the service name to resolve to the virtual IP address:
```
docker exec -it $(docker ps | grep etcd | awk {'print $1'}) ping mysql-galera
```
Or, retrieve the virtual IP address through the “docker service inspect” command:
```
docker service inspect mysql-galera -f "{{ .Endpoint.VirtualIPs }}"
```
### Deploying Applications
```
docker service create \
--name wordpress \
--replicas 2 \
-p 80:80 \
--network mynet \
--env WORDPRESS_DB_HOST=mysql-galera \
--env WORDPRESS_DB_USER=root \
--env WORDPRESS_DB_PASSWORD=mypassword \
wordpress
```
If we connect directly to the PublishedPort, with a simple loop, we can see that the MySQL service is load balanced among containers:
```
 while true; do mysql -uroot -pmypassword -h127.0.0.1 -P3306 -NBe 'select @@wsrep_node_address'; sleep 1; done
```

> http://severalnines.com/blog/mysql-docker-introduction-docker-swarm-mode-and-multi-host-networking
