---
source_url: https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-aws-configuration-profile-credentials.html
---

# AWS configuration profile credentials
<a name="jdbc-v3-driver-aws-configuration-profile-credentials"></a>

You can use credentials stored in an AWS configuration profile by setting the following connection parameters. AWS configuration profiles are typically stored in files in the `~/.aws` directory). For information about AWS configuration profiles, see [Use profiles](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credentials-profiles.html) in the *AWS SDK for Java Developer Guide*.

## Credentials provider
<a name="jdbc-v3-driver-aws-configuration-profile-credentials-provider"></a>

The credentials provider that will be used to authenticate requests to AWS. Set the value of this parameter to `ProfileCredentials`.

| Parameter name | Alias | Parameter type | Default value | Value to use |
| --- | --- | --- | --- | --- |
| CredentialsProvider | AWSCredentialsProviderClass (deprecated) | Required | none | ProfileCredentials |

## Profile name
<a name="jdbc-v3-driver-profile-name"></a>

The name of the AWS configuration profile whose credentials should be used to authenticate the request to Athena.

| Parameter name | Alias | Parameter type | Default value |
| --- | --- | --- | --- |
| ProfileName | none | Required | none |

**Note**
The profile name can also be specified as the value of the `CredentialsProviderArguments` parameter, although this use is deprecated.
