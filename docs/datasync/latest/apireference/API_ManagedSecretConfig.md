---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_ManagedSecretConfig.html
---

# ManagedSecretConfig
<a name="API_ManagedSecretConfig"></a>

Specifies configuration information for a DataSync-managed secret, such as an authentication token or set of credentials that DataSync uses to access a specific transfer location. DataSync uses the default AWS-managed KMS key to encrypt this secret in AWS Secrets Manager.

## Contents
<a name="API_ManagedSecretConfig_Contents"></a>

 ** SecretArn **   <a name="DataSync-Type-ManagedSecretConfig-SecretArn"></a>
Specifies the ARN for an AWS Secrets Manager secret.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^(arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):secretsmanager:[a-z\-0-9]+:[0-9]{12}:secret:.*|)$`
Required: No

## See Also
<a name="API_ManagedSecretConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/ManagedSecretConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/ManagedSecretConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/ManagedSecretConfig)
