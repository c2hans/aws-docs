---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_MediaLiveTransitEncryption.html
---

# MediaLiveTransitEncryption
<a name="API_MediaLiveTransitEncryption"></a>

The encryption configuration that defines how content is encrypted during transit between MediaConnect Router and MediaLive. This configuration determines whether encryption keys are automatically managed by the service or manually managed through AWS Secrets Manager.

## Contents
<a name="API_MediaLiveTransitEncryption_Contents"></a>

 ** encryptionKeyConfiguration **   <a name="mediaconnect-Type-MediaLiveTransitEncryption-encryptionKeyConfiguration"></a>
The configuration details for the MediaLive encryption key.
Type: [MediaLiveTransitEncryptionKeyConfiguration](API_MediaLiveTransitEncryptionKeyConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** encryptionKeyType **   <a name="mediaconnect-Type-MediaLiveTransitEncryption-encryptionKeyType"></a>
The type of encryption key to use for MediaLive transit encryption.
Type: String
Valid Values: `SECRETS_MANAGER | AUTOMATIC`
Required: No

## See Also
<a name="API_MediaLiveTransitEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/MediaLiveTransitEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/MediaLiveTransitEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/MediaLiveTransitEncryption)
