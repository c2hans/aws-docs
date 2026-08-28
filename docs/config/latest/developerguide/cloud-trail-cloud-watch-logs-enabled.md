---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/cloud-trail-cloud-watch-logs-enabled.html
---

# cloud-trail-cloud-watch-logs-enabled
<a name="cloud-trail-cloud-watch-logs-enabled"></a>

Checks if AWS CloudTrail trails are configured to send logs to CloudWatch logs. The trail is NON\_COMPLIANT if the CloudWatchLogsLogGroupArn property of the trail is empty.

**Identifier:** CLOUD\_TRAIL\_CLOUD\_WATCH\_LOGS\_ENABLED

**Resource Types:** AWS::CloudTrail::Trail

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

expectedDeliveryWindowAge (Optional)Type: int
Maximum age in hours of the most recent delivery to CloudWatch logs that satisfies compliance.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d361c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
