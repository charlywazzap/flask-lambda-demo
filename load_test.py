from locust import HttpUser, task,between
import random
class RandomApiUser(HttpUser):
    wait_time = between(0.5, 5)
    @task(2)
    def hello_world(self):
        self.client.get("/")

    @task(2)
    def get_users(self):
        id = random.randrange(2000)
        self.client.get(f"/users/{id}")

    @task(1)
    def try_error(self):
        self.client.get(f"/random_err/")
