celery -A test_celery worker -l info -P eventlet

celery multi start w1 -A test_celery -l info  # 限用与Linux

## 3W条数据 30秒客户端完成发送

## 3W条数据 服务器2分30s全部处理完毕