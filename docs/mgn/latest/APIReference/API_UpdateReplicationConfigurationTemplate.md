---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_UpdateReplicationConfigurationTemplate.html
---

# UpdateReplicationConfigurationTemplate
<a name="API_UpdateReplicationConfigurationTemplate"></a>

Updates multiple ReplicationConfigurationTemplates by ID.

## Request Syntax
<a name="API_UpdateReplicationConfigurationTemplate_RequestSyntax"></a>

```
POST /UpdateReplicationConfigurationTemplate HTTP/1.1
Content-type: application/json

{
   "arn": "{{string}}",
   "associateDefaultSecurityGroup": {{boolean}},
   "bandwidthThrottling": {{number}},
   "createPublicIP": {{boolean}},
   "dataPlaneRouting": "{{string}}",
   "defaultLargeStagingDiskType": "{{string}}",
   "ebsEncryption": "{{string}}",
   "ebsEncryptionKeyArn": "{{string}}",
   "internetProtocol": "{{string}}",
   "replicationConfigurationTemplateID": "{{string}}",
   "replicationServerInstanceType": "{{string}}",
   "replicationServersSecurityGroupsIDs": [ "{{string}}" ],
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
<a name="API_UpdateReplicationConfigurationTemplate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateReplicationConfigurationTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arn](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-request-arn"></a>
Update replication configuration template ARN request.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** [associateDefaultSecurityGroup](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-request-associateDefaultSecurityGroup"></a>
Update replication configuration template associate default Application Migration Service Security group request.
Type: Boolean
Required: No

 ** [bandwidthThrottling](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-request-bandwidthThrottling"></a>
Update replication configuration template bandwidth throttling request.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 10000.
Required: No

 ** [createPublicIP](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-request-createPublicIP"></a>
Update replication configuration template create Public IP request.
Type: Boolean
Required: No

 ** [dataPlaneRouting](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-request-dataPlaneRouting"></a>
Update replication configuration template data plane routing request.
Type: String
Valid Values: `PRIVATE_IP | PUBLIC_IP`
Required: No

 ** [defaultLargeStagingDiskType](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-request-defaultLargeStagingDiskType"></a>
Update replication configuration template use default large Staging Disk type request.
Type: String
Valid Values: `GP2 | ST1 | GP3`
Required: No

 ** [ebsEncryption](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-request-ebsEncryption"></a>
Update replication configuration template EBS encryption request.
Type: String
Valid Values: `DEFAULT | CUSTOM`
Required: No

 ** [ebsEncryptionKeyArn](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-request-ebsEncryptionKeyArn"></a>
Update replication configuration template EBS encryption key ARN request.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** [internetProtocol](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-request-internetProtocol"></a>
Update replication configuration template internet protocol request.
Type: String
Valid Values: `IPV4 | IPV6`
Required: No

 ** [replicationConfigurationTemplateID](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-request-replicationConfigurationTemplateID"></a>
Update replication configuration template template ID request.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `rct-[0-9a-zA-Z]{17}`
Required: Yes

 ** [replicationServerInstanceType](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-request-replicationServerInstanceType"></a>
Update replication configuration template Replication Server instance type request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** [replicationServersSecurityGroupsIDs](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-request-replicationServersSecurityGroupsIDs"></a>
Update replication configuration template Replication Server Security groups IDs request.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `sg-[0-9a-fA-F]{8,}`
Required: No

 ** [stagingAreaSubnetId](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-request-stagingAreaSubnetId"></a>
Update replication configuration template Staging Area subnet ID request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `subnet-[0-9a-fA-F]{8,}`
Required: No

 ** [stagingAreaTags](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-request-stagingAreaTags"></a>
Update replication configuration template Staging Area Tags request.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [storageConfiguration](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-request-storageConfiguration"></a>
Update replication configuration template storage configuration request.
Type: [StorageConfiguration](API_StorageConfiguration.md) object
Required: No

 ** [storeSnapshotOnLocalZone](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-request-storeSnapshotOnLocalZone"></a>
Update replication configuration template store snapshot on local zone request.
Type: Boolean
Required: No

 ** [useDedicatedReplicationServer](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-request-useDedicatedReplicationServer"></a>
Update replication configuration template use dedicated Replication Server request.
Type: Boolean
Required: No

 ** [useFipsEndpoint](#API_UpdateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-request-useFipsEndpoint"></a>
Update replication configuration template use Fips Endpoint request.
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
   "bandwidthThrottling": number,
   "createPublicIP": boolean,
   "dataPlaneRouting": "string",
   "defaultLargeStagingDiskType": "string",
   "ebsEncryption": "string",
   "ebsEncryptionKeyArn": "string",
   "internetProtocol": "string",
   "replicationConfigurationTemplateID": "string",
   "replicationServerInstanceType": "string",
   "replicationServersSecurityGroupsIDs": [ "string" ],
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
   "tags": {
      "string" : "string"
   },
   "useDedicatedReplicationServer": boolean,
   "useFipsEndpoint": boolean
}
```

