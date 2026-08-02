---
source_url: https://docs.aws.amazon.com/signer/latest/api/API_SigningPlatformOverrides.html
---

# SigningPlatformOverrides
<a name="API_SigningPlatformOverrides"></a>

Any overrides that are applied to the signing configuration of a signing platform.

## Contents
<a name="API_SigningPlatformOverrides_Contents"></a>

 ** signingConfiguration **   <a name="signer-Type-SigningPlatformOverrides-signingConfiguration"></a>
A signing configuration that overrides the default encryption or hash algorithm of a signing job.
Type: [SigningConfigurationOverrides](API_SigningConfigurationOverrides.md) object
Required: No

 ** signingImageFormat **   <a name="signer-Type-SigningPlatformOverrides-signingImageFormat"></a>
A signed image is a JSON object. When overriding the default signing platform configuration, a customer can select either of two signing formats, `JSONEmbedded` or `JSONDetached`. (A third format value, `JSON`, is reserved for future use.) With `JSONEmbedded`, the signing image has the payload embedded in it. With `JSONDetached`, the payload is not be embedded in the signing image.
Type: String
Valid Values: `JSON | JSONEmbedded | JSONDetached`
Required: No

## See Also
<a name="API_SigningPlatformOverrides_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/SigningPlatformOverrides)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/SigningPlatformOverrides)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/SigningPlatformOverrides)
