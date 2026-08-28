---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_KeyGroupList.html
---

# KeyGroupList
<a name="API_KeyGroupList"></a>

A list of key groups.

## Contents
<a name="API_KeyGroupList_Contents"></a>

 ** MaxItems **   <a name="cloudfront-Type-KeyGroupList-MaxItems"></a>
The maximum number of key groups requested.
Type: Integer
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-KeyGroupList-Quantity"></a>
The number of key groups returned in the response.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-KeyGroupList-Items"></a>
A list of key groups.
Type: Array of [KeyGroupSummary](API_KeyGroupSummary.md) objects
Required: No

 ** NextMarker **   <a name="cloudfront-Type-KeyGroupList-NextMarker"></a>
If there are more items in the list than are in this response, this element is present. It contains the value that you should use in the `Marker` field of a subsequent request to continue listing key groups.
Type: String
Required: No

## See Also
<a name="API_KeyGroupList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/KeyGroupList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/KeyGroupList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/KeyGroupList)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
