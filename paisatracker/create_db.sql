DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS expenses;


CREATE TABLE users (id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                     hash TEXT NOT NULL,
                     email VARCHAR(255) UNIQUE NOT NULL
                     );
CREATE UNIQUE INDEX email ON users (email);

CREATE TABLE expenses (
    expense_id INTEGER PRIMARY KEY ,
    user_id INT,
    amount DECIMAL(10,2),
    category VARCHAR(50),
    description TEXT,
    date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id)
);