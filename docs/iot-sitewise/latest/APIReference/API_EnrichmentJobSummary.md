---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_EnrichmentJobSummary.html
---

# EnrichmentJobSummary
<a name="API_EnrichmentJobSummary"></a>

Summary information for an enrichment job returned by ListEnrichmentJobs. This lightweight representation includes identifiers, status, and key metadata without the full job configuration.

Use DescribeEnrichmentJob to retrieve:
+ Complete job configuration (trim settings, full parameters)
+ Detailed timestamps (completedAt, cancelledAt)
+ Failure messages for failed jobs

The summary is optimized for display in lists and dashboards, providing enough information to identify and filter jobs without the overhead of full configuration details.

## Contents
<a name="API_EnrichmentJobSummary_Contents"></a>

 ** createdAt **   <a name="iotsitewise-Type-EnrichmentJobSummary-createdAt"></a>
Timestamp when the job was created in ISO 8601 format.
Type: Timestamp
Required: Yes

 ** datasetId **   <a name="iotsitewise-Type-EnrichmentJobSummary-datasetId"></a>
The dataset being enriched. Useful for filtering and identifying jobs without fetching the full configuration. This allows you to quickly find all jobs related to a specific dataset.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** jobId **   <a name="iotsitewise-Type-EnrichmentJobSummary-jobId"></a>
Unique identifier for the enrichment job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** jobType **   <a name="iotsitewise-Type-EnrichmentJobSummary-jobType"></a>
The type of enrichment job. Currently EVENT\_DETECTION is the only supported type.
Type: String
Valid Values: `EVENT_DETECTION`
Required: Yes

 ** status **   <a name="iotsitewise-Type-EnrichmentJobSummary-status"></a>
Current status of the job: PENDING, RUNNING, COMPLETED, FAILED, TIMED\_OUT, or CANCELLED. Use this to quickly identify active jobs or jobs requiring attention.
Type: String
Valid Values: `PENDING | RUNNING | COMPLETED | FAILED | TIMED_OUT | CANCELLED`
Required: Yes

 ** workspaceName **   <a name="iotsitewise-Type-EnrichmentJobSummary-workspaceName"></a>
The name of the IoT SiteWise workspace containing this job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** propertyAlias **   <a name="iotsitewise-Type-EnrichmentJobSummary-propertyAlias"></a>
The property alias (human-readable sensor name) of the time series being enriched. Present when the job was created using a propertyAlias. Use this to identify which sensor the job analyzes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** timeSeriesId **   <a name="iotsitewise-Type-EnrichmentJobSummary-timeSeriesId"></a>
The system identifier of the time series being enriched. Present when the job was created using a timeSeriesId. Use this to identify which time series the job analyzes.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 73.
Required: No

 ** updatedAt **   <a name="iotsitewise-Type-EnrichmentJobSummary-updatedAt"></a>
Timestamp of the last job status change in ISO 8601 format. Use this to track recent activity and identify stale jobs. For active jobs, this shows the last time the job transitioned to a new status.
Type: Timestamp
Required: No

## See Also
<a name="API_EnrichmentJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/EnrichmentJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/EnrichmentJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/EnrichmentJobSummary)
