import psycopg2
from faker import Faker
import random

# Підключення до бази даних
conn = psycopg2.connect(
    dbname="task_manager",
    user="taniashynder",
    password="",  # якщо пароль є, впиши його
    host="localhost"
)
cur = conn.cursor()
fake = Faker()

# Додавання користувачів
for _ in range(5):
    fullname = fake.name()
    email = fake.unique.email()
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

# Отримуємо id статусів
cur.execute("SELECT id FROM status")
status_ids = [row[0] for row in cur.fetchall()]

# Отримуємо id користувачів
cur.execute("SELECT id FROM users")
user_ids = [row[0] for row in cur.fetchall()]

# Додавання завдань
for _ in range(10):
    title = fake.sentence(nb_words=4)
    description = fake.text(max_nb_chars=50)
    status_id = random.choice(status_ids)
    user_id = random.choice(user_ids)
    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                (title, description, status_id, user_id))

conn.commit()
cur.close()
conn.close()
print("Seed completed!")

