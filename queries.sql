-- 1. Всі завдання певного користувача
SELECT * FROM tasks WHERE user_id = 1;

-- 2. Завдання за статусом 'new'
SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');

-- 3. Оновлення статусу завдання
UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 1;

-- 4. Користувачі без завдань
SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks);

-- 5. Додавання нового завдання
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('Новий приклад', 'Опис нового завдання', (SELECT id FROM status WHERE name = 'new'), 2);

-- 6. Завдання, що не завершено
SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');

-- 7. Видалення завдання за id
DELETE FROM tasks WHERE id = 1;

-- 8. Користувачі з певною електронною поштою
SELECT * FROM users WHERE email LIKE '%@example.com';

-- 9. Оновлення імені користувача
UPDATE users SET fullname = 'Нове ім’я' WHERE id = 2;

-- 10. Кількість завдань по статусах
SELECT s.name AS status, COUNT(t.id) AS task_count
FROM status s
LEFT JOIN tasks t ON s.id = t.status_id
GROUP BY s.name;

-- 11. Завдання для користувачів з певним доменом email
SELECT t.id, t.title, t.description, u.fullname, u.email
FROM tasks t
JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%@example.com';

-- 12. Завдання без опису
SELECT * FROM tasks WHERE description IS NULL OR description = '';

-- 13. Користувачі та їхні завдання зі статусом 'in progress'
SELECT u.fullname, u.email, t.title, t.description
FROM users u
INNER JOIN tasks t ON u.id = t.user_id
WHERE t.status_id = (SELECT id FROM status WHERE name = 'in progress');

-- 14. Користувачі та кількість їхніх завдань
SELECT u.fullname, u.email, COUNT(t.id) AS task_count
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.id;

