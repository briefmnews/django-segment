import analytics


def analytics_sync_mode(func):
    def inner(*args, **kwargs):
        analytics.sync_mode = True
        func(*args, **kwargs)
        analytics.sync_mode = False

    return inner
