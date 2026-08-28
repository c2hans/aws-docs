---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_Paths.html
---

# Paths
<a name="API_Paths"></a>

A complex type that contains information about the objects that you want to invalidate using paths and tags. For more information, see [Specifying the Objects to Invalidate](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html#invalidation-specifying-objects) in the *Amazon CloudFront Developer Guide*.

## Contents
<a name="API_Paths_Contents"></a>

 ** Quantity **   <a name="cloudfront-Type-Paths-Quantity"></a>
The number of invalidation paths specified for the objects that you want to invalidate.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-Paths-Items"></a>
A complex type that contains a list of the paths and tags that you want to invalidate.
Type: Array of strings
Required: No

## See Also
<a name="API_Paths_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/Paths)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/Paths)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/Paths)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
