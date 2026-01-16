# 🚀 Professional Portfolio & Custom Admin CRM

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

A fully dynamic **Portfolio Website** featuring a powerful **Admin Dashboard** (CRM) to manage client inquiries and project showcases. Built with a focus on clean UI and efficient data handling.

---

## 🔥 Key Features

### 1. 💼 Dynamic Admin Dashboard
- **Lead Management:** View, track, and manage client inquiries in real-time.
- **Status System:**
  - 🟡 **Pending:** Mark new leads for follow-up.
  - 🟢 **Pass/Contacted:** Mark completed interactions to keep the inbox clean.
- **Quick Actions:** One-click buttons to **Call** 📞, **Email** 📧, or **Delete** 🗑️ leads.

### 2. 🎨 Project Showcase
- **CRUD Operations:** Add, Update, and Remove portfolio projects dynamically.
- **Image Handling:** Seamless image uploads for project thumbnails.

### 3. 📱 Modern UI/UX
- **Responsive Design:** Mobile-first layout using **Bootstrap 5**.
- **Visual Cues:** Color-coded cards and badges for quick status identification.

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Backend** | Python, Django |
| **Frontend** | HTML5, CSS3, Bootstrap 5, Jinja2 |
| **Database** | SQLite (Default) / PostgreSQL |
| **Version Control** | Git & GitHub |

---

## ⚙️ Installation Guide

Run the following commands to set up the project locally:

bash
# 1. Clone the repository
git clone [https://github.com/jayupithadiya/Interior-Design-Management-System](https://github.com/jayupithadiya/Interior-Design-Management-System)

# 2. Navigate to directory
cd YOUR-REPO-NAME

# 3. Create & Activate Virtual Environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install Dependencies
pip install -r requirements.txt

# 5. Apply Migrations
python manage.py makemigrations

python manage.py migrate

# 6. Create Superuser (Admin)
python manage.py createsuperuser

# 7. Run Server
python manage.py runserver
