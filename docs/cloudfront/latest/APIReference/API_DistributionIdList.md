---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DistributionIdList.html
---

# DistributionIdList
<a name="API_DistributionIdList"></a>

A list of distribution IDs.

## Contents
<a name="API_DistributionIdList_Contents"></a>

 ** IsTruncated **   <a name="cloudfront-Type-DistributionIdList-IsTruncated"></a>
A flag that indicates whether more distribution IDs remain to be listed. If your results were truncated, you can make a subsequent request using the `Marker` request field to retrieve more distribution IDs in the list.
Type: Boolean
Required: Yes

 ** Marker **   <a name="cloudfront-Type-DistributionIdList-Marker"></a>
The value provided in the `Marker` request field.
Type: String
Required: Yes

 ** MaxItems **   <a name="cloudfront-Type-DistributionIdList-MaxItems"></a>
The maximum number of distribution IDs requested.
Type: Integer
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-DistributionIdList-Quantity"></a>
The total number of distribution IDs returned in the response.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-DistributionIdList-Items"></a>
Contains the distribution IDs in the list.
Type: Array of strings
Required: No

 ** NextMarker **   <a name="cloudfront-Type-DistributionIdList-NextMarker"></a>
Contains the value that you should use in the `Marker` field of a subsequent request to continue listing distribution IDs where you left off.
Type: String
Required: No

## See Also
<a name="API_DistributionIdList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DistributionIdList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DistributionIdList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DistributionIdList)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
