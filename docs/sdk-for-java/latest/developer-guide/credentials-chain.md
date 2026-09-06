---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credentials-chain.html
---

# Default credentials provider chain in the AWS SDK for Java 2.x
<a name="credentials-chain"></a>

The default credentials provider chain in the AWS SDK for Java 2.x automatically searches for AWS credentials in a predefined sequence of locations, allowing applications to authenticate with AWS services without explicitly specifying credential sources.

The default credentials provider chain is implemented by the [DefaultCredentialsProvider](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/auth/credentials/DefaultCredentialsProvider.html) class. It sequentially delegates to other credentials provider implementations that check for configuration in various locations. The first credentials provider that can find all necessary configuration elements causes the chain to end.

To use the default credentials provider chain to supply temporary credentials, create a service client builder but don't specify a credentials provider. The following code snippet creates a `DynamoDbClient` that uses the default credentials provider chain to locate and retrieve configuration settings.

```
// Any external Region configuration is overridden.
// The SDK uses the default credentials provider chain because no specific credentials provider is specified.
Region region = Region.US_WEST_2;
DynamoDbClient ddb =
    DynamoDbClient.builder()
                  .region(region)
                  .build();
```

## Credential settings retrieval order
<a name="credentials-default"></a>

The default credentials provider chain of the SDK for Java 2.x searches for configuration in your environment using a predefined sequence.

1. Java system properties
   + The SDK uses the [SystemPropertyCredentialsProvider](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/auth/credentials/SystemPropertyCredentialsProvider.html) class to load temporary credentials from the `aws.accessKeyId`, `aws.secretAccessKey`, and `aws.sessionToken` Java system properties.
