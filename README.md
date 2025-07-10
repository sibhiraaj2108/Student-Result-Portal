# 🎓 Student Result Portal

A simple Django-based web application that allows faculty members to perform CRUD operations on student results, including filtering by student name and subject.

## 🧰 Features

✅ Add new student results  
✏️ Edit existing results  
🗑️ Delete results with confirmation  
🔍 Filter by student name or subject  
📄 View all results in a clean, responsive table

## 📁 Project Structure

├── manage.py  
├── db.sqlite3  
├── templates/  
│   ├── result_list.html  
│   ├── result_form.html  
│   └── result_confirm_delete.html  
├── your_app_name/  
│   ├── __init__.py  
│   ├── admin.py  
│   ├── models.py  
│   ├── views.py  
│   ├── forms.py  
│   ├── urls.py  
│   ├── migrations/  
│   │   └── 0001_initial.py  
├── project_name/  
│   ├── __init__.py  
│   ├── settings.py  
│   ├── urls.py  
│   └── wsgi.py  

> 🔁 Replace `your_app_name` and `project_name` with your actual app and project folder names.

## 🚀 Getting Started

### Prerequisites

- Python 3.10+  
- pip  
- virtualenv (recommended)

### Installation Steps

```bash
# Clone the project (or unzip the folder)
cd student-result-portal

# Optional: Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install django

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
Visit http://127.0.0.1:8000/ to use the portal.

🧪 How to Use
Homepage: Displays all student results.

Add Result: Click “Add Result” to enter new student data.

Edit/Delete: Buttons available per record.

Search/Filter: Use the filter box to narrow results.

🛠️ Technologies Used
Python 🐍

Django 🌐

SQLite 🗃️

HTML & Bootstrap (for styling)

🙋‍♂️ Author
👤 sibhiraaj2108
GitHub: sibhiraaj2108
