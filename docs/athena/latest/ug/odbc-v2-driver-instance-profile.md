---
source_url: https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-instance-profile.html
---

# Instance profile
<a name="odbc-v2-driver-instance-profile"></a>

This authentication type is used on EC2 instances and is delivered through the Amazon EC2 metadata service.

## Authentication type
<a name="odbc-v2-driver-instance-profile-authentication-type"></a>

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| --- | --- | --- | --- |
| AuthenticationType | Required | IAM Credentials | AuthenticationType=Instance Profile; |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
