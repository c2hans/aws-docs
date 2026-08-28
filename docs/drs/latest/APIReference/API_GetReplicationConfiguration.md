---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_GetReplicationConfiguration.html
---

# GetReplicationConfiguration
<a name="API_GetReplicationConfiguration"></a>

Gets a ReplicationConfiguration, filtered by Source Server ID.

## Request Syntax
<a name="API_GetReplicationConfiguration_RequestSyntax"></a>

```
POST /GetReplicationConfiguration HTTP/1.1
Content-type: application/json

{
   "sourceServerID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetReplicationConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetReplicationConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [sourceServerID](#API_GetReplicationConfiguration_RequestSyntax) **   <a name="drs-GetReplicationConfiguration-request-sourceServerID"></a>
The ID of the Source Serve for this Replication Configuration.r
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: Yes

## Response Syntax
<a name="API_GetReplicationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "associateDefaultSecurityGroup": boolean,
   "autoReplicateNewDisks": boolean,
   "bandwidthThrottling": number,
   "createPublicIP": boolean,
   "dataPlaneRouting": "string",
   "defaultLargeStagingDiskType": "string",
   "ebsEncryption": "string",
   "ebsEncryptionKeyArn": "string",
   "internetProtocol": "string",
   "name": "string",
   "pitPolicy": [
      {
         "enabled": boolean,
         "interval": number,
         "retentionDuration": number,
         "ruleID": number,
         "units": "string"
      }
   ],
   "replicatedDisks": [
      {
         "deviceName": "string",
         "iops": number,
         "isBootDisk": boolean,
         "optimizedStagingDiskType": "string",
         "stagingDiskType": "string",
         "throughput": number
      }
   ],
   "replicationServerInstanceType": "string",
   "replicationServersSecurityGroupsIDs": [ "string" ],
   "sourceServerID": "string",
   "stagingAreaSubnetId": "string",
   "stagingAreaTags": {
      "string" : "string"
   },
   "useDedicatedReplicationServer": boolean
}
```

## Response Elements
<a name="API_GetReplicationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [associateDefaultSecurityGroup](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="drs-GetReplicationConfiguration-response-associateDefaultSecurityGroup"></a>
Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration.
Type: Boolean

 ** [autoReplicateNewDisks](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="drs-GetReplicationConfiguration-response-autoReplicateNewDisks"></a>
Whether to allow the AWS replication agent to automatically replicate newly added disks.
Type: Boolean

 ** [bandwidthThrottling](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="drs-GetReplicationConfiguration-response-bandwidthThrottling"></a>
Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.
Type: Long
Valid Range: Minimum value of 0.

 ** [createPublicIP](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="drs-GetReplicationConfiguration-response-createPublicIP"></a>
Whether to create a Public IP for the Recovery Instance by default.
Type: Boolean

 ** [dataPlaneRouting](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="drs-GetReplicationConfiguration-response-dataPlaneRouting"></a>
The data plane routing mechanism that will be used for replication.
Type: String
Valid Values: `PRIVATE_IP | PUBLIC_IP`

 ** [defaultLargeStagingDiskType](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="drs-GetReplicationConfiguration-response-defaultLargeStagingDiskType"></a>
The Staging Disk EBS volume type to be used during replication.
Type: String
Valid Values: `GP2 | GP3 | ST1 | AUTO`

 ** [ebsEncryption](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="drs-GetReplicationConfiguration-response-ebsEncryption"></a>
The type of EBS encryption to be used during replication.
Type: String
Valid Values: `DEFAULT | CUSTOM | NONE`

 ** [ebsEncryptionKeyArn](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="drs-GetReplicationConfiguration-response-ebsEncryptionKeyArn"></a>
The ARN of the EBS encryption key to be used during replication.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.{16,2044}`

 ** [internetProtocol](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="drs-GetReplicationConfiguration-response-internetProtocol"></a>
Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)
Type: String
Valid Values: `IPV4 | IPV6`

 ** [name](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="drs-GetReplicationConfiguration-response-name"></a>
The name of the Replication Configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.

 ** [pitPolicy](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="drs-GetReplicationConfiguration-response-pitPolicy"></a>
The Point in time (PIT) policy to manage snapshots taken during replication.
Type: Array of [PITPolicyRule](API_PITPolicyRule.md) objects
Array Members: Fixed number of 3 items.

 ** [replicatedDisks](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="drs-GetReplicationConfiguration-response-replicatedDisks"></a>
The configuration of the disks of the Source Server to be replicated.
Type: Array of [ReplicationConfigurationReplicatedDisk](API_ReplicationConfigurationReplicatedDisk.md) objects
Array Members: Minimum number of 0 items. Maximum number of 60 items.

 ** [replicationServerInstanceType](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="drs-GetReplicationConfiguration-response-replicationServerInstanceType"></a>
The instance type to be used for the replication server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [replicationServersSecurityGroupsIDs](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="drs-GetReplicationConfiguration-response-replicationServersSecurityGroupsIDs"></a>
The security group IDs that will be used by the replication server.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `sg-[0-9a-fA-F]{8,}`

 ** [sourceServerID](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="drs-GetReplicationConfiguration-response-sourceServerID"></a>
The ID of the Source Server for this Replication Configuration.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`

 ** [stagingAreaSubnetId](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="drs-GetReplicationConfiguration-response-stagingAreaSubnetId"></a>
The subnet to be used by the replication staging area.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `subnet-[0-9a-fA-F]{8,}`

 ** [stagingAreaTags](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="drs-GetReplicationConfiguration-response-stagingAreaTags"></a>
A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [useDedicatedReplicationServer](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="drs-GetReplicationConfiguration-response-useDedicatedReplicationServer"></a>
Whether to use a dedicated Replication Server in the replication staging area.
Type: Boolean

## Errors
<a name="API_GetReplicationConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource for this operation was not found.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
Quota code.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
 ** serviceCode **
Service code.
HTTP Status Code: 429

 ** UninitializedAccountException **
The account performing the request has not been initialized.
HTTP Status Code: 400

## See Also
<a name="API_GetReplicationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/GetReplicationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/GetReplicationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/GetReplicationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/GetReplicationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/GetReplicationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/GetReplicationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/GetReplicationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/GetReplicationConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/GetReplicationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/GetReplicationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
