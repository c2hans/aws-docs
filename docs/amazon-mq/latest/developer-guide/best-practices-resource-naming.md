---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/best-practices-resource-naming.html
---

# Best practices for resource naming in Amazon MQ for RabbitMQ
<a name="best-practices-resource-naming"></a>

 Although RabbitMQ permits arbitrary UTF-8 characters in vhost names, queue names, exchange names, and policy names, Amazon MQ for RabbitMQ recommends using a standard character set.

## Naming conventions
<a name="naming-conventions"></a>

 We recommend following supported characters for vhost names, queue names, exchange names, and policy names:
+ Letters (A–Z, a–z)
+ Numbers (0–9)
+ Hyphens (`-`), underscores (`_`), periods (`.`), colons (`:`), and forward slashes (`/`)

**Important**
Using other special characters in vhost names, queue names, exchange names, or policy names may prevent Amazon MQ from performing certain broker maintenance operations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MQ. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazon-mq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
