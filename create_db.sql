DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS expenses CASCADE;

CREATE TABLE users (
    id SERIAL PRIMARY KEY, -- SERIAL is used for auto-incrementing IDs in PostgreSQL
    username TEXT NOT NULL,
    hash TEXT NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE expenses (
    expense_id SERIAL PRIMARY KEY, -- SERIAL for auto-incrementing IDs
    user_id INT NOT NULL,
    amount NUMERIC(10, 2), -- NUMERIC is used for fixed-point numbers in PostgreSQL
    category VARCHAR(50),
    description TEXT,
    date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE -- Ensures related expenses are deleted when a user is deleted
);
