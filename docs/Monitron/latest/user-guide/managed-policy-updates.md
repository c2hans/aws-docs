---
source_url: https://docs.aws.amazon.com/Monitron/latest/user-guide/managed-policy-updates.html
---

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Amazon Monitron updates to AWS managed policies
<a name="managed-policy-updates"></a>

View details about updates to AWS managed policies for Amazon Monitron since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the Amazon Monitron document history page.

| Change | Description | Date |
| --- | --- | --- |
| AWSServiceRoleForMonitronPolicy - Update to an existing policy | Added `sso:CreateApplicationAssignment` and `sso:ListApplicationAssignments` to [role permissions policy](https://docs.aws.amazon.com/Monitron/latest/user-guide/using-service-linked-roles.html). | September 30, 2024 |
| AmazonMonitronFullAccess - Update to an existing policy | Amazon Monitron added permissions to describe and list Kinesis Data Streams, and describe get, and create CloudWatch log groups, log streams, and log events.<br />You must use these permissions to use the Amazon Monitron console to display information about Kinesis Data Streams and CloudWatch Logs. | June 8, 2022 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Monitron. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Monitron` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
