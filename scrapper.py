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

def printList(pList):

	for e in pList:

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
listtitle = []

listpoints = []

listcomments = []

listnews = []

list1 = []

list2 = []

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
	listtitle.append(e.text)

#getting the points and comments from each td
for e in eq2:
	subtext = e.text
	subtext = ' '.join(subtext.split())
	subtext = subtext.split(" ")
	if "points" in e.text:
		listpoints.append(int(subtext[0]))
	else:
		listpoints.append(-1)
	if "comments" in e.text:
		listcomments.append(int(subtext[10]))
	else:
		listcomments.append(-1)

#adding each object to the list
for i in range(30):
	listnews.append(HackerNews(i + 1, listtitle[i], listpoints[i], listcomments[i]))

#filtering titles with more than 5 words or with 5 or less words
for e in listnews:
	if str(e.title).__len__() > 5:
		list1.append(e)
	else:
		list2.append(e)

#sorting by comments
list1.sort(key=lambda x: x.comments, reverse=True)
#sorting by points
list2.sort(key=lambda x: x.points, reverse=True)

#printing the information
print("Hacker News\n")
printList(listnews)
print("Hacker News filtered by comments\n")
printList(list1)
print("Hacker News filtered by points")
printList(list2)