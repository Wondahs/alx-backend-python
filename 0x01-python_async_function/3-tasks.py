#!/usr/bin/env python3
'''Task 3: Asyncio Tasks'''
import asyncio
from typing import Awaitable


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable[float]:
    '''
    Takes an integer max_delay and returns a asyncio.Task.
    '''
    return asyncio.create_task(wait_random(max_delay))
