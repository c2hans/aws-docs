---
source_url: https://docs.aws.amazon.com/lambda/latest/dg/services-mq-errors.html
---

# Troubleshoot Amazon MQ event source mapping errors
<a name="services-mq-errors"></a>

When a Lambda function encounters an unrecoverable error, your Amazon MQ consumer stops processing records. Any other consumers can continue processing, provided that they do not encounter the same error. To determine the potential cause of a stopped consumer, check the `StateTransitionReason` field in the return details of your `EventSourceMapping` for one of the following codes:

**`ESM_CONFIG_NOT_VALID`**
The event source mapping configuration is not valid.

**`EVENT_SOURCE_AUTHN_ERROR`**
Lambda failed to authenticate the event source.

**`EVENT_SOURCE_AUTHZ_ERROR`**
Lambda does not have the required permissions to access the event source.

**`FUNCTION_CONFIG_NOT_VALID`**
The function's configuration is not valid.

Records also go unprocessed if Lambda drops them due to their size. The size limit for Lambda records is 6 MB. To redeliver messages upon function error, you can use a dead-letter queue (DLQ). For more information, see [Message Redelivery and DLQ Handling](https://activemq.apache.org/message-redelivery-and-dlq-handling) on the Apache ActiveMQ website and [Reliability Guide](https://www.rabbitmq.com/reliability.html) on the RabbitMQ website.

**Note**
Lambda does not support custom redelivery policies. Instead, Lambda uses a policy with the default values from the [Redelivery Policy](https://activemq.apache.org/redelivery-policy) page on the Apache ActiveMQ website, with `maximumRedeliveries` set to 6.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
