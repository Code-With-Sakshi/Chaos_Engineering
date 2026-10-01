# 🏢 Visitor Management System

A simple digital visitor management system designed for apartment security guards to replace the traditional paper visitor register.

The system allows the security guard to register visitors, automatically record entry time, record exit time when the visitor leaves, view visitors currently inside, and search visitor records by flat number.

---

## 📌 Problem Statement

The apartment gate currently uses a paper visitor register, which can become difficult to maintain and search.

This system provides a digital solution where the security guard can:

* Register a visitor
* Enter the visitor's name
* Select the apartment wing
* Enter the flat number
* Enter the visitor's phone number
* Automatically record the entry time
* Record the exit time when the visitor leaves
* View visitors currently inside the apartment
* Search visitor records by flat number

---

## ✨ Features

### 👤 Visitor Registration

The security guard can enter:

* Visitor Name
* Wing (A or B)
* Flat Number (1–40)
* Phone Number (10 or 12 digits)

The entry time is automatically recorded by the system.

### 🚪 Visitor Exit

When a visitor leaves, the guard clicks the **Exit** button.

The system:

* Records the current exit time
* Changes the visitor status from `Inside` to `Exit`
* Keeps the previous visit in the database

If the same person visits again, the guard registers them as a **new visit**, creating a new record while preserving the previous visit history.

### 👥 Visitors Inside

The system keeps track of visitors whose status is currently:

```text
Inside
```

### 🔎 Search by Flat Number

The guard can search visitor records using the flat number.

The system displays the visitor history associated with that flat.

### 📊 Dashboard

The home dashboard displays:

* Number of visitors currently inside
* Number of visitors who visited today
* New visitor registration form

---

## 🛡️ Input Validation

The system validates visitor information before saving it.

### Wing

Only:

```text
A
B
```

are accepted.

### Flat Number

Valid range:

```text
1–40
```

### Phone Number

The phone number must contain:

```text
10 digits
```

or

```text
12 digits
```

---

## 🛠️ Technology Stack

| Technology             | Purpose                       |
| ---------------------- | ----------------------------- |
| HTML5                  | Web page structure            |
| CSS3                   | User interface and styling    |
| Python                 | Backend programming           |
| Flask                  | Web framework                 |
| MySQL                  | Database                      |
| mysql-connector-python | Python–MySQL connection       |
| python-dotenv          | Loading environment variables |
| Git                    | Version control               |
| GitHub                 | Source code repository        |

---

## 🏗️ System Architecture

```text
Security Guard
      ↓
 HTML / CSS Interface
      ↓
     Flask
      ↓
mysql-connector-python
      ↓
     MySQL
      ↓
visitor_management
      ↓
   visitors
```

---

## 🗄️ Database

### Database Name

```text
visitor_management
```

### Table

```text
visitors
```

### Main Fields

| Field          | Description                       |
| -------------- | --------------------------------- |
| `id`           | Unique visitor visit ID           |
| `visitor_name` | Name of visitor                   |
| `wing`         | Apartment wing A or B             |
| `flat_number`  | Flat number from 1–40             |
| `phone`        | Visitor phone number              |
| `entry_time`   | Automatically recorded entry time |
| `exit_time`    | Recorded when visitor leaves      |
| `status`       | `Inside` or `Exit`                |

---

## 🔄 Visitor Flow

```text
Visitor Arrives
      ↓
Guard Opens Dashboard
      ↓
Enter Visitor Details
      ↓
Validation
      ↓
Register Visitor
      ↓
Status = Inside
      ↓
Visitor Leaves
      ↓
Guard Clicks Exit
      ↓
Exit Time Recorded
      ↓
Status = Exit
```

If the same visitor comes again:

```text
Previous Visit
10:00 AM → 11:00 AM
Status = Exit

        ↓

New Visit
3:00 PM → —
Status = Inside
```

The previous visit is not overwritten.

---

## 🔐 Environment Variables

Database credentials are stored in a `.env` file instead of directly inside `app.py`.

Example:

```env
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=visitor_management
```

The `.env` file is excluded from GitHub using `.gitignore`.

---

## 📁 Project Structure

```text
Chaos/
│
├── app.py
├── .env
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── visitors.html
│   └── search.html
│
└── static/
    └── style.css
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Code-With-Sakshi/Chaos_Engineering.git
```

### 2. Open the Project

```bash
cd Chaos_Engineering
```

### 3. Install Required Packages

```bash
pip install flask mysql-connector-python python-dotenv
```

### 4. Configure `.env`

Create a `.env` file in the project root:

```env
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=visitor_management
```

### 5. Create the Database

Open MySQL and run:

```sql
CREATE DATABASE visitor_management;

USE visitor_management;
```

### 6. Create the Visitors Table

```sql
CREATE TABLE visitors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    visitor_name VARCHAR(100) NOT NULL,
    wing VARCHAR(1) NOT NULL,
    flat_number INT NOT NULL,
    phone VARCHAR(12) NOT NULL,
    entry_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    exit_time DATETIME NULL,
    status VARCHAR(10) NOT NULL DEFAULT 'Inside'
);
```

### 7. Run the Application

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

---

## 🚀 Future Improvements

Possible improvements include:

* Visitor photo capture
* Resident notification when a visitor arrives
* Visitor ID verification
* Export visitor records
* Date-based visitor reports
* Authentication for security guards
* Automatic visitor history reports
* Improved mobile interface

---

## 🎯 Competition Context

This project was developed for the **Chaos Engineering — Programming & AI Problem-Solving Competition**.

The application focuses on solving a real-world apartment security problem through a simple digital visitor registration and tracking system.

### Core Principle

> Build it. Break it. Fix it. Explain it.

The system is designed to be understandable, testable, and adaptable to unexpected requirements during the competition.

---

## 👩‍💻 Author

**Sakshi Bute**
**Aarya Ghawale**
**Shreya Pise**


GitHub:
https://github.com/Code-With-Sakshi

---

## 📄 License

This project is created for educational and competition purposes.
