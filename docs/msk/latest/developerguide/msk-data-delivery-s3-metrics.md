---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-s3-metrics.html
---

# Amazon CloudWatch metrics
<a name="msk-data-delivery-s3-metrics"></a>

| Metric name | Description | Unit |
| --- | --- | --- |
| `DeliveryToS3.DataFreshness` | Age of the oldest record delivered; rising values indicate delivery lag or stall. | Seconds |
| `DeliveryToS3.BytesIn` | Volume read into the delivery path. | Bytes |
| `DeliveryToS3.BytesProcessed` | Volume processed. | Bytes |
| `DeliveryToS3.BytesOut` | Volume written to the destination. | Bytes |
| `DeliveryToS3.RecordCount` | Total records seen. | Count |
| `DeliveryToS3.SuccessfulRecordCount` | Records delivered successfully. | Count |
| `DeliveryToS3.FailedRecordCount` | Records that failed delivery; non-zero is the key error signal. | Count |
| `DeliveryToS3.DeliverySuccess` | Successful delivery operations. | Count |
| `DeliveryToS3.DLQDeliverySuccess` | Records successfully routed to the dead-letter queue. | Count |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
