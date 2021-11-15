import types
from importlib.abc import Loader
from typing import Any, Mapping, Sequence

# `__import__` and `import_module` return type should be kept the same as `builtins.__import__`
def __import__(
    name: str,
    globals: Mapping[str, Any] | None = ...,
    locals: Mapping[str, Any] | None = ...,
    fromlist: Sequence[str] = ...,
    level: int = ...,
) -> types.ModuleType: ...
def import_module(name: str, package: str | None = ...) -> types.ModuleType: ...
def find_loader(name: str, path: str | None = ...) -> Loader | None: ...
def invalidate_caches() -> None: ...
def reload(module: types.ModuleType) -> types.ModuleType: ...
