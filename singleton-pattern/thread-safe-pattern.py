import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(ThreadSafeSingleton, cls).__new__(cls)
        return cls._instance

# Usage
instance1 = ThreadSafeSingleton()
instance2 = ThreadSafeSingleton()
print(instance1 is instance2)  # True
