import pika
import sys


class Producer:
    def __init__(self, message):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.exchange_declare(exchange='continuity.event.clustinator.finished',
                                 exchange_type='topic', durable=False, auto_delete=True)

        routing_key = sys.argv[1] if len(sys.argv) > 2 else '#'

        channel.basic_publish(
            exchange='continuity.event.clustinator.finished', routing_key=routing_key, body=message)

        print(" [x] Sent %r:%r" % (routing_key, message))

        connection.close()
