---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_OriginRequestPolicy.html
---

# OriginRequestPolicy
<a name="API_OriginRequestPolicy"></a>

An origin request policy.

When it's attached to a cache behavior, the origin request policy determines the values that CloudFront includes in requests that it sends to the origin. Each request that CloudFront sends to the origin includes the following:
+ The request body and the URL path (without the domain name) from the viewer request.
+ The headers that CloudFront automatically includes in every origin request, including `Host`, `User-Agent`, and `X-Amz-Cf-Id`.
+ All HTTP headers, cookies, and URL query strings that are specified in the cache policy or the origin request policy. These can include items from the viewer request and, in the case of headers, additional ones that are added by CloudFront.

CloudFront sends a request when it can't find an object in its cache that matches the request. If you want to send values to the origin and also include them in the cache key, use `CachePolicy`.

## Contents
<a name="API_OriginRequestPolicy_Contents"></a>

 ** Id **   <a name="cloudfront-Type-OriginRequestPolicy-Id"></a>
The unique identifier for the origin request policy.
Type: String
Required: Yes

 ** LastModifiedTime **   <a name="cloudfront-Type-OriginRequestPolicy-LastModifiedTime"></a>
The date and time when the origin request policy was last modified.
Type: Timestamp
Required: Yes

 ** OriginRequestPolicyConfig **   <a name="cloudfront-Type-OriginRequestPolicy-OriginRequestPolicyConfig"></a>
The origin request policy configuration.
Type: [OriginRequestPolicyConfig](API_OriginRequestPolicyConfig.md) object
Required: Yes

## See Also
<a name="API_OriginRequestPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/OriginRequestPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/OriginRequestPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/OriginRequestPolicy)
