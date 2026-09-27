---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_TlsEncryption.html
---

# TlsEncryption
<a name="API_TlsEncryption"></a>

The Transport Layer Security (TLS) encryption settings used to establish a secure connection to a destination.

## Contents
<a name="API_TlsEncryption_Contents"></a>

 ** encryptionConfiguration **   <a name="mediaconnect-Type-TlsEncryption-encryptionConfiguration"></a>
The configuration settings for the specified TLS encryption type.
Type: [TlsEncryptionConfiguration](API_TlsEncryptionConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** encryptionType **   <a name="mediaconnect-Type-TlsEncryption-encryptionType"></a>
The type of TLS encryption to use for the connection.
Type: String
Valid Values: `PUBLIC`
Required: No

## See Also
<a name="API_TlsEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/TlsEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/TlsEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/TlsEncryption)
