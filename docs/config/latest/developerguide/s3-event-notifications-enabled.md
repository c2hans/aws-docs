---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/s3-event-notifications-enabled.html
---

# s3-event-notifications-enabled
<a name="s3-event-notifications-enabled"></a>

Checks if Amazon S3 Events Notifications are enabled on an S3 bucket. The rule is NON\_COMPLIANT if S3 Events Notifications are not set on a bucket, or if the event type or destination do not match the `eventTypes` and destinationArn parameters.

**Identifier:** S3\_EVENT\_NOTIFICATIONS\_ENABLED

**Resource Types:** AWS::S3::Bucket

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Mexico (Central), Asia Pacific (Taipei) Region

**Parameters:**

destinationArn (Optional)Type: String
The Amazon Resource Name (ARN) of the destination for the event notification (Amazon SNS topic, AWS Lambda, Amazon SQS Queue).

eventTypes (Optional)Type: CSV
Comma-separated list of the preferred Amazon S3 event types

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1421c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
