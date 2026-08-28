---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CustomHeaders.html
---

# CustomHeaders
<a name="API_CustomHeaders"></a>

A complex type that contains the list of Custom Headers for each origin.

## Contents
<a name="API_CustomHeaders_Contents"></a>

 ** Quantity **   <a name="cloudfront-Type-CustomHeaders-Quantity"></a>
The number of custom headers, if any, for this distribution.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-CustomHeaders-Items"></a>
 **Optional**: A list that contains one `OriginCustomHeader` element for each custom header that you want CloudFront to forward to the origin. If Quantity is `0`, omit `Items`.
Type: Array of [OriginCustomHeader](API_OriginCustomHeader.md) objects
Required: No

## See Also
<a name="API_CustomHeaders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CustomHeaders)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CustomHeaders)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CustomHeaders)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
