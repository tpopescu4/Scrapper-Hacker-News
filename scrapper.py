#importing libraries

from bs4 import BeautifulSoup

import requests


#constructor for storing attributes

class HackerNews:

    def __init__(self, rank, title, points, comments):

        self.rank = rank
        self.title = title
        self.points = points
        self.comments = comments


#function to print the list of news

def print_list(p_list):

	for e in p_list:

			print(e.rank, end=" ")

			print(e.title, end=" ")

			if e.points != -1:

				print("No votes", end=" ")
			else:

				print(e.points, end=" points ")

			if e.comments == -1:

				print("No comments", end=" ")
			else:

				print(e.comments, end=" comments ")

			print("\n")

#initializing lists
list_title = []

list_points = []

list_comments = []

list_news = []

list_by_comms = []

list_by_points = []

#getting the html from the url
result = requests.get('https://news.ycombinator.com')
content = result.text
soup = BeautifulSoup(result.content, 'html.parser')

#tags in which we'll find the information
eq = soup.find('table')
eq1 = eq.find_all('a', class_='titlelink')
eq2 = eq.find_all('td', class_='subtext')

#getting titles
for e in eq1:
	list_title.append(e.text)

#getting the points and comments from each td
for e in eq2:
	subtext = e.text
	subtext = ' '.join(subtext.split())
	subtext = subtext.split(" ")
	if "points" in e.text:
		list_points.append(int(subtext[0]))
	else:
		list_points.append(-1)
	if "comments" in e.text:
		list_comments.append(int(subtext[10]))
	else:
		list_comments.append(-1)

#adding each object to the list
for i in range(30):
	list_news.append(HackerNews(i + 1, list_title[i], list_points[i], list_comments[i]))

#filtering titles with more than 5 words or with 5 or less words
for e in list_news:
	if str(e.title).__len__() > 5:
		list_by_comms.append(e)
	else:
		list_by_points.append(e)

#sorting by comments
list_by_comms.sort(key=lambda x: x.comments, reverse=True)
#sorting by points
list_by_points.sort(key=lambda x: x.points, reverse=True)

#printing the information
print("Hacker News\n")
print_list(listnews)
print("Hacker News filtered by comments\n")
print_list(list_by_comms) 
print("Hacker News filtered by points")
print_list(list_by_points)
