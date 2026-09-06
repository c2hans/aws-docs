---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CloudFrontOriginAccessIdentity.html
---

# CloudFrontOriginAccessIdentity
<a name="API_CloudFrontOriginAccessIdentity"></a>

CloudFront origin access identity.

## Contents
<a name="API_CloudFrontOriginAccessIdentity_Contents"></a>

 ** Id **   <a name="cloudfront-Type-CloudFrontOriginAccessIdentity-Id"></a>
The ID for the origin access identity, for example, `E74FTE3AJFJ256A`.
Type: String
Required: Yes

 ** S3CanonicalUserId **   <a name="cloudfront-Type-CloudFrontOriginAccessIdentity-S3CanonicalUserId"></a>
The Amazon S3 canonical user ID for the origin access identity, used when giving the origin access identity read permission to an object in Amazon S3.
Type: String
Required: Yes

 ** CloudFrontOriginAccessIdentityConfig **   <a name="cloudfront-Type-CloudFrontOriginAccessIdentity-CloudFrontOriginAccessIdentityConfig"></a>
The current configuration information for the identity.
Type: [CloudFrontOriginAccessIdentityConfig](API_CloudFrontOriginAccessIdentityConfig.md) object
Required: No

## See Also
<a name="API_CloudFrontOriginAccessIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CloudFrontOriginAccessIdentity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CloudFrontOriginAccessIdentity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CloudFrontOriginAccessIdentity)
