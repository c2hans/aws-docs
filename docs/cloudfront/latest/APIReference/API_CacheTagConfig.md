---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CacheTagConfig.html
---

# CacheTagConfig
<a name="API_CacheTagConfig"></a>

A complex type that specifies the HTTP header name from which CloudFront extracts cache tags from origin responses. When you add `CacheTagConfig` to a distribution, CloudFront reads the specified header from origin responses, parses the comma-separated tag values, and stores them with the cached object. You can then invalidate cached objects by tag using the `CreateInvalidation` API.

## Contents
<a name="API_CacheTagConfig_Contents"></a>

 ** HeaderName **   <a name="cloudfront-Type-CacheTagConfig-HeaderName"></a>
The name of the HTTP header that your origin includes in responses. CloudFront uses this header to extract cache tags. The header value must contain comma-separated tag values (for example, `product:electronics, category:tv, brand:example`).
Type: String
Required: Yes

## See Also
<a name="API_CacheTagConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CacheTagConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CacheTagConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CacheTagConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
