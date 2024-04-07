CREATE TABLE messages (
	id SERIAL PRIMARY KEY,
	content TEXT,
	topic TEXT,
	sent_at TIMESTAMP
);