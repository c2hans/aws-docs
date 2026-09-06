---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_IcebergRetentionMetrics.html
---

# IcebergRetentionMetrics
<a name="API_IcebergRetentionMetrics"></a>

Snapshot retention metrics for Iceberg for the optimizer run.

## Contents
<a name="API_IcebergRetentionMetrics_Contents"></a>

 ** DpuHours **   <a name="Glue-Type-IcebergRetentionMetrics-DpuHours"></a>
The number of DPU hours consumed by the job.
Type: Double
Required: No

 ** JobDurationInHour **   <a name="Glue-Type-IcebergRetentionMetrics-JobDurationInHour"></a>
The duration of the job in hours.
Type: Double
Required: No

 ** NumberOfDataFilesDeleted **   <a name="Glue-Type-IcebergRetentionMetrics-NumberOfDataFilesDeleted"></a>
The number of data files deleted by the retention job run.
Type: Long
Required: No

 ** NumberOfDpus **   <a name="Glue-Type-IcebergRetentionMetrics-NumberOfDpus"></a>
The number of DPUs consumed by the job, rounded up to the nearest whole number.
Type: Integer
Required: No

 ** NumberOfManifestFilesDeleted **   <a name="Glue-Type-IcebergRetentionMetrics-NumberOfManifestFilesDeleted"></a>
The number of manifest files deleted by the retention job run.
Type: Long
Required: No

 ** NumberOfManifestListsDeleted **   <a name="Glue-Type-IcebergRetentionMetrics-NumberOfManifestListsDeleted"></a>
The number of manifest lists deleted by the retention job run.
Type: Long
Required: No

## See Also
<a name="API_IcebergRetentionMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IcebergRetentionMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IcebergRetentionMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IcebergRetentionMetrics)
