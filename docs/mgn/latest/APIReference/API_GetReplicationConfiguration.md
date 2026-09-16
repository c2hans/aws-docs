---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_GetReplicationConfiguration.html
---

# GetReplicationConfiguration
<a name="API_GetReplicationConfiguration"></a>

Lists all ReplicationConfigurations, filtered by Source Server ID.

## Request Syntax
<a name="API_GetReplicationConfiguration_RequestSyntax"></a>

```
POST /GetReplicationConfiguration HTTP/1.1
Content-type: application/json

{
   "accountID": "{{string}}",
   "sourceServerID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetReplicationConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetReplicationConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountID](#API_GetReplicationConfiguration_RequestSyntax) **   <a name="mgn-GetReplicationConfiguration-request-accountID"></a>
Request to get Replication Configuration by Account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** [sourceServerID](#API_GetReplicationConfiguration_RequestSyntax) **   <a name="mgn-GetReplicationConfiguration-request-sourceServerID"></a>
Request to get Replication Configuration by Source Server ID.
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
<a name="API_GetReplicationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [associateDefaultSecurityGroup](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="mgn-GetReplicationConfiguration-response-associateDefaultSecurityGroup"></a>
Replication Configuration associate default Application Migration Service Security Group.
Type: Boolean

 ** [bandwidthThrottling](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="mgn-GetReplicationConfiguration-response-bandwidthThrottling"></a>
Replication Configuration set bandwidth throttling.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 10000.

 ** [createPublicIP](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="mgn-GetReplicationConfiguration-response-createPublicIP"></a>
Replication Configuration create Public IP.
Type: Boolean

 ** [dataPlaneRouting](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="mgn-GetReplicationConfiguration-response-dataPlaneRouting"></a>
Replication Configuration data plane routing.
Type: String
Valid Values: `PRIVATE_IP | PUBLIC_IP`

 ** [defaultLargeStagingDiskType](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="mgn-GetReplicationConfiguration-response-defaultLargeStagingDiskType"></a>
Replication Configuration use default large Staging Disks.
Type: String
Valid Values: `GP2 | ST1 | GP3`

 ** [ebsEncryption](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="mgn-GetReplicationConfiguration-response-ebsEncryption"></a>
Replication Configuration EBS encryption.
Type: String
Valid Values: `DEFAULT | CUSTOM`

 ** [ebsEncryptionKeyArn](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="mgn-GetReplicationConfiguration-response-ebsEncryptionKeyArn"></a>
Replication Configuration EBS encryption key ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [internetProtocol](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="mgn-GetReplicationConfiguration-response-internetProtocol"></a>
Replication Configuration internet protocol.
Type: String
Valid Values: `IPV4 | IPV6`

 ** [name](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="mgn-GetReplicationConfiguration-response-name"></a>
Replication Configuration name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.

 ** [replicatedDisks](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="mgn-GetReplicationConfiguration-response-replicatedDisks"></a>
Replication Configuration replicated disks.
Type: Array of [ReplicationConfigurationReplicatedDisk](API_ReplicationConfigurationReplicatedDisk.md) objects
Array Members: Minimum number of 0 items. Maximum number of 60 items.

 ** [replicationServerInstanceType](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="mgn-GetReplicationConfiguration-response-replicationServerInstanceType"></a>
Replication Configuration Replication Server instance type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [replicationServersSecurityGroupsIDs](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="mgn-GetReplicationConfiguration-response-replicationServersSecurityGroupsIDs"></a>
Replication Configuration Replication Server Security Group IDs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `sg-[0-9a-fA-F]{8,}`

 ** [sourceServerID](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="mgn-GetReplicationConfiguration-response-sourceServerID"></a>
Replication Configuration Source Server ID.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`

 ** [stagingAreaSubnetId](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="mgn-GetReplicationConfiguration-response-stagingAreaSubnetId"></a>
Replication Configuration Staging Area subnet ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `subnet-[0-9a-fA-F]{8,}`

 ** [stagingAreaTags](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="mgn-GetReplicationConfiguration-response-stagingAreaTags"></a>
Replication Configuration Staging Area tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [storageConfiguration](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="mgn-GetReplicationConfiguration-response-storageConfiguration"></a>
Replication Configuration storage configuration.
Type: [StorageConfiguration](API_StorageConfiguration.md) object

 ** [storeSnapshotOnLocalZone](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="mgn-GetReplicationConfiguration-response-storeSnapshotOnLocalZone"></a>
Replication Configuration store snapshot on local zone.
Type: Boolean

 ** [useDedicatedReplicationServer](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="mgn-GetReplicationConfiguration-response-useDedicatedReplicationServer"></a>
Replication Configuration use Dedicated Replication Server.
Type: Boolean

 ** [useFipsEndpoint](#API_GetReplicationConfiguration_ResponseSyntax) **   <a name="mgn-GetReplicationConfiguration-response-useFipsEndpoint"></a>
Replication Configuration use Fips Endpoint.
Type: Boolean

## Errors
<a name="API_GetReplicationConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

## See Also
<a name="API_GetReplicationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/GetReplicationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/GetReplicationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/GetReplicationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/GetReplicationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/GetReplicationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/GetReplicationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/GetReplicationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/GetReplicationConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/GetReplicationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/GetReplicationConfiguration)
