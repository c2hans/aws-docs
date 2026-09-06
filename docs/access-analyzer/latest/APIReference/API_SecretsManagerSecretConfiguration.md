---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_SecretsManagerSecretConfiguration.html
---

# SecretsManagerSecretConfiguration
<a name="API_SecretsManagerSecretConfiguration"></a>

The configuration for a Secrets Manager secret. For more information, see [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html).

You can propose a configuration for a new secret or an existing secret that you own by specifying the secret policy and optional AWS KMS encryption key. If the configuration is for an existing secret and you do not specify the secret policy, the access preview uses the existing policy for the secret. If the access preview is for a new resource and you do not specify the policy, the access preview assumes a secret without a policy. To propose deletion of an existing policy, you can specify an empty string. If the proposed configuration is for a new secret and you do not specify the KMS key ID, the access preview uses the AWS managed key `aws/secretsmanager`. If you specify an empty string for the KMS key ID, the access preview uses the AWS managed key of the AWS account. For more information about secret policy limits, see [Quotas for AWS Secrets Manager.](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_limits.html).

## Contents
<a name="API_SecretsManagerSecretConfiguration_Contents"></a>

 ** kmsKeyId **   <a name="accessanalyzer-Type-SecretsManagerSecretConfiguration-kmsKeyId"></a>
The proposed ARN, key ID, or alias of the KMS key.
Type: String
Required: No

 ** secretPolicy **   <a name="accessanalyzer-Type-SecretsManagerSecretConfiguration-secretPolicy"></a>
The proposed resource policy defining who can access or manage the secret.
Type: String
Required: No

## See Also
<a name="API_SecretsManagerSecretConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/SecretsManagerSecretConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/SecretsManagerSecretConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/SecretsManagerSecretConfiguration)
