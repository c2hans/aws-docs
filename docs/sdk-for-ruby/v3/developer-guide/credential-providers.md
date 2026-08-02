---
source_url: https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/credential-providers.html
---

# Using AWS SDK for Ruby credential providers
<a name="credential-providers"></a>

All requests to AWS must be cryptographically signed by using credentials issued by AWS. At runtime, the SDK retrieves configuration values for credentials by checking several locations.

Authentication with AWS can be handled outside of your codebase. Many authentication methods can be automatically detected, used, and refreshed by the SDK using the credential provider chain.

For guided options for getting started on AWS authentication for your project, see [Authentication and access](https://docs.aws.amazon.com/sdkref/latest/guide/access.html) in the *AWS SDKs and Tools Reference Guide*.

## Credential provider chain
<a name="credchain"></a>

All SDKs have a series of places (or sources) that they check in order to get valid credentials to use to make a request to an AWS service. After valid credentials are found, the search is stopped. This systematic search is called the default credential provider chain.

**Note**
If you followed the recommended approach for new users to get started, you authenticated using login with console credentials during [Authenticating with AWS using AWS SDK for Ruby](credentials.md). Other authentication methods are useful for different situations. To avoid security risks, we recommend always using short-term credentials. For other authentication method procedures, see [Authentication and access](https://docs.aws.amazon.com/sdkref/latest/guide/access.html) in the *AWS SDKs and Tools Reference Guide*.

For each step in the chain, there are different ways to set the values. Setting values directly in code always takes precedence, followed by setting as environment variables, and then in the shared AWS `config` file.

The *AWS SDKs and Tools Reference Guide* has information on SDK configuration settings used by all AWS SDKs and the AWS CLI. To learn more about how to configure the SDK through the shared AWS `config` file, see [Shared config and credentials files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html). To learn more about how to configure the SDK through setting environment variables, see [Environment variables support](https://docs.aws.amazon.com/sdkref/latest/guide/environment-variables.html).

To authenticate with AWS, the AWS SDK for Ruby checks the credential providers in the order listed in the following table.

| Credential provider by precedence | *AWS SDKs and Tools Reference Guide* | *AWS SDK for Ruby API Reference* |
| --- | --- | --- |
| AWS access keys (temporary and long-term credentials) | [AWS access keys](https://docs.aws.amazon.com/sdkref/latest/guide/feature-static-credentials.html) | [https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/Credentials.html](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/Credentials.html)<br />[https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/SharedCredentials.html](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/SharedCredentials.html) |
| Web identity token from AWS Security Token Service (AWS STS)  | [Assume role credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-assume-role-credentials.html)Using `role_arn`, `role_session_name`, and `web_identity_token_file` | [https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/AssumeRoleWebIdentityCredentials.html](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/AssumeRoleWebIdentityCredentials.html)  |
| AWS IAM Identity Center. In this guide, see [Authenticating with AWS using AWS SDK for Ruby](credentials.md). | [IAM Identity Center credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sso-credentials.html) | [https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/SSOCredentials.html](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/SSOCredentials.html) |
| Trusted entity provider (such as AWS\_ROLE\_ARN). In this guide, see [Creating an AWS STS access token](#aws-ruby-sdk-credentials-access-token). | [Assume role credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-assume-role-credentials.html)Using `role_arn` and `role_session_name` | [https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/AssumeRoleCredentials.html](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/AssumeRoleCredentials.html) |
| Login credential provider | [Login credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-login-credentials.html) | [https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/LoginCredentials.html](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/LoginCredentials.html) |
| Process credential provider | [Process credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-process-credentials.html) | [https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/ProcessCredentials.html](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/ProcessCredentials.html) |
| Amazon Elastic Container Service (Amazon ECS) credentials | [Container credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-container-credentials.html) | [https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/ECSCredentials.html](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/ECSCredentials.html) |
| Amazon Elastic Compute Cloud (Amazon EC2) instance profile credentials (IMDS credential provider) | [IMDS credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-imds-credentials.html) | [https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/InstanceProfileCredentials.html](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/InstanceProfileCredentials.html) |

If the AWS SDK for Ruby environment variable `AWS_SDK_CONFIG_OPT_OUT` is set, the shared AWS `config` file, typically at` ~/.aws/config`, will not be parsed for credentials.

## Creating an AWS STS access token
<a name="aws-ruby-sdk-credentials-access-token"></a>

Assuming a role involves using a set of temporary security credentials that you can use to access AWS resources that you might not normally have access to. These temporary credentials consist of an access key ID, a secret access key, and a security token. You can use the [https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/AssumeRoleCredentials.html](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/AssumeRoleCredentials.html) method to create an AWS Security Token Service (AWS STS) access token.

The following example uses an access token to create an Amazon S3 client object, where `linked::account::arn` is the Amazon Resource Name (ARN) of the role to assume and `session-name` is an identifier for the assumed role session.

```
role_credentials = Aws::AssumeRoleCredentials.new(
  client: Aws::STS::Client.new,
  role_arn: "{{linked::account::arn}}",
  role_session_name: "{{session-name}}"
)

s3 = Aws::S3::Client.new(credentials: role_credentials)
```

For more information about setting `role_arn` or `role_session_name`, or about setting these using the shared AWS `config` file instead, see [Assume role credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-assume-role-credentials.html) in the *AWS SDKs and Tools Reference Guide*.
