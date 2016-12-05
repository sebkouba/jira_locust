# -*- coding: utf-8 -*-
from locust import HttpLocust, TaskSet, task
from credentials import username, password


# try logging in!


class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start called when a Locust start before any task is scheduled """
        self.login()

    def login(self):
        login_url = "/rest/auth/1/session"
        headers = {'Content-Type': 'application/json'}
        self.client.post(login_url,
                         json={"username": username, "password": password},
                         headers=headers)

    @task(1)
    def index(self):
        self.client.get("/")

    @task(3)
    def search(self):
        self.client.get("/issues/?jql=")


    @task(10)
    def myopentasks(self):
        self.client.get("/issues/?filter=-1")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 2000
