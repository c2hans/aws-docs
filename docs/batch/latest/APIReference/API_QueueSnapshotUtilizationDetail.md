---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_QueueSnapshotUtilizationDetail.html
---

# QueueSnapshotUtilizationDetail
<a name="API_QueueSnapshotUtilizationDetail"></a>

The job queue utilization at a specific point in time, including total capacity usage, and quota share or fairshare utilization breakdown depending on the job queue scheduling policy.

## Contents
<a name="API_QueueSnapshotUtilizationDetail_Contents"></a>

 ** fairshareUtilization **   <a name="Batch-Type-QueueSnapshotUtilizationDetail-fairshareUtilization"></a>
The utilization information for a fairshare scheduling job queues, including active share count and top capacity utilization by share.
Type: [FairshareUtilizationDetail](API_FairshareUtilizationDetail.md) object
Required: No

 ** lastUpdatedAt **   <a name="Batch-Type-QueueSnapshotUtilizationDetail-lastUpdatedAt"></a>
The Unix timestamp (in milliseconds) for when the queue utilization information was last updated.
Type: Long
Required: No

 ** quotaShareUtilization **   <a name="Batch-Type-QueueSnapshotUtilizationDetail-quotaShareUtilization"></a>
The utilization information for a job queue with a quota share scheduling policy.
Type: [QuotaShareUtilizationDetail](API_QuotaShareUtilizationDetail.md) object
Required: No

 ** totalCapacityUsage **   <a name="Batch-Type-QueueSnapshotUtilizationDetail-totalCapacityUsage"></a>
The total capacity usage for the entire job queue.
Type: Array of [QueueSnapshotCapacityUsage](API_QueueSnapshotCapacityUsage.md) objects
Required: No

## See Also
<a name="API_QueueSnapshotUtilizationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/QueueSnapshotUtilizationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/QueueSnapshotUtilizationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/QueueSnapshotUtilizationDetail)
