-- Report Route: Last 7 Days
SELECT * FROM expenses
WHERE date >= date('now', '-7 days') AND user_id=?;

SELECT SUM(amount) FROM expenses
WHERE date >= date('now', '-7 days') AND category='income' AND user_id=?;

SELECT SUM(amount) FROM expenses
WHERE date >= date('now', '-7 days') AND category='expense' AND user_id=?;

-- Report Route: This Month
SELECT * FROM expenses
WHERE strftime('%Y-%m', date) = strftime('%Y-%m', 'now') AND user_id=?;

SELECT SUM(amount) FROM expenses
WHERE strftime('%Y-%m', date) = strftime('%Y-%m', 'now') AND category='income' AND user_id=?;

SELECT SUM(amount) FROM expenses
WHERE strftime('%Y-%m', date) = strftime('%Y-%m', 'now') AND category='expense' AND user_id=?;

-- Report Route: Last Month
SELECT * FROM expenses
WHERE strftime('%Y-%m', date) = strftime('%Y-%m', 'now', '-1 month') AND user_id=?;

SELECT SUM(amount) FROM expenses
WHERE strftime('%Y-%m', date) = strftime('%Y-%m', 'now', '-1 month') AND category='income' AND user_id=?;

SELECT SUM(amount) FROM expenses
WHERE strftime('%Y-%m', date) = strftime('%Y-%m', 'now', '-1 month') AND category='expense' AND user_id=?;

-- Expense Route
SELECT * FROM expenses
WHERE category=? AND user_id=? ORDER BY expense_id DESC LIMIT 100;

-- Income Route
SELECT * FROM expenses
WHERE category=? AND user_id=? ORDER BY expense_id DESC LIMIT 100;

-- Home Route: Insert Expense
INSERT INTO expenses (user_id, amount, category, description, date)
VALUES (?, ?, ?, ?, ?);

-- Home Route: Select Recent Expenses
SELECT * FROM expenses
WHERE user_id=? ORDER BY expense_id DESC LIMIT 5;

-- Login Route
SELECT * FROM users
WHERE email=?;

-- Register Route
SELECT * FROM users
WHERE email=?;

INSERT INTO users (username, hash, email)
VALUES (?, ?, ?);

-- Mail Sent Route
SELECT email FROM users
WHERE email=?;

-- Forgot Route
UPDATE users
SET hash=?
WHERE email=?;