---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_VpcOriginList.html
---

# VpcOriginList
<a name="API_VpcOriginList"></a>

A list of CloudFront VPC origins.

## Contents
<a name="API_VpcOriginList_Contents"></a>

 ** IsTruncated **   <a name="cloudfront-Type-VpcOriginList-IsTruncated"></a>
A flag that indicates whether more VPC origins remain to be listed. If your results were truncated, you can make a follow-up pagination request using the `Marker` request parameter to retrieve more VPC origins in the list.
Type: Boolean
Required: Yes

 ** Marker **   <a name="cloudfront-Type-VpcOriginList-Marker"></a>
The marker associated with the VPC origins list.
Type: String
Required: Yes

 ** MaxItems **   <a name="cloudfront-Type-VpcOriginList-MaxItems"></a>
The maximum number of items included in the list.
Type: Integer
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-VpcOriginList-Quantity"></a>
The number of VPC origins in the list.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-VpcOriginList-Items"></a>
The items of the VPC origins list.
Type: Array of [VpcOriginSummary](API_VpcOriginSummary.md) objects
Required: No

 ** NextMarker **   <a name="cloudfront-Type-VpcOriginList-NextMarker"></a>
The next marker associated with the VPC origins list.
Type: String
Required: No

## See Also
<a name="API_VpcOriginList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/VpcOriginList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/VpcOriginList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/VpcOriginList)
