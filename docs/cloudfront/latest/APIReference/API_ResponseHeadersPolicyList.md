---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ResponseHeadersPolicyList.html
---

# ResponseHeadersPolicyList
<a name="API_ResponseHeadersPolicyList"></a>

A list of response headers policies.

## Contents
<a name="API_ResponseHeadersPolicyList_Contents"></a>

 ** MaxItems **   <a name="cloudfront-Type-ResponseHeadersPolicyList-MaxItems"></a>
The maximum number of response headers policies requested.
Type: Integer
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-ResponseHeadersPolicyList-Quantity"></a>
The number of response headers policies returned.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-ResponseHeadersPolicyList-Items"></a>
The response headers policies in the list.
Type: Array of [ResponseHeadersPolicySummary](API_ResponseHeadersPolicySummary.md) objects
Required: No

 ** NextMarker **   <a name="cloudfront-Type-ResponseHeadersPolicyList-NextMarker"></a>
If there are more items in the list than are in this response, this element is present. It contains the value that you should use in the `Marker` field of a subsequent request to continue listing response headers policies where you left off.
Type: String
Required: No

## See Also
<a name="API_ResponseHeadersPolicyList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ResponseHeadersPolicyList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ResponseHeadersPolicyList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ResponseHeadersPolicyList)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
