---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_OriginCustomHeader.html
---

# OriginCustomHeader
<a name="API_OriginCustomHeader"></a>

A complex type that contains `HeaderName` and `HeaderValue` elements, if any, for this distribution.

## Contents
<a name="API_OriginCustomHeader_Contents"></a>

 ** HeaderName **   <a name="cloudfront-Type-OriginCustomHeader-HeaderName"></a>
The name of a header that you want CloudFront to send to your origin. For more information, see [Adding Custom Headers to Origin Requests](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html) in the * Amazon CloudFront Developer Guide*.
Type: String
Required: Yes

 ** HeaderValue **   <a name="cloudfront-Type-OriginCustomHeader-HeaderValue"></a>
The value for the header that you specified in the `HeaderName` field.
Type: String
Required: Yes

## See Also
<a name="API_OriginCustomHeader_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/OriginCustomHeader)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/OriginCustomHeader)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/OriginCustomHeader)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
