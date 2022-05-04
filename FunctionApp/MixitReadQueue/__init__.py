import logging

import azure.functions as func


def main(msg: func.ServiceBusMessage):
    logging.info('Python ServiceBus queue trigger processed messagefgiohjiofghjofg: %s',
                 msg.get_body().decode('utf-8'))
