---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_SourceServer.html
---

# SourceServer
<a name="API_SourceServer"></a>

## Contents
<a name="API_SourceServer_Contents"></a>

 ** agentVersion **   <a name="drs-Type-SourceServer-agentVersion"></a>
The version of the DRS agent installed on the source server
Type: String
Pattern: `[0-9]{1,5}.[0-9]{1,5}.[0-9]{1,5}(.[0-9]{4}.[0-9]{3}.[0-9]{4})?`
Required: No

 ** arn **   <a name="drs-Type-SourceServer-arn"></a>
The ARN of the Source Server.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.{16,2044}`
Required: No

 ** dataReplicationInfo **   <a name="drs-Type-SourceServer-dataReplicationInfo"></a>
The Data Replication Info of the Source Server.
Type: [DataReplicationInfo](API_DataReplicationInfo.md) object
Required: No

 ** lastLaunchResult **   <a name="drs-Type-SourceServer-lastLaunchResult"></a>
The status of the last recovery launch of this Source Server.
Type: String
Valid Values: `NOT_STARTED | PENDING | SUCCEEDED | FAILED`
Required: No

 ** lifeCycle **   <a name="drs-Type-SourceServer-lifeCycle"></a>
The lifecycle information of this Source Server.
Type: [LifeCycle](API_LifeCycle.md) object
Required: No

 ** recoveryInstanceId **   <a name="drs-Type-SourceServer-recoveryInstanceId"></a>
The ID of the Recovery Instance associated with this Source Server.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 19.
Pattern: `i-[0-9a-fA-F]{8,}`
Required: No

 ** replicationDirection **   <a name="drs-Type-SourceServer-replicationDirection"></a>
Replication direction of the Source Server.
Type: String
Valid Values: `FAILOVER | FAILBACK`
Required: No

 ** reversedDirectionSourceServerArn **   <a name="drs-Type-SourceServer-reversedDirectionSourceServerArn"></a>
For EC2-originated Source Servers which have been failed over and then failed back, this value will mean the ARN of the Source Server on the opposite replication direction.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:[0-9a-zA-Z_-]+:){3}([0-9]{12,}):source-server/(s-[0-9a-zA-Z]{17})`
Required: No

 ** sourceCloudProperties **   <a name="drs-Type-SourceServer-sourceCloudProperties"></a>
Source cloud properties of the Source Server.
Type: [SourceCloudProperties](API_SourceCloudProperties.md) object
Required: No

 ** sourceNetworkID **   <a name="drs-Type-SourceServer-sourceNetworkID"></a>
ID of the Source Network which is protecting this Source Server's network.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `sn-[0-9a-zA-Z]{17}`
Required: No

 ** sourceProperties **   <a name="drs-Type-SourceServer-sourceProperties"></a>
The source properties of the Source Server.
Type: [SourceProperties](API_SourceProperties.md) object
Required: No

 ** sourceServerID **   <a name="drs-Type-SourceServer-sourceServerID"></a>
The ID of the Source Server.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: No

 ** stagingArea **   <a name="drs-Type-SourceServer-stagingArea"></a>
The staging area of the source server.
Type: [StagingArea](API_StagingArea.md) object
Required: No

 ** tags **   <a name="drs-Type-SourceServer-tags"></a>
The tags associated with the Source Server.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_SourceServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/SourceServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/SourceServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/SourceServer)
