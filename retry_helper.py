import time

def retry(n=3, delay=0.5):
    def deco(fn):
        def wrap(*a, **kw):
            for i in range(n):
                try:
                    return fn(*a, **kw)
                except Exception:
                    if i == n - 1:
                        raise
                    time.sleep(delay * (2 ** i))
        return wrap
    return deco
