# 95% query http 10 users
# - insert new user
# - get data for a given user
# - 10 users in the cache

USER=0
DATA=1
user_data = [] # retain order
user_map = {}

first = None

def insert_user(user, data):
    user_index = -1

    meta = ( data, None, first )

    if user in user_map:
        ( data, prev, nxt ) = user_map[user]

        tmp = prev
        if prev is not None:
            prev = nxt
        if nxt is not None:
            nxt = tmp
        del user_map[user]
    user_map[user] = meta
    first = meta
    

def get_data_for_user(user):
    ( data, prev, nxt ) = user_map[user]
    return data

if __name__ == "__main__":
    users = {
        '1': ('datadata', None, '2'),
        '2': ('datadat', 1, 3),
        '3': 'datada',
        '4': 'datad',
        '5': 'data',
        '6': 'dat',
    }

    insert_user('1', users['1'])
    print get_data_for_user('1')

