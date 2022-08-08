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
		if e.points == -1:
			print("No votes", end=" ")
		else:
			print(e.points, end=" points ")
		if e.comments == -1:
			print("No comments", end=" ")
		else:
			print(e.comments, end=" comments ")
		print("\n")

#initializing lists
titles = []
points = []
comments = []
news = []
by_comms = []
by_points = []

#getting the html from the url
result = requests.get('https://news.ycombinator.com')
content = result.text
soup = BeautifulSoup(result.content, 'html.parser')

#tags in which we'll find the information
table = soup.find('table')
title_tag = table.find_all('a', class_='titlelink')
subtext_tag = table.find_all('td', class_='subtext')

#getting titles
for e in title_tag:
	titles.append(e.text)

#getting the points and comments from each td
for e in subtext_tag:
	text = e.text
	text = ' '.join(text.split())
	text = text.split(" ")
	print(text)
	if "points" in e.text:
		points.append(int(text[0]))
	else:
		points.append(-1)
	if "comments" in e.text and "points" in e.text:
		comments.append(int(text[10]))
	elif "comments" in e.text:
		comments.append(int(text[8]))
	else:
		comments.append(-1)

#adding each object to the list
for i in range(30):
	news.append(HackerNews(i + 1, titles[i], points[i], comments[i]))

#filtering titles with more than 5 words or with 5 or less words
for e in news:
	if str(e.title).__len__() > 5:
		by_comms.append(e)
	else:
		by_points.append(e)

#sorting by comments
by_comms.sort(key=lambda x: x.comments, reverse=True)
#sorting by points
by_points.sort(key=lambda x: x.points, reverse=True)

#printing the information
print("Hacker News:\n")
print_list(news)
if by_comms:
	print("Hacker News filtered by comments with more than 5 words on the title:\n")
	print_list(by_comms)
if by_points:
	print("Hacker News filtered by points with 5 or less words on the title:\n")
	print_list(by_points)