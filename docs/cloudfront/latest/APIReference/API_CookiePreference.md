---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CookiePreference.html
---

# CookiePreference
<a name="API_CookiePreference"></a>

This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field.

If you want to include cookies in the cache key, use `CookiesConfig` in a cache policy. See `CachePolicy`.

If you want to send cookies to the origin but not include them in the cache key, use `CookiesConfig` in an origin request policy. See `OriginRequestPolicy`.

A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see [Caching Content Based on Cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html) in the *Amazon CloudFront Developer Guide*.

## Contents
<a name="API_CookiePreference_Contents"></a>

 ** Forward **   <a name="cloudfront-Type-CookiePreference-Forward"></a>
This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field.
If you want to include cookies in the cache key, use a cache policy. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) in the *Amazon CloudFront Developer Guide*.
If you want to send cookies to the origin but not include them in the cache key, use origin request policy. For more information, see [Creating origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy) in the *Amazon CloudFront Developer Guide*.
Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the `WhitelistedNames` complex type.
Amazon S3 doesn't process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the `Forward` element.
Type: String
Valid Values: `none | whitelist | all`
Required: Yes

 ** WhitelistedNames **   <a name="cloudfront-Type-CookiePreference-WhitelistedNames"></a>
This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field.
If you want to include cookies in the cache key, use a cache policy. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) in the *Amazon CloudFront Developer Guide*.
If you want to send cookies to the origin but not include them in the cache key, use an origin request policy. For more information, see [Creating origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy) in the *Amazon CloudFront Developer Guide*.
Required if you specify `whitelist` for the value of `Forward`. A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.
If you specify `all` or `none` for the value of `Forward`, omit `WhitelistedNames`. If you change the value of `Forward` from `whitelist` to `all` or `none` and you don't delete the `WhitelistedNames` element and its child elements, CloudFront deletes them automatically.
For the current limit on the number of cookie names that you can whitelist for each cache behavior, see [ CloudFront Limits](https://docs.aws.amazon.com/general/latest/gr/xrefaws_service_limits.html#limits_cloudfront) in the * AWS General Reference*.
Type: [CookieNames](API_CookieNames.md) object
Required: No

## See Also
<a name="API_CookiePreference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CookiePreference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CookiePreference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CookiePreference)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
