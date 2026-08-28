---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ResponseHeadersPolicyCustomHeader.html
---

# ResponseHeadersPolicyCustomHeader
<a name="API_ResponseHeadersPolicyCustomHeader"></a>

An HTTP response header name and its value. CloudFront includes this header in HTTP responses that it sends for requests that match a cache behavior that's associated with this response headers policy.

## Contents
<a name="API_ResponseHeadersPolicyCustomHeader_Contents"></a>

 ** Header **   <a name="cloudfront-Type-ResponseHeadersPolicyCustomHeader-Header"></a>
The HTTP response header name.
Type: String
Required: Yes

 ** Override **   <a name="cloudfront-Type-ResponseHeadersPolicyCustomHeader-Override"></a>
A Boolean that determines whether CloudFront overrides a response header with the same name received from the origin with the header specified here.
Type: Boolean
Required: Yes

 ** Value **   <a name="cloudfront-Type-ResponseHeadersPolicyCustomHeader-Value"></a>
The value for the HTTP response header.
Type: String
Required: Yes

## See Also
<a name="API_ResponseHeadersPolicyCustomHeader_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyCustomHeader)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyCustomHeader)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyCustomHeader)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
