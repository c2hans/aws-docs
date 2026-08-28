---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DistributionList.html
---

# DistributionList
<a name="API_DistributionList"></a>

A distribution list.

## Contents
<a name="API_DistributionList_Contents"></a>

 ** IsTruncated **   <a name="cloudfront-Type-DistributionList-IsTruncated"></a>
A flag that indicates whether more distributions remain to be listed. If your results were truncated, you can make a follow-up pagination request using the `Marker` request parameter to retrieve more distributions in the list.
Type: Boolean
Required: Yes

 ** Marker **   <a name="cloudfront-Type-DistributionList-Marker"></a>
The value you provided for the `Marker` request parameter.
Type: String
Required: Yes

 ** MaxItems **   <a name="cloudfront-Type-DistributionList-MaxItems"></a>
The value you provided for the `MaxItems` request parameter.
Type: Integer
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-DistributionList-Quantity"></a>
The number of distributions that were created by the current AWS account.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-DistributionList-Items"></a>
A complex type that contains one `DistributionSummary` element for each distribution that was created by the current AWS account.
Type: Array of [DistributionSummary](API_DistributionSummary.md) objects
Required: No

 ** NextMarker **   <a name="cloudfront-Type-DistributionList-NextMarker"></a>
If `IsTruncated` is `true`, this element is present and contains the value you can use for the `Marker` request parameter to continue listing your distributions where they left off.
Type: String
Required: No

## See Also
<a name="API_DistributionList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DistributionList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DistributionList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DistributionList)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
