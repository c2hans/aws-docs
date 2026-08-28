---
source_url: https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/credential-providers.html
---

# Using AWS SDK for Swift credential providers
<a name="credential-providers"></a>

 All requests to AWS must be cryptographically signed by using credentials issued by AWS. At runtime, the SDK retrieves configuration values for credentials by checking several locations.

If the retrieved configuration includes [AWS IAM Identity Center single sign-on access settings](authenticating.md), the SDK works with the IAM Identity Center to retrieve temporary credentials that it uses to make request to AWS services.

If the retrieved configuration includes [temporary credentials](https://docs.aws.amazon.com/sdkref/latest/guide/access-temp-idc.html), the SDK uses them to make AWS service calls. Temporary credentials consist of access keys and a session token.

Authentication with AWS can be handled outside of your codebase. Many authentication methods can be automatically detected, used, and refreshed by the SDK using the credential provider chain.

For guided options for getting started on AWS authentication for your project, see [Authentication and access](https://docs.aws.amazon.com/sdkref/latest/guide/access.html) in the *AWS SDKs and Tools Reference Guide*.

## The credential provider chain
<a name="credproviders-default-credentials-provider-chain"></a>

If you don't explicitly specify a credential provider when constructing a client, the AWS SDK for Swift uses a credential provider chain that checks a series of places where you can supply credentials. Once the SDK finds credentials in one of these locations, the search stops.

## Credential retrieval order
<a name="credproviders-credential-retrieval-order"></a>

The credential provider chain searches for credentials using the following predefined sequence:

1. **Access key environment variables**

   The SDK attempts to load credentials from the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` environment variables.

1. **The shared AWS `config` and `credentials` files**

   The SDK attempts to load credentials from the `[default]` profile in the shared AWS `config` and `credentials` files. You can use the `AWS_PROFILE` environment variable to choose a named profile you want the SDK to load instead of using `[default]`. The `config` and `credentials` files are shared by various AWS SDKs and tools. For more information on these files, see the [Shared `config` and `credentials` files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html) in the *AWS SDKs and Tools Reference Guide*.

   If you use console credentials to authenticate, this is when the SDK uses the login token that was set up by running AWS CLI command `aws login`. The SDK uses the temporary credentials from the cached token when it calls AWS services. For detailed information about this process, see [Understand SDK credential resolution for AWS services](https://docs.aws.amazon.com/sdkref/latest/guide/understanding-sso.html#idccredres) in the *AWS SDKs and Tools Reference Guide*.

   If you use IAM Identity Center to authenticate, this is when the SDK uses the single sign-on token that was set up by running AWS CLI command `aws sso login`. The SDK uses the temporary credentials that the IAM Identity Center exchanged for a valid token. The SDK then uses the temporary credentials when it calls AWS services. For detailed information about this process, see [Understand SDK credential resolution for AWS services](https://docs.aws.amazon.com/sdkref/latest/guide/understanding-sso.html#idccredres) in the *AWS SDKs and Tools Reference Guide*.
   +  For guidance on configuring this provider, see [IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html) in the *AWS SDKs and Tools Reference Guide*.
   +  For details on SDK configuration properties for this provider, see [IAM Identity Center credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sso-credentials.html) in the *AWS SDKs and Tools Reference Guide*.

1. **AWS STS web identity**

   When creating mobile applications or client-based web applications that require access to AWS, AWS Security Token Service (AWS STS) returns a set of temporary security credentials for federated users who are authenticated through a public identity provider (IdP).
   + When you specify this in a profile, the SDK or tool attempts to retrieve temporary credentials using AWS STS `AssumeRoleWithWebIdentity` API method. For details on this method, see [AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html) in the *AWS Security Token Service API Reference*.
   +  For guidance on configuring this provider, see [Federate with web identity or OpenID Connect](https://docs.aws.amazon.com/sdkref/latest/guide/access-assume-role.html#webidentity) in the *AWS SDKs and Tools Reference Guide*.
   +  For details on SDK configuration properties for this provider, see [Assume role credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-assume-role-credentials.html) in the *AWS SDKs and Tools Reference Guide*.

1. **Amazon ECS and Amazon EKS container credentials **

   Your Amazon Elastic Container Service tasks and Kubernetes service accounts can have an IAM role associated with them. The permissions granted in the IAM role are assumed by the containers running in the task or containers of the pod. This role allows your application code (on the container) to use other AWS services.

   The SDK attempts to retrieve credentials from the `AWS_CONTAINER_CREDENTIALS_RELATIVE_URI` or `AWS_CONTAINER_CREDENTIALS_FULL_URI` environment variables, which can be set automatically by Amazon ECS and Amazon EKS.
   + For details on setting up this role for Amazon ECS, see [ Amazon ECS task IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*.
   + For Amazon EKS setup information, see [Setting up the Amazon EKS Pod Identity Agent](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-agent-setup.html) in the **Amazon EKS User Guide**.
   +  For details on SDK configuration properties for this provider, see [Container credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-container-credentials.html) in the *AWS SDKs and Tools Reference Guide*.

1. **Amazon EC2 Instance Metadata Service **

   Create an IAM role and attach it to your instance. The SDK application on the instance attempts to retrieve the credentials provided by the role from the instance metadata.
   + For details on setting up this role and using metadata, [IAM roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) and [Work with instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) in the *Amazon EC2 User Guide*.
   +  For details on SDK configuration properties for this provider, see [IMDS credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-imds-credentials.html) in the *AWS SDKs and Tools Reference Guide*.

For details on AWS credential provider configuration settings, see [Standardized credential providers](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html) in the *Settings reference* of the *AWS SDKs and Tools Reference Guide*.

## Credential identity resolvers
<a name="identity-types"></a>

A **credential identity resolver** is an object that takes some form of identity, verifies that it's valid for use by the application, and returns credentials that can be used when using an AWS service . There are several supported ways to obtain a valid identity, and each has a corresponding credential identity resolver type available for you to use, depending on which authorization methods you want to use.

The credential identity resolver acts as an adaptor between the identity and the AWS service. By providing a credential identity resolver to the service instead of directly providing the user's credentials, the service is able to fetch currently-valid credentials for the identity at any time, as long as the identity provider allows it.

Identity features in the AWS SDK for Swift are defined in the module `AWSSDKIdentity`. In the `AWSSDKIdentity` module, credentials are represented by the struct `[AWSCredentialIdentity](https://sdk.amazonaws.com/swift/api/smithyidentity/latest/documentation/smithyidentity/awscredentialidentity)`. See [AWS security credentials](/IAM/latest/UserGuide/security-creds.html#AccessKeys) in the IAM User Guide for further information about AWS credentials.

There are several credential identity resolver types available as a means of obtaining an identity to use for authentication. Some credential identity resolvers are specific to a given source while others encompass an assortment of identity sources that share similar technologies. For example, the `STSWebIdentityCredentialIdentityResolver`, which uses a JSON Web Token (JWT) as the source identity for which to return AWS credentials. The JWT can come from a number of different services, including Amazon Cognito federated identities, Sign In With Apple, Google, or Facebook. See [Identity pools third-party identity providers](/cognito/latest/developerguide/external-identity-providers.html) for information on third-party identity providers.

`[CachedAWSCredentialIdentityResolver](https://sdk.amazonaws.com/swift/api/awssdkidentity/latest/documentation/awssdkidentity/cachedawscredentialidentityresolver)`
A credential identity resolver that is chained with another one so it can cache the resolved identity for re-use until an expiration time elapses.

`[CognitoAWSCredentialIdentityResolver](https://sdk.amazonaws.com/swift/api/awssdkidentity/latest/documentation/awssdkidentity/cognitoawscredentialidentityresolver)`
A credential identity resolver that uses an Amazon Cognito Identity Pool or a Cognito Identity ID to resolve credentials.

`[CustomAWSCredentialIdentityResolver](https://sdk.amazonaws.com/swift/api/awssdkidentity/latest/documentation/awssdkidentity/customawscredentialidentityresolver)`
A credential identity resolver that uses another credential identity resolver's output to resolve the credentials in a custom way.

`[DefaultAWSCredentialIdentityResolverChain](https://sdk.amazonaws.com/swift/api/awssdkidentity/latest/documentation/awssdkidentity/defaultawscredentialidentityresolverchain)`
Represents a chain of credential identity resolvers that attempt to resolve the identity following the standard search order. See [Credential provider chain](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html#credentialProviderChain) in the AWS SDKs and Tools Reference Guide for details on the credential provider chain.

`[ECSAWSCredentialIdentityResolver](https://sdk.amazonaws.com/swift/api/awssdkidentity/latest/documentation/awssdkidentity/ecsawscredentialidentityresolver)`
Obtains credentials from an Amazon Elastic Container Service container's metadata.

`[EnvironmentAWSCredentialIdentityResolver](https://sdk.amazonaws.com/swift/api/awssdkidentity/latest/documentation/awssdkidentity/environmentawscredentialidentityresolver)`
Resolves credentials using the environment variables `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN`.

`[IMDSAWSCredentialIdentityResolver](https://sdk.amazonaws.com/swift/api/awssdkidentity/latest/documentation/awssdkidentity/imdsawscredentialidentityresolver)`
Uses IMDSv2 to fetch credentials within an Amazon Elastic Compute Cloud instance.

`[LoginAWSCredentialIdentityResolver](https://sdk.amazonaws.com/swift/api/awssdkidentity/latest/documentation/awssdkidentity/loginawscredentialidentityresolver)`
 Resolves credentials using console credentials with AWS Signin.

`[ProcessAWSCredentialIdentityResolver](https://sdk.amazonaws.com/swift/api/awssdkidentity/latest/documentation/awssdkidentity/processawscredentialidentityresolver)`
Resolves credentials by running a command or process. The process to run is sourced from a profile in the AWS `config` file. The profile key that identifies the process to use is `credential_process`.

`[ProfileAWSCredentialIdentityResolver](https://sdk.amazonaws.com/swift/api/awssdkidentity/latest/documentation/awssdkidentity/profileawscredentialidentityresolver)`
Uses the specified profile from an AWS `config` file to resolve credentials.

`[SSOAWSCredentialIdentityResolver](https://sdk.amazonaws.com/swift/api/awssdkidentity/latest/documentation/awssdkidentity/ssoawscredentialidentityresolver)`
Resolves credentials using a single-sign-on login with AWS IAM Identity Center.

[`StaticAWSCredentialIdentityResolver`](https://sdk.amazonaws.com/swift/api/awssdkidentity/latest/documentation/awssdkidentity/staticawscredentialidentityresolver)
A credential resolver that uses specified credentials in the form of an `[AWSCredentialIdentity](https://sdk.amazonaws.com/swift/api/smithyidentity/latest/documentation/smithyidentity/awscredentialidentity)` object.

`[STSAssumeRoleAWSCredentialIdentityResolver](https://sdk.amazonaws.com/swift/api/awssdkidentity/latest/documentation/awssdkidentity/stsassumeroleawscredentialidentityresolver)`
Uses another credential identity resolver to assume a specified AWS Identity and Access Management role, then fetch the assumed credentials using AWS Security Token Service.

[`STSWebIdentityAWSCredentialIdentityResolver`](https://sdk.amazonaws.com/swift/api/awssdkidentity/latest/documentation/awssdkidentity/stswebidentityawscredentialidentityresolver)
Exchanges a JSON Web Token (JWT) for credentials using AWS Security Token Service.

## Getting credentials from an identity
<a name="identity-steps"></a>

The process of using a credential identity resolver involves four primary steps:

1. Use an appropriate sign-in service to obtain an identity in a form supported by AWS.

1. Create a credential identity resolver of the type that corresponds to the given identity.

1. When creating an AWS service client object, provide the credential identity resolver as the value of its configuration's `awsCredentialIdentityResolver` property.

1. Call service functions using the service client object.

The following sections provide examples using some of the credential identity providers supported by AWS.

## Login credential identity resolver with AWS Signin
<a name="identity-login"></a>

Authenticating for an AWS service using console credentials requires first creating login token with AWS Command Line Interface. See [Login for AWS local development using console credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html) for more details.

Once the login token is created and cached by AWS CLI command **aws login** or **aws login --profile {{profile-name}}**, your application can use `LoginAWSCredentialIdentityResolver` to obtain credentials using the established login token.

To create a Login credential identity resolver, create a new `LoginAWSCredentialIdentityResolver` that uses the desired settings for the profile name, `config` file path, and `credentials` file path. Any of these can be `nil` to use the same default value the AWS CLI would use.

**Note**
To use credential identity resolvers, you must import the `AWSSDKIdentity` module:

```
import AWSSDKIdentity
```

```
let identityResolver = try LoginAWSCredentialIdentityResolver(
    profileName: profile,
    configFilePath: config,
    credentialsFilePath: credentials
)
```

To use this resolver to provide credentials to an AWS service, set the service configuration's `awsCredentialIdentityResolver` to the created credential identity resolver.

```
// Get an S3Client with which to access Amazon S3.
let configuration = try await S3Client.S3ClientConfiguration(
    awsCredentialIdentityResolver: identityResolver
)
let client = S3Client(config: configuration)

// Use "Paginated" to get all the buckets. This lets the SDK handle
// the 'continuationToken' in "ListBucketsOutput".
let pages = client.listBucketsPaginated(
    input: ListBucketsInput(maxBuckets: 10)
)
```

## SSO credential identity resolvers with AWS IAM Identity Center
<a name="identity-sso"></a>

Authenticating for an AWS service using SSO requires first configuring SSO access using AWS IAM Identity Center. See [IAM Identity Center authentication for your SDK or tool](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html) in the AWS SDKs and Tools Reference Guide for instructions on setting up IAM Identity Center and configuring SSO access on computers that will use your application.

Once a user has authenticated with the AWS Command Line Interface (AWS CLI) command **aws sso login** or **aws sso login --profile {{profile-name}}**, your application can use an `[SSOAWSCredentialIdentityResolver](https://sdk.amazonaws.com/swift/api/awssdkidentity/latest/documentation/awssdkidentity/ssoawscredentialidentityresolver)` to obtain credentials using the established IAM Identity Center identity.

To create an SSO credential identity resolver, create a new `SSOAWSCredentialIdentityResolver` that uses the desired settings for the profile name, `config` file path, and `credentials` file path. Any of these can be `nil` to use the same default value the AWS CLI would use.

**Note**
To use credential identity resolvers, you must import the `AWSSDKIdentity` module:

```
import AWSSDKIdentity
```

```
            let identityResolver = try SSOAWSCredentialIdentityResolver(
                profileName: profile,
                configFilePath: config,
                credentialsFilePath: credentials
            )
```

To use the IAM Identity Center identity resolver to provide credentials to an AWS service, set the service configuration's `awsCredentialIdentityResolver` to the created credential identity resolver.

```
        // Get an S3Client with which to access Amazon S3.
        let configuration = try await S3Client.S3ClientConfiguration(
            awsCredentialIdentityResolver: identityResolver
        )
        let client = S3Client(config: configuration)

        // Use "Paginated" to get all the buckets. This lets the SDK handle
        // the 'continuationToken' in "ListBucketsOutput".
        let pages = client.listBucketsPaginated(
            input: ListBucketsInput(maxBuckets: 10)
        )
```

With the service configured this way, each time the SDK accesses the AWS service, it uses the credentials returned by the SSO credential identity resolver to authenticate the request.

## Static credential identity resolvers
<a name="identity-example-static"></a>

**Warning**
Static credential identity resolvers are highly unsafe unless used with care. They can return hard-coded credentials, which are inherently unsafe to use. Only use static credential identity resolvers when experimenting, testing, or generating safe static credentials from another source before using them.

Static credential identity resolvers use AWS credentials as an identity. To create a static credential identity resolver, create an `AWSCredentialIdentity` object with the static credentials, then create a new `StaticAWSCredentialIdentityResolver` that uses that identity.

**Note**
To use credential identity resolvers, you must import the `AWSSDKIdentity` module:

```
import AWSSDKIdentity
```

```
        let credentials = AWSCredentialIdentity(
            accessKey: accessKey,
            secret: secretKey,
            sessionToken: sessionToken
        )

        let identityResolver = try StaticAWSCredentialIdentityResolver(credentials)
```

To use the static credential identity resolver to provide credentials to an AWS service, use it as the service configuration's `awsCredentialIdentityResolver`.:

```
            let s3Configuration = try await S3Client.S3ClientConfiguration(
                awsCredentialIdentityResolver: identityResolver,
                region: region
            )
            let client = S3Client(config: s3Configuration)

            // Use "Paginated" to get all the buckets. This lets the SDK handle
            // the 'continuationToken' in "ListBucketsOutput".
            let pages = client.listBucketsPaginated(
                input: ListBucketsInput( maxBuckets: 10)
            )
```

When the service client asks the credential identity resolver for its credentials, the resolver returns the `AWSCredentialIdentity` struct's access key, secret, and session token.

The complete example is [available on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/sts/AssumeRole).

## Amazon Cognito credential identity resolvers
<a name="identity-cognito-resolvers"></a>

To use Amazon Cognito to provide credentials to an AWS service, first create an object of type `CognitoAWSCredentialIdentityResolver`, specifying the Amazon Cognito Identity Pool ID of the identity pool to use for credentials:

```
        // Create a Cognito credential resolver that uses the Cognito Identity
        // Pool.
        let cognitoCredentialResolver = try CognitoAWSCredentialIdentityResolver(
            identityPoolId: identityPoolID,
            identityPoolRegion: region
        )
```

Once the credential identity resolver has been created, you can instruct service clients to use it to resolve credentials by including the `awsCredentialIdentityResolver` property in the client's configuration with its value set to the `CognitoAWSCredentialIdentityResolver`.

```
        let s3Config = try await S3Client.S3ClientConfiguration(
            awsCredentialIdentityResolver: cognitoCredentialResolver,
            region: region
        )
        let s3Client = S3Client(config: s3Config)

        let listBucketsOutput = try await s3Client.listBuckets(
            input: ListBucketsInput()
        )
```

This example creates an Amazon S3 client that uses the Amazon Cognito credential identity resolver to authenticate when using the S3 client. All AWS actions performed using the client will authenticate using the resolved credentials, as shown here by calling `S3Client.listBuckets(input:)`.

## Additional information
<a name="identity-additional-information"></a>
+ [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html): SSO token provider configuration

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Swift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-swift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