## Response Elements
<a name="API_UpdateReplicationConfigurationTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-response-arn"></a>
Replication Configuration template ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [associateDefaultSecurityGroup](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-response-associateDefaultSecurityGroup"></a>
Replication Configuration template associate default Application Migration Service Security group.
Type: Boolean

 ** [bandwidthThrottling](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-response-bandwidthThrottling"></a>
Replication Configuration template bandwidth throttling.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 10000.

 ** [createPublicIP](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-response-createPublicIP"></a>
Replication Configuration template create Public IP.
Type: Boolean

 ** [dataPlaneRouting](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-response-dataPlaneRouting"></a>
Replication Configuration template data plane routing.
Type: String
Valid Values: `PRIVATE_IP | PUBLIC_IP`

 ** [defaultLargeStagingDiskType](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-response-defaultLargeStagingDiskType"></a>
Replication Configuration template use default large Staging Disk type.
Type: String
Valid Values: `GP2 | ST1 | GP3`

 ** [ebsEncryption](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-response-ebsEncryption"></a>
Replication Configuration template EBS encryption.
Type: String
Valid Values: `DEFAULT | CUSTOM`

 ** [ebsEncryptionKeyArn](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-response-ebsEncryptionKeyArn"></a>
Replication Configuration template EBS encryption key ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [internetProtocol](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-response-internetProtocol"></a>
Replication Configuration template internet protocol.
Type: String
Valid Values: `IPV4 | IPV6`

 ** [replicationConfigurationTemplateID](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-response-replicationConfigurationTemplateID"></a>
Replication Configuration template ID.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `rct-[0-9a-zA-Z]{17}`

 ** [replicationServerInstanceType](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-response-replicationServerInstanceType"></a>
Replication Configuration template server instance type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [replicationServersSecurityGroupsIDs](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-response-replicationServersSecurityGroupsIDs"></a>
Replication Configuration template server Security Groups IDs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `sg-[0-9a-fA-F]{8,}`

 ** [stagingAreaSubnetId](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-response-stagingAreaSubnetId"></a>
Replication Configuration template Staging Area subnet ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `subnet-[0-9a-fA-F]{8,}`

 ** [stagingAreaTags](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-response-stagingAreaTags"></a>
Replication Configuration template Staging Area Tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [storageConfiguration](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-response-storageConfiguration"></a>
Replication Configuration template storage configuration.
Type: [StorageConfiguration](API_StorageConfiguration.md) object

 ** [storeSnapshotOnLocalZone](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-response-storeSnapshotOnLocalZone"></a>
Replication Configuration template store snapshot on local zone.
Type: Boolean

 ** [tags](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-response-tags"></a>
Replication Configuration template Tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [useDedicatedReplicationServer](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-response-useDedicatedReplicationServer"></a>
Replication Configuration template use Dedicated Replication Server.
Type: Boolean

 ** [useFipsEndpoint](#API_UpdateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateReplicationConfigurationTemplate-response-useFipsEndpoint"></a>
Replication Configuration template use Fips Endpoint.
Type: Boolean

## Errors
<a name="API_UpdateReplicationConfigurationTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Operating denied due to a file permission or access check error.
HTTP Status Code: 403

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
<a name="API_UpdateReplicationConfigurationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/UpdateReplicationConfigurationTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/UpdateReplicationConfigurationTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/UpdateReplicationConfigurationTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/UpdateReplicationConfigurationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/UpdateReplicationConfigurationTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/UpdateReplicationConfigurationTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/UpdateReplicationConfigurationTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/UpdateReplicationConfigurationTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/UpdateReplicationConfigurationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/UpdateReplicationConfigurationTemplate)
