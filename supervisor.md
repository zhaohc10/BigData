
supervisor可以对进程组统一管理，也就是说咱们可以把需要管理的进程写到一个组里面，然后我们把这个组作为一个对象进行管理，如启动，停止，重启等等操作;  

启动服务端supervisord -c /etc/supervisord.conf。 接着运行sudo supervisorctl status ，如果没有报错，就说明服务端启动正常了;  

supervisorctl tail hello 可以查看进程的输出   
supervisorctl reread hello 重新加载hello的配置  
supervisorctl remove hello 只有在hello停止运行的时候，才可以。这句是将hello从进程守护列表中移除  
supervisorctl reload 重新加载下配置
