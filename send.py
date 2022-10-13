import pika

credentials = pika.PlainCredentials('admin', 'lalula2702')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('nigma.uz', port=5672, virtual_host='/', credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=b'Hello world')
print(" [x] Sent 'Hello World!'")
connection.close()
