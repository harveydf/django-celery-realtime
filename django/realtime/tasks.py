import time
import redis
from celery import task

redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

@task(bind=True)
def generate_csv(self):
    time.sleep(10)
    redis_client.publish(self.request.id, 'http://bit.ly/2a2EiIQ')
