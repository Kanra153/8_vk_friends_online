import vk
import getpass

APP_ID = 6374021


def get_user_login():
    user_login = input('Please, input your login: ')
    return user_login


def get_user_password():
    user_password = getpass.getpass('Please, input your password: ')
    return user_password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friends_id = api.friends.getOnline()
    friends_online = api.users.get(user_ids=friends_id)
    return friends_online


def output_friends_to_console(friends_online):
     for friend in friends_online:
         print(friend['first_name'], friend['last_name'])

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    print('Your friends online:')
    output_friends_to_console(friends_online)
