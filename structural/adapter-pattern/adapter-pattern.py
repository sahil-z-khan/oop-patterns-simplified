from abc import ABC, abstractmethod

# JSONLogger Class
class JSONLogger(ABC):
    @abstractmethod
    def log_message(self, message: str) -> None:
        pass

# XMLLogger Class
class XMLLogger:
    def log(self, XML_message: str) -> None:
        print(XML_message)

# Adapter
class LoggerAdapter(JSONLogger):
    def __init__(self, XML_logger: XMLLogger) -> None:
        self.XML_logger = XML_logger # Attach XMLLogger Object to self

    def log_message(self, message: str) -> None:
        self.XML_logger.log(message) # call "JSONLogger"s log_message but instead we are calling .log on xml

logger = LoggerAdapter(XMLLogger())
logger.log_message("<message>hello</message>")
