---
source_url: https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-default-credentials.html
---

# Default credentials
<a name="odbc-v2-driver-default-credentials"></a>

You can use the default credentials that you configure on your client system to connect to Amazon Athena. For information about using default credentials, see [Using the Default Credential Provider Chain](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html#credentials-default) in the *AWS SDK for Java Developer Guide*.

## Authentication type
<a name="odbc-v2-driver-default-credentials-authentication"></a>

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| --- | --- | --- | --- |
| AuthenticationType | Required | IAM Credentials | AuthenticationType=Default Credentials; |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
