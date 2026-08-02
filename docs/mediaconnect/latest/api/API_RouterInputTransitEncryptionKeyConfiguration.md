---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RouterInputTransitEncryptionKeyConfiguration.html
---

# RouterInputTransitEncryptionKeyConfiguration
<a name="API_RouterInputTransitEncryptionKeyConfiguration"></a>

Defines the configuration settings for transit encryption keys.

## Contents
<a name="API_RouterInputTransitEncryptionKeyConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** automatic **   <a name="mediaconnect-Type-RouterInputTransitEncryptionKeyConfiguration-automatic"></a>
Configuration settings for automatic encryption key management, where MediaConnect handles key creation and rotation.
Type: [AutomaticEncryptionKeyConfiguration](API_AutomaticEncryptionKeyConfiguration.md) object
Required: No

 ** secretsManager **   <a name="mediaconnect-Type-RouterInputTransitEncryptionKeyConfiguration-secretsManager"></a>
The configuration settings for transit encryption using AWS Secrets Manager, including the secret ARN and role ARN.
Type: [SecretsManagerEncryptionKeyConfiguration](API_SecretsManagerEncryptionKeyConfiguration.md) object
Required: No

## See Also
<a name="API_RouterInputTransitEncryptionKeyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RouterInputTransitEncryptionKeyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RouterInputTransitEncryptionKeyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RouterInputTransitEncryptionKeyConfiguration)
