#!/usr/bin/env python3
import vk
import login_info

user_list = []
for line in open('user_list', 'r'):
  user_list.append(line)
user_ids = ','.join(user_list)

vkapi = vk.API(app_id=login_info.app_id(), access_token=login_info.access_token())

users = vkapi.users.get(user_ids=user_ids, fields='name,online', count=5)
for user in users:
  print(user.get('first_name') + ' ' + user.get('last_name') + ' ' + str(user.get('online')))
