---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_StorageClassAnalysisDataExport.html
---

# StorageClassAnalysisDataExport
<a name="API_StorageClassAnalysisDataExport"></a>

Container for data related to the storage class analysis for an Amazon S3 bucket for export.

## Contents
<a name="API_StorageClassAnalysisDataExport_Contents"></a>

 ** Destination **   <a name="AmazonS3-Type-StorageClassAnalysisDataExport-Destination"></a>
The place to store the data for an analysis.
Type: [AnalyticsExportDestination](API_AnalyticsExportDestination.md) data type
Required: Yes

 ** OutputSchemaVersion **   <a name="AmazonS3-Type-StorageClassAnalysisDataExport-OutputSchemaVersion"></a>
The version of the output schema to use when exporting data. Must be `V_1`.
Type: String
Valid Values: `V_1`
Required: Yes

## See Also
<a name="API_StorageClassAnalysisDataExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/StorageClassAnalysisDataExport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/StorageClassAnalysisDataExport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/StorageClassAnalysisDataExport)
