---
source_url: https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-default-credentials.html
---

# Default credentials
<a name="jdbc-v3-driver-default-credentials"></a>

You can use the default credentials that you configure on your client system to connect to Amazon Athena by setting the following connection parameters. For information about using default credentials, see [Using the Default Credential Provider Chain](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html#credentials-default) in the *AWS SDK for Java Developer Guide*.

## Credentials provider
<a name="jdbc-v3-driver-credentials-provider"></a>

The credentials provider that will be used to authenticate requests to AWS. Set the value of this parameter to `DefaultChain`.

| Parameter name | Alias | Parameter type | Default value | Value to use |
| --- | --- | --- | --- | --- |
| CredentialsProvider | AWSCredentialsProviderClass (deprecated) | Required | none | DefaultChain |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
