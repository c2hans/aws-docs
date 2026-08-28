---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_Replication.html
---

# Replication
<a name="API_Replication"></a>

Provides information that describes a serverless replication created by the `CreateReplication` operation.

## Contents
<a name="API_Replication_Contents"></a>

 ** CdcStartPosition **   <a name="DMS-Type-Replication-CdcStartPosition"></a>
Indicates the start time for a change data capture (CDC) operation. Use either `CdcStartTime` or `CdcStartPosition` to specify when you want a CDC operation to start. Specifying both values results in an error.
Type: String
Required: No

 ** CdcStartTime **   <a name="DMS-Type-Replication-CdcStartTime"></a>
Indicates the start time for a change data capture (CDC) operation. Use either `CdcStartTime` or `CdcStartPosition` to specify when you want a CDC operation to start. Specifying both values results in an error.
Type: Timestamp
Required: No

 ** CdcStopPosition **   <a name="DMS-Type-Replication-CdcStopPosition"></a>
Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.
Type: String
Required: No

 ** FailureMessages **   <a name="DMS-Type-Replication-FailureMessages"></a>
Error and other information about why a serverless replication failed.
Type: Array of strings
Required: No

 ** IsReadOnly **   <a name="DMS-Type-Replication-IsReadOnly"></a>
Indicates whether the serverless replication is read-only. When set to `true`, this replication is managed by AWS DMS as part of a zero-ETL integration and cannot be modified or deleted directly. You can only modify or delete read-only replications through their associated zero-ETL integration.
Type: Boolean
Required: No

 ** PremigrationAssessmentStatuses **   <a name="DMS-Type-Replication-PremigrationAssessmentStatuses"></a>
The status output of premigration assessment in describe-replications.
Type: Array of [PremigrationAssessmentStatus](API_PremigrationAssessmentStatus.md) objects
Required: No

 ** ProvisionData **   <a name="DMS-Type-Replication-ProvisionData"></a>
Information about provisioning resources for an AWS DMS serverless replication.
Type: [ProvisionData](API_ProvisionData.md) object
Required: No

 ** RecoveryCheckpoint **   <a name="DMS-Type-Replication-RecoveryCheckpoint"></a>
Indicates the last checkpoint that occurred during a change data capture (CDC) operation. You can provide this value to the `CdcStartPosition` parameter to start a CDC operation that begins at that checkpoint.
Type: String
Required: No

 ** ReplicationConfigArn **   <a name="DMS-Type-Replication-ReplicationConfigArn"></a>
The Amazon Resource Name for the `ReplicationConfig` associated with the replication.
Type: String
Required: No

 ** ReplicationConfigIdentifier **   <a name="DMS-Type-Replication-ReplicationConfigIdentifier"></a>
The identifier for the `ReplicationConfig` associated with the replication.
Type: String
Required: No

 ** ReplicationCreateTime **   <a name="DMS-Type-Replication-ReplicationCreateTime"></a>
The time the serverless replication was created.
Type: Timestamp
Required: No

 ** ReplicationDeprovisionTime **   <a name="DMS-Type-Replication-ReplicationDeprovisionTime"></a>
The timestamp when DMS will deprovision the replication.
Type: Timestamp
Required: No

 ** ReplicationLastStopTime **   <a name="DMS-Type-Replication-ReplicationLastStopTime"></a>
The timestamp when replication was last stopped.
Type: Timestamp
Required: No

 ** ReplicationStats **   <a name="DMS-Type-Replication-ReplicationStats"></a>
This object provides a collection of statistics about a serverless replication.
Type: [ReplicationStats](API_ReplicationStats.md) object
Required: No

 ** ReplicationType **   <a name="DMS-Type-Replication-ReplicationType"></a>
The type of the serverless replication.
Type: String
Valid Values: `full-load | cdc | full-load-and-cdc`
Required: No

 ** ReplicationUpdateTime **   <a name="DMS-Type-Replication-ReplicationUpdateTime"></a>
The time the serverless replication was updated.
Type: Timestamp
Required: No

 ** SourceEndpointArn **   <a name="DMS-Type-Replication-SourceEndpointArn"></a>
The Amazon Resource Name for an existing `Endpoint` the serverless replication uses for its data source.
Type: String
Required: No

 ** StartReplicationType **   <a name="DMS-Type-Replication-StartReplicationType"></a>
The type of replication to start.
Type: String
Required: No

 ** Status **   <a name="DMS-Type-Replication-Status"></a>
The current status of the serverless replication.
Type: String
Required: No

 ** StopReason **   <a name="DMS-Type-Replication-StopReason"></a>
The reason the replication task was stopped. This response parameter can return one of the following values:
+  `"Stop Reason NORMAL"`
+  `"Stop Reason RECOVERABLE_ERROR"`
+  `"Stop Reason FATAL_ERROR"`
+  `"Stop Reason FULL_LOAD_ONLY_FINISHED"`
+  `"Stop Reason STOPPED_AFTER_FULL_LOAD"` – Full load completed, with cached changes not applied
+  `"Stop Reason STOPPED_AFTER_CACHED_EVENTS"` – Full load completed, with cached changes applied
+  `"Stop Reason EXPRESS_LICENSE_LIMITS_REACHED"`
+  `"Stop Reason STOPPED_AFTER_DDL_APPLY"` – User-defined stop task after DDL applied
+  `"Stop Reason STOPPED_DUE_TO_LOW_MEMORY"`
+  `"Stop Reason STOPPED_DUE_TO_LOW_DISK"`
+  `"Stop Reason STOPPED_AT_SERVER_TIME"` – User-defined server time for stopping task
+  `"Stop Reason STOPPED_AT_COMMIT_TIME"` – User-defined commit time for stopping task
+  `"Stop Reason RECONFIGURATION_RESTART"`
+  `"Stop Reason RECYCLE_TASK"`
Type: String
Required: No

 ** TargetEndpointArn **   <a name="DMS-Type-Replication-TargetEndpointArn"></a>
The Amazon Resource Name for an existing `Endpoint` the serverless replication uses for its data target.
Type: String
Required: No

## See Also
<a name="API_Replication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/Replication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/Replication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/Replication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
