CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    display_name VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS peeps_id_seq;
CREATE TABLE peeps (
    id SERIAL PRIMARY KEY,
    content VARCHAR(255),
    post_time TIMESTAMPTZ,
    user_id int, 
    constraint fk_user foreign key(user_id)
      references users(id)
      on delete cascade
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (username, display_name) VALUES ('Test', 'Test Display');
INSERT INTO peeps (content, post_time, user_id) VALUES ('Test peep', NOW(), 1);
