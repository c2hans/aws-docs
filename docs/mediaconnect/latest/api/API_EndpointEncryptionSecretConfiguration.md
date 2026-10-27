---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_EndpointEncryptionSecretConfiguration.html
---

# EndpointEncryptionSecretConfiguration
<a name="API_EndpointEncryptionSecretConfiguration"></a>

The configuration for the AWS Secrets Manager secret that holds the key or passphrase used to encrypt an endpoint connection.

## Contents
<a name="API_EndpointEncryptionSecretConfiguration_Contents"></a>

 ** secretArn **   <a name="mediaconnect-Type-EndpointEncryptionSecretConfiguration-secretArn"></a>
The ARN of the AWS Secrets Manager secret that holds the key or passphrase. The secret must be encrypted with a customer managed AWS KMS key that is enabled and symmetric; it cannot use the AWS managed key `aws/secretsmanager`. The secret must be in the same AWS account and Region as the endpoint.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9/_+=.@-]+`
Required: Yes

## See Also
<a name="API_EndpointEncryptionSecretConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/EndpointEncryptionSecretConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/EndpointEncryptionSecretConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/EndpointEncryptionSecretConfiguration)
