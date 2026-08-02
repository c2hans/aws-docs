---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/credential-providers.html
---

# Credentials providers
<a name="credential-providers"></a>

**Important**
 **The order in which the default credential provider chain resolves credentials changed with version 1.4.0. For details, see the note below.**

When you send requests to Amazon Web Services using the AWS SDK for Kotlin, requests must be cryptographically signed with credentials issued by AWS. The Kotlin SDK signs the request automatically for you. To acquire the credentials, the SDK can use configuration settings that are located in several places, for example JVM system properties, environment variables, shared AWS `config` and `credentials` files, and Amazon EC2 instance metadata.

The SDK uses the *credentials provider* abstraction to simplify the process of retrieving credentials from various sources. The SDK contains [several credentials provider implementations](/sdk-for-kotlin/api/latest/aws-config/aws.sdk.kotlin.runtime.auth.credentials/index.html).

For example, If the retrieved configuration includes IAM Identity Center single sign-on access settings from the shared `config` file, the SDK works with the IAM Identity Center to retrieve temporary credentials that it uses to make request to AWS services. With this approach to acquiring credentials, the SDK uses the IAM Identity Center provider (also known as the SSO credentials provider). The [set up section](setup-basic-onetime-setup.md#setup-sso-access) of this guide described this configuration.

To use a specific credentials provider, you can specify one when you create a service client. Alternatively, you can use the default credentials provider chain to search for configuration settings automatically.

## The default credentials provider chain
<a name="default-credential-provider-chain"></a>

When not explicitly specified at client construction, the SDK for Kotlin uses a credentials provider that sequentially checks each place where you can supply credentials. This default credentials provider is implemented as a chain of credentials providers.

To use the default chain to supply credentials in your application, create a service client without explicitly providing a `credentialsProvider` property.

```
val ddb = DynamoDbClient {
    region = "us-east-2"
}
```

For more information about service client creation, see [construct and configure a client](creating-clients.md).

### Learn about the default credentials provider chain
<a name="default-credentials-retrieval-order"></a>

The default credentials provider chain searches for credentials configuration using the following predefined sequence. When the configured settings provide valid credentials, the chain stops.

 **1. [AWS access keys (JVM system properties)](/sdkref/latest/guide/feature-static-credentials.html) **
The SDK looks for the `aws.accessKeyId`, `aws.secretAccessKey`, and `aws.sessionToken` JVM system properties.

 **2. [AWS access keys (environment variables)](/sdkref/latest/guide/feature-static-credentials.html) **
The SDK attempts to load credentials from the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` environment variables.

 **3. [Web identity token](/sdkref/latest/guide/access-assume-role-web.html) **
The SDK looks for the environment variables `AWS_WEB_IDENTITY_TOKEN_FILE` and `AWS_ROLE_ARN` (or the JVM system properties `aws.webIdentityTokenFile` and `aws.roleArn`). Based on the token information and the role, the SDK acquires temporary credentials.

 **4. [A profile in a configuration file](/sdkref/latest/guide/file-format.html) **
In this step, the SDK uses settings associated with a profile. By default, the SDK uses the shared AWS `config` and `credentials` files, but if the `AWS_CONFIG_FILE` environment variable is set, the SDK uses that value. If the `AWS_PROFILE` environment variable (or `aws.profile` JVM system property) is *not* set, the SDK looks for the “default” profile, otherwise it looks for the profile that matches the `AWS_PROFILE` value.
The SDK looks for the profile based on the configuration described in the previous paragraph and uses the settings defined there. If the settings found by the SDK contain a mix of settings for different credential-provider approaches, the SDK uses the following ordering:

1.  [AWS access keys (configuration file)](/sdkref/latest/guide/feature-static-credentials.html) - The SDK uses the settings for `aws_access_key_id`, `aws_access_key_id`, and `aws_session_token`.

1.  [Assume role configuration](/sdkref/latest/guide/access-assume-role.html) - If the SDK finds `role_arn` and `source_profile` or `credential_source` settings, it attempts to assume a role. If the SDK finds the `source_profile` setting, it sources credentials from another profile to receive temporary credentials for the role specified by `role_arn`. If the SDK finds the `credential_source` setting, it sources credentials from an Amazon ECS container, an Amazon EC2 instance, or from environment variables depending on the value of the `credential_source` setting. It then uses those credentials to acquire temporary credentials for the role.

   A profile should contain either the `source_profile` setting or the `credential_source` setting, but not both.

1.  [Web identity token configuration](/sdkref/latest/guide/access-assume-role-web.html) - If the SDK finds `role_arn` and `web_identity_token_file` settings, it acquires temporary credentials to access AWS resources based on the `role_arn` and the token.

1.  [SSO token configuration](/sdkref/latest/guide/feature-sso-credentials.html) - If the SDK finds `sso_session`, `sso_account_id`, `sso_role_name` settings (along with a companion `sso-session` section in the configuration files), the SDK retrieves temporary credentials from the IAM Identity Center service.

1.  [Legacy SSO configuration](/sdkref/latest/guide/feature-sso-credentials.html#sso-legacy) - If the SDK finds `sso_start_url`, `sso_region`, `sso_account_id`, and `sso_role_name` settings, the SDK retrieves temporary credentials from the IAM Identity Center service.

1.  [Login configuration](/sdkref/latest/guide/feature-sso-credentials.html#sso-legacy) - If the SDK finds a `login_session` setting, it uses the temporary credentials from the login session, or attempts to refresh them if they expire in under 5 mins. To learn how to start a login session, see the [AWS CLI user guide](/cli/latest/userguide/cli-configure-sign-in.html).

1.  [Process configuration](/sdkref/latest/guide/feature-process-credentials.html) - If the SDK finds a `credential_process` setting, it uses the path value to invoke a process and acquire temporary credentials.

 **5. [Container credentials](/sdkref/latest/guide/feature-container-credentials.html) **
The SDK looks for environment variables `AWS_CONTAINER_CREDENTIALS_RELATIVE_URI` or `AWS_CONTAINER_CREDENTIALS_FULL_URI` and `AWS_CONTAINER_AUTHORIZATION_TOKEN_FILE` or `AWS_CONTAINER_AUTHORIZATION_TOKEN`. It uses these values to load credentials from the specified HTTP endpoint through a GET request.

 **6. [IMDS credentials](/sdkref/latest/guide/feature-imds-credentials.html) **
The SDK attempts to fetch credentials from the [Instance Metadata Service](/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) at the default or configured HTTP endpoint. The SDK only supports [IMDSv2](/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html).

If credentials still aren’t resolved at this point, client creation fails with an exception.

**Note**
The ordering of credentials resolution described above is current for the `1.4.x+` release of the SDK for Kotlin. Before the `1.4.0` release, items number 3 and 4 were switched and the current 4a item followed the current 4g item.

## Specify a credentials provider
<a name="explicit-credential-provider"></a>

You can specify a credentials provider instead of using the default provider chain. This approach gives you direct control over which credentials the SDK uses.

For example, to use the credentials for an assumed IAM role, specify an `StsAssumeRoleCredentialsProvider` when you create the client:

```
val ddb = DynamoDbClient {
    region = "us-east-1"
    credentialsProvider = StsAssumeRoleCredentialsProvider()
}
```

You can also create a custom chain (`CredentialsProviderChain`) that combines multiple providers in your preferred order.

### Cache credentials with a standalone provider
<a name="credentials-caching"></a>

**Important**
The default chain caches credentials automatically. Standalone providers don’t cache credentials. To avoid fetching credentials on every API call, wrap your provider with a `CachedCredentialsProvider`. The cached provider fetches new credentials only when current ones expire.

To cache credentials with a standalone provider, use the `CachedCredentialsProvider` class:

```
val ddb = DynamoDbClient {
     region = "us-east-1"
     credentialsProvider = CachedCredentialsProvider(StsAssumeRoleCredentialsProvider())
 }
```

Alternatively, use the `cached()` extension function for more concise code:

```
val ddb = DynamoDbClient {
      region = "us-east-1"
      credentialsProvider = StsAssumeRoleCredentialsProvider().cached()
 }
```
