from git import Repo
import git
remoteUrl = 'https://github.com/arijitbanerjee12/slackautomation.git'
localFolder = '/tmp/slackautomation'

myrepo = git.Repo.clone_from(remoteUrl,localFolder)