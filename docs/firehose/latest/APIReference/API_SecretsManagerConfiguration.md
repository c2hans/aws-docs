---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_SecretsManagerConfiguration.html
---

# SecretsManagerConfiguration
<a name="API_SecretsManagerConfiguration"></a>

The structure that defines how Firehose accesses the secret.

## Contents
<a name="API_SecretsManagerConfiguration_Contents"></a>

 ** Enabled **   <a name="Firehose-Type-SecretsManagerConfiguration-Enabled"></a>
Specifies whether you want to use the secrets manager feature. When set as `True` the secrets manager configuration overwrites the existing secrets in the destination configuration. When it's set to `False` Firehose falls back to the credentials in the destination configuration.
Type: Boolean
Required: Yes

 ** RoleARN **   <a name="Firehose-Type-SecretsManagerConfiguration-RoleARN"></a>
 Specifies the role that Firehose assumes when calling the Secrets Manager API operation. When you provide the role, it overrides any destination specific role defined in the destination configuration. If you do not provide the then we use the destination specific role. This parameter is required for Splunk.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** SecretARN **   <a name="Firehose-Type-SecretsManagerConfiguration-SecretARN"></a>
The ARN of the secret that stores your credentials. It must be in the same region as the Firehose stream and the role. The secret ARN can reside in a different account than the Firehose stream and role as Firehose supports cross-account secret access. This parameter is required when **Enabled** is set to `True`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.*:secretsmanager:[a-zA-Z0-9\-]+:\d{12}:secret:[a-zA-Z0-9\-/_+=.@!]+`
Required: No

## See Also
<a name="API_SecretsManagerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/SecretsManagerConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/SecretsManagerConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/SecretsManagerConfiguration)
