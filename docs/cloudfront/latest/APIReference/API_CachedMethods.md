---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CachedMethods.html
---

# CachedMethods
<a name="API_CachedMethods"></a>

A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:
+ CloudFront caches responses to `GET` and `HEAD` requests.
+ CloudFront caches responses to `GET`, `HEAD`, and `OPTIONS` requests.

If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.

## Contents
<a name="API_CachedMethods_Contents"></a>

 ** Items **   <a name="cloudfront-Type-CachedMethods-Items"></a>
A complex type that contains the HTTP methods that you want CloudFront to cache responses to. Valid values for `CachedMethods` include `GET`, `HEAD`, and `OPTIONS`, depending on which caching option you choose. For more information, see the preceding section.
Type: Array of strings
Valid Values: `GET | HEAD | POST | PUT | PATCH | OPTIONS | DELETE`
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-CachedMethods-Quantity"></a>
The number of HTTP methods for which you want CloudFront to cache responses. Valid values are `2` (for caching responses to `GET` and `HEAD` requests) and `3` (for caching responses to `GET`, `HEAD`, and `OPTIONS` requests).
Type: Integer
Required: Yes

## See Also
<a name="API_CachedMethods_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CachedMethods)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CachedMethods)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CachedMethods)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
