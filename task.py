# -*- coding:utf-8 -*-
# Created by yanlei on 16-8-16 at 下午12:08

from config import huey


@huey.task()
def count_beans(num):
    print('---counted %s beans ---' % num)
    return 'Counted %s beans' % num
