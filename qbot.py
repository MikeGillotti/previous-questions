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



if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to))
allsub=reddit.subreddit("NoStupidQuestions+askreddit+answers+advice+help+tooafraidtoask")

nostupidq=reddit.subreddit("explainlikeimfive")
for posts in nostupidq.stream.submissions():
	if posts.id not in posts_replied_to:
		self_text = str(posts.selftext)
		if not self_text:
			if len(posts.title) > 15:

				searchlist =[]
				searchlist2 =[]

				post_title=re.escape(posts.title)
				nostupid_results=list(nostupidq.search('title:'+post_title, limit=10))
				search_results=list(allsub.search('title:'+post_title, limit=10))
	
				for i in search_results:
					if i != posts.id:

						searchlist.append('['+i.title+']('+i.permalink+')'+"\n\n")
				search_results_txt=map(str, searchlist)

				for i in nostupid_results:
					if i != posts.id:

						searchlist2.append('['+i.title+']('+i.permalink+')'+"\n\n")
				nostupid_results_txt=map(str, searchlist2)

				if not searchlist2:
					nostupid_results_text_show='';
				else:
					nostupid_results_text_show='From this subreddit, \n\n- '+'- '.join(nostupid_results_txt)+'\n\n'

				if not searchlist:
					search_results_txt_show='';
				else:
					search_results_txt_show='From other subreddits, \n\n- '+'- '.join(search_results_txt)

				if len(searchlist) + len(searchlist2) > 0:
					str_title=str(posts.title)
					reddit_user=str(posts.author)

					posts.reply('Hello '+reddit_user+',\n\n I would like to help you find what you'+"'"+'re looking for. \n\n '+nostupid_results_text_show+ search_results_txt_show)


					print('*****'+posts.title+'******')
					for i in search_results:
						if i != posts.id:

							print(i.title)
					print("---------------")
					posts_replied_to.append(posts.id)
		with open("posts_replied_to.txt", "w") as f:
			for p in posts_replied_to:
				f.write(p + "\n")
	
