---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_StreamingDistributionList.html
---

# StreamingDistributionList
<a name="API_StreamingDistributionList"></a>

A streaming distribution list.

## Contents
<a name="API_StreamingDistributionList_Contents"></a>

 ** IsTruncated **   <a name="cloudfront-Type-StreamingDistributionList-IsTruncated"></a>
A flag that indicates whether more streaming distributions remain to be listed. If your results were truncated, you can make a follow-up pagination request using the `Marker` request parameter to retrieve more distributions in the list.
Type: Boolean
Required: Yes

 ** Marker **   <a name="cloudfront-Type-StreamingDistributionList-Marker"></a>
The value you provided for the `Marker` request parameter.
Type: String
Required: Yes

 ** MaxItems **   <a name="cloudfront-Type-StreamingDistributionList-MaxItems"></a>
The value you provided for the `MaxItems` request parameter.
Type: Integer
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-StreamingDistributionList-Quantity"></a>
The number of streaming distributions that were created by the current AWS account.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-StreamingDistributionList-Items"></a>
A complex type that contains one `StreamingDistributionSummary` element for each distribution that was created by the current AWS account.
Type: Array of [StreamingDistributionSummary](API_StreamingDistributionSummary.md) objects
Required: No

 ** NextMarker **   <a name="cloudfront-Type-StreamingDistributionList-NextMarker"></a>
If `IsTruncated` is `true`, this element is present and contains the value you can use for the `Marker` request parameter to continue listing your RTMP distributions where they left off.
Type: String
Required: No

## See Also
<a name="API_StreamingDistributionList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/StreamingDistributionList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/StreamingDistributionList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/StreamingDistributionList)
