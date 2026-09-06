---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-client-credentials.html
---

# Credentials provider changes
<a name="migration-client-credentials"></a>

This section provides a mapping of the name changes of credentials provider classes and methods between versions 1.x and 2.x of the AWS SDK for Java.

## Notable differences
<a name="client-credentials"></a>
+ The default credentials provider loads system properties before environment variables in version 2.x. For more information, see [Using credentials](credentials.md).
+ The constructor method is replaced with the `create` or `builder` methods.
**Example**

  ```
  DefaultCredentialsProvider.create();
  ```
+ Asynchronous refresh is no longer set by default. You must specify it with the `builder` of the credentials provider.
**Example**

  ```
  ContainerCredentialsProvider provider = ContainerCredentialsProvider.builder()
          		.asyncCredentialUpdateEnabled(true)
          		.build();
  ```
+ You can specify a path to a custom profile file using the `ProfileCredentialsProvider.builder()`.
**Example**

  ```
  ProfileCredentialsProvider profile = ProfileCredentialsProvider.builder()
          		.profileFile(ProfileFile.builder().content(Paths.get("myProfileFile.file")).build())
          		.build();
  ```
+ Profile file format has changed to more closely match the AWS CLI. For details, see [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) in the *AWS Command Line Interface User Guide*.

## Credentials provider changes mapped between versions 1.x and 2.x
<a name="credentials-changes-mapping"></a>

### `AWSCredentialsProvider`
<a name="credentials-provider-changes-AWSCredentialsProvider"></a>

| Change category | 1.x | 2.x |
| --- | --- | --- |
| Package/class name | com.amazonaws.auth.AWSCredentialsProvider | software.amazon.awssdk.auth.credentials.AwsCredentialsProvider |
| Method name | getCredentials | resolveCredentials |
| Unsupported method | refresh | Not supported |

### `DefaultAWSCredentialsProviderChain`
<a name="credentials-provider-changes-DefaultAWSCredentialsProviderChain"></a>

| Change category | 1.x | 2.x |
| --- | --- | --- |
| Package/class name | com.amazonaws.auth.DefaultAWSCredentialsProviderChain | software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider |
| Creation | new DefaultAWSCredentialsProviderChain | DefaultCredentialsProvider.create |
| Unsupported method | getInstance | Not supported |
| Priority order of external settings | Environment variables before system properties | System properties before environment variables |

### `AWSStaticCredentialsProvider`
<a name="credentials-provider-changes-AWSStaticCredentialsProvider"></a>

| Change category | 1.x | 2.x |
| --- | --- | --- |
| Package/class name | com.amazonaws.auth.AWSStaticCredentialsProvider | software.amazon.awssdk.auth.credentials.StaticCredentialsProvider |
| Creation | new AWSStaticCredentialsProvider | StaticCredentialsProvider.create |

### `EnvironmentVariableCredentialsProvider`
<a name="credentials-provider-changes-EnvironmentVariableCredentialsProvider"></a>

| Change category | 1.x | 2.x |
| --- | --- | --- |
| Package/class name | com.amazonaws.auth.EnvironmentVariableCredentialsProvider | software.amazon.awssdk.auth.credentials.EnvironmentVariableCredentialsProvider |
| Creation | new EnvironmentVariableCredentialsProvider | EnvironmentVariableCredentialsProvider.create |
| Environment variable name | AWS\_ACCESS\_KEY | AWS\_ACCESS\_KEY\_ID |
|  | AWS\_SECRET\_KEY | AWS\_SECRET\_ACCESS\_KEY |

### `SystemPropertiesCredentialsProvider`
<a name="credentials-provider-changes-SystemPropertiesCredentialsProvider"></a>

| Change category | 1.x | 2.x |
| --- | --- | --- |
| Package/class name | com.amazonaws.auth.SystemPropertiesCredentialsProvider | software.amazon.awssdk.auth.credentials.SystemPropertyCredentialsProvider |
| Creation | new SystemPropertiesCredentialsProvider | SystemPropertiesCredentialsProvider.create |
| System property name | aws.secretKey | aws.secretAccessKey |

### `ProfileCredentialsProvider`
<a name="credentials-provider-changes-ProfileCredentialsProvider"></a>

| Change category | 1.x | 2.x |
| --- | --- | --- |
| Package/class name | com.amazonaws.auth.profile.ProfileCredentialsProvider | software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider |
| Creation | new ProfileCredentialsProvider | ProfileCredentialsProvider.create |
| Location of custom profile |  +  `AWS_CREDENTIAL_PROFILES_FILE` environment variable <br />+  `new ProfileCredentialsProvider`   |  +  `AWS_SHARED_CREDENTIALS_FILE` environment variable <br />+  `ProfileCredentialsProvider.builder`   |

