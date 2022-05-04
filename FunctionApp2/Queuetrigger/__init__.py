import logging

import azure.functions as func

def main(msg: func.ServiceBusMessage,
         msg2: func.Out[func.QueueMessage]) -> str:
    logging.info('Python ServiceBus queue trigger processed message: %s',
                 msg.get_body().decode('utf-8'))
    logging.info('Dit is een test: %s',
                 msg.get_body().decode('utf-8'))
    msg2.set(msg.get_body().decode('utf-8'))
    logging.info(msg2)
