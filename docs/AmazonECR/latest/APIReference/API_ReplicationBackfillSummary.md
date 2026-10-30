---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ReplicationBackfillSummary.html
---

# ReplicationBackfillSummary
<a name="API_ReplicationBackfillSummary"></a>

An object representing a summary of a replication backfill, including its status, destination, progress, and start and end times.

## Contents
<a name="API_ReplicationBackfillSummary_Contents"></a>

 ** destination **   <a name="ECR-Type-ReplicationBackfillSummary-destination"></a>
The destination Region and registry to which the images are replicated.
Type: [ReplicationDestination](API_ReplicationDestination.md) object
Required: Yes

 ** replicationBackfillId **   <a name="ECR-Type-ReplicationBackfillSummary-replicationBackfillId"></a>
The ID of the replication backfill.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** startedAt **   <a name="ECR-Type-ReplicationBackfillSummary-startedAt"></a>
The date and time, in JavaScript date format, when the replication backfill was started.
Type: Timestamp
Required: Yes

 ** status **   <a name="ECR-Type-ReplicationBackfillSummary-status"></a>
The current status of the replication backfill.
Type: String
Valid Values: `PREPARING | IN_PROGRESS | COMPLETE | FAILED | STOPPING | STOPPED`
Required: Yes

 ** endedAt **   <a name="ECR-Type-ReplicationBackfillSummary-endedAt"></a>
The date and time, in JavaScript date format, when the replication backfill ended. This value is `null` while the replication backfill is still in progress.
Type: Timestamp
Required: No

 ** failureCode **   <a name="ECR-Type-ReplicationBackfillSummary-failureCode"></a>
The failure code for a replication backfill that has failed.
Type: String
Required: No

 ** progress **   <a name="ECR-Type-ReplicationBackfillSummary-progress"></a>
The progress of the replication backfill, including the total, completed, and failed replication counts. This value is `null` until the replication backfill finishes preparing the set of images to replicate. It is therefore `null` while the replication backfill is `PREPARING`, and remains `null` if the replication backfill is stopped before preparation completes.
Type: [ReplicationBackfillProgress](API_ReplicationBackfillProgress.md) object
Required: No

## See Also
<a name="API_ReplicationBackfillSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/ReplicationBackfillSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/ReplicationBackfillSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/ReplicationBackfillSummary)
