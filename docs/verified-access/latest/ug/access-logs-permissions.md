---
source_url: https://docs.aws.amazon.com/verified-access/latest/ug/access-logs-permissions.html
---

# Verified Access logging permissions
<a name="access-logs-permissions"></a>

The IAM principal being used to configure the logging destination needs to have certain permissions for logging to work properly. The following sections show the permissions required for each logging destination.

**For delivery to CloudWatch Logs:**
+ `ec2:ModifyVerifiedAccessInstanceLoggingConfiguration` on the Verified Access instance
+ `logs:CreateLogDelivery`, `logs:DeleteLogDelivery`, `logs:GetLogDelivery`, `logs:ListLogDeliveries`, and `logs:UpdateLogDelivery` on all resources
+ `logs:DescribeLogGroups`, `logs:DescribeResourcePolicies`, and `logs:PutResourcePolicy` on the destination log group

**For delivery to Amazon S3:**
+ `ec2:ModifyVerifiedAccessInstanceLoggingConfiguration` on the Verified Access instance
+ `logs:CreateLogDelivery`, `logs:DeleteLogDelivery`, `logs:GetLogDelivery`, `logs:ListLogDeliveries`, and `logs:UpdateLogDelivery` on all resources
+ `s3:GetBucketPolicy` and `s3:PutBucketPolicy` on the destination bucket

**For delivery to Firehose:**
+ `ec2:ModifyVerifiedAccessInstanceLoggingConfiguration` on the Verified Access instance
+ `firehose:TagDeliveryStream` on all resources
+ `iam:CreateServiceLinkedRole` on all resources
+ `logs:CreateLogDelivery`, `logs:DeleteLogDelivery`, `logs:GetLogDelivery`, `logs:ListLogDeliveries`, and `logs:UpdateLogDelivery` on all resources

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Verified Access. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verified-access` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
