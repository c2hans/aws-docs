---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_QueryStringCacheKeys.html
---

# QueryStringCacheKeys
<a name="API_QueryStringCacheKeys"></a>

This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field.

If you want to include query strings in the cache key, use `QueryStringsConfig` in a cache policy. See `CachePolicy`.

If you want to send query strings to the origin but not include them in the cache key, use `QueryStringsConfig` in an origin request policy. See `OriginRequestPolicy`.

A complex type that contains information about the query string parameters that you want CloudFront to use for caching for a cache behavior.

## Contents
<a name="API_QueryStringCacheKeys_Contents"></a>

 ** Quantity **   <a name="cloudfront-Type-QueryStringCacheKeys-Quantity"></a>
The number of `whitelisted` query string parameters for a cache behavior.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-QueryStringCacheKeys-Items"></a>
A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If `Quantity` is 0, you can omit `Items`.
Type: Array of strings
Required: No

## See Also
<a name="API_QueryStringCacheKeys_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/QueryStringCacheKeys)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/QueryStringCacheKeys)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/QueryStringCacheKeys)
