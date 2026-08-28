---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/va-sample-lambda.html
---

# Voice analytics example Lambda function for the Amazon Chime SDK
<a name="va-sample-lambda"></a>

The Python code in the following example processes notifications received from a Voice Connector. You can add the code to an AWS Lambda function. You can also use it to trigger your Amazon SQS queue, Amazon SNS topic, or Amazon Kinesis Data Stream. You can then store the notifications in an `EventTable` for future processing. For the exact notification formats, see [Understanding notifications for the Amazon Chime SDK](va-notification-targets.md).

```
import base64
import boto3
import json
import logging
import time

from datetime import datetime
from enum import Enum

log = logging.getLogger()
log.setLevel(logging.INFO)

dynamo = boto3.client("dynamodb")

EVENT_TABLE_NAME = "EventTable"

class EventType(Enum):
    """
    This example code uses a single Lambda processor to handle either
    triggers from SQS, SNS, Lambda, or Kinesis. You can adapt it to fit your
    desired infrastructure depending on what you prefer. To distinguish
    where we get events from, we use an EventType enum as an
    example to show the different ways of parsing the notifications.
    """
    SQS = "SQS"
    SNS = "SNS"
    LAMBDA = "LAMBDA"
    KINESIS = "KINESIS"

class AnalyticsType(Enum):
    """
    Define the various analytics event types that this Lambda will
    handle.
    """
    SPEAKER_SEARCH = "SpeakerSearch"
    VOICE_TONE_ANALYSIS = "VoiceToneAnalysis"
    ANALYTICS_READY = "AnalyticsReady"
    UNKNOWN = "UNKNOWN"

class DetailType(Enum):
    """
    Define the  various detail types that Voice Connector's voice
    analytics feature can return.
    """
    SPEAKER_SEARCH_TYPE = "SpeakerSearchStatus"
    VOICE_TONE_ANALYSIS_TYPE = "VoiceToneAnalysisStatus"
    ANALYTICS_READY = "VoiceAnalyticsStatus"

def handle(event, context):
    """
    Example of how to handle incoming Voice Analytics notification messages
    from Voice Connector.
    """
    logging.info(f"Received event of type {type(event)} with payload {event}")
    is_lambda = True

    # Handle triggers from SQS, SNS, and KDS. Use the below code if you would like
    # to use this Lambda as a trigger for an existing SQS queue, SNS topic or Kinesis
    # stream.
    if "Records" in event:
        logging.info("Handling event from SQS or SNS since Records exists")
        is_lambda = False
        for record in event.get("Records", []):
            _process_record(record)

    # If you would prefer to have your Lambda invoked directly, use the
    # below code to have the Voice Connector directly invoke your Lambda.
    # In this scenario, there are no "Records" passed.
    if is_lambda:
        logging.info(f"Handling event from Lambda")
        event_type = EventType.LAMBDA
        _process_notification_event(event_type, event)

def _process_record(record):
    # SQS and Kinesis use eventSource.
    event_source = record.get("eventSource")

    # SNS uses EventSource.
    if not event_source:
        event_source = record.get("EventSource")

    # Assign the event type explicitly based on the event source value.
    event_type = None
    if event_source == "aws:sqs":
        event = record["body"]
        event_type = EventType.SQS
    elif event_source == "aws:sns":
        event = record["Sns"]["Message"]
        event_type = EventType.SNS
    elif event_source == "aws:kinesis":
        raw_data = record["kinesis"]["data"]
        raw_message = base64.b64decode(raw_data).decode('utf-8')
        event = json.loads(raw_message)
        event_type = EventType.KINESIS
    else:
        raise Exception(f"Event source {event_source} is not supported")

    _process_notification_event(event_type, event)

def _process_notification_event(
    event_type: EventType,
    event: dict
):
    """
    Extract the attributes from the Voice Analytics notification message
    and store it as a DynamoDB item to process later.
    """
    message_id = event.get("id")
    analytics_type = _get_analytics_type(event.get("detail-type"))
    pk = None
    if analytics_type == AnalyticsType.ANALYTICS_READY.value or analytics_type == AnalyticsType.UNKNOWN.value:
        transaction_id = event.get("detail").get("transactionId")
        pk = f"transactionId#{transaction_id}#notificationType#{event_type.value}#analyticsType#{analytics_type}"
    else:
        task_id = event.get("detail").get("taskId")
        pk = f"taskId#{task_id}#notificationType#{event_type.value}#analyticsType#{analytics_type}"
    logging.info(f"Generated PK {pk}")
    _create_request_record(pk, message_id, json.dumps(event))

def _create_request_record(pk: str, sk: str, body: str):
    """
    Record this notification message into the Dynamo db table
    """
    try:
        # Use consistent ISO8601 date format.
        # 2019-08-01T23:09:35.369156 -> 2019-08-01T23:09:35.369Z
        time_now = (
            datetime.utcnow().isoformat()[:-3] + "Z"
        )
        response = dynamo.put_item(
            Item={
                "PK": {"S": pk},
                "SK": {"S": sk},
                "body": {"S": body},
                "createdOn": {"S": time_now},
            },
            TableName=EVENT_TABLE_NAME,
        )
        logging.info(f"Added record in table {EVENT_TABLE_NAME}, response : {response}")
    except Exception as e:
        logging.error(f"Error in adding record: {e}")

def _get_analytics_type(detail_type: str):
    """
    Get analytics type based on message detail type value.
    """
    if detail_type == DetailType.SPEAKER_SEARCH_TYPE.value:
        return AnalyticsType.SPEAKER_SEARCH.value
    elif detail_type == DetailType.VOICE_TONE_ANALYSIS_TYPE.value:
        return AnalyticsType.VOICE_TONE_ANALYSIS.value
    elif detail_type == DetailType.ANALYTICS_READY.value:
        return AnalyticsType.ANALYTICS_READY.value
    else:
        return AnalyticsType.UNKNOWN.value
```

**Important**
You must receive consent before you call the [StartSpeakerSearchTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_StartSpeakerSearchTask) or [StartVoiceToneAnalysis](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_StartVoiceToneAnalysis.html) APIs. We recommend that you persist the events in a holding area, such as Amazon DynamoDB, until you receive consent.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
