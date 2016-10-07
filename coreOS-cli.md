### coreOS cheat sheet
```
cat /etc/os-release

systemctl list-units

# Use this when you changed a unit file on disk
systemctl daemon-reload

systemctl status etcd

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
