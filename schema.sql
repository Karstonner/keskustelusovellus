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
	title TEXT CHECK(title IS NOT NULL AND length(title) > 1 AND length(title) < 50),
	opening TEXT CHECK(opening IS NOT NULL AND length(opening) > 1 AND length(opening) < 280)
);
CREATE TABLE messages (
	id SERIAL PRIMARY KEY,
	content TEXT CHECK(content IS NOT NULL AND length(content) > 1 AND length(content) < 280),
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