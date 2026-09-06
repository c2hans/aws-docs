---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_Encryption.html
---

# Encryption
<a name="API_Encryption"></a>

The parameters for encrypting content.

## Contents
<a name="API_Encryption_Contents"></a>

 ** EncryptionMethod **   <a name="mediapackage-Type-Encryption-EncryptionMethod"></a>
The encryption method to use.
Type: [EncryptionMethod](API_EncryptionMethod.md) object
Required: Yes

 ** SpekeKeyProvider **   <a name="mediapackage-Type-Encryption-SpekeKeyProvider"></a>
The parameters for the SPEKE key provider.
Type: [SpekeKeyProvider](API_SpekeKeyProvider.md) object
Required: Yes

 ** CmafExcludeSegmentDrmMetadata **   <a name="mediapackage-Type-Encryption-CmafExcludeSegmentDrmMetadata"></a>
Excludes SEIG and SGPD boxes from segment metadata in CMAF containers.
When set to `true`, MediaPackage omits these DRM metadata boxes from CMAF segments, which can improve compatibility with certain devices and players that don't support these boxes.
Important considerations:
+ This setting only affects CMAF container formats
+ Key rotation can still be handled through media playlist signaling
+ PSSH and TENC boxes remain unaffected
+ Default behavior is preserved when this setting is disabled
Valid values: `true` \| `false`
Default: `false`
Type: Boolean
Required: No

 ** ConstantInitializationVector **   <a name="mediapackage-Type-Encryption-ConstantInitializationVector"></a>
A 128-bit, 16-byte hex value represented by a 32-character string, used in conjunction with the key for encrypting content. If you don't specify a value, then MediaPackage creates the constant initialization vector (IV).
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-fA-F]+`
Required: No

 ** KeyRotationIntervalSeconds **   <a name="mediapackage-Type-Encryption-KeyRotationIntervalSeconds"></a>
The frequency (in seconds) of key changes for live workflows, in which content is streamed real time. The service retrieves content keys before the live content begins streaming, and then retrieves them as needed over the lifetime of the workflow. By default, key rotation is set to 300 seconds (5 minutes), the minimum rotation interval, which is equivalent to setting it to 300. If you don't enter an interval, content keys aren't rotated.
The following example setting causes the service to rotate keys every thirty minutes: `1800`
Type: Integer
Valid Range: Minimum value of 300. Maximum value of 31536000.
Required: No

## See Also
<a name="API_Encryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/Encryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/Encryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/Encryption)
