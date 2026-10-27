---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_EndpointEncryptionConfiguration.html
---

# EndpointEncryptionConfiguration
<a name="API_EndpointEncryptionConfiguration"></a>

The encryption settings for an endpoint connection. This is a union type, so exactly one of its members is set: `secretsManager` when you store the encryption key or passphrase in AWS Secrets Manager, or `automatic` when you let MediaConnect determine the encryption key when the endpoint connects.

## Contents
<a name="API_EndpointEncryptionConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** automatic **   <a name="mediaconnect-Type-EndpointEncryptionConfiguration-automatic"></a>
The configuration for automatic encryption, where MediaConnect determines the encryption key when the endpoint connects.
Type: [AutomaticEndpointEncryptionConfiguration](API_AutomaticEndpointEncryptionConfiguration.md) object
Required: No

 ** secretsManager **   <a name="mediaconnect-Type-EndpointEncryptionConfiguration-secretsManager"></a>
The encryption configuration for a connection that uses a key or passphrase that you store in AWS Secrets Manager.
Type: [SecretsManagerEndpointEncryptionConfiguration](API_SecretsManagerEndpointEncryptionConfiguration.md) object
Required: No

## See Also
<a name="API_EndpointEncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/EndpointEncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/EndpointEncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/EndpointEncryptionConfiguration)
