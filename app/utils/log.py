import sys
from functools import lru_cache
from loguru import logger

class LogHelper:
    def __init__(self):
        self.logger = logger
        self.logger.remove()

        formatter = (
            "<green>{time:YYYYMMDD HH:mm:ss}</green> | "  # 绿色显示时间
            "{process.name} | "  # 显示进程名
            "{thread.name} | "  # 显示线程名
            "<cyan>{module}</cyan>.<cyan>{function}</cyan>"  # 青色显示模块名和方法名
            ":<cyan>{line}</cyan> | "  # 青色显示行号
            "<level>{level}</level>: "  # 显示日志等级
            "<level>{message}</level>",
        )

        self.logger.add(
            sys.stdout,
            format = formatter[0],
        )

        @lru_cache
        def get_logger(self):
            return self.logger

LogHelpers = LogHelper()

log = LogHelpers.get_logger()