---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationTaskStats.html
---

# ReplicationTaskStats
<a name="API_ReplicationTaskStats"></a>

In response to a request by the `DescribeReplicationTasks` operation, this object provides a collection of statistics about a replication task.

## Contents
<a name="API_ReplicationTaskStats_Contents"></a>

 ** ElapsedTimeMillis **   <a name="DMS-Type-ReplicationTaskStats-ElapsedTimeMillis"></a>
The elapsed time of the task, in milliseconds.
Type: Long
Required: No

 ** FreshStartDate **   <a name="DMS-Type-ReplicationTaskStats-FreshStartDate"></a>
The date the replication task was started either with a fresh start or a target reload.
Type: Timestamp
Required: No

 ** FullLoadFinishDate **   <a name="DMS-Type-ReplicationTaskStats-FullLoadFinishDate"></a>
The date the replication task full load was completed.
Type: Timestamp
Required: No

 ** FullLoadProgressPercent **   <a name="DMS-Type-ReplicationTaskStats-FullLoadProgressPercent"></a>
The percent complete for the full load migration task.
Type: Integer
Required: No

 ** FullLoadStartDate **   <a name="DMS-Type-ReplicationTaskStats-FullLoadStartDate"></a>
The date the replication task full load was started.
Type: Timestamp
Required: No

 ** StartDate **   <a name="DMS-Type-ReplicationTaskStats-StartDate"></a>
The date the replication task was started either with a fresh start or a resume. For more information, see [StartReplicationTaskType](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html#DMS-StartReplicationTask-request-StartReplicationTaskType).
Type: Timestamp
Required: No

 ** StopDate **   <a name="DMS-Type-ReplicationTaskStats-StopDate"></a>
The date the replication task was stopped.
Type: Timestamp
Required: No

 ** TablesErrored **   <a name="DMS-Type-ReplicationTaskStats-TablesErrored"></a>
The number of errors that have occurred during this task.
Type: Integer
Required: No

 ** TablesLoaded **   <a name="DMS-Type-ReplicationTaskStats-TablesLoaded"></a>
The number of tables loaded for this task.
Type: Integer
Required: No

 ** TablesLoading **   <a name="DMS-Type-ReplicationTaskStats-TablesLoading"></a>
The number of tables currently loading for this task.
Type: Integer
Required: No

 ** TablesQueued **   <a name="DMS-Type-ReplicationTaskStats-TablesQueued"></a>
The number of tables queued for this task.
Type: Integer
Required: No

## See Also
<a name="API_ReplicationTaskStats_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ReplicationTaskStats)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ReplicationTaskStats)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ReplicationTaskStats)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
