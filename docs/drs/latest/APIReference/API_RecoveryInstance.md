---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryInstance.html
---

# RecoveryInstance
<a name="API_RecoveryInstance"></a>

A Recovery Instance is a replica of a Source Server running on EC2.

## Contents
<a name="API_RecoveryInstance_Contents"></a>

 ** agentVersion **   <a name="drs-Type-RecoveryInstance-agentVersion"></a>
The version of the DRS agent installed on the recovery instance
Type: String
Pattern: `[0-9]{1,5}.[0-9]{1,5}.[0-9]{1,5}(.[0-9]{4}.[0-9]{3}.[0-9]{4})?`
Required: No

 ** arn **   <a name="drs-Type-RecoveryInstance-arn"></a>
The ARN of the Recovery Instance.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.{16,2044}`
Required: No

 ** dataReplicationInfo **   <a name="drs-Type-RecoveryInstance-dataReplicationInfo"></a>
The Data Replication Info of the Recovery Instance.
Type: [RecoveryInstanceDataReplicationInfo](API_RecoveryInstanceDataReplicationInfo.md) object
Required: No

 ** ec2InstanceID **   <a name="drs-Type-RecoveryInstance-ec2InstanceID"></a>
The EC2 instance ID of the Recovery Instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `i-[0-9a-fA-F]{8,}`
Required: No

 ** ec2InstanceState **   <a name="drs-Type-RecoveryInstance-ec2InstanceState"></a>
The state of the EC2 instance for this Recovery Instance.
Type: String
Valid Values: `PENDING | RUNNING | STOPPING | STOPPED | SHUTTING-DOWN | TERMINATED | NOT_FOUND`
Required: No

 ** failback **   <a name="drs-Type-RecoveryInstance-failback"></a>
An object representing failback related information of the Recovery Instance.
Type: [RecoveryInstanceFailback](API_RecoveryInstanceFailback.md) object
Required: No

 ** isDrill **   <a name="drs-Type-RecoveryInstance-isDrill"></a>
Whether this Recovery Instance was created for a drill or for an actual Recovery event.
Type: Boolean
Required: No

 ** jobID **   <a name="drs-Type-RecoveryInstance-jobID"></a>
The ID of the Job that created the Recovery Instance.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `drsjob-[0-9a-zA-Z]{17}`
Required: No

 ** originAvailabilityZone **   <a name="drs-Type-RecoveryInstance-originAvailabilityZone"></a>
AWS availability zone associated with the recovery instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `(us(-gov)?|ap|ca|cn|eu|eusc|sa|af|me|mx|il)-([a-z]{2}-)?(central|north|(north(?:east|west))|south|south(?:east|west)|east|west)-[0-9][a-z]`
Required: No

 ** originEnvironment **   <a name="drs-Type-RecoveryInstance-originEnvironment"></a>
Environment (On Premises / AWS) of the instance that the recovery instance originated from.
Type: String
Valid Values: `ON_PREMISES | AWS`
Required: No

 ** pointInTimeSnapshotDateTime **   <a name="drs-Type-RecoveryInstance-pointInTimeSnapshotDateTime"></a>
The date and time of the Point in Time (PIT) snapshot that this Recovery Instance was launched from.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** recoveryInstanceID **   <a name="drs-Type-RecoveryInstance-recoveryInstanceID"></a>
The ID of the Recovery Instance.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 19.
Pattern: `i-[0-9a-fA-F]{8,}`
Required: No

 ** recoveryInstanceProperties **   <a name="drs-Type-RecoveryInstance-recoveryInstanceProperties"></a>
Properties of the Recovery Instance machine.
Type: [RecoveryInstanceProperties](API_RecoveryInstanceProperties.md) object
Required: No

 ** sourceOutpostArn **   <a name="drs-Type-RecoveryInstance-sourceOutpostArn"></a>
The ARN of the source Outpost
Type: String
Length Constraints: Minimum length of 20. Maximum length of 255.
Pattern: `arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/op-[a-f0-9]{17}`
Required: No

 ** sourceServerID **   <a name="drs-Type-RecoveryInstance-sourceServerID"></a>
The Source Server ID that this Recovery Instance is associated with.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: No

 ** tags **   <a name="drs-Type-RecoveryInstance-tags"></a>
An array of tags that are associated with the Recovery Instance.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_RecoveryInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/RecoveryInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/RecoveryInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/RecoveryInstance)
