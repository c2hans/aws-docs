---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_ExportStatus.html
---

# ExportStatus
<a name="API_DataExports_ExportStatus"></a>

The status of the data export.

## Contents
<a name="API_DataExports_ExportStatus_Contents"></a>

 ** CreatedAt **   <a name="awscostmanagement-Type-DataExports_ExportStatus-CreatedAt"></a>
The timestamp of when the export was created.
Type: Timestamp
Required: No

 ** LastRefreshedAt **   <a name="awscostmanagement-Type-DataExports_ExportStatus-LastRefreshedAt"></a>
The timestamp of when the export was last generated.
Type: Timestamp
Required: No

 ** LastUpdatedAt **   <a name="awscostmanagement-Type-DataExports_ExportStatus-LastUpdatedAt"></a>
The timestamp of when the export was updated.
Type: Timestamp
Required: No

 ** StatusCode **   <a name="awscostmanagement-Type-DataExports_ExportStatus-StatusCode"></a>
The status code for the request.
Type: String
Valid Values: `HEALTHY | UNHEALTHY`
Required: No

 ** StatusReason **   <a name="awscostmanagement-Type-DataExports_ExportStatus-StatusReason"></a>
The description for the status code.
Type: String
Valid Values: `INSUFFICIENT_PERMISSION | BILL_OWNER_CHANGED | INTERNAL_FAILURE | DEPRECATED`
Required: No

## See Also
<a name="API_DataExports_ExportStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-data-exports-2023-11-26/ExportStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-data-exports-2023-11-26/ExportStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-data-exports-2023-11-26/ExportStatus)
