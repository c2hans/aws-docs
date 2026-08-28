---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_DataReplicationInfo.html
---

# DataReplicationInfo
<a name="API_DataReplicationInfo"></a>

Request data replication info.

## Contents
<a name="API_DataReplicationInfo_Contents"></a>

 ** dataReplicationError **   <a name="mgn-Type-DataReplicationInfo-dataReplicationError"></a>
Error in obtaining data replication info.
Type: [DataReplicationError](API_DataReplicationError.md) object
Required: No

 ** dataReplicationInitiation **   <a name="mgn-Type-DataReplicationInfo-dataReplicationInitiation"></a>
Request to query whether data replication has been initiated.
Type: [DataReplicationInitiation](API_DataReplicationInitiation.md) object
Required: No

 ** dataReplicationState **   <a name="mgn-Type-DataReplicationInfo-dataReplicationState"></a>
Request to query the data replication state.
Type: String
Valid Values: `STOPPED | INITIATING | INITIAL_SYNC | BACKLOG | CREATING_SNAPSHOT | CONTINUOUS | PAUSED | RESCAN | STALLED | DISCONNECTED | PENDING_SNAPSHOT_SHIPPING | SHIPPING_SNAPSHOT`
Required: No

 ** etaDateTime **   <a name="mgn-Type-DataReplicationInfo-etaDateTime"></a>
Request to query the time when data replication will be complete.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** lagDuration **   <a name="mgn-Type-DataReplicationInfo-lagDuration"></a>
Request to query data replication lag duration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** lastSnapshotDateTime **   <a name="mgn-Type-DataReplicationInfo-lastSnapshotDateTime"></a>
Request to query data replication last snapshot time.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** replicatedDisks **   <a name="mgn-Type-DataReplicationInfo-replicatedDisks"></a>
Request to query disks replicated.
Type: Array of [DataReplicationInfoReplicatedDisk](API_DataReplicationInfoReplicatedDisk.md) objects
Array Members: Minimum number of 0 items. Maximum number of 60 items.
Required: No

 ** replicatorId **   <a name="mgn-Type-DataReplicationInfo-replicatorId"></a>
Replication server instance ID.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `i-[0-9a-zA-Z]{17}`
Required: No

## See Also
<a name="API_DataReplicationInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/DataReplicationInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/DataReplicationInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/DataReplicationInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
