# ISP (Interface Segregation Principle)


from abc import abstractmethod


class Machine:
    
    def print(self, document):
        raise NotImplementedError
    
    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFuncionPrinter(Machine):

    def print(self, documen):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):

    def print(self, document):
        #ok
        pass

    def fax(self, documen):
        raise NotImplementedError('Printer cannot fax')

    def scan(self, document):
        """
            Not Supported!
        """
        raise NotImplementedError('Printer canno scan!')


class Printer:
    
    @abstractmethod
    def print(self, documen):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):

    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    
    def print(self, document):
        pass

    def scan(self, document):
        pass


class MultiFunctionDevice(Printer, Scanner):

    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):

    def __init__(self, printer, scanner) -> None:
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        return super().print(document)

    def scan(self, document):
        return super().scan(document)

