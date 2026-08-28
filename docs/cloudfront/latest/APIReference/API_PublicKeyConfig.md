---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_PublicKeyConfig.html
---

# PublicKeyConfig
<a name="API_PublicKeyConfig"></a>

Configuration information about a public key that you can use with [signed URLs and signed cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html), or with [field-level encryption](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html).

CloudFront supports signed URLs and signed cookies with RSA 2048 or ECDSA 256 key signatures. Field-level encryption is only compatible with RSA 2048 key signatures.

## Contents
<a name="API_PublicKeyConfig_Contents"></a>

 ** CallerReference **   <a name="cloudfront-Type-PublicKeyConfig-CallerReference"></a>
A string included in the request to help make sure that the request can't be replayed.
Type: String
Required: Yes

 ** EncodedKey **   <a name="cloudfront-Type-PublicKeyConfig-EncodedKey"></a>
The public key that you can use with [signed URLs and signed cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html), or with [field-level encryption](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html).
Type: String
Required: Yes

 ** Name **   <a name="cloudfront-Type-PublicKeyConfig-Name"></a>
A name to help identify the public key.
Type: String
Required: Yes

 ** Comment **   <a name="cloudfront-Type-PublicKeyConfig-Comment"></a>
A comment to describe the public key. The comment cannot be longer than 128 characters.
Type: String
Required: No

## See Also
<a name="API_PublicKeyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/PublicKeyConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/PublicKeyConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/PublicKeyConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
