#!/bin/bash

MODULES_PATH=./modules
mkdir nginx-install

./configure --prefix=`pwd`/nginx-install \
            --with-debug \
            --with-file-aio --with-threads  \
            --with-http_secure_link_module \
            --add-module=$MODULES_PATH/mytest_config \
            --add-module=$MODULES_PATH/my_test_module \
            --add-module=$MODULES_PATH/mytest_subrequest \
            --add-module=$MODULES_PATH/mytest_upstream \
            --add-module=$MODULES_PATH/ngx_http_myfilter_module \
            --add-module=$MODULES_PATH/sendfile_test \
            --add-module=$MODULES_PATH/nginx-requestkey-module-master \
            --add-module=$MODULES_PATH/redis2-nginx-module-master 

make -j4 && make install
