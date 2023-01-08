import praw
import re
import pdb
import os
import string
import traceback
from time import sleep
import pprint
reddit=praw.Reddit(client_id='',
	               client_secret='',
	               username='',
	               password='',
	               user_agent='')

while True:

	comments = reddit.user.me().comments.new(limit=25)
	for comment in comments:
			#	comment_score=str(comment.score)
		if comment.score <= 0:
			comment.delete()
