---
source_url: https://docs.aws.amazon.com/lambda/latest/dg/kafka-starting-positions.html
---

# Apache Kafka polling and stream starting positions in Lambda
<a name="kafka-starting-positions"></a>

The [ StartingPosition parameter](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html#lambda-CreateEventSourceMapping-request-StartingPosition) tells Lambda when to start reading messages from your Amazon MSK or self-managed Apache Kafka stream. There are three options to choose from:
+ **Latest** – Lambda starts reading just after the most recent record in the Kafka topic.
+ **Trim horizon** – Lambda starts reading from the last untrimmed record in the Kafka topic. This is also the oldest record in the topic.
+ **At timestamp** – Lambda starts reading from a position defined by a timestamp, in Unix time seconds. Use the [ StartingPositionTimestamp parameter](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html#lambda-CreateEventSourceMapping-request-StartingPositionTimestamp) to specify the timestamp.

Stream polling during an event source mapping create or update is eventually consistent:
+ During event source mapping creation, it might take several minutes to start polling events from the stream.
+ During event source mapping updates, it might take up to 90 seconds to stop and restart polling events from the stream.

This behavior means that if you specify `LATEST` as the starting position for the stream, the event source mapping could miss events during a create or update. To ensure that no events are missed, specify either `TRIM_HORIZON` or `AT_TIMESTAMP`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
