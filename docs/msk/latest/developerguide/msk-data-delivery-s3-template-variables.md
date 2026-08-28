---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-s3-template-variables.html
---

# Variables
<a name="msk-data-delivery-s3-template-variables"></a>

Variables use the `!{name}` syntax. The supported variables are:

| Variable | Description |
| --- | --- |
| `!{channel-id}` | The Channel ID. |
| `!{topic-name}` | The source Kafka topic name. |
| `!{partition-id}` | The source Kafka partition ID. |
| `!{kafka-offset}` | The Kafka offset of the first record in the object. |
| `!{sequence-number}` | A monotonic per-object (batch) sequence number. |
| `!{yyyy}` | Year (4-digit). |
| `!{YY}` | Year (2-digit). |
| `!{MM}` | Month. |
| `!{dd}` | Day. |
| `!{HH}` | Hour (24-hour). |
| `!{mm}` | Minute. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
