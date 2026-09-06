---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_UpdateReplicationConfiguration.html
---

# UpdateReplicationConfiguration
<a name="API_UpdateReplicationConfiguration"></a>

Allows you to update multiple ReplicationConfigurations by Source Server ID.

## Request Syntax
<a name="API_UpdateReplicationConfiguration_RequestSyntax"></a>

```
POST /UpdateReplicationConfiguration HTTP/1.1
Content-type: application/json

{
   "accountID": "{{string}}",
   "associateDefaultSecurityGroup": {{boolean}},
   "bandwidthThrottling": {{number}},
   "createPublicIP": {{boolean}},
   "dataPlaneRouting": "{{string}}",
   "defaultLargeStagingDiskType": "{{string}}",
   "ebsEncryption": "{{string}}",
   "ebsEncryptionKeyArn": "{{string}}",
   "internetProtocol": "{{string}}",
   "name": "{{string}}",
   "replicatedDisks": [
      {
         "deviceName": "{{string}}",
         "iops": {{number}},
         "isBootDisk": {{boolean}},
         "stagingDiskType": "{{string}}",
         "throughput": {{number}}
      }
   ],
   "replicationServerInstanceType": "{{string}}",
   "replicationServersSecurityGroupsIDs": [ "{{string}}" ],
   "sourceServerID": "{{string}}",
   "stagingAreaSubnetId": "{{string}}",
   "stagingAreaTags": {
      "{{string}}" : "{{string}}"
   },
   "storageConfiguration": {
      "fsxOntapConfiguration": {
         "credentialsSecretArn": "{{string}}",
         "storageVirtualMachineId": "{{string}}"
      },
      "storageType": "{{string}}"
   },
   "storeSnapshotOnLocalZone": {{boolean}},
   "useDedicatedReplicationServer": {{boolean}},
   "useFipsEndpoint": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UpdateReplicationConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateReplicationConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountID](#API_UpdateReplicationConfiguration_RequestSyntax) **   <a name="mgn-UpdateReplicationConfiguration-request-accountID"></a>
Update replication configuration Account ID request.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** [associateDefaultSecurityGroup](#API_UpdateReplicationConfiguration_RequestSyntax) **   <a name="mgn-UpdateReplicationConfiguration-request-associateDefaultSecurityGroup"></a>
Update replication configuration associate default Application Migration Service Security group request.
Type: Boolean
Required: No

 ** [bandwidthThrottling](#API_UpdateReplicationConfiguration_RequestSyntax) **   <a name="mgn-UpdateReplicationConfiguration-request-bandwidthThrottling"></a>
Update replication configuration bandwidth throttling request.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 10000.
Required: No

 ** [createPublicIP](#API_UpdateReplicationConfiguration_RequestSyntax) **   <a name="mgn-UpdateReplicationConfiguration-request-createPublicIP"></a>
Update replication configuration create Public IP request.
Type: Boolean
Required: No

 ** [dataPlaneRouting](#API_UpdateReplicationConfiguration_RequestSyntax) **   <a name="mgn-UpdateReplicationConfiguration-request-dataPlaneRouting"></a>
Update replication configuration data plane routing request.
Type: String
Valid Values: `PRIVATE_IP | PUBLIC_IP`
Required: No

 ** [defaultLargeStagingDiskType](#API_UpdateReplicationConfiguration_RequestSyntax) **   <a name="mgn-UpdateReplicationConfiguration-request-defaultLargeStagingDiskType"></a>
Update replication configuration use default large Staging Disk type request.
Type: String
Valid Values: `GP2 | ST1 | GP3`
Required: No

 ** [ebsEncryption](#API_UpdateReplicationConfiguration_RequestSyntax) **   <a name="mgn-UpdateReplicationConfiguration-request-ebsEncryption"></a>
Update replication configuration EBS encryption request.
Type: String
Valid Values: `DEFAULT | CUSTOM`
Required: No

 ** [ebsEncryptionKeyArn](#API_UpdateReplicationConfiguration_RequestSyntax) **   <a name="mgn-UpdateReplicationConfiguration-request-ebsEncryptionKeyArn"></a>
Update replication configuration EBS encryption key ARN request.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** [internetProtocol](#API_UpdateReplicationConfiguration_RequestSyntax) **   <a name="mgn-UpdateReplicationConfiguration-request-internetProtocol"></a>
Update replication configuration internet protocol.
Type: String
Valid Values: `IPV4 | IPV6`
Required: No

 ** [name](#API_UpdateReplicationConfiguration_RequestSyntax) **   <a name="mgn-UpdateReplicationConfiguration-request-name"></a>
Update replication configuration name request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** [replicatedDisks](#API_UpdateReplicationConfiguration_RequestSyntax) **   <a name="mgn-UpdateReplicationConfiguration-request-replicatedDisks"></a>
Update replication configuration replicated disks request.
Type: Array of [ReplicationConfigurationReplicatedDisk](API_ReplicationConfigurationReplicatedDisk.md) objects
Array Members: Minimum number of 0 items. Maximum number of 60 items.
Required: No

 ** [replicationServerInstanceType](#API_UpdateReplicationConfiguration_RequestSyntax) **   <a name="mgn-UpdateReplicationConfiguration-request-replicationServerInstanceType"></a>
Update replication configuration Replication Server instance type request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** [replicationServersSecurityGroupsIDs](#API_UpdateReplicationConfiguration_RequestSyntax) **   <a name="mgn-UpdateReplicationConfiguration-request-replicationServersSecurityGroupsIDs"></a>
Update replication configuration Replication Server Security Groups IDs request.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `sg-[0-9a-fA-F]{8,}`
Required: No

 ** [sourceServerID](#API_UpdateReplicationConfiguration_RequestSyntax) **   <a name="mgn-UpdateReplicationConfiguration-request-sourceServerID"></a>
Update replication configuration Source Server ID request.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: Yes

 ** [stagingAreaSubnetId](#API_UpdateReplicationConfiguration_RequestSyntax) **   <a name="mgn-UpdateReplicationConfiguration-request-stagingAreaSubnetId"></a>
Update replication configuration Staging Area subnet request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `subnet-[0-9a-fA-F]{8,}`
Required: No

 ** [stagingAreaTags](#API_UpdateReplicationConfiguration_RequestSyntax) **   <a name="mgn-UpdateReplicationConfiguration-request-stagingAreaTags"></a>
Update replication configuration Staging Area Tags request.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [storageConfiguration](#API_UpdateReplicationConfiguration_RequestSyntax) **   <a name="mgn-UpdateReplicationConfiguration-request-storageConfiguration"></a>
Update replication configuration storage configuration.
Type: [StorageConfiguration](API_StorageConfiguration.md) object
Required: No

 ** [storeSnapshotOnLocalZone](#API_UpdateReplicationConfiguration_RequestSyntax) **   <a name="mgn-UpdateReplicationConfiguration-request-storeSnapshotOnLocalZone"></a>
Update replication configuration store snapshot on local zone.
Type: Boolean
Required: No

 ** [useDedicatedReplicationServer](#API_UpdateReplicationConfiguration_RequestSyntax) **   <a name="mgn-UpdateReplicationConfiguration-request-useDedicatedReplicationServer"></a>
Update replication configuration use dedicated Replication Server request.
Type: Boolean
Required: No

 ** [useFipsEndpoint](#API_UpdateReplicationConfiguration_RequestSyntax) **   <a name="mgn-UpdateReplicationConfiguration-request-useFipsEndpoint"></a>
Update replication configuration use Fips Endpoint.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateReplicationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "associateDefaultSecurityGroup": boolean,
   "bandwidthThrottling": number,
   "createPublicIP": boolean,
   "dataPlaneRouting": "string",
   "defaultLargeStagingDiskType": "string",
   "ebsEncryption": "string",
   "ebsEncryptionKeyArn": "string",
   "internetProtocol": "string",
   "name": "string",
   "replicatedDisks": [
      {
         "deviceName": "string",
         "iops": number,
         "isBootDisk": boolean,
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
   "storageConfiguration": {
      "fsxOntapConfiguration": {
         "credentialsSecretArn": "string",
         "storageVirtualMachineId": "string"
      },
      "storageType": "string"
   },
   "storeSnapshotOnLocalZone": boolean,
   "useDedicatedReplicationServer": boolean,
   "useFipsEndpoint": boolean
}
```

