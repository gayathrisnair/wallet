# Wallet App

## Getting Started
wallet transaction system which has the following functionalities

- Create Wallet for a User using phone Number
- Credit money to wallet
- Debit money from wallet
- Get current Balance

### Prerequisites
 - Python
 - Django
 - sqlite

### How to Run
 - $ python manage.py makemigrations
 - $ python manage.py migrate
 - $ python manage.py runserver

## Features to be added:
 - Integer and length validations on input phoneNumber
 - decimal and Number validations on amount fields
 - BaseEntity with columns created_at , updated_at, is_deleted(for soft deletion)
 - Log Table for capturing each transactions- Database Locking(optimistic write db lock) or synchronized block in python to handle race conditions of multiple transactions on same wallet
 - Basic Auth/ api-key to authenticate requests


# Postman collection: 
- https://www.getpostman.com/collections/0a6a7692c2e4d2e6e163


