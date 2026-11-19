---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_StorageLensCostAndUsageReportsSelectionCriteria.html
---

# StorageLensCostAndUsageReportsSelectionCriteria

A container for the selection criteria used by the S3 Storage Lens AWS Cost and Usage Reports (AWS CUR) publish configuration. The selection criteria specifies the minimum and maximum prefix depth (both inclusive) for which cost data is published to AWS CUR. You must provide both `MinDepth` and `MaxDepth` together, or neither; `MinDepth` must be less than or equal to `MaxDepth`, and the difference must not exceed 4. If neither is provided, `MinDepth` defaults to `1` and `MaxDepth` defaults to `3`.

## Contents
<a name="API_control_StorageLensCostAndUsageReportsSelectionCriteria_Contents"></a>

 ** MaxDepth **   <a name="AmazonS3-Type-control_StorageLensCostAndUsageReportsSelectionCriteria-MaxDepth"></a>
The maximum prefix depth (inclusive) for which cost data is published to AWS CUR. You must provide both `MinDepth` and `MaxDepth` together, or neither. If neither is provided, `MaxDepth` defaults to `3`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 15.
Required: No

 ** MinDepth **   <a name="AmazonS3-Type-control_StorageLensCostAndUsageReportsSelectionCriteria-MinDepth"></a>
The minimum prefix depth (inclusive) for which cost data is published to AWS CUR. You must provide both `MinDepth` and `MaxDepth` together, or neither. If neither is provided, `MinDepth` defaults to `1`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 15.
Required: No

## See Also
<a name="API_control_StorageLensCostAndUsageReportsSelectionCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/StorageLensCostAndUsageReportsSelectionCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/StorageLensCostAndUsageReportsSelectionCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/StorageLensCostAndUsageReportsSelectionCriteria)
