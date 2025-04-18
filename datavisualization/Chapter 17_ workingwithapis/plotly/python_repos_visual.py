import requests
from plotly.graph_objs import Bar
from plotly import offline
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars, labels = [], [], []
for repo_dict in repo_dicts:
	repo_names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])
	owner = repo_dict['owner']['login']
	description = repo_dict['description']
	label = f"{owner}<br />{description}"
	labels.append(label)

data = [{
	'type': 'bar',
	'x': repo_names,
	'y': stars,
	'hovertext': labels,
	'marker': {
		'color': 'rgb(60, 100, 150)',
		'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
	},
	'opacity': 0.6,
}]
my_layout = {
	'title': 'Most-Starred Python Projects on GitHub',
	'xaxis': {
		'title': 'Repository',
		
	},
	'yaxis': {
		'title': 'Stars',
		
	},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')



