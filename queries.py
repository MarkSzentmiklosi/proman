import data_manager


def get_boards(user_id):
    return data_manager.execute_select('''SELECT * FROM boards
                                        WHERE user_id = %(user_id)s;
                                       ''',
                                       {'user_id': user_id})


def get_cards(board_id):
    return data_manager.execute_select('''SELECT * FROM cards
                                        WHERE board_id = %(board_id)s;
                                       ''',
                                       {'board_id': board_id})


def get_hashed_pass(user_name):
    return data_manager.execute_select('''SELECT password FROM users
                                        WHERE user_name = %(user_name)s;
                                       ''',
                                       {'user_name': user_name})


def create_user(username, password):
    return data_manager.execute_dml_statement("""
    INSERT INTO users
    (user_name,password)
    VALUES(%(username)s,%(password)s)
    RETURNING id;
    """, {'username': username,
          'password': password})


def check_username(username):
    return data_manager.execute_select("""
    SELECT user_name
    FROM users
    WHERE user_name = %(username)s;
    """, {'username': username})


def get_userid_by_name(username):
    return data_manager.execute_dml_statement("""
                                            SELECT id FROM users
                                            WHERE user_name = %(user_name)s;
                                            """,
                                              {'user_name': username})


def create_board(board_title, user_id):
    return data_manager.execute_select("""
                                        INSERT INTO boards (title, is_active, user_id, creation_time, modified_time)
                                        VALUES (%(board_title)s, 'false', %(user_id)s, now(), now())
                                        RETURNING id
                                        """,
                                       {
                                           'board_title': board_title,
                                           'user_id': user_id
                                       })


def save_board_status(boardId, is_active):
    return data_manager.execute_select("""
    UPDATE boards
    SET is_active = %(is_active)s
    WHERE boards.id = %(boardId)s
    """, {'is_active': is_active,
          'boardId': boardId})
