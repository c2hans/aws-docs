---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/credproviders.html
---

# Using AWS SDK for C\+\+ credential providers
<a name="credproviders"></a>

 All requests to AWS must be cryptographically signed by using credentials issued by AWS. At runtime, the SDK retrieves configuration values for credentials by checking several locations.

Authentication with AWS can be handled outside of your codebase. Many authentication methods can be automatically detected, used, and refreshed by the SDK using the credential provider chain.

For guided options for getting started on AWS authentication for your project, see [Authentication and access](https://docs.aws.amazon.com/sdkref/latest/guide/access.html) in the *AWS SDKs and Tools Reference Guide*.

## The credential provider chain
<a name="credproviders-default-credentials-provider-chain"></a>

If you don't explicitly specify a credential provider when constructing a client, the SDK for C\+\+ uses a credential provider chain that checks a series of places where you can supply credentials. Once the SDK finds credentials in one of these locations, the search stops.

### Credential retrieval order
<a name="credproviders-credential-retrieval-order"></a>

All SDKs have a series of places (or sources) that they check in order to get valid credentials to use to make a request to an AWS service. After valid credentials are found, the search is stopped. This systematic search is called the credential provider chain.

For each step in the chain, there are different ways to set the values. Setting values directly in code always takes precedence, followed by setting as environment variables, and then in the shared AWS `config` file. For more information, see [Precedence of settings](https://docs.aws.amazon.com/sdkref/latest/guide/settings-reference.html#precedenceOfSettings) in the *AWS SDKs and Tools Reference Guide*.

The SDK attempts to load credentials from the `[default]` profile in the shared AWS `config` and `credentials` files. You can use the `AWS_PROFILE` environment variable to choose a named profile you want the SDK to load instead of using `[default]`. The `config` and `credentials` files are shared by AWS SDKs and tools. The *AWS SDKs and Tools Reference Guide* has information on SDK configuration settings used by all AWS SDKs and the AWS CLI. To learn more about how to configure the SDK through the shared AWS `config` file, see [Shared config and credentials files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html). To learn more about how to configure the SDK through setting environment variables, see [Environment variables support](https://docs.aws.amazon.com/sdkref/latest/guide/environment-variables.html).

To authenticate with AWS, the SDK for C\+\+ checks the credential providers in the following order.

1. **AWS access keys (temporary and long-term credentials)**

   The SDK attempts to load credentials from the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` environment variables, or from the shared AWS `credentials` file.
   +  For guidance on configuring this provider, see [AWS access keys](https://docs.aws.amazon.com/sdkref/latest/guide/access-users.html) in the *AWS SDKs and Tools Reference Guide*.
   +  For details on SDK configuration properties for this provider, see [AWS access keys](https://docs.aws.amazon.com/sdkref/latest/guide/feature-static-credentials.html) in the *AWS SDKs and Tools Reference Guide*.

1. **AWS STS web identity**

   When creating mobile applications or client-based web applications that require access to AWS, AWS Security Token Service (AWS STS) returns a set of temporary security credentials for federated users who are authenticated through a public identity provider (IdP).
   + When you specify this in a profile, the SDK or tool attempts to retrieve temporary credentials using AWS STS `AssumeRoleWithWebIdentity` API method. For details on this method, see [AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html) in the *AWS Security Token Service API Reference*.
   +  For guidance on configuring this provider, see [Federate with web identity or OpenID Connect](https://docs.aws.amazon.com/sdkref/latest/guide/access-assume-role.html#webidentity) in the *AWS SDKs and Tools Reference Guide*.
   +  For details on SDK configuration properties for this provider, see [Assume role credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-assume-role-credentials.html) in the *AWS SDKs and Tools Reference Guide*.

1. **IAM Identity Center**

   If you use IAM Identity Center to authenticate, this is when the SDK for C\+\+ uses the single sign-on token that was set up by running AWS CLI command `aws sso login`. The SDK uses the temporary credentials that the IAM Identity Center exchanged for a valid token. The SDK then uses the temporary credentials when it calls AWS services. For detailed information about this process, see [Understand SDK credential resolution for AWS services](https://docs.aws.amazon.com/sdkref/latest/guide/understanding-sso.html#idccredres) in the *AWS SDKs and Tools Reference Guide*.
   +  For guidance on configuring this provider, see [IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html) in the *AWS SDKs and Tools Reference Guide*.
   +  For details on SDK configuration properties for this provider, see [IAM Identity Center credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sso-credentials.html) in the *AWS SDKs and Tools Reference Guide*.

1. **Login credential identity resolver with AWS Signin**

   If you use AWS sign in and console credentials to authenticate, this is when the SDK for C\+\+ uses the console credentials set up by running `aws login` or `aws login --profile` in the CLI. The SDK uses these credentials when it calls AWS services.
   +  For detailed information about this process, see [Login for AWS local development using console credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html) in the *AWS SDKs and Tools Reference Guide*.

1. **External process provider**

   This provider can be used to provide custom implementations, such as retrieving credentials from an on-premises credentials store or integrating with your on-premises identify provider.
   +  For guidance on one way to configure this provider, see [IAM Roles Anywhere](https://docs.aws.amazon.com/sdkref/latest/guide/access-rolesanywhere.html) in the *AWS SDKs and Tools Reference Guide*.
   +  For details on SDK configuration properties for this provider, see [Process credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-process-credentials.html) in the *AWS SDKs and Tools Reference Guide*.

1. **Amazon ECS and Amazon EKS container credentials **

   Your Amazon Elastic Container Service tasks and Kubernetes service accounts can have an IAM role associated with them. The permissions granted in the IAM role are assumed by the containers running in the task or containers of the pod. This role allows your SDK for C\+\+ application code (on the container) to use other AWS services.

   The SDK attempts to retrieve credentials from the `AWS_CONTAINER_CREDENTIALS_RELATIVE_URI` or `AWS_CONTAINER_CREDENTIALS_FULL_URI` environment variables, which can be set automatically by Amazon ECS and Amazon EKS.
   + For details on setting up this role for Amazon ECS, see [ Amazon ECS task IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*.
   + For Amazon EKS setup information, see [Setting up the Amazon EKS Pod Identity Agent](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-agent-setup.html) in the **Amazon EKS User Guide**.
   +  For details on SDK configuration properties for this provider, see [Container credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-container-credentials.html) in the *AWS SDKs and Tools Reference Guide*.

1. **Amazon EC2 Instance Metadata Service **

   Create an IAM role and attach it to your instance. The SDK for C\+\+ application on the instance attempts to retrieve the credentials provided by the role from the instance metadata.
   + For details on setting up this role and using metadata, [IAM roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) and [Work with instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) in the *Amazon EC2 User Guide*.
   +  For details on SDK configuration properties for this provider, see [IMDS credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-imds-credentials.html) in the *AWS SDKs and Tools Reference Guide*.

The credential provider chain can be reviewed at [https://github.com/aws/aws-sdk-cpp/blob/main/src/aws-cpp-sdk-core/source/auth/AWSCredentialsProviderChain.cpp#L43-L86](https://github.com/aws/aws-sdk-cpp/blob/main/src/aws-cpp-sdk-core/source/auth/AWSCredentialsProviderChain.cpp#L43-L86) in the AWS SDK for C\+\+ source code on GitHub.

If you followed the recommended approach for new users to get started, you set up AWS Login Credentials authentication during [Authenticating with AWS using AWS SDK for C\+\+](credentials.md) of the Getting started topic. Other authentication methods are useful for different situations. To avoid security risks, we recommend always using short-term credentials. For other authentication method procedures, see [Authentication and access](https://docs.aws.amazon.com/sdkref/latest/guide/access.html) in the *AWS SDKs and Tools Reference Guide*.

## Explicit credential provider
<a name="credproviders-explicit-credentials-provider"></a>

Instead of relying on the credential provider chain to detect your authentication method, you can specify a specific credential provider that the SDK should use. You can do this by providing credentials in your service client's constructor.

The following example creates an Amazon Simple Storage Service client by directly providing temporary access credentials instead of using the chain.

```
    SDKOptions options;
    Aws::InitAPI(options);
    {
        const auto cred_provider = Aws::MakeShared<Auth::SimpleAWSCredentialsProvider>("TestAllocationTag",
            "awsAccessKeyId",
            "awsSecretKey",
            "sessionToken");
        S3Client client{cred_provider};
    }
    Aws::ShutdownAPI(options);
```

## Identity caching
<a name="credproviders-identity-caching"></a>

The SDK will cache credentials and other identity types such as SSO tokens. By default, the SDK uses a lazy cache implementation that loads credentials upon first request, caches them, and then attempts to refresh them during another request when they are close to expiring. Clients created from the same [https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-core/html/struct_aws_1_1_client_1_1_client_configuration.html](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-core/html/struct_aws_1_1_client_1_1_client_configuration.html) share a cache.
