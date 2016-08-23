import praw
import time


already_replied = []

while True:
	print('Entering True')
	r = praw.Reddit(user_agent='This is a Dog Lover\'s script by /u/AFake_Opitic')
	r.login('ILoveDogsbot', 'nick135376')
	for comment in praw.helpers.comment_stream(r, 'aww', limit=30):
		if 'i love cats' in comment.body.lower() and comment.id not in already_replied:
			print('Entering if')
			comment.reply('I Love Dogs! They are superior!\n\nI am a bot. you can provide me feedback at /r/ilovedogsbot!')
			already_replied.add(comment.id)
			print('commented')
	print('entering sleep')
	time.sleep(10)
