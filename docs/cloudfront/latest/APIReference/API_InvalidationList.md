---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_InvalidationList.html
---

# InvalidationList
<a name="API_InvalidationList"></a>

The `InvalidationList` complex type describes the list of invalidation objects. For more information about invalidation, see [Invalidating Objects (Web Distributions Only)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html) in the *Amazon CloudFront Developer Guide*.

## Contents
<a name="API_InvalidationList_Contents"></a>

 ** IsTruncated **   <a name="cloudfront-Type-InvalidationList-IsTruncated"></a>
A flag that indicates whether more invalidation batch requests remain to be listed. If your results were truncated, you can make a follow-up pagination request using the `Marker` request parameter to retrieve more invalidation batches in the list.
Type: Boolean
Required: Yes

 ** Marker **   <a name="cloudfront-Type-InvalidationList-Marker"></a>
The value that you provided for the `Marker` request parameter.
Type: String
Required: Yes

 ** MaxItems **   <a name="cloudfront-Type-InvalidationList-MaxItems"></a>
The value that you provided for the `MaxItems` request parameter.
Type: Integer
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-InvalidationList-Quantity"></a>
The number of invalidation batches that were created by the current AWS account.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-InvalidationList-Items"></a>
A complex type that contains one `InvalidationSummary` element for each invalidation batch created by the current AWS account.
Type: Array of [InvalidationSummary](API_InvalidationSummary.md) objects
Required: No

 ** NextMarker **   <a name="cloudfront-Type-InvalidationList-NextMarker"></a>
If `IsTruncated` is `true`, this element is present and contains the value that you can use for the `Marker` request parameter to continue listing your invalidation batches where they left off.
Type: String
Required: No

## See Also
<a name="API_InvalidationList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/InvalidationList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/InvalidationList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/InvalidationList)
