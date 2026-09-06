---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_PublicKey.html
---

# PublicKey
<a name="API_PublicKey"></a>

A public key that you can use with [signed URLs and signed cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html), or with [field-level encryption](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html).

CloudFront supports signed URLs and signed cookies with RSA 2048 or ECDSA 256 key signatures. Field-level encryption is only compatible with RSA 2048 key signatures.

## Contents
<a name="API_PublicKey_Contents"></a>

 ** CreatedTime **   <a name="cloudfront-Type-PublicKey-CreatedTime"></a>
The date and time when the public key was uploaded.
Type: Timestamp
Required: Yes

 ** Id **   <a name="cloudfront-Type-PublicKey-Id"></a>
The identifier of the public key.
Type: String
Required: Yes

 ** PublicKeyConfig **   <a name="cloudfront-Type-PublicKey-PublicKeyConfig"></a>
Configuration information about a public key that you can use with [signed URLs and signed cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html), or with [field-level encryption](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html).
Type: [PublicKeyConfig](API_PublicKeyConfig.md) object
Required: Yes

## See Also
<a name="API_PublicKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/PublicKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/PublicKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/PublicKey)
