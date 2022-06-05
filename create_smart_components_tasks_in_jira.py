import argparse
from jira import JIRA

jiraOptions = {'server': "PROJECT URL IN JIRA LIKE https://something.atlassian.net/"}

jira = JIRA(options=jiraOptions, basic_auth=(
    "ACCOUNT EMAIL", "API KEY"))


parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', dest='name', help='Name')
parser.add_argument('-u', '--url', dest='url', help='URL')
args = parser.parse_args()

epic_name = 'Short name for {}'.format(args.name)
epic_summary = 'Do something {}'.format(args.name)
epic_description = 'Domain: {} \n\n and some text'.format(args.url)

# Create an EPIC
new_epic = jira.create_issue(project='TEST',
                             customfield_10011=epic_name,
                             summary=epic_summary,
                             description=epic_description,
                             issuetype={'name': 'Epic'},
                             )
# Subtask list
sm_list = [
    {'name': 'Subtask 1',
        'link': 'test1.com'},
    {'name': 'Subtask 2',
        'link': 'test2.com'},
    {'name': 'Subtask 3',
        'link': 'test3.com'},
    {'name': 'Subtask 4',
        'link': 'test4.com'},
    {'name': 'Subtask 5',
        'link': 'test5.com'},
    {'name': 'Subtask 6',
        'link': 'test6.com'},
    {'name': 'Subtask 7',
        'link': 'test7.com'},
]

# Add subtusk to EPIC
for c in sm_list:
    new_issue = jira.create_issue(project='TEST',
                                  summary='{} - {}'.format(args.name,
                                                           c['name']),
                                  customfield_10014=new_epic.key,
                                  description='*Subject* \n {} \n\n *Design example* \n {} \n\n *Mobile* \n\n *Desktop* \n\n'.format(
                                      args.url, c['link']),
                                  issuetype={'name': 'Task'},
                                  )
