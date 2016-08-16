# -*- coding:utf-8 -*-
# Created by yanlei on 16-8-16 at 下午12:09

from config import huey
from task import count_beans


if __name__ == "__main__":
    beans = 1000
    count_beans(beans)
    print('Enqueued job to count %s beans' % beans)
