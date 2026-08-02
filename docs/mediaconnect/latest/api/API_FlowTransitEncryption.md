---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_FlowTransitEncryption.html
---

# FlowTransitEncryption
<a name="API_FlowTransitEncryption"></a>

The configuration that defines how content is encrypted during transit between the MediaConnect router and a MediaConnect flow.

## Contents
<a name="API_FlowTransitEncryption_Contents"></a>

 ** encryptionKeyConfiguration **   <a name="mediaconnect-Type-FlowTransitEncryption-encryptionKeyConfiguration"></a>
The configuration details for the encryption key.
Type: [FlowTransitEncryptionKeyConfiguration](API_FlowTransitEncryptionKeyConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** encryptionKeyType **   <a name="mediaconnect-Type-FlowTransitEncryption-encryptionKeyType"></a>
The type of encryption key to use for flow transit encryption.
Type: String
Valid Values: `SECRETS_MANAGER | AUTOMATIC`
Required: No

## See Also
<a name="API_FlowTransitEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/FlowTransitEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/FlowTransitEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/FlowTransitEncryption)
