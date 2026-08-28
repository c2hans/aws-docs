---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_UpdateReplicationConfigurationTemplate.html
---

# UpdateReplicationConfigurationTemplate
<a name="API_UpdateReplicationConfigurationTemplate"></a>

Updates a ReplicationConfigurationTemplate by ID.

## Request Syntax
<a name="API_UpdateReplicationConfigurationTemplate_RequestSyntax"></a>

```
POST /UpdateReplicationConfigurationTemplate HTTP/1.1
Content-type: application/json

{
   "arn": "{{string}}",
   "associateDefaultSecurityGroup": {{boolean}},
   "autoReplicateNewDisks": {{boolean}},
   "bandwidthThrottling": {{number}},
   "createPublicIP": {{boolean}},
   "dataPlaneRouting": "{{string}}",
   "defaultLargeStagingDiskType": "{{string}}",
   "ebsEncryption": "{{string}}",
   "ebsEncryptionKeyArn": "{{string}}",
   "internetProtocol": "{{string}}",
   "pitPolicy": [
      {
         "enabled": {{boolean}},
         "interval": {{number}},
         "retentionDuration": {{number}},
         "ruleID": {{number}},
         "units": "{{string}}"
      }
   ],
   "replicationConfigurationTemplateID": "{{string}}",
   "replicationServerInstanceType": "{{string}}",
   "replicationServersSecurityGroupsIDs": [ "{{string}}" ],
   "stagingAreaSubnetId": "{{string}}",
   "stagingAreaTags": {
      "{{string}}" : "{{string}}"
   },
   "useDedicatedReplicationServer": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UpdateReplicationConfigurationTemplate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateReplicationConfigurationTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arn](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-request-arn"></a>
The Replication Configuration Template ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.{16,2044}`
Required: No

 ** [associateDefaultSecurityGroup](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-request-associateDefaultSecurityGroup"></a>
Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration Template.
Type: Boolean
Required: No

 ** [autoReplicateNewDisks](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-request-autoReplicateNewDisks"></a>
Whether to allow the AWS replication agent to automatically replicate newly added disks.
Type: Boolean
Required: No

 ** [bandwidthThrottling](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-request-bandwidthThrottling"></a>
Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** [createPublicIP](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-request-createPublicIP"></a>
Whether to create a Public IP for the Recovery Instance by default.
Type: Boolean
Required: No

 ** [dataPlaneRouting](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-request-dataPlaneRouting"></a>
The data plane routing mechanism that will be used for replication.
Type: String
Valid Values: `PRIVATE_IP | PUBLIC_IP`
Required: No

 ** [defaultLargeStagingDiskType](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-request-defaultLargeStagingDiskType"></a>
The Staging Disk EBS volume type to be used during replication.
Type: String
Valid Values: `GP2 | GP3 | ST1 | AUTO`
Required: No

 ** [ebsEncryption](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-request-ebsEncryption"></a>
The type of EBS encryption to be used during replication.
Type: String
Valid Values: `DEFAULT | CUSTOM | NONE`
Required: No

 ** [ebsEncryptionKeyArn](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-request-ebsEncryptionKeyArn"></a>
The ARN of the EBS encryption key to be used during replication.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.{16,2044}`
Required: No

 ** [internetProtocol](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-request-internetProtocol"></a>
Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)
Type: String
Valid Values: `IPV4 | IPV6`
Required: No

 ** [pitPolicy](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-request-pitPolicy"></a>
The Point in time (PIT) policy to manage snapshots taken during replication.
Type: Array of [PITPolicyRule](API_PITPolicyRule.md) objects
Array Members: Fixed number of 3 items.
Required: No

 ** [replicationConfigurationTemplateID](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-request-replicationConfigurationTemplateID"></a>
The Replication Configuration Template ID.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `rct-[0-9a-zA-Z]{17}`
Required: Yes

 ** [replicationServerInstanceType](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-request-replicationServerInstanceType"></a>
The instance type to be used for the replication server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** [replicationServersSecurityGroupsIDs](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-request-replicationServersSecurityGroupsIDs"></a>
The security group IDs that will be used by the replication server.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `sg-[0-9a-fA-F]{8,}`
Required: No

 ** [stagingAreaSubnetId](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-request-stagingAreaSubnetId"></a>
The subnet to be used by the replication staging area.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `subnet-[0-9a-fA-F]{8,}`
Required: No

 ** [stagingAreaTags](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-request-stagingAreaTags"></a>
A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [useDedicatedReplicationServer](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-request-useDedicatedReplicationServer"></a>
Whether to use a dedicated Replication Server in the replication staging area.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateReplicationConfigurationTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "associateDefaultSecurityGroup": boolean,
   "autoReplicateNewDisks": boolean,
   "bandwidthThrottling": number,
   "createPublicIP": boolean,
   "dataPlaneRouting": "string",
   "defaultLargeStagingDiskType": "string",
   "ebsEncryption": "string",
   "ebsEncryptionKeyArn": "string",
   "internetProtocol": "string",
   "pitPolicy": [
      {
         "enabled": boolean,
         "interval": number,
         "retentionDuration": number,
         "ruleID": number,
         "units": "string"
      }
   ],
   "replicationConfigurationTemplateID": "string",
   "replicationServerInstanceType": "string",
   "replicationServersSecurityGroupsIDs": [ "string" ],
   "stagingAreaSubnetId": "string",
   "stagingAreaTags": {
      "string" : "string"
   },
   "tags": {
      "string" : "string"
   },
   "useDedicatedReplicationServer": boolean
}
```

## Response Elements
<a name="API_UpdateReplicationConfigurationTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-response-arn"></a>
The Replication Configuration Template ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.{16,2044}`

 ** [associateDefaultSecurityGroup](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-response-associateDefaultSecurityGroup"></a>
Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration Template.
Type: Boolean

 ** [autoReplicateNewDisks](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-response-autoReplicateNewDisks"></a>
Whether to allow the AWS replication agent to automatically replicate newly added disks.
Type: Boolean

 ** [bandwidthThrottling](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-response-bandwidthThrottling"></a>
Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.
Type: Long
Valid Range: Minimum value of 0.

 ** [createPublicIP](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-response-createPublicIP"></a>
Whether to create a Public IP for the Recovery Instance by default.
Type: Boolean

 ** [dataPlaneRouting](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-response-dataPlaneRouting"></a>
The data plane routing mechanism that will be used for replication.
Type: String
Valid Values: `PRIVATE_IP | PUBLIC_IP`

 ** [defaultLargeStagingDiskType](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-response-defaultLargeStagingDiskType"></a>
The Staging Disk EBS volume type to be used during replication.
Type: String
Valid Values: `GP2 | GP3 | ST1 | AUTO`

 ** [ebsEncryption](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-response-ebsEncryption"></a>
The type of EBS encryption to be used during replication.
Type: String
Valid Values: `DEFAULT | CUSTOM | NONE`

 ** [ebsEncryptionKeyArn](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-response-ebsEncryptionKeyArn"></a>
The ARN of the EBS encryption key to be used during replication.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.{16,2044}`

 ** [internetProtocol](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-response-internetProtocol"></a>
Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)
Type: String
Valid Values: `IPV4 | IPV6`

 ** [pitPolicy](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-response-pitPolicy"></a>
The Point in time (PIT) policy to manage snapshots taken during replication.
Type: Array of [PITPolicyRule](API_PITPolicyRule.md) objects
Array Members: Fixed number of 3 items.

 ** [replicationConfigurationTemplateID](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-response-replicationConfigurationTemplateID"></a>
The Replication Configuration Template ID.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `rct-[0-9a-zA-Z]{17}`

 ** [replicationServerInstanceType](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-response-replicationServerInstanceType"></a>
The instance type to be used for the replication server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [replicationServersSecurityGroupsIDs](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-response-replicationServersSecurityGroupsIDs"></a>
The security group IDs that will be used by the replication server.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `sg-[0-9a-fA-F]{8,}`

 ** [stagingAreaSubnetId](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-response-stagingAreaSubnetId"></a>
The subnet to be used by the replication staging area.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `subnet-[0-9a-fA-F]{8,}`

 ** [stagingAreaTags](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-response-stagingAreaTags"></a>
A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [tags](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-response-tags"></a>
A set of tags to be associated with the Replication Configuration Template resource.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [useDedicatedReplicationServer](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="drs-UpdateReplicationConfigurationTemplate-response-useDedicatedReplicationServer"></a>
Whether to use a dedicated Replication Server in the replication staging area.
Type: Boolean

## Errors
<a name="API_UpdateReplicationConfigurationTemplate_Errors"></a>

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

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
Validation exception reason.
HTTP Status Code: 400

## See Also
<a name="API_UpdateReplicationConfigurationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/UpdateReplicationConfigurationTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/UpdateReplicationConfigurationTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/UpdateReplicationConfigurationTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/UpdateReplicationConfigurationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/UpdateReplicationConfigurationTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/UpdateReplicationConfigurationTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/UpdateReplicationConfigurationTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/UpdateReplicationConfigurationTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/UpdateReplicationConfigurationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/UpdateReplicationConfigurationTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
