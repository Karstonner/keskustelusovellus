CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	tunnus TEXT UNIQUE,
	salasana TEXT,
	is_admin INTEGER
);
CREATE TABLE topics (
	id SERIAL PRIMARY KEY,
	name TEXT UNIQUE
);
CREATE TABLE threads (
	id SERIAL PRIMARY KEY,
	topic INTEGER REFERENCES topics,
	creator INTEGER REFERENCES users,
	title TEXT,
	opening TEXT
);
CREATE TABLE messages (
	id SERIAL PRIMARY KEY,
	content TEXT,
	topic TEXT,
	thread INTEGER REFERENCES threads,
	user_id INTEGER REFERENCES users,
	sent_at TIMESTAMP
);
