aws help
## config the aws-cli on your OS
# vi ~/.aws/config
aws configure
  <myKEY>
  <myPWD>
  us-west-1b
  json

aws ec2 describe-instances --output table --region us-west-1

## enable the completer function
which aws_completer
# find / -name aws_completer
complete -C '/usr/bin/aws_completer' aws

********************************

ssh -i autoshift-ca.pem core@<IP>
ssh -i autoshift-ca.pem core@<IP>
ssh -i autoshift-ca.pem core@<IP>

#
# The custom ICMP rule in the security group is not what it takes, a least for me. 
# But the following rule will work:
# Type: All ICMP 
# Protocol: TCP
# Port range: 0 - 65535
# Source: Anywhere - 0.0.0.0/0


*******************
https://coreos.com/os/docs/latest/booting-on-ec2.html

1.	You need open port 2379, 2380, 7001 and 4001 between servers in the etcd cluster. 
2.	generate one at https://discovery.etcd.io/new?size=3
3.  Cloud-config is intended to bring up a cluster of machines into a minimal useful state
	# just launch more with the same cloud-config, 
	# New instances will join the cluster regardless of region 
	# 	if the security groups are configured correctly.
	On every boot, coreos-cloudinit looks for a config file to configure your host. 
	# sudo coreos-cloudinit --from-file=/home/core/cloud-config.yaml

#*******************
#cloud-config

coreos:
  etcd2:
    # generate a new token for each unique cluster from https://discovery.etcd.io/new?size=3
    # specify the initial size of your cluster with ?size=X
    discovery: https://discovery.etcd.io/<token>
    # multi-region and multi-cloud deployments need to use $public_ipv4
    advertise-client-urls: http://$private_ipv4:2379,http://$private_ipv4:4001
    initial-advertise-peer-urls: http://$private_ipv4:2380
    # listen on both the official ports and the legacy ports
    # legacy ports can be omitted if your application doesn't depend on them
    listen-client-urls: http://0.0.0.0:2379,http://0.0.0.0:4001
    listen-peer-urls: http://$private_ipv4:2380,http://$private_ipv4:7001
  units:
    - name: etcd2.service
      command: start
    - name: fleet.service
      command: start
# *******************        
4. ssh -i MyKeyPair.pem core@some-public-ip  
fleetctl list-machines  
5. If you want to check if that particular instance is a leader execute the following :
curl -L http://127.0.0.1:4001/v2/stats/leader  


*******************
# http://www.mbejda.com/setting-up-a-coreos-cluster-on-aws/

	# https://coreos.com/os/docs/latest/booting-on-ec2.html
	# https://s3.amazonaws.com/coreos.com/dist/aws/coreos-stable-hvm.template

#https://discovery.etcd.io/new

#cloud-config
coreos:
  etcd:
    discovery: https://discovery.etcd.io/<token>
    addr: $private_ipv4:4001
    peer-addr: $private_ipv4:7001
  units:
    - name: etcd.service
      command: start
    - name: fleet.service
      command: start

aws ec2 run-instances --image-id ami-0eacc46e --count 3 --instance-type t2.micro --key-name <my.pem> --security-groups <> --user-data file://core-test.yml  
