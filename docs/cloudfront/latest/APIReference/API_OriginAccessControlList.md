---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_OriginAccessControlList.html
---

# OriginAccessControlList
<a name="API_OriginAccessControlList"></a>

A list of CloudFront origin access controls.

## Contents
<a name="API_OriginAccessControlList_Contents"></a>

 ** IsTruncated **   <a name="cloudfront-Type-OriginAccessControlList-IsTruncated"></a>
If there are more items in the list than are in this response, this value is `true`.
Type: Boolean
Required: Yes

 ** Marker **   <a name="cloudfront-Type-OriginAccessControlList-Marker"></a>
The value of the `Marker` field that was provided in the request.
Type: String
Required: Yes

 ** MaxItems **   <a name="cloudfront-Type-OriginAccessControlList-MaxItems"></a>
The maximum number of origin access controls requested.
Type: Integer
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-OriginAccessControlList-Quantity"></a>
The number of origin access controls returned in the response.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-OriginAccessControlList-Items"></a>
Contains the origin access controls in the list.
Type: Array of [OriginAccessControlSummary](API_OriginAccessControlSummary.md) objects
Required: No

 ** NextMarker **   <a name="cloudfront-Type-OriginAccessControlList-NextMarker"></a>
If there are more items in the list than are in this response, this element is present. It contains the value to use in the `Marker` field of another request to continue listing origin access controls.
Type: String
Required: No

## See Also
<a name="API_OriginAccessControlList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/OriginAccessControlList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/OriginAccessControlList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/OriginAccessControlList)
