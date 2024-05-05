DROP TABLE IF EXISTS participants CASCADE;
DROP TABLE IF EXISTS messages CASCADE;
DROP TABLE IF EXISTS threads CASCADE;
DROP TABLE IF EXISTS topics CASCADE;
DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	tunnus TEXT UNIQUE,
	salasana TEXT
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
	thread INTEGER REFERENCES threads,
	user_id INTEGER REFERENCES users,
	sent_at TIMESTAMP
);
CREATE TABLE participants (
	user_id INTEGER REFERENCES users,
	thread INTEGER REFERENCES threads
);
	

INSERT INTO topics (name) VALUES ('musiikki');
INSERT INTO topics (name) VALUES ('ruoka');
INSERT INTO topics (name) VALUES ('yliopisto');