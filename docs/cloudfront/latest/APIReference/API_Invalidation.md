---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_Invalidation.html
---

# Invalidation
<a name="API_Invalidation"></a>

An invalidation.

## Contents
<a name="API_Invalidation_Contents"></a>

 ** CreateTime **   <a name="cloudfront-Type-Invalidation-CreateTime"></a>
The date and time the invalidation request was first made.
Type: Timestamp
Required: Yes

 ** Id **   <a name="cloudfront-Type-Invalidation-Id"></a>
The identifier for the invalidation request. For example: `IDFDVBD632BHDS5`.
Type: String
Required: Yes

 ** InvalidationBatch **   <a name="cloudfront-Type-Invalidation-InvalidationBatch"></a>
The current invalidation information for the batch request.
Type: [InvalidationBatch](API_InvalidationBatch.md) object
Required: Yes

 ** Status **   <a name="cloudfront-Type-Invalidation-Status"></a>
The status of the invalidation request. When the invalidation batch is finished, the status is `Completed`.
Type: String
Required: Yes

## See Also
<a name="API_Invalidation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/Invalidation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/Invalidation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/Invalidation)
