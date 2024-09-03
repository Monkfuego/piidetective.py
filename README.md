# detective.py

##PII Detection Utility

This Python script provides a set of functions to detect various types of Personally Identifiable Information (PII) from text. The PII types supported include identifiers like GSTIN, phone numbers, email addresses, bank account numbers, credit card numbers, IP addresses, and document-specific identifiers such as Aadhar, PAN, passport numbers, and more.


##Key Features
Individual PII Detection Functions: The script includes specific functions to detect different types of PII. Each function is named in the format piitypecheck(), such as gstincheck(), emailcheck(), driverlicensecheck(), etc. These functions take a text input and return:

The number of matches found.
The actual matched data.

###Comprehensive PII Detection: 
The piidetect function checks for all supported PII types in the provided text. It returns a list of tuples, where each tuple contains:


The type of PII detected (e.g., Aadhar Card, Email, Phone Number).
The matched data.
Supported PII Types

#Generic PII:


GSTIN (India's Goods and Services Tax Identification Number)
Phone Numbers (Indian format)

Email Addresses

Bank Account Numbers (Indian format)

Credit Card Numbers

IPv4 and IPv6 Addresses

IFSC Codes (Indian Financial System Codes)

Vehicle Registration Numbers (Indian format)

NPS PRAN (National Pension System Permanent Retirement Account Number)


#Document-Specific PII:

Aadhar Card Numbers

PAN Card Numbers

Voter ID Numbers

Passport Numbers

Driver's License Numbers

NREGA Job Card Numbers
