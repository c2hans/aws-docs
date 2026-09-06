---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_DataReplicationInfo.html
---

# DataReplicationInfo
<a name="API_DataReplicationInfo"></a>

Information about Data Replication

## Contents
<a name="API_DataReplicationInfo_Contents"></a>

 ** dataReplicationError **   <a name="drs-Type-DataReplicationInfo-dataReplicationError"></a>
Error in data replication.
Type: [DataReplicationError](API_DataReplicationError.md) object
Required: No

 ** dataReplicationInitiation **   <a name="drs-Type-DataReplicationInfo-dataReplicationInitiation"></a>
Information about whether the data replication has been initiated.
Type: [DataReplicationInitiation](API_DataReplicationInitiation.md) object
Required: No

 ** dataReplicationState **   <a name="drs-Type-DataReplicationInfo-dataReplicationState"></a>
The state of the data replication.
Type: String
Valid Values: `STOPPED | INITIATING | INITIAL_SYNC | BACKLOG | CREATING_SNAPSHOT | CONTINUOUS | PAUSED | RESCAN | STALLED | DISCONNECTED`
Required: No

 ** etaDateTime **   <a name="drs-Type-DataReplicationInfo-etaDateTime"></a>
An estimate of when the data replication will be completed.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** lagDuration **   <a name="drs-Type-DataReplicationInfo-lagDuration"></a>
Data replication lag duration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** replicatedDisks **   <a name="drs-Type-DataReplicationInfo-replicatedDisks"></a>
The disks that should be replicated.
Type: Array of [DataReplicationInfoReplicatedDisk](API_DataReplicationInfoReplicatedDisk.md) objects
Array Members: Minimum number of 0 items. Maximum number of 60 items.
Required: No

 ** stagingAvailabilityZone **   <a name="drs-Type-DataReplicationInfo-stagingAvailabilityZone"></a>
AWS Availability zone into which data is being replicated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `(us(-gov)?|ap|ca|cn|eu|eusc|sa|af|me|mx|il)-([a-z]{2}-)?(central|north|(north(?:east|west))|south|south(?:east|west)|east|west)-[0-9][a-z]`
Required: No

 ** stagingOutpostArn **   <a name="drs-Type-DataReplicationInfo-stagingOutpostArn"></a>
The ARN of the staging Outpost
Type: String
Length Constraints: Minimum length of 20. Maximum length of 255.
Pattern: `arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/op-[a-f0-9]{17}`
Required: No

## See Also
<a name="API_DataReplicationInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/DataReplicationInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/DataReplicationInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/DataReplicationInfo)
