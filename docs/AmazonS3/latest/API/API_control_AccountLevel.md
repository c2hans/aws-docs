---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AccountLevel.html
---

# AccountLevel
<a name="API_control_AccountLevel"></a>

A container element for the account-level Amazon S3 Storage Lens configuration.

**Note**
You must enable Storage Lens metrics consistently at both the account level and bucket level, or your request will fail.

For more information about S3 Storage Lens, see [Assessing your storage activity and usage with S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens.html) in the *Amazon S3 User Guide*. For a complete list of S3 Storage Lens metrics, see [S3 Storage Lens metrics glossary](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_metrics_glossary.html) in the *Amazon S3 User Guide*.

## Contents
<a name="API_control_AccountLevel_Contents"></a>

 ** BucketLevel **   <a name="AmazonS3-Type-control_AccountLevel-BucketLevel"></a>
A container element for the S3 Storage Lens bucket-level configuration.
Type: [BucketLevel](API_control_BucketLevel.md) data type
Required: Yes

 ** ActivityMetrics **   <a name="AmazonS3-Type-control_AccountLevel-ActivityMetrics"></a>
A container element for S3 Storage Lens activity metrics.
Type: [ActivityMetrics](API_control_ActivityMetrics.md) data type
Required: No

 ** AdvancedCostOptimizationMetrics **   <a name="AmazonS3-Type-control_AccountLevel-AdvancedCostOptimizationMetrics"></a>
A container element for S3 Storage Lens advanced cost-optimization metrics.
Type: [AdvancedCostOptimizationMetrics](API_control_AdvancedCostOptimizationMetrics.md) data type
Required: No

 ** AdvancedDataProtectionMetrics **   <a name="AmazonS3-Type-control_AccountLevel-AdvancedDataProtectionMetrics"></a>
A container element for S3 Storage Lens advanced data-protection metrics.
Type: [AdvancedDataProtectionMetrics](API_control_AdvancedDataProtectionMetrics.md) data type
Required: No

 ** AdvancedPerformanceMetrics **   <a name="AmazonS3-Type-control_AccountLevel-AdvancedPerformanceMetrics"></a>
A container element for S3 Storage Lens advanced performance metrics.
Type: [AdvancedPerformanceMetrics](API_control_AdvancedPerformanceMetrics.md) data type
Required: No

 ** DetailedStatusCodesMetrics **   <a name="AmazonS3-Type-control_AccountLevel-DetailedStatusCodesMetrics"></a>
A container element for detailed status code metrics.
Type: [DetailedStatusCodesMetrics](API_control_DetailedStatusCodesMetrics.md) data type
Required: No

 ** StorageLensGroupLevel **   <a name="AmazonS3-Type-control_AccountLevel-StorageLensGroupLevel"></a>
 A container element for S3 Storage Lens groups metrics.
Type: [StorageLensGroupLevel](API_control_StorageLensGroupLevel.md) data type
Required: No

## See Also
<a name="API_control_AccountLevel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/AccountLevel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/AccountLevel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/AccountLevel)
