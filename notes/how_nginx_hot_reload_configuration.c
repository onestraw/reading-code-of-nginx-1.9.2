/* 
quit过程：主进程收到quit信号，然后发送quit信号给worker进程，worker进程收到后
close listen的监听fd，然后等待已有的连接处理完毕，子进程退出

reload过程，master进程收到reload信号，则重新加载配置文件，同时创建新的worker
进程，然后发送quit信号到原来的worker子进程，源worker子进程就会拒绝bind
接受客户端连接,全部由新的worker进程来接收连接。

热升级过程:首先通过kill发送SIGUSR2(NGX_CHANGEBIN_SIGNAL)信号给源master进程，该进程收到该信号后，把该进程bind监听的fd全部设置到NGINX
环境变量中，然后通过fork+execve来设置环境变量生效。然后重启新的nginx进程，这样新的nginx进程就可以获取到之前master bind的fd。
*/ 
