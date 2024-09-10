class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class ReportGenerator:
    def generate(self, employee):
        return f"Employee Report for {employee.name}"

class EmailSender:
    def send(self, email, content):
        print(f"Sending email to {email} with content:\n{content}")

# Penggunaan
employee = Employee("John Doe", "john.doe@example.com")
report_generator = ReportGenerator()
email_sender = EmailSender()

report = report_generator.generate(employee)
email_sender.send(employee.email, report)
