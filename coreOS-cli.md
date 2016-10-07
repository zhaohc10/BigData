### coreOS cheat sheet
```
cat /etc/os-release

systemctl list-units

# Use this when you changed a unit file on disk
systemctl daemon-reload

systemctl status etcd

fleetctl list-units
fleetctl list-unit-files
fleetctl submit myapp.service
fleetctl start myapp
fleetctl destroy myapp
fleetctl journal --lines=100 myapp
fleetctl journal -f myapp

```

> ##### Install new software
> ``` 
 create a unit file like this :my.service
 cp ~/my.service /etc/systemd/system/   
 systemctl enable my.service    
 systemctl start my.service  
> ```
>#####  Follow the unit’s progress    
>```
 journalctl -u my.service -f
 >```
