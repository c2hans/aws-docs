---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ReplicationBackfillProgress.html
---

# ReplicationBackfillProgress
<a name="API_ReplicationBackfillProgress"></a>

An object representing the progress of a replication backfill, including the total, completed, and failed replication counts.

## Contents
<a name="API_ReplicationBackfillProgress_Contents"></a>

 ** completedReplicationCount **   <a name="ECR-Type-ReplicationBackfillProgress-completedReplicationCount"></a>
The number of replications that have completed successfully.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** failedReplicationCount **   <a name="ECR-Type-ReplicationBackfillProgress-failedReplicationCount"></a>
The number of replications that have failed.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** failureCodes **   <a name="ECR-Type-ReplicationBackfillProgress-failureCodes"></a>
The distinct failure codes for the replications that have failed. Each failure code appears at most once, regardless of how many replications failed with that code.
Type: Array of strings
Required: Yes

 ** totalReplicationCount **   <a name="ECR-Type-ReplicationBackfillProgress-totalReplicationCount"></a>
The total number of replications that the backfill will perform. Each image and tag combination is counted as a single replication.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

## See Also
<a name="API_ReplicationBackfillProgress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/ReplicationBackfillProgress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/ReplicationBackfillProgress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/ReplicationBackfillProgress)