**Note**
For information on how to set Java system properties, see the [System Properties](https://docs.oracle.com/javase/tutorial/essential/environment/sysprop.html) tutorial on the official *Java Tutorials* website.

1. Environment variables
   + The SDK uses the [EnvironmentVariableCredentialsProvider](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/auth/credentials/EnvironmentVariableCredentialsProvider.html) class to load temporary credentials from the `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` environment variables.

1. Web identity token and IAM role ARN
   + The SDK uses the [WebIdentityTokenFileCredentialsProvider](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/auth/credentials/WebIdentityTokenFileCredentialsProvider.html) class to load credentials by assuming a role using a web identity token.
   + The credentials provider looks for the following environment variables or JVM system properties:
     + `AWS_WEB_IDENTITY_TOKEN_FILE or aws.webIdentityTokenFile`
     + `AWS_ROLE_ARN` or `aws.roleArn`
     + `AWS_ROLE_SESSION_NAME` or `aws.roleSessionName` (optional)
   + After the SDK acquires the values, it calls the AWS Security Token Service (STS) and uses the temporary credentials it returns to sign requests.
   + Runtime environments such as Amazon Elastic Kubernetes Service (EKS) automatically make web identity tokens available to AWS SDKs, enabling applications to obtain temporary AWS credentials.

1. The shared `credentials` and `config` files
   + The SDK uses the [ProfileCredentialsProvider](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/auth/credentials/ProfileCredentialsProvider.html) to load IAM Identity Center single sign-on settings or temporary credentials from the `[default]` profile in the shared `credentials` and `config` files.

     The AWS SDKs and Tools Reference Guide has [detailed information](https://docs.aws.amazon.com/sdkref/latest/guide/understanding-sso.html#idccredres) about how the SDK for Java works with the IAM Identity Center single sign-on token to get temporary credentials that the SDK uses to call AWS services.
**Note**
The `credentials` and `config` files are shared by various AWS SDKs and Tools. For more information, see [The .aws/credentials and .aws/config files](https://docs.aws.amazon.com/sdkref/latest/guide/creds-config-files.html) in the AWS SDKs and Tools Reference Guide.
   + Because a profile in the shared `credentials` and `config` files can contain many different sets of settings, the `ProfileCredentialsProvider` delegates to a series of other providers to look for settings under the `[default]` profile:
     + **Web identity token credentials** (class `WebIdentityTokenCredentialsProvider`): When the profile contains `role_arn` and `web_identity_token_file`.
     + **SSO credentials** (class `SsoCredentialsProvider`): When the profile contains SSO-related properties such as `sso_role_name`, `sso_account_id`.
     + **Role-based credentials with source profile** (class `StsAssumeRoleCredentialsProvider`): When the profile contains `role_arn` and `source_profile`.
     + **Role-based credentials with credential source** (class `StsAssumeRoleWithSourceCredentialsProvider`): When the profile contains `role_arn` and `credential_source`.
       + When `credential_source = Environment`: It uses a chain of `SystemPropertyCredentialsProvider` and `EnvironmentVariableCredentialsProvider`
       + When `credential_source = Ec2InstanceMetadata`: It uses `InstanceProfileCredentialsProvider`
       + When `credential_source = EcsContainer`: It uses `ContainerCredentialsProvider`
     + **Console login credentials** (class `LoginCredentialsProvider`): When the profile contains `login_session`
     + **Process credentials** (class `ProcessCredentialsProvider`): When the profile contains `credential_process`.
     + **Session credentials** (class `StaticSessionCredentialsProvider`): When the profile contains `aws_access_key_id`, `aws_secret_access_key`, and `aws_session_token`.
     + **Basic credentials** (class `StaticCredentialsProvider`): When the profile contains `aws_access_key_id` and `aws_secret_access_key`.

1.  Amazon ECS container credentials
   + The SDK uses the [ContainerCredentialsProvider](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/auth/credentials/ContainerCredentialsProvider.html) class to load temporary credentials using the following environment variables:

     1. `AWS_CONTAINER_CREDENTIALS_RELATIVE_URI` or `AWS_CONTAINER_CREDENTIALS_FULL_URI`

     1. `AWS_CONTAINER_AUTHORIZATION_TOKEN_FILE` or `AWS_CONTAINER_AUTHORIZATION_TOKEN`

   The ECS container agent automatically sets the `AWS_CONTAINER_CREDENTIALS_RELATIVE_URI` environment variable, which points to the ECS credentials endpoint. The other environment variables are typically set in specific scenarios where the standard ECS credential endpoint isn't used.

1.  Amazon EC2 instance IAM role-provided credentials
   + The SDK uses the [InstanceProfileCredentialsProvider](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/auth/credentials/InstanceProfileCredentialsProvider.html) class to load temporary credentials from the Amazon EC2 metadata service.

1. If the SDK can't find the necessary configuration settings through all this steps listed above, it throws an exception with output similar to the following:

   ```
   software.amazon.awssdk.core.exception.SdkClientException: Unable to load credentials from any of the providers
   in the chain AwsCredentialsProviderChain(credentialsProviders=[SystemPropertyCredentialsProvider(),
   EnvironmentVariableCredentialsProvider(), WebIdentityTokenCredentialsProvider(), ProfileCredentialsProvider(),
   ContainerCredentialsProvider(), InstanceProfileCredentialsProvider()])
   ```

## Use the `DefaultCredentialsProvider` in code
<a name="default-credentials-provider-in-code"></a>

You can explicitly use the default credentials provider chain in your code. This is functionally equivalent to you not specifying a credentials provider at all, since the SDK uses `DefaultCredentialsProvider` by default. However, explicitly using it can make your code more readable and self-documenting. It clearly shows your intention to use the default credentials chain.

```
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;

public class ExplicitDefaultCredentialsExample {
    public static void main(String[] args) {
        // Explicitly create the DefaultCredentialsProvider.
        DefaultCredentialsProvider defaultCredentialsProvider = DefaultCredentialsProvider
                                                                    .builder().build();

        // Use it with any service client.
        S3Client s3Client = S3Client.builder()
            .region(Region.US_WEST_2)
            .credentialsProvider(defaultCredentialsProvider)
            .build();

        // Now you can use the client with the default credentials chain.
        s3Client.listBuckets();
    }
}
```

When you build the default credentials provider you can provide more configuration:

```
DefaultCredentialsProvider customizedProvider = DefaultCredentialsProvider.builder()
    .profileName("custom-profile")  // Use a specific profile if the chain gets to the `ProfileCredentialsProvider` stage.
    .asyncCredentialUpdateEnabled(true)  // Enable async credential updates.
    .build();
```

This approach gives you more control while still providing the convenience of the default credentials chain.
