---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-iam.html
---

# IAM roles and policies for MSK Connect
<a name="msk-connect-iam"></a>

This section helps you set up the appropriate IAM policies and roles to securely deploy and manage Amazon MSK Connect within your AWS environment. The following sections explain the service execution role that must be used with MSK Connect, including the required trust policy and additional permissions needed when connecting to an IAM-authenticated MSK cluster. The page also provides examples of comprehensive IAM policies to grant full access to MSK Connect functionality, as well as details on AWS managed policies available for the service.

**Topics**
+ [Understand service execution role](msk-connect-service-execution-role.md)
+ [Example of IAM policy for MSK Connect](mkc-iam-policy-examples.md)
+ [Prevent cross-service confused deputy problem](cross-service-confused-deputy-prevention.md)
+ [AWS managed policies for MSK Connect](mkc-security-iam-awsmanpol.md)
+ [Use service-linked roles for MSK Connect](mkc-using-service-linked-roles.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