### `ContainerCredentialsProvider`
<a name="credentials-provider-changes-ContainerCredentialsProvider"></a>

| Change category | 1.x | 2.x |
| --- | --- | --- |
| Package/class name | com.amazonaws.auth.ContainerCredentialsProvider | software.amazon.awssdk.auth.credentials.ContainerCredentialsProvider |
| Creation | new ContainerCredentialsProvider | ContainerCredentialsProvider.create |
| Specify asynchronous refresh | Not supported | Default behavior |

### `InstanceProfileCredentialsProvider`
<a name="credentials-provider-changes-InstanceProfileCredentialsProvider"></a>

| Change category | 1.x | 2.x |
| --- | --- | --- |
| Package/class name | com.amazonaws.auth.InstanceProfileCredentialsProvider | software.amazon.awssdk.auth.credentials.InstanceProfileCredentialsProvider |
| Creation | new InstanceProfileCredentialsProvider | InstanceProfileCredentialsProvider.create |
| Specify asynchronous refresh | new InstanceProfileCredentialsProvider(true) | `InstanceProfileCredentialProvider.builder().asyncCredentialUpdateEnabled(true).build()` |
| System property name | com.amazonaws.sdk.disableEc2Metadata | aws.disableEc2Metadata |
|  | com.amazonaws.sdk.ec2MetadataServiceEndpointOverride | aws.ec2MetadataServiceEndpoint |

### `STSAssumeRoleSessionCredentialsProvider`
<a name="credentials-provider-changes-STSAssumeRoleSessionCredentialsProvider"></a>

| Change category | 1.x | 2.x |
| --- | --- | --- |
| Package/class name | com.amazonaws.auth.STSAssumeRoleSessionCredentialsProvider | software.amazon.awssdk.services.sts.auth.StsAssumeRoleCredentialsProvider |
| Creation |  +  `new STSAssumeRoleSessionCredentialsProvider` <br />+  `new STSAssumeRoleSessionCredentialsProvider.Builder`   | StsAssumeRoleCredentialsProvider.builder |
| Asynchronous refresh | Default behavior | Default behavior |
| Configuration | new STSAssumeRoleSessionCredentialsProvider.Builder | Configure a StsClient and AssumeRoleRequest request |

### `STSSessionCredentialsProvider`
<a name="credentials-provider-changes-STSSessionCredentialsProvider"></a>

| Change category | 1.x | 2.x |
| --- | --- | --- |
| Package/class name | com.amazonaws.auth.STSSessionCredentialsProvider | software.amazon.awssdk.services.sts.auth.StsGetSessionTokenCredentialsProvider |
| Creation | `new STSSessionCredentialsProvider` | StsGetSessionTokenCredentialsProvider.builder |
| Asynchronous refresh | Default behavior | StsGetSessionTokenCredentialsProvider.builder |
| Configuration | Constructor parameters | Configure an StsClient and GetSessionTokenRequest request in a builder |

### `WebIdentityFederationSessionCredentialsProvider`
<a name="credentials-provider-changes-WebIdentityFederationSessionCredentialsProvider"></a>

| Change category | 1.x | 2.x |
| --- | --- | --- |
| Package/class name | com.amazonaws.auth.WebIdentityFederationSessionCredentialsProvider | software.amazon.awssdk.services.sts.auth.StsAssumeRoleWithWebIdentityCredentialsProvider |
| Creation | `new WebIdentityFederationSessionCredentialsProvider` | StsAssumeRoleWithWebIdentityCredentialsProvider.builder |
| Asynchronous refresh | Default behavior | StsAssumeRoleWithWebIdentityCredentialsProvider.builder |
| Configuration | Constructor parameters | Configure an StsClient and AssumeRoleWithWebIdentityRequest request in a builder |

### Classes replaced
<a name="credentials-provider-changes-Replacements"></a>

| 1.x class | 2.x replacement classes |
| --- | --- |
| com.amazonaws.auth.EC2ContainerCredentialsProviderWrapper | software.amazon.awssdk.auth.credentials.ContainerCredentialsProvider and software.amazon.awssdk.auth.credentials.InstanceProfileCredentialsProvider |
| com.amazonaws.services.s3.S3CredentialsProviderChain | software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider and software.amazon.awssdk.auth.credentials.AnonymousCredentialsProvider |

### Classes removed
<a name="credentials-provider-changes-Removed"></a>

| 1.x class |
| --- |
| com.amazonaws.auth.ClasspathPropertiesFileCredentialsProvider |
| com.amazonaws.auth.PropertiesFileCredentialsProvider |
