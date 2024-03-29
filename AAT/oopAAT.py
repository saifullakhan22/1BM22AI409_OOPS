# -*- coding: utf-8 -*-
"""OOPpres.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fHiCEqBoHw8ZWI6JZQ0SnwFZaYRh4EMF

Single Responsibility Principle

SRP states that a class should have only one responsibility
"""

import random

class TemperatureSensor:
    def __init__(self, location):
        self.location = location

    def measure_temperature(self):
        # Simulate measuring temperature
        temperature = 25 + random.uniform(-5, 5)
        return temperature


class TemperatureReporter:
    def __init__(self, sensor):
        self.sensor = sensor

    def report_temperature(self):
        temperature = self.sensor.measure_temperature()
        print(f"Temperature at {self.sensor.location}: {temperature} degrees Celsius")


if __name__ == "__main__":
    living_room_sensor = TemperatureSensor("Living Room")
    living_room_reporter = TemperatureReporter(living_room_sensor)

    kitchen_sensor = TemperatureSensor("Kitchen")
    kitchen_reporter = TemperatureReporter(kitchen_sensor)

    # Report temperature for the living room
    living_room_reporter.report_temperature()

    # Report temperature for the kitchen
    kitchen_reporter.report_temperature()

"""The Open-Closed Principle (OCP) is another SOLID principle that states that a class should be open for extension but closed for modification."""

from abc import ABC, abstractmethod

# Abstract class representing a payment method
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Concrete implementation of a credit card payment
class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

# Concrete implementation of a PayPal payment
class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# PaymentProcessor class follows the Open-Closed Principle
class PaymentProcessor:
    def __init__(self):
        self.payment_methods = []

    def add_payment_method(self, payment_method):
        self.payment_methods.append(payment_method)

    def process_payments(self, amount):
        for payment_method in self.payment_methods:
            payment_method.process_payment(amount)

if __name__ == "__main__":
    credit_card_payment = CreditCardPayment()
    paypal_payment = PayPalPayment()

    processor = PaymentProcessor()

    processor.add_payment_method(credit_card_payment)
    processor.add_payment_method(paypal_payment)

    # Process payments without modifying existing code
    processor.process_payments(100)

"""
The Liskov Substitution Principle (LSP) is one of the SOLID principles and states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.

document management system:"""

from abc import ABC, abstractmethod

# Abstract class representing a document
class Document(ABC):
    def __init__(self, content):
        self.content = content

    @abstractmethod
    def display(self):
        pass

# TextDocument is a subclass of Document
class TextDocument(Document):
    def display(self):
        print(f"Text Document: {self.content}")

# PDFDocument is another subclass of Document
class PDFDocument(Document):
    def display(self):
        print(f"PDF Document: {self.content}")

# DocumentViewer can display any Document or its subclass
class DocumentViewer:
    def view_document(self, document):
        document.display()

if __name__ == "__main__":
    text_document = TextDocument("This is a text document.")
    pdf_document = PDFDocument("This is a PDF document.")

    viewer = DocumentViewer()

    # The viewer can display any Document or its subclass
    viewer.view_document(text_document)  # Output: Text Document: This is a text document.
    viewer.view_document(pdf_document)   # Output: PDF Document: This is a PDF document.

"""
The Interface Segregation Principle (ISP) is one of the SOLID principles, stating that a class should not be forced to implement interfaces it does not use. In other words, a class should only be required to implement the methods that are relevant to its behavior.

Let's consider a real-life example using an electronic device scenario:
"""

from abc import ABC, abstractmethod

# Interface for devices with display capabilities
class Displayable(ABC):
    @abstractmethod
    def display(self):
        pass

# Interface for devices with printing capabilities
class Printable(ABC):
    @abstractmethod
    def print_document(self):
        pass

# Printer implements only the Printable interface
class Printer(Printable):
    def print_document(self):
        print("Printing document...")

# Tablet implements only the Displayable interface
class Tablet(Displayable):
    def display(self):
        print("Displaying content on the tablet...")

# AllInOneDevice implements both Displayable and Printable interfaces
class AllInOneDevice(Displayable, Printable):
    def display(self):
        print("Displaying content on the all-in-one device...")

    def print_document(self):
        print("Printing document on the all-in-one device...")

if __name__ == "__main__":
    printer = Printer()
    tablet = Tablet()
    all_in_one_device = AllInOneDevice()

    # Each device can be used based on its capabilities
    printer.print_document()             # Output: Printing document...
    tablet.display()                     # Output: Displaying content on the tablet...
    all_in_one_device.display()          # Output: Displaying content on the all-in-one device...
    all_in_one_device.print_document()   # Output: Printing document on the all-in-one device...

"""The Dependency Inversion Principle (DIP) is one of the SOLID principles, which suggests that high-level modules (e.g., business logic) should not depend on low-level modules (e.g., data access or external services). Instead, both should depend on abstractions (interfaces or abstract classes).

Here's a real-life example using a notification system
"""

from abc import ABC, abstractmethod

# Abstraction for a notification service
class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass

# Concrete implementation of an email notification service
class EmailNotificationService(NotificationService):
    def send_notification(self, message):
        print(f"Sending email notification: {message}")

# Concrete implementation of an SMS notification service
class SMSNotificationService(NotificationService):
    def send_notification(self, message):
        print(f"Sending SMS notification: {message}")

# High-level module that depends on an abstraction (NotificationService)
class NotificationClient:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def send_message(self, message):
        # Business logic
        self.notification_service.send_notification(message)

if __name__ == "__main__":
    email_notification_service = EmailNotificationService()
    sms_notification_service = SMSNotificationService()

    # High-level module (NotificationClient) depends on abstractions (NotificationService)
    email_client = NotificationClient(email_notification_service)
    sms_client = NotificationClient(sms_notification_service)

    # The high-level module can easily switch between different notification services
    email_client.send_message("Hello via email!")   # Output: Sending email notification: Hello via email!
    sms_client.send_message("Hello via SMS!")       # Output: Sending SMS notification: Hello via SMS!
