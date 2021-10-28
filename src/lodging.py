import os
import sys
import json
import string
from copy import deepcopy
from typing import Dict, Any

from logging import DEBUG, INFO, WARNING, WARNING, ERROR, CRITICAL

LogLevel = int

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if callable(o):
            o = o()
        return super().default(o)

def _encode_json(data: Any) -> str:
    pass

def encode_json_template(data: Dict[str, Any]) -> str:
    if isinstance(data, dict):
        pass
    elif isinstance(data, list):
        pass

class JSONLogger:
    def __init__(self, level: LogLevel = INFO, base_data: Dict[str, Any] = {}, jsonCLS: json.JSONEncoder = None) -> None:
        self.output = sys.stdout
        self._flush = True
        self.level = level
        self.base_data = base_data
        self.jsonCLS = jsonCLS or JSONEncoder

    def copy(self, with_fields: Dict[str, Any] = {}) -> 'JSONLogger':
        return JSONLogger(self.level, deepcopy({**self.base_data, **with_fields}), self.jsonCLS)

    def isEnabledFor(self, level: LogLevel) -> bool:
        return level >= self.level

    def _merge_data(self, data: Dict[str, Any] = {}) -> Dict[str, Any]:
        d = {**self.base_data, **data}
        return {k: (v() if callable(v) else v) for k, v in d.items() if v is not None}

    def _log(self, level: LogLevel, data: Dict[str, Any]) -> None:
        if not self.isEnabledFor(level): return
        d = json.dumps(self._merge_data(data), cls=self.jsonCLS)
        print(d, file=self.output, flush=self._flush)
    
    def log(self, level: LogLevel, data: Dict[str, Any] = {}) -> None:
        self._log(level, data)

    def debug(self, data: Dict[str, Any] = {}) -> None:
        self._log(DEBUG, data)

    def info(self, data: Dict[str, Any] = {}) -> None:
        self._log(INFO, data)

    def warning(self, data: Dict[str, Any] = {}) -> None:
        self._log(WARNING, data)
    
    def error(self, data: Dict[str, Any] = {}) -> None:
        self._log(ERROR, data)

    def critical(self, data: Dict[str, Any] = {}) -> None:
        self._log(CRITICAL, data)
