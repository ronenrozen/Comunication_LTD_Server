from comunication_ltd import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    old_password_1 = db.Column(db.String(120), nullable=True)
    old_password_2 = db.Column(db.String(120), nullable=True)
    salt = db.Column(db.LargeBinary, nullable=False)
    forgot_password = db.Column(db.String(120), nullable=True)
    password_attempts = db.Column(db.Integer, nullable=False, default=0)
    blocked = db.Column(db.Boolean, nullable=False, default=False)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"User(User ID:{self.id}'," \
               f"Email - {self.email}'," \
               f"Password - '{self.password}'," \
               f"Old_password_1 - '{self.old_password_1}'," \
               f"Old_password_2 - '{self.old_password_2}'," \
               f"salt - {self.salt}'," \
               f"Forgot_password - {self.forgot_password}'," \
               f"password_attempt - {self.password_attempt}'," \
               f"blocked - {self.blocked}'," \
               f"Created : - {self.date_created})"


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(120), nullable=False)
    sector = db.Column(db.String(120), nullable=True)
    email = db.Column(db.String(120), nullable=False)
    package_id = db.Column(db.Integer, db.ForeignKey('package.package_id'))
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"Customer(Customer ID:{self.id}'," \
               f"Customer Name - {self.customer_name}'," \
               f"email - '{self.email}'," \
               f"Created : - {self.date_created})"


class Package(db.Model):
    package_id = db.Column(db.Integer, primary_key=True)
    package_name = db.Column(db.String(120), nullable=False)
    package_size = db.Column(db.Integer, nullable=False)
    package_price = db.Column(db.Integer, nullable=False)
    customers = db.relationship('Customer', backref='package')

    def __repr__(self):
        return f"Package(Package ID:{self.id}'," \
               f"Package Name - {self.package_name}'," \
               f"Package Size - {self.package_size}'," \
               f"Package price - '{self.package_price}'," \
               f"Package Customers : - {self.customers})"
