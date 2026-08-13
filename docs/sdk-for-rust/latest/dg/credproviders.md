---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/credproviders.html
---

# Using AWS SDK for Rust credential providers
<a name="credproviders"></a>

 All requests to AWS must be cryptographically signed by using credentials issued by AWS. At runtime, the SDK retrieves configuration values for credentials by checking several locations.

If the retrieved configuration includes [AWS IAM Identity Center single sign-on access settings](credentials.md), the SDK works with the IAM Identity Center to retrieve temporary credentials that it uses to make request to AWS services.

If the retrieved configuration includes [temporary credentials](https://docs.aws.amazon.com/sdkref/latest/guide/access-temp-idc.html), the SDK uses them to make AWS service calls. Temporary credentials consist of access keys and a session token.

Authentication with AWS can be handled outside of your codebase. Many authentication methods can be automatically detected, used, and refreshed by the SDK using the credential provider chain.

For guided options for getting started on AWS authentication for your project, see [Authentication and access](https://docs.aws.amazon.com/sdkref/latest/guide/access.html) in the *AWS SDKs and Tools Reference Guide*.

## The credential provider chain
<a name="credproviders-default-credentials-provider-chain"></a>

If you don't explicitly specify a credential provider when constructing a client, the SDK for Rust uses a credential provider chain that checks a series of places where you can supply credentials. Once the SDK finds credentials in one of these locations, the search stops. For details on constructing clients, see [Configuring AWS SDK for Rust service clients in code](config-code.md).

The following example doesn't specify a credential provider in the code. The SDK uses the credential provider chain to detect the authentication that has been set up in the hosting environment, and uses that authentication for calls to AWS services.

```
let config = aws_config::defaults(BehaviorVersion::latest()).load().await;
let s3 = aws_sdk_s3::Client::new(&config);
```

### Credential retrieval order
<a name="credproviders-credential-retrieval-order"></a>

The credential provider chain searches for credentials using the following predefined sequence:

1. **Access key environment variables**

   The SDK attempts to load credentials from the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` environment variables.

1. **The shared AWS `config` and `credentials` files**

   The SDK attempts to load credentials from the `[default]` profile in the shared AWS `config` and `credentials` files. You can use the `AWS_PROFILE` environment variable to choose a named profile you want the SDK to load instead of using `[default]`. The `config` and `credentials` files are shared by various AWS SDKs and tools. For more information on these files, see the [Shared `config` and `credentials` files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html) in the *AWS SDKs and Tools Reference Guide*. For more information on standardized providers you can specify in a profile, see [AWS SDKs and Tools standardized credential providers](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html).

1. **AWS STS web identity**

   When creating mobile applications or client-based web applications that require access to AWS, AWS Security Token Service (AWS STS) returns a set of temporary security credentials for federated users who are authenticated through a public identity provider (IdP).
   + When you specify this in a profile, the SDK or tool attempts to retrieve temporary credentials using AWS STS `AssumeRoleWithWebIdentity` API method. For details on this method, see [AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html) in the *AWS Security Token Service API Reference*.
   +  For guidance on configuring this provider, see [Federate with web identity or OpenID Connect](https://docs.aws.amazon.com/sdkref/latest/guide/access-assume-role.html#webidentity) in the *AWS SDKs and Tools Reference Guide*.
   +  For details on SDK configuration properties for this provider, see [Assume role credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-assume-role-credentials.html) in the *AWS SDKs and Tools Reference Guide*.

1. **Amazon ECS and Amazon EKS container credentials **

   Your Amazon Elastic Container Service tasks and Kubernetes service accounts can have an IAM role associated with them. The permissions granted in the IAM role are assumed by the containers running in the task or containers of the pod. This role allows your SDK for Rust application code (on the container) to use other AWS services.

   The SDK attempts to retrieve credentials from the `AWS_CONTAINER_CREDENTIALS_RELATIVE_URI` or `AWS_CONTAINER_CREDENTIALS_FULL_URI` environment variables, which can be set automatically by Amazon ECS and Amazon EKS.
   + For details on setting up this role for Amazon ECS, see [ Amazon ECS task IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*.
   + For Amazon EKS setup information, see [Setting up the Amazon EKS Pod Identity Agent](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-agent-setup.html) in the **Amazon EKS User Guide**.
   +  For details on SDK configuration properties for this provider, see [Container credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-container-credentials.html) in the *AWS SDKs and Tools Reference Guide*.

1. **Amazon EC2 Instance Metadata Service **

   Create an IAM role and attach it to your instance. The SDK for Rust application on the instance attempts to retrieve the credentials provided by the role from the instance metadata.
   + The SDK for Rust only supports [IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html).
   + For details on setting up this role and using metadata, [IAM roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) and [Work with instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) in the *Amazon EC2 User Guide*.
   +  For details on SDK configuration properties for this provider, see [IMDS credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-imds-credentials.html) in the *AWS SDKs and Tools Reference Guide*.

1. If credentials still aren't resolved at this point, the operation panics with an error.

For details on AWS credential provider configuration settings, see [Standardized credential providers](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html) in the *Settings reference* of the *AWS SDKs and Tools Reference Guide*.

## Explicit credential provider
<a name="credproviders-explicit-credentials-provider"></a>

Instead of relying on the credential provider chain to detect your authentication method, you can specify a specific credential provider that the SDK should use. When you load your general configuration using `aws_config::defaults`, you can specify a custom credential provider as shown in the following:

```
let config = aws_config::defaults(BehaviorVersion::latest())
    .credentials_provider(MyCredentialsProvider::new())
    .load()
    .await;
```

You can implement your own credential provider by implementing the [`ProvideCredentials`](https://docs.rs/aws-credential-types/latest/aws_credential_types/provider/trait.ProvideCredentials.html) trait.

## Identity caching
<a name="credproviders-identity-caching"></a>

The SDK will cache credentials and other identity types such as SSO tokens. By default, the SDK uses a lazy cache implementation that loads credentials upon first request, caches them, and then attempts to refresh them during another request when they are close to expiring. Clients created from the same `SdkConfig` will share an [`IdentityCache`](https://docs.rs/aws-smithy-runtime/latest/aws_smithy_runtime/client/identity/struct.IdentityCache.html).
