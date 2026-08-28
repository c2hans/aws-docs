---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CacheBehaviors.html
---

# CacheBehaviors
<a name="API_CacheBehaviors"></a>

A complex type that contains zero or more `CacheBehavior` elements.

## Contents
<a name="API_CacheBehaviors_Contents"></a>

 ** Quantity **   <a name="cloudfront-Type-CacheBehaviors-Quantity"></a>
The number of cache behaviors for this distribution.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-CacheBehaviors-Items"></a>
Optional: A complex type that contains cache behaviors for this distribution. If `Quantity` is `0`, you can omit `Items`.
Type: Array of [CacheBehavior](API_CacheBehavior.md) objects
Required: No

## See Also
<a name="API_CacheBehaviors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CacheBehaviors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CacheBehaviors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CacheBehaviors)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
