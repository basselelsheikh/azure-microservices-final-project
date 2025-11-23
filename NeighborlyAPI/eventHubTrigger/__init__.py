import json
import logging
import azure.functions as func


def main(event: func.EventGridEvent):

    event_data = event.get_json() 

    logging.info('Function triggered to process an Event Grid message.')
    logging.info(f'Event ID: {event.id}')
    logging.info(f'Topic: {event.topic}, Subject: {event.subject}')
    logging.info(f'Event Type: {event.event_type}, Event Time: {event.event_time}')
    
    logging.info(f'Event Data (JSON): {event_data}')

    result = json.dumps({
        'id': event.id,
        'data': event_data,
        'topic': event.topic,
        'subject': event.subject,
        'event_type': event.event_type,
    })

    logging.info('Python EventGrid trigger successfully processed the event: %s', result)