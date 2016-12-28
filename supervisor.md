
supervisor可以对进程组统一管理，也就是说咱们可以把需要管理的进程写到一个组里面，然后我们把这个组作为一个对象进行管理，如启动，停止，重启等等操作;  

# supervisor组件  
### supervisord  
supervisord是supervisor的服务端程序。  
干的活：启动supervisor程序自身，启动supervisor管理的子进程，响应来自clients的请求，重启闪退或异常退出的子进程，把子进程的stderr或stdout记录到日志文件中，生成和处理Event  
### supervisorctl  
这东西还是有点用的，如果说supervisord是supervisor的服务端程序，那么supervisorctl就是client端程序了。 
supervisorctl有一个类型shell的命令行界面，我们可以利用它来查看子进程状态，启动/停止/重启子进程，获取running子进程的列表等等。。  
最牛逼的一点是，supervisorctl不仅可以连接到本机上的supervisord，还可以连接到远程的supervisord，当然在本机上面是通过UNIX socket连接的，远程是通过TCP socket连接的。  
supervisorctl和supervisord之间的通信，是通过xml_rpc完成的。    
相应的配置在[supervisorctl]块里面  



启动服务端supervisord -c /etc/supervisord.conf。 接着运行sudo supervisorctl status ，如果没有报错，就说明服务端启动正常了;  

supervisorctl tail hello 可以查看进程的输出   
supervisorctl reread hello 重新加载hello的配置  
supervisorctl remove hello 只有在hello停止运行的时候，才可以。这句是将hello从进程守护列表中移除  
supervisorctl reload 重新加载下配置
