---
source_url: https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-custom-credentials.html
---

# Custom credentials
<a name="jdbc-v3-driver-custom-credentials"></a>

You can use this authentication type to provide your own credentials by using a Java class that implements the [AwsCredentialsProvider](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/auth/credentials/AwsCredentialsProvider.html) interface.

## Credentials provider
<a name="jdbc-v3-driver-custom-credentials-credentials-provider"></a>

The credentials provider that will be used to authenticate requests to AWS. Set the value of this parameter to the fully qualified class name of the custom class that implements the [AwsCredentialsProvider](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/auth/credentials/AwsCredentialsProvider.html) interface. At runtime, that class must be on the Java class path of the application that uses the JDBC driver.

| Parameter name | Alias | Parameter type | Default value | Value to use |
| --- | --- | --- | --- | --- |
| CredentialsProvider | AWSCredentialsProviderClass (deprecated) | Required | none | The fully qualified class name of the custom implementation of AwsCredentialsProvider |

## Credentials provider arguments
<a name="jdbc-v3-driver-credentials-provider-arguments"></a>

A comma-separated list of string arguments for the custom credentials provider constructor.

| Parameter name | Alias | Parameter type | Default value |
| --- | --- | --- | --- |
| CredentialsProviderArguments | AwsCredentialsProviderArguments (deprecated) | Optional | none |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
