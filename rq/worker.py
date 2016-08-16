# -*- coding:utf-8 -*-
# Created by yanlei on 16-8-16 at 下午1:41
import os
import redis
from rq import Worker, Queue, Connection


listen = ['high', 'default', 'low']
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
