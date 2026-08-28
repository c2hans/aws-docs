---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationTask.html
---

# ReplicationTask
<a name="API_ReplicationTask"></a>

Provides information that describes a replication task created by the `CreateReplicationTask` operation.

## Contents
<a name="API_ReplicationTask_Contents"></a>

 ** CdcStartPosition **   <a name="DMS-Type-ReplicationTask-CdcStartPosition"></a>
Indicates when you want a change data capture (CDC) operation to start. Use either `CdcStartPosition` or `CdcStartTime` to specify when you want the CDC operation to start. Specifying both values results in an error.
The value can be in date, checkpoint, or LSN/SCN format.
Date Example: --cdc-start-position “2018-03-08T12:12:12”
Checkpoint Example: --cdc-start-position "checkpoint:V1\#27\#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876\#0\#0\#\*\#0\#93"
LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”
Type: String
Required: No

 ** CdcStopPosition **   <a name="DMS-Type-ReplicationTask-CdcStopPosition"></a>
Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.
Server time example: --cdc-stop-position “server\_time:2018-02-09T12:12:12”
Commit time example: --cdc-stop-position “commit\_time:2018-02-09T12:12:12“
Type: String
Required: No

 ** LastFailureMessage **   <a name="DMS-Type-ReplicationTask-LastFailureMessage"></a>
The last error (failure) message generated for the replication task.
Type: String
Required: No

 ** MigrationType **   <a name="DMS-Type-ReplicationTask-MigrationType"></a>
The type of migration.
Type: String
Valid Values: `full-load | cdc | full-load-and-cdc`
Required: No

 ** RecoveryCheckpoint **   <a name="DMS-Type-ReplicationTask-RecoveryCheckpoint"></a>
Indicates the last checkpoint that occurred during a change data capture (CDC) operation. You can provide this value to the `CdcStartPosition` parameter to start a CDC operation that begins at that checkpoint.
Type: String
Required: No

 ** ReplicationInstanceArn **   <a name="DMS-Type-ReplicationTask-ReplicationInstanceArn"></a>
The ARN of the replication instance.
Type: String
Required: No

 ** ReplicationTaskArn **   <a name="DMS-Type-ReplicationTask-ReplicationTaskArn"></a>
The Amazon Resource Name (ARN) of the replication task.
Type: String
Required: No

 ** ReplicationTaskCreationDate **   <a name="DMS-Type-ReplicationTask-ReplicationTaskCreationDate"></a>
The date the replication task was created.
Type: Timestamp
Required: No

 ** ReplicationTaskIdentifier **   <a name="DMS-Type-ReplicationTask-ReplicationTaskIdentifier"></a>
The user-assigned replication task identifier or name.
Constraints:
+ Must contain 1-255 alphanumeric characters or hyphens.
+ First character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
Type: String
Required: No

 ** ReplicationTaskSettings **   <a name="DMS-Type-ReplicationTask-ReplicationTaskSettings"></a>
The settings for the replication task.
Type: String
Required: No

 ** ReplicationTaskStartDate **   <a name="DMS-Type-ReplicationTask-ReplicationTaskStartDate"></a>
The date the replication task is scheduled to start.
Type: Timestamp
Required: No

 ** ReplicationTaskStats **   <a name="DMS-Type-ReplicationTask-ReplicationTaskStats"></a>
The statistics for the task, including elapsed time, tables loaded, and table errors.
Type: [ReplicationTaskStats](API_ReplicationTaskStats.md) object
Required: No

 ** SourceEndpointArn **   <a name="DMS-Type-ReplicationTask-SourceEndpointArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the endpoint.
Type: String
Required: No

 ** Status **   <a name="DMS-Type-ReplicationTask-Status"></a>
