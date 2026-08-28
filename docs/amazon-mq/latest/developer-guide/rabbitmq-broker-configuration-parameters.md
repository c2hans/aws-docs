---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-broker-configuration-parameters.html
---

# Configuring a RabbitMQ broker
<a name="rabbitmq-broker-configuration-parameters"></a>

A configuration contains all the settings for your RabbitMQ broker in Cuttlefish format. You can create a configuration before creating any brokers. You can then apply the configuration to one or more brokers.

## Attributes
<a name="configuration-attributes"></a>

A broker configuration has several attributes, for example:
+ A name (MyConfiguration)
+ An ID (c-1234a5b6-78cd-901e-2fgh-3i45j6k178l9)
+ An Amazon Resource Name (ARN) (arn:aws:mq:us-east-2:123456789012:configuration:c-1234a5b678cd-901e-2fgh-3i45j6k178l9)

For a full list of configuration attributes, see the following in the Amazon MQ REST API Reference:
+ [REST Operation ID: Configuration](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-configuration.html)
+ [REST Operation ID: Configurations](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-configurations.html)

For a full list of configuration revision attributes, see the following:
+ [REST Operation ID: Configuration Revision](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-configuration-revision.html)
+ [REST Operation ID: Configuration Revisions](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-configuration-revisions.html)

Topics
+ [Creating and applying RabbitMQ broker configurations](rabbitmq-creating-applying-configurations.md)
+ [Edit a Amazon MQ for RabbitMQ Configuration Revision](edit-current-rabbitmq-configuration-console.md)
+ [Configurable values for RabbitMQ on Amazon MQ](configurable-values.md)
+ [ARN support in RabbitMQ configuration](arn-support-rabbitmq-configuration.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MQ. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazon-mq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
