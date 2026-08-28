---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CachePolicyQueryStringsConfig.html
---

# CachePolicyQueryStringsConfig
<a name="API_CachePolicyQueryStringsConfig"></a>

An object that determines whether any URL query strings in viewer requests (and if so, which query strings) are included in the cache key and in requests that CloudFront sends to the origin.

## Contents
<a name="API_CachePolicyQueryStringsConfig_Contents"></a>

 ** QueryStringBehavior **   <a name="cloudfront-Type-CachePolicyQueryStringsConfig-QueryStringBehavior"></a>
Determines whether any URL query strings in viewer requests are included in the cache key and in requests that CloudFront sends to the origin. Valid values are:
+  `none` – No query strings in viewer requests are included in the cache key or in requests that CloudFront sends to the origin. Even when this field is set to `none`, any query strings that are listed in an `OriginRequestPolicy` *are* included in origin requests.
+  `whitelist` – Only the query strings in viewer requests that are listed in the `QueryStringNames` type are included in the cache key and in requests that CloudFront sends to the origin.
+  `allExcept` – All query strings in viewer requests are included in the cache key and in requests that CloudFront sends to the origin, * **except** * those that are listed in the `QueryStringNames` type, which are not included.
+  `all` – All query strings in viewer requests are included in the cache key and in requests that CloudFront sends to the origin.
Type: String
Valid Values: `none | whitelist | allExcept | all`
Required: Yes

 ** QueryStrings **   <a name="cloudfront-Type-CachePolicyQueryStringsConfig-QueryStrings"></a>
Contains the specific query strings in viewer requests that either * **are** * or * **are not** * included in the cache key and in requests that CloudFront sends to the origin. The behavior depends on whether the `QueryStringBehavior` field in the `CachePolicyQueryStringsConfig` type is set to `whitelist` (the listed query strings * **are** * included) or `allExcept` (the listed query strings * **are not** * included, but all other query strings are).
Type: [QueryStringNames](API_QueryStringNames.md) object
Required: No

## See Also
<a name="API_CachePolicyQueryStringsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CachePolicyQueryStringsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CachePolicyQueryStringsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CachePolicyQueryStringsConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
