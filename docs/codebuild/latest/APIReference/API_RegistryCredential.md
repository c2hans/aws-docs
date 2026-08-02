---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_RegistryCredential.html
---

# RegistryCredential
<a name="API_RegistryCredential"></a>

 Information about credentials that provide access to a private Docker registry. When this is set:
+  `imagePullCredentialsType` must be set to `SERVICE_ROLE`.
+  images cannot be curated or an Amazon ECR image.

 For more information, see [Private Registry with AWS Secrets Manager Sample for AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-private-registry.html).

## Contents
<a name="API_RegistryCredential_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** credential **   <a name="CodeBuild-Type-RegistryCredential-credential"></a>
 The Amazon Resource Name (ARN) or name of credentials created using AWS Secrets Manager.
 The `credential` can use the name of the credentials only if they exist in your current AWS Region.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** credentialProvider **   <a name="CodeBuild-Type-RegistryCredential-credentialProvider"></a>
 The service that created the credentials to access a private Docker registry. The valid value, SECRETS\_MANAGER, is for AWS Secrets Manager.
Type: String
Valid Values: `SECRETS_MANAGER`
Required: Yes

## See Also
<a name="API_RegistryCredential_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/RegistryCredential)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/RegistryCredential)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/RegistryCredential)
