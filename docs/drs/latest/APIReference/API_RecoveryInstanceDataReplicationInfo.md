---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryInstanceDataReplicationInfo.html
---

# RecoveryInstanceDataReplicationInfo
<a name="API_RecoveryInstanceDataReplicationInfo"></a>

Information about Data Replication

## Contents
<a name="API_RecoveryInstanceDataReplicationInfo_Contents"></a>

 ** dataReplicationError **   <a name="drs-Type-RecoveryInstanceDataReplicationInfo-dataReplicationError"></a>
Information about Data Replication
Type: [RecoveryInstanceDataReplicationError](API_RecoveryInstanceDataReplicationError.md) object
Required: No

 ** dataReplicationInitiation **   <a name="drs-Type-RecoveryInstanceDataReplicationInfo-dataReplicationInitiation"></a>
Information about whether the data replication has been initiated.
Type: [RecoveryInstanceDataReplicationInitiation](API_RecoveryInstanceDataReplicationInitiation.md) object
Required: No

 ** dataReplicationState **   <a name="drs-Type-RecoveryInstanceDataReplicationInfo-dataReplicationState"></a>
The state of the data replication.
Type: String
Valid Values: `STOPPED | INITIATING | INITIAL_SYNC | BACKLOG | CREATING_SNAPSHOT | CONTINUOUS | PAUSED | RESCAN | STALLED | DISCONNECTED | REPLICATION_STATE_NOT_AVAILABLE | NOT_STARTED`
Required: No

 ** etaDateTime **   <a name="drs-Type-RecoveryInstanceDataReplicationInfo-etaDateTime"></a>
An estimate of when the data replication will be completed.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** lagDuration **   <a name="drs-Type-RecoveryInstanceDataReplicationInfo-lagDuration"></a>
Data replication lag duration.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** replicatedDisks **   <a name="drs-Type-RecoveryInstanceDataReplicationInfo-replicatedDisks"></a>
The disks that should be replicated.
Type: Array of [RecoveryInstanceDataReplicationInfoReplicatedDisk](API_RecoveryInstanceDataReplicationInfoReplicatedDisk.md) objects
Array Members: Minimum number of 0 items. Maximum number of 60 items.
Required: No

 ** stagingAvailabilityZone **   <a name="drs-Type-RecoveryInstanceDataReplicationInfo-stagingAvailabilityZone"></a>
AWS Availability zone into which data is being replicated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `(us(-gov)?|ap|ca|cn|eu|eusc|sa|af|me|mx|il)-([a-z]{2}-)?(central|north|(north(?:east|west))|south|south(?:east|west)|east|west)-[0-9][a-z]`
Required: No

 ** stagingOutpostArn **   <a name="drs-Type-RecoveryInstanceDataReplicationInfo-stagingOutpostArn"></a>
The ARN of the staging Outpost
Type: String
Length Constraints: Minimum length of 20. Maximum length of 255.
Pattern: `arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/op-[a-f0-9]{17}`
Required: No

## See Also
<a name="API_RecoveryInstanceDataReplicationInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/RecoveryInstanceDataReplicationInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/RecoveryInstanceDataReplicationInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/RecoveryInstanceDataReplicationInfo)
