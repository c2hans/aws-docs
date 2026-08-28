---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_IcebergOrphanFileDeletionMetrics.html
---

# IcebergOrphanFileDeletionMetrics
<a name="API_IcebergOrphanFileDeletionMetrics"></a>

Orphan file deletion metrics for Iceberg for the optimizer run.

## Contents
<a name="API_IcebergOrphanFileDeletionMetrics_Contents"></a>

 ** DpuHours **   <a name="Glue-Type-IcebergOrphanFileDeletionMetrics-DpuHours"></a>
The number of DPU hours consumed by the job.
Type: Double
Required: No

 ** JobDurationInHour **   <a name="Glue-Type-IcebergOrphanFileDeletionMetrics-JobDurationInHour"></a>
The duration of the job in hours.
Type: Double
Required: No

 ** NumberOfDpus **   <a name="Glue-Type-IcebergOrphanFileDeletionMetrics-NumberOfDpus"></a>
The number of DPUs consumed by the job, rounded up to the nearest whole number.
Type: Integer
Required: No

 ** NumberOfOrphanFilesDeleted **   <a name="Glue-Type-IcebergOrphanFileDeletionMetrics-NumberOfOrphanFilesDeleted"></a>
The number of orphan files deleted by the orphan file deletion job run.
Type: Long
Required: No

## See Also
<a name="API_IcebergOrphanFileDeletionMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IcebergOrphanFileDeletionMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IcebergOrphanFileDeletionMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IcebergOrphanFileDeletionMetrics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
