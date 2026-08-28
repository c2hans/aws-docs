---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-iceberg-metrics.html
---

# Amazon CloudWatch metrics
<a name="msk-data-delivery-iceberg-metrics"></a>

| Metric name | Description | Unit |
| --- | --- | --- |
| `DeliveryToIceberg.DataFreshness` | Age of the oldest record delivered; rising values indicate delivery lag or stall. | Seconds |
| `DeliveryToIceberg.BytesIn` | Volume read into the delivery path. | Bytes |
| `DeliveryToIceberg.BytesProcessed` | Volume processed. | Bytes |
| `DeliveryToIceberg.BytesOut` | Volume written to the destination. | Bytes |
| `DeliveryToIceberg.TotalRowCount` | Total rows seen. | Count |
| `DeliveryToIceberg.SuccessfulRowCount` | Rows delivered successfully. | Count |
| `DeliveryToIceberg.FailedRowCount` | Rows that failed delivery; non-zero is the key error signal. | Count |
| `DeliveryToIceberg.CommitSuccess` | Successful Iceberg commits. | Count |
| `DeliveryToIceberg.DLQDeliverySuccess` | Records successfully routed to the dead-letter queue. | Count |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
