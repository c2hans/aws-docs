---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cisco-ise-pipeline-setup.html
---

# CloudWatch pipelines configuration for Cisco ISE
<a name="cisco-ise-pipeline-setup"></a>

The Cisco ISE setup on AWS reads log data from Amazon S3 buckets using Amazon SQS notifications for new object events.

Configure the Cisco ISE source with the following parameters:

```
source:
  s3:
    aws:
      region: "<region>"
      sts_role_arn: "arn:aws:iam::<account>:role/<role-name>"
    compression: "gzip"
    codec:
      multiline:
        continuation_line_end_pattern: "\\\\$"
        omit_matched_section: true
        line_separator: ""
    data_source_name: "cisco_ise"
    notification_type: "sqs"
    sqs:
      queue_url: "https://sqs.<region>.amazonaws.com/<account>/<queue-name>"
```Parameters

`notification_type` (required)
Specifies the notification mechanism. Must be `sqs` to use Amazon SQS for Amazon S3 event notifications.

`data_source_name` (required)
Identifies the data source. Value: `cisco_ise`.

`aws.region` (required)
The AWS Region where the Amazon S3 bucket and Amazon SQS queue are located.

`aws.sts_role_arn` (required)
The ARN of the IAM role to assume for accessing Amazon S3 and Amazon SQS resources.

`codec` (required)
Codec configuration for parsing Amazon S3 objects. Must be `multiline` for ISE syslog format.

`compression` (optional)
Compression type of Amazon S3 objects. Valid values: `gzip`, `none`. Default: `none`.

`sqs.queue_url` (required)
The complete Amazon SQS queue URL that receives Amazon S3 bucket notifications.

`on_error` (optional)
Determines how to handle errors in Amazon SQS. Valid values: `retain_messages`, `delete_messages`. Default: `retain_messages`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
