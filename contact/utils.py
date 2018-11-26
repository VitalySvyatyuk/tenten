import json
import base64
from google.cloud import pubsub_v1

from django.conf import settings


def send_to_pubsub(data):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(
        settings.PUBSUB_PROJECT,
        settings.PUBSUB_TOPIC)
    payload = json.dumps(data).encode('ascii')
    publisher.publish(topic_path, data=payload)
    return
