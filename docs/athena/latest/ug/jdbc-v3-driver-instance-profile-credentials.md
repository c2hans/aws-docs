---
source_url: https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-instance-profile-credentials.html
---

# Instance profile credentials
<a name="jdbc-v3-driver-instance-profile-credentials"></a>

This authentication type is used on Amazon EC2 instances. An *instance profile* is a profile attached to an Amazon EC2 instance. Using an instance profile credentials provider delegates the management of AWS credentials to the Amazon EC2 Instance Metadata Service. This removes the need for developers to store credentials permanently on the Amazon EC2 instance or worry about rotating or managing temporary credentials.

## Credentials provider
<a name="jdbc-v3-driver-instance-profile-credentials-provider"></a>

The credentials provider that will be used to authenticate requests to AWS. Set the value of this parameter to `InstanceProfile`.

| Parameter name | Alias | Parameter type | Default value | Value to use |
| --- | --- | --- | --- | --- |
| CredentialsProvider | AWSCredentialsProviderClass (deprecated) | Required | none | InstanceProfile |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
