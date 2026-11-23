---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/credential-providers.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Credential providers

Before the AWS SDK for Python v4 can sign a request to an AWS service, it uses an *identity resolver* to obtain an *identity*. For these requests, the identity is a set of AWS credentials. A *credential resolver* is an identity resolver that retrieves AWS credentials from a configured source. Sources can include environment variables, an assumed IAM role, or another credential resolver. If you don't configure credentials, the SDK uses its default credential resolver chain.

**Important**
During the Developer Preview, the AWS SDK for Python v4 supports fewer credential sources than other AWS SDKs. For example, it doesn't support AWS IAM Identity Center or AWS Management Console sign-in credentials. We plan to add more credential sources in future releases.

This page explains how the SDK resolves credentials and how to configure credential sources. It includes the following topics:
+ [Default credential resolver chain](#credproviders-default-chain) describes how the SDK finds credentials automatically.
+ [Configure a specific credential resolver](#credproviders-specific-resolver) shows how to use one credential source instead of the default chain.
+ [Configure static credentials](#credproviders-static) shows how to provide credentials directly to a client configuration.

For more information about credential resolution across AWS SDKs and tools, see [Standardized credential providers](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html) in the *AWS SDKs and Tools Reference Guide*.

## Default credential resolver chain
<a name="credproviders-default-chain"></a>

If you don't specify static credentials or a credential resolver when you create a client, the SDK assembles the default credential resolver chain. During assembly, *credential providers* inspect the available configuration and add the applicable credential resolvers to the chain. When the SDK needs credentials, the chain calls each resolver in a predefined order. It stops at the first resolver that returns valid credentials.

Synchronous and asynchronous clients support the same credential sources.

To use the default chain, resolve the configuration without setting the `aws_credentials_identity_resolver` field or any of the static credential fields:

```python
from aws_sdk_bedrock_runtime import BedrockRuntimeClient, BedrockRuntimeConfig

def create_client() -> BedrockRuntimeClient:
    config = BedrockRuntimeConfig.resolve(region="us-east-1")
    return BedrockRuntimeClient(config=config)
```

### Credential sources
<a name="credproviders-source-packages"></a>

The resolvers in the default chain use two kinds of credential sources:
+ **Local sources** read credentials from your environment or local system. They include environment variables, the shared AWS `config` and `credentials` files, and a `credential_process` command in a profile. Every service client supports these sources without additional packages.
+ **Network-based sources** fetch credentials over the network, such as assuming an IAM role with the AWS Security Token Service or querying the Amazon EC2 Instance Metadata Service.

The chain uses a resolver for a network-based source only after you install its package, even when the source is configured in the environment or shared config file. Each package registers a credential provider with the SDK. During assembly, the provider determines whether its source applies and adds the resolver to the chain.

Each network-based source ships in a separate package:

| Credential source | Package |
| --- | --- |
| Assume an IAM role with AWS STS | aws-credentials-sts |
| Web identity (OpenID Connect token) with AWS STS | aws-credentials-sts |
| Amazon ECS and Amazon EKS container credentials | aws-credentials-http |
| Amazon EC2 Instance Metadata Service (IMDS) | aws-credentials-imds |

Install the package for each source that your application uses. Installing the package is all that the default chain needs. You don't need to change your code.

```bash
python -m pip install aws-credentials-sts    # Assume role and web identity
python -m pip install aws-credentials-http   # Container credentials
python -m pip install aws-credentials-imds   # EC2 Instance Metadata Service
```

These packages also export resolver classes. To use a single source directly instead of the default chain, see [Configure a specific credential resolver](#credproviders-specific-resolver).

### Credential retrieval order
<a name="credproviders-retrieval-order"></a>

Depending on your configuration, the chain can contain resolvers for the following credential sources. It calls the resolvers in this order and stops at the first one that returns valid credentials:

1. **[Access key environment variables](https://docs.aws.amazon.com/sdkref/latest/guide/feature-static-credentials.html)**

   The SDK reads the `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and (if set) `AWS_SESSION_TOKEN` environment variables.

1. **Web identity token environment variables**

   If the `AWS_WEB_IDENTITY_TOKEN_FILE` and `AWS_ROLE_ARN` environment variables are set, the SDK reads the OpenID Connect (OIDC) token from the file. It then obtains temporary credentials by calling AWS Security Token Service `AssumeRoleWithWebIdentity`.

   **Requires the `aws-credentials-sts` package.**

1. **[Shared AWS `config` and `credentials` files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html)**

   The SDK reads settings from the shared AWS `config` and `credentials` files. It uses the profile that you specify, or the `[default]` profile if you don't specify one.

   When a profile contains settings for more than one credential type, the SDK uses them in the following order:

   1. **[Assume role](https://docs.aws.amazon.com/sdkref/latest/guide/access-assume-role.html)**

      If the profile has a `role_arn` setting with a `source_profile` or `credential_source`, the SDK obtains temporary credentials by calling AWS Security Token Service `AssumeRole`.

      **Requires the `aws-credentials-sts` package.**

   1. **[Static access keys](https://docs.aws.amazon.com/sdkref/latest/guide/feature-static-credentials.html)**

      The SDK uses the `aws_access_key_id`, `aws_secret_access_key`, and `aws_session_token` settings from the profile.

   1. **Web identity**

      If the profile has `role_arn` and `web_identity_token_file` settings, the SDK obtains temporary credentials by calling AWS Security Token Service `AssumeRoleWithWebIdentity`.

      **Requires the `aws-credentials-sts` package.**

   1. **[Process credentials](https://docs.aws.amazon.com/sdkref/latest/guide/feature-process-credentials.html)**

      If the profile has a `credential_process` setting, the SDK runs the specified process and reads credentials from its output.

1. **[Amazon ECS and Amazon EKS container credentials](https://docs.aws.amazon.com/sdkref/latest/guide/feature-container-credentials.html)**

   The SDK obtains credentials from an HTTP endpoint, which it locates from the `AWS_CONTAINER_CREDENTIALS_RELATIVE_URI` or `AWS_CONTAINER_CREDENTIALS_FULL_URI` environment variables. Amazon Elastic Container Service (Amazon ECS) and Amazon Elastic Kubernetes Service (Amazon EKS) set these automatically when a task or pod has an IAM role.

   **Requires the `aws-credentials-http` package.**

1. **[Amazon EC2 Instance Metadata Service](https://docs.aws.amazon.com/sdkref/latest/guide/feature-imds-credentials.html)**

   The SDK obtains credentials from the IAM role attached to the Amazon EC2 instance that the application runs on, through the Instance Metadata Service (IMDS).

   **Requires the `aws-credentials-imds` package.**

If no resolver returns valid credentials, the SDK raises an error when it signs the first request.

## Configure a specific credential resolver
<a name="credproviders-specific-resolver"></a>

To use a particular credential source instead of the default chain, set the `aws_credentials_identity_resolver` configuration field to an instance of a resolver class. Use a resolver that matches the client mode.

The following example uses `EnvironmentCredentialsResolver`, which reads credentials only from environment variables.

 **Imports**

```python
from aws_sdk_bedrock_runtime import BedrockRuntimeClient, BedrockRuntimeConfig
from smithy_aws_core.identity import EnvironmentCredentialsResolver
```

 **Code**

```python
def create_client() -> BedrockRuntimeClient:
    config = BedrockRuntimeConfig.resolve(
        region="us-east-1",
        aws_credentials_identity_resolver=EnvironmentCredentialsResolver(),
    )
    return BedrockRuntimeClient(config=config)
```

For an asynchronous client, pass `AsyncEnvironmentCredentialsResolver()` from `smithy_aws_core.aio.identity` to `await AsyncBedrockRuntimeConfig.resolve()`.

The following table lists the available resolvers for each client mode:

| Synchronous resolver | Asynchronous resolver | Credential source |
| --- | --- | --- |
| StaticCredentialsResolver from smithy\_aws\_core.identity | AsyncStaticCredentialsResolver from smithy\_aws\_core.aio.identity | A fixed set of credentials that you supply. For a simpler option, see [Configure static credentials](#credproviders-static). |
| EnvironmentCredentialsResolver from smithy\_aws\_core.identity | AsyncEnvironmentCredentialsResolver from smithy\_aws\_core.aio.identity | Environment variables (AWS\_ACCESS\_KEY\_ID, AWS\_SECRET\_ACCESS\_KEY, and AWS\_SESSION\_TOKEN). |
| ProcessCredentialsResolver from smithy\_aws\_core.identity | AsyncProcessCredentialsResolver from smithy\_aws\_core.aio.identity | An external command that returns credentials in its JSON output. |
| AssumeRoleCredentialsResolver from aws\_credentials\_sts | AsyncAssumeRoleCredentialsResolver from aws\_credentials\_sts.aio | Temporary credentials for an IAM role, obtained by calling AWS STS AssumeRole with a role and source resolver that you specify. |
| ProfileAssumeRoleCredentialsResolver from aws\_credentials\_sts | AsyncProfileAssumeRoleCredentialsResolver from aws\_credentials\_sts.aio | Temporary credentials for an IAM role, using the assume-role settings (role\_arn with source\_profile or credential\_source) in a shared config profile. |
| WebIdentityCredentialsResolver from aws\_credentials\_sts | AsyncWebIdentityCredentialsResolver from aws\_credentials\_sts.aio | Temporary credentials for an IAM role, obtained by calling AWS STS AssumeRoleWithWebIdentity with an OpenID Connect (OIDC) token file. |
| ContainerCredentialsResolver from aws\_credentials\_http | AsyncContainerCredentialsResolver from aws\_credentials\_http.aio | A container credential endpoint, such as the one provided by Amazon ECS and Amazon EKS. |
| IMDSCredentialsResolver from aws\_credentials\_imds | AsyncIMDSCredentialsResolver from aws\_credentials\_imds.aio | An Amazon EC2 instance's metadata, through the Instance Metadata Service (IMDS). |

The resolvers in `smithy_aws_core.identity` and `smithy_aws_core.aio.identity` come with every service client. To use a resolver from an `aws_credentials_*` module, install its package first. For more information, see [Credential sources](#credproviders-source-packages).

## Configure static credentials
<a name="credproviders-static"></a>

To use a specific set of credentials, provide them in the `aws_access_key_id`, `aws_secret_access_key`, and (optionally) `aws_session_token` configuration fields. Use static credentials when your application already holds credentials, such as credentials that it retrieves from a secrets manager.

**Warning**
Don't hardcode credentials in source code. Static credentials are appropriate when your application obtains them at runtime from a secure source. For local development, prefer short-term credentials supplied through environment variables or the shared AWS configuration files.

 **Imports**

```python
from aws_sdk_bedrock_runtime import BedrockRuntimeClient, BedrockRuntimeConfig
```

 **Code**

```python
def create_client(
    access_key_id: str,
    secret_access_key: str,
    session_token: str | None = None,  # None for long-term credentials.
) -> BedrockRuntimeClient:
    config = BedrockRuntimeConfig.resolve(
        region="us-east-1",
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key,
        aws_session_token=session_token,
    )
    return BedrockRuntimeClient(config=config)
```

The asynchronous config class takes the same fields.
