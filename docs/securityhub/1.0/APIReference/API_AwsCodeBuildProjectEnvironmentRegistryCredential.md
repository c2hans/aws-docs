---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsCodeBuildProjectEnvironmentRegistryCredential.html
---

# AwsCodeBuildProjectEnvironmentRegistryCredential
<a name="API_AwsCodeBuildProjectEnvironmentRegistryCredential"></a>

The credentials for access to a private registry.

## Contents
<a name="API_AwsCodeBuildProjectEnvironmentRegistryCredential_Contents"></a>

 ** Credential **   <a name="securityhub-Type-AwsCodeBuildProjectEnvironmentRegistryCredential-Credential"></a>
The ARN or name of credentials created using AWS Secrets Manager.
The credential can use the name of the credentials only if they exist in your current AWS Region.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CredentialProvider **   <a name="securityhub-Type-AwsCodeBuildProjectEnvironmentRegistryCredential-CredentialProvider"></a>
The service that created the credentials to access a private Docker registry.
The valid value,` SECRETS_MANAGER`, is for AWS Secrets Manager.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsCodeBuildProjectEnvironmentRegistryCredential_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsCodeBuildProjectEnvironmentRegistryCredential)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsCodeBuildProjectEnvironmentRegistryCredential)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsCodeBuildProjectEnvironmentRegistryCredential)
