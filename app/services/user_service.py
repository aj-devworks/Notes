from .repository import create_user, get_user_by_username, get_user_by_id, get_all_users, update_user, delete_user


def create_user_service(username, password):
    if not username or not password:
        raise ValueError("Username and password are required fields")
    return create_user(username, password)


def get_user_service(user_id):
    if not user_id:
        raise ValueError("User id is required")
    user = get_user_by_id(user_id)
    if not user:
        raise ValueError("User not found")
    return user


def get_user_by_username_service(username):
    if not username:
        raise ValueError("Username is required")
    user = get_user_by_username(username)
    if not user:
        raise ValueError("User not found")
    return user


def get_all_users_service():
    return get_all_users()


def update_user_service(user_id, **kwargs):
    if not user_id:
        raise ValueError("User id is required")
    return update_user(user_id, **kwargs)


def delete_user_service(user_id):
    if not user_id:
        raise ValueError("User id is required")
    return delete_user(user_id)