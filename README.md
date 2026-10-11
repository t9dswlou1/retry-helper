# retry-helper

A small retry helper with jittered exponential backoff and a max-elapsed guard.

## Why

Written while learning the language properly, and kept because it still works.

## Install

```bash
pip install retry-helper
```

## Usage

```python
from retry_helper import retryHelper

result = retryHelper("example")
print(result)
```

## Notes

- No runtime dependencies outside the standard library.
- Tested on Python 3.9 and newer.

## License

MIT