The status of the replication task. This response parameter can return one of the following values:
+  `"moving"` – The task is being moved in response to running the [`MoveReplicationTask`](https://docs.aws.amazon.com/dms/latest/APIReference/API_MoveReplicationTask.html) operation.
+  `"creating"` – The task is being created in response to running the [`CreateReplicationTask`](https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateReplicationTask.html) operation.
+  `"deleting"` – The task is being deleted in response to running the [`DeleteReplicationTask`](https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteReplicationTask.html) operation.
+  `"failed"` – The task failed to successfully complete the database migration in response to running the [`StartReplicationTask`](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html) operation.
+  `"failed-move"` – The task failed to move in response to running the [`MoveReplicationTask`](https://docs.aws.amazon.com/dms/latest/APIReference/API_MoveReplicationTask.html) operation.
+  `"modifying"` – The task definition is being modified in response to running the [`ModifyReplicationTask`](https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyReplicationTask.html) operation.
+  `"ready"` – The task is in a `ready` state where it can respond to other task operations, such as [`StartReplicationTask`](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html) or [`DeleteReplicationTask`](https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteReplicationTask.html).
+  `"running"` – The task is performing a database migration in response to running the [`StartReplicationTask`](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html) operation.
+  `"starting"` – The task is preparing to perform a database migration in response to running the [`StartReplicationTask`](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html) operation.
+  `"stopped"` – The task has stopped in response to running the [`StopReplicationTask`](https://docs.aws.amazon.com/dms/latest/APIReference/API_StopReplicationTask.html) operation.
+  `"stopping"` – The task is preparing to stop in response to running the [`StopReplicationTask`](https://docs.aws.amazon.com/dms/latest/APIReference/API_StopReplicationTask.html) operation.
+  `"testing"` – The database migration specified for this task is being tested in response to running either the [`StartReplicationTaskAssessmentRun`](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessmentRun.html) or the [`StartReplicationTaskAssessment`](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessment.html) operation.
**Note**
 [`StartReplicationTaskAssessmentRun`](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessmentRun.html) is an improved premigration task assessment operation. The [`StartReplicationTaskAssessment`](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessment.html) operation assesses data type compatibility only between the source and target database of a given migration task. In contrast, [`StartReplicationTaskAssessmentRun`](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessmentRun.html) enables you to specify a variety of premigration task assessments in addition to data type compatibility. These assessments include ones for the validity of primary key definitions and likely issues with database migration performance, among others.
Type: String
Required: No

 ** StopReason **   <a name="DMS-Type-ReplicationTask-StopReason"></a>
The reason the replication task was stopped. This response parameter can return one of the following values:
+  `"Stop Reason NORMAL"` – The task completed successfully with no additional information returned.
+  `"Stop Reason RECOVERABLE_ERROR"`
+  `"Stop Reason FATAL_ERROR"`
+  `"Stop Reason FULL_LOAD_ONLY_FINISHED"` – The task completed the full load phase. DMS applied cached changes if you set `StopTaskCachedChangesApplied` to `true`.
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

 ** TableMappings **   <a name="DMS-Type-ReplicationTask-TableMappings"></a>
Table mappings specified in the task.
Type: String
Required: No

 ** TargetEndpointArn **   <a name="DMS-Type-ReplicationTask-TargetEndpointArn"></a>
The ARN that uniquely identifies the endpoint.
Type: String
Required: No

 ** TargetReplicationInstanceArn **   <a name="DMS-Type-ReplicationTask-TargetReplicationInstanceArn"></a>
The ARN of the replication instance to which this task is moved in response to running the [`MoveReplicationTask`](https://docs.aws.amazon.com/dms/latest/APIReference/API_MoveReplicationTask.html) operation. Otherwise, this response parameter isn't a member of the `ReplicationTask` object.
Type: String
Required: No

 ** TaskData **   <a name="DMS-Type-ReplicationTask-TaskData"></a>
Supplemental information that the task requires to migrate the data for certain source and target endpoints. For more information, see [Specifying Supplemental Data for Task Settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.TaskData.html) in the * AWS Database Migration Service User Guide.*
Type: String
Required: No

## See Also
<a name="API_ReplicationTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ReplicationTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ReplicationTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ReplicationTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
