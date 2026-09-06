---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/setting-credentials-node.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Set credentials in Node.js
<a name="setting-credentials-node"></a>

We recommend that new users who are developing locally and are not given a method of authentication by their employer to set up AWS IAM Identity Center. For more information, see [SDK authentication with AWS](getting-your-credentials.md).

There are several ways in Node.js to supply your credentials to the SDK. Some of these are more secure and others afford greater convenience while developing an application. When obtaining credentials in Node.js, be careful about relying on more than one source, such as an environment variable and a JSON file you load. You can change the permissions under which your code runs without realizing the change has happened.

AWS SDK for JavaScript V3 provides a default credential provider chain in Node.js, so you are not required to supply a credential provider explicitly. The default [credential provider chain](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html#credentialProviderChain) attempts to resolve the credentials from a variety of different sources in a given precedence, until a credential is returned from the one of the sources. You can find the credential provider chain for SDK for JavaScript V3 [here](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-credential-providers/#fromnodeproviderchain).

## Credential provider chain
<a name="credchain"></a>

All SDKs have a series of places (or sources) that they check in order to get valid credentials to use to make a request to an AWS service. After valid credentials are found, the search is stopped. This systematic search is called the default credential provider chain.

For each step in the chain, there are different ways to set the values. Setting values directly in code always takes precedence, followed by setting as environment variables, and then in the shared AWS `config` file. For more information, see [Precedence of settings](https://docs.aws.amazon.com/sdkref/latest/guide/settings-reference.html#precedenceOfSettings) in the *AWS SDKs and Tools Reference Guide*.

The *AWS SDKs and Tools Reference Guide* has information on SDK configuration settings used by all AWS SDKs and the AWS CLI. To learn more about how to configure the SDK through the shared AWS `config` file, see [Shared config and credentials files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html). To learn more about how to configure the SDK through setting environment variables, see [Environment variables support](https://docs.aws.amazon.com/sdkref/latest/guide/environment-variables.html).

To authenticate with AWS, the AWS SDK for JavaScript checks the credential providers in the order listed in the following table.

- **[`fromEnv()`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-credential-providers/#fromenv) **
  - **Credential provider(s) available:** AWS access keys from environment variables
  - ***AWS SDKs and Tools Reference Guide*:** [AWS access keys](https://docs.aws.amazon.com/sdkref/latest/guide/feature-static-credentials.html)

- **[`fromSSO()`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-credential-providers/#fromsso)**
  - **Credential provider(s) available:** AWS IAM Identity Center. In this guide, see [SDK authentication with AWS](getting-your-credentials.md).
  - ***AWS SDKs and Tools Reference Guide*:** [IAM Identity Center credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sso-credentials.html)

- ** [`fromIni()`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-credential-providers/#fromini) **
  - **Credential provider(s) available:** AWS access keys from shared `config` and `credentials` files / ***AWS SDKs and Tools Reference Guide*:** [AWS access keys](https://docs.aws.amazon.com/sdkref/latest/guide/feature-static-credentials.html)
  - **Credential provider(s) available:** Trusted entity provider (such as `AWS_ROLE_ARN`) / ***AWS SDKs and Tools Reference Guide*:** [Assume an IAM role](https://docs.aws.amazon.com/sdkref/latest/guide/feature-assume-role-credentials.html#credOrSourceAssumeRole)
  - **Credential provider(s) available:** Web identity token from AWS Security Token Service (AWS STS) / ***AWS SDKs and Tools Reference Guide*:** [Federate with web identity or OpenID Connect](https://docs.aws.amazon.com/sdkref/latest/guide/feature-assume-role-credentials.html#webidentity)
  - **Credential provider(s) available:** Amazon Elastic Container Service (Amazon ECS) credentials / ***AWS SDKs and Tools Reference Guide*:** [Container credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-container-credentials.html)
  - **Credential provider(s) available:** Amazon Elastic Compute Cloud (Amazon EC2) instance profile credentials (IMDS credential provider) / ***AWS SDKs and Tools Reference Guide*:** [IMDS credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-imds-credentials.html)
  - **Credential provider(s) available:** Process credential provider / ***AWS SDKs and Tools Reference Guide*:** [Process credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-process-credentials.html)
  - **Credential provider(s) available:** AWS IAM Identity Center / ***AWS SDKs and Tools Reference Guide*:** [IAM Identity Center credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sso-credentials.html)
  - **Credential provider(s) available:** Login credentials provider / ***AWS SDKs and Tools Reference Guide*:** [Login credentials provider](https://docs.aws.amazon.com/sdkref/latest/guide/access-login.html)

- ** [`fromLoginCredentials()`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-credential-providers/#fromlogincredentials) **
  - **Credential provider(s) available:** Login credentials provider
  - ***AWS SDKs and Tools Reference Guide*:** [Login credentials provider](https://docs.aws.amazon.com/sdkref/latest/guide/access-login.html)

- **[`fromProcess()`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-credential-providers/#fromprocess)**
  - **Credential provider(s) available:** Process credential provider
  - ***AWS SDKs and Tools Reference Guide*:** [Process credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-process-credentials.html)

- **[`fromTokenFile()`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-credential-providers/#fromtokenfile)**
  - **Credential provider(s) available:** Web identity token from AWS Security Token Service (AWS STS)
  - ***AWS SDKs and Tools Reference Guide*:** [Federate with web identity or OpenID Connect](https://docs.aws.amazon.com/sdkref/latest/guide/feature-assume-role-credentials.html#webidentity)

- **[`fromContainerMetadata()`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-credential-providers/#fromcontainermetadata-and-frominstancemetadata)**
  - **Credential provider(s) available:** Amazon Elastic Container Service (Amazon ECS) credentials
  - ***AWS SDKs and Tools Reference Guide*:** [Container credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-container-credentials.html)

- **[`fromInstanceMetadata()`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-credential-providers/#fromcontainermetadata-and-frominstancemetadata)**
  - **Credential provider(s) available:** Amazon Elastic Compute Cloud (Amazon EC2) instance profile credentials (IMDS credential provider)
  - ***AWS SDKs and Tools Reference Guide*:** [IMDS credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-imds-credentials.html)

If you followed the recommended approach for new users to get started, you set up AWS IAM Identity Center authentication during [SDK authentication with AWS](getting-your-credentials.md) of the Getting started topic. Other authentication methods are useful for different situations. To avoid security risks, we recommend always using short-term credentials. For other authentication method procedures, see [Authentication and access](https://docs.aws.amazon.com/sdkref/latest/guide/access.html) in the *AWS SDKs and Tools Reference Guide*.

The topics in this section describe how to load credentials into Node.js.

**Topics**
+ [Credential provider chain](#credchain)
+ [Load credentials in Node.js from IAM roles for Amazon EC2](loading-node-credentials-iam.md)
+ [Load credentials for a Node.js Lambda function](loading-node-credentials-lambda.md)
