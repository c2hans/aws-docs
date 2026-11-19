---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_StorageLensCostAndUsageReportsPrefixLevel.html
---

# StorageLensCostAndUsageReportsPrefixLevel

A container for the prefix-level configuration that determines the prefixes for which S3 Storage Lens publishes cost data to AWS Cost and Usage Reports (AWS CUR).

## Contents
<a name="API_control_StorageLensCostAndUsageReportsPrefixLevel_Contents"></a>

 ** IsEnabled **   <a name="AmazonS3-Type-control_StorageLensCostAndUsageReportsPrefixLevel-IsEnabled"></a>
Indicates whether prefix-level cost data publishing to AWS CUR is enabled.
Type: Boolean
Required: Yes

 ** SelectionCriteria **   <a name="AmazonS3-Type-control_StorageLensCostAndUsageReportsPrefixLevel-SelectionCriteria"></a>
A container for the selection criteria that determines the prefix depths for which cost data is published to AWS CUR.
Type: [StorageLensCostAndUsageReportsSelectionCriteria](API_control_StorageLensCostAndUsageReportsSelectionCriteria.md) data type
Required: No

## See Also
<a name="API_control_StorageLensCostAndUsageReportsPrefixLevel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/StorageLensCostAndUsageReportsPrefixLevel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/StorageLensCostAndUsageReportsPrefixLevel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/StorageLensCostAndUsageReportsPrefixLevel)