## Response Elements
<a name="API_UpdateReplicationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [associateDefaultSecurityGroup](#API_UpdateReplicationConfiguration_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfiguration-response-associateDefaultSecurityGroup"></a>
Replication Configuration associate default Application Migration Service Security Group.
Type: Boolean

 ** [bandwidthThrottling](#API_UpdateReplicationConfiguration_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfiguration-response-bandwidthThrottling"></a>
Replication Configuration set bandwidth throttling.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 10000.

 ** [createPublicIP](#API_UpdateReplicationConfiguration_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfiguration-response-createPublicIP"></a>
Replication Configuration create Public IP.
Type: Boolean

 ** [dataPlaneRouting](#API_UpdateReplicationConfiguration_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfiguration-response-dataPlaneRouting"></a>
Replication Configuration data plane routing.
Type: String
Valid Values: `PRIVATE_IP | PUBLIC_IP`

 ** [defaultLargeStagingDiskType](#API_UpdateReplicationConfiguration_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfiguration-response-defaultLargeStagingDiskType"></a>
Replication Configuration use default large Staging Disks.
Type: String
Valid Values: `GP2 | ST1 | GP3`

 ** [ebsEncryption](#API_UpdateReplicationConfiguration_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfiguration-response-ebsEncryption"></a>
Replication Configuration EBS encryption.
Type: String
Valid Values: `DEFAULT | CUSTOM`

 ** [ebsEncryptionKeyArn](#API_UpdateReplicationConfiguration_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfiguration-response-ebsEncryptionKeyArn"></a>
Replication Configuration EBS encryption key ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [internetProtocol](#API_UpdateReplicationConfiguration_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfiguration-response-internetProtocol"></a>
Replication Configuration internet protocol.
Type: String
Valid Values: `IPV4 | IPV6`

 ** [name](#API_UpdateReplicationConfiguration_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfiguration-response-name"></a>
Replication Configuration name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.

 ** [replicatedDisks](#API_UpdateReplicationConfiguration_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfiguration-response-replicatedDisks"></a>
Replication Configuration replicated disks.
Type: Array of [ReplicationConfigurationReplicatedDisk](API_ReplicationConfigurationReplicatedDisk.md) objects
Array Members: Minimum number of 0 items. Maximum number of 60 items.

 ** [replicationServerInstanceType](#API_UpdateReplicationConfiguration_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfiguration-response-replicationServerInstanceType"></a>
Replication Configuration Replication Server instance type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [replicationServersSecurityGroupsIDs](#API_UpdateReplicationConfiguration_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfiguration-response-replicationServersSecurityGroupsIDs"></a>
Replication Configuration Replication Server Security Group IDs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `sg-[0-9a-fA-F]{8,}`

 ** [sourceServerID](#API_UpdateReplicationConfiguration_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfiguration-response-sourceServerID"></a>
Replication Configuration Source Server ID.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`

 ** [stagingAreaSubnetId](#API_UpdateReplicationConfiguration_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfiguration-response-stagingAreaSubnetId"></a>
Replication Configuration Staging Area subnet ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `subnet-[0-9a-fA-F]{8,}`

 ** [stagingAreaTags](#API_UpdateReplicationConfiguration_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfiguration-response-stagingAreaTags"></a>
Replication Configuration Staging Area tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [storageConfiguration](#API_UpdateReplicationConfiguration_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfiguration-response-storageConfiguration"></a>
Replication Configuration storage configuration.
Type: [StorageConfiguration](API_StorageConfiguration.md) object

 ** [storeSnapshotOnLocalZone](#API_UpdateReplicationConfiguration_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfiguration-response-storeSnapshotOnLocalZone"></a>
Replication Configuration store snapshot on local zone.
Type: Boolean

 ** [useDedicatedReplicationServer](#API_UpdateReplicationConfiguration_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfiguration-response-useDedicatedReplicationServer"></a>
Replication Configuration use Dedicated Replication Server.
Type: Boolean

 ** [useFipsEndpoint](#API_UpdateReplicationConfiguration_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfiguration-response-useFipsEndpoint"></a>
Replication Configuration use Fips Endpoint.
Type: Boolean

## Errors
<a name="API_UpdateReplicationConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Operation denied due to a file permission or access check error.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the target resource.
 ** errors **
Conflict Exception specific errors.
 ** resourceId **
A conflict occurred when prompting for the Resource ID.
 ** resourceType **
A conflict occurred when prompting for resource type.
HTTP Status Code: 409

 ** ResourceNotFoundException **
Resource not found exception.
 ** resourceId **
Resource ID not found error.
 ** resourceType **
Resource type not found error.
HTTP Status Code: 404

 ** UninitializedAccountException **
Uninitialized account exception.
HTTP Status Code: 400

 ** ValidationException **
Validate exception.
 ** fieldList **
Validate exception field list.
 ** reason **
Validate exception reason.
HTTP Status Code: 400

## See Also
<a name="API_UpdateReplicationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/UpdateReplicationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/UpdateReplicationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/UpdateReplicationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/UpdateReplicationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/UpdateReplicationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/UpdateReplicationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/UpdateReplicationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/UpdateReplicationConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/UpdateReplicationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/UpdateReplicationConfiguration)
