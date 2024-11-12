class Singleton:
    _instance = None  # Class variable to store the instance

    def __new__(cls, text):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)  # creat the instance using itself
            cls._instance.text = text  # Set the text property when the instance is created
        return cls._instance # return the 1st instance


# Test the Singleton pattern
singleton1 = Singleton("hi")
singleton2 = Singleton("hello")

print(singleton1 is singleton2)  # True, both variables refer to the same instance
print(singleton1.text)  # "hi" (the text of the first instance)
print(singleton2.text)  # "hi" (Singleton text is shared)
