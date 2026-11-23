---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DistributionIdOwnerList.html
---

# DistributionIdOwnerList

The list of distribution IDs and the AWS accounts that they belong to.

## Contents
<a name="API_DistributionIdOwnerList_Contents"></a>

 ** IsTruncated **   <a name="cloudfront-Type-DistributionIdOwnerList-IsTruncated"></a>
A flag that indicates whether more `DistributionIdOwner` objects remain to be listed. If your results were truncated, you can make a follow-up pagination request using the `Marker` request parameter to retrieve more results in the list.
Type: Boolean
Required: Yes

 ** Marker **   <a name="cloudfront-Type-DistributionIdOwnerList-Marker"></a>
Use this field when paginating results to indicate where to begin in your list of `DistributionIdOwner` objects. The response includes distributions in the list that occur after the marker. To get the next page of the list, set this field's value to the value of `NextMarker` from the current page's response.
Type: String
Required: Yes

 ** MaxItems **   <a name="cloudfront-Type-DistributionIdOwnerList-MaxItems"></a>
The maximum number of `DistributionIdOwner` objects to return.
Type: Integer
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-DistributionIdOwnerList-Quantity"></a>
Specifies the actual number of `DistributionIdOwner` objects included in the list for the current page.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-DistributionIdOwnerList-Items"></a>
The number of `DistributionIdOwner` objects.
Type: Array of [DistributionIdOwner](API_DistributionIdOwner.md) objects
Required: No

 ** NextMarker **   <a name="cloudfront-Type-DistributionIdOwnerList-NextMarker"></a>
A token used for pagination of results returned in the response. You can use the token from the previous request to define where the current request should begin.
Type: String
Required: No

## See Also
<a name="API_DistributionIdOwnerList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DistributionIdOwnerList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DistributionIdOwnerList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DistributionIdOwnerList)
