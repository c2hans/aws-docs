---
source_url: https://docs.aws.amazon.com/reference-architecture-diagrams/latest/manufacturing-on-aws/mfg-smart-products.html
---

# Smart products
<a name="mfg-smart-products"></a>

The smart products diagram shows how to connect manufactured products and machines to AWS for telemetry and event processing.

![Smart products diagram for connecting manufactured products to AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/manufacturing-on-aws/images/manufacturing-on-aws-ra-5.png)

1. Use [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/) to connect products by using MQTT (Message Queuing Telemetry Transport).

1. Ingest telemetry to Amazon S3 with Amazon Data Firehose for durable storage.

1. Define event logic with [AWS IoT Events](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/internet-of-things-services.html#aws-iot-events) and [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/) for alerting.

1. Build microservices with Lambda and [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) to process telemetry and serve applications.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Reference Architecture Diagrams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query reference-architecture-diagrams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
