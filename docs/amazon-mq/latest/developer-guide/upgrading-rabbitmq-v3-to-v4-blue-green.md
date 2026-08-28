---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/upgrading-rabbitmq-v3-to-v4-blue-green.html
---

# Blue-green deployment from RabbitMQ 3 to 4
<a name="upgrading-rabbitmq-v3-to-v4-blue-green"></a>

 Amazon MQ does not provide a managed blue-green deployment option for upgrading from RabbitMQ 3.13 to RabbitMQ 4.2. If you choose to perform a blue-green deployment independently, this approach requires application code changes to redirect producers and consumers to the new broker.

 For detailed instructions, see [Blue-green deployment](https://www.rabbitmq.com/docs/blue-green-upgrade) in the RabbitMQ documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MQ. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazon-mq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
