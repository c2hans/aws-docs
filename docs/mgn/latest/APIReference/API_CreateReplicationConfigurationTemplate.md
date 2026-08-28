---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_CreateReplicationConfigurationTemplate.html
---

# CreateReplicationConfigurationTemplate
<a name="API_CreateReplicationConfigurationTemplate"></a>

Creates a new ReplicationConfigurationTemplate.

## Request Syntax
<a name="API_CreateReplicationConfigurationTemplate_RequestSyntax"></a>

```
POST /CreateReplicationConfigurationTemplate HTTP/1.1
Content-type: application/json

{
   "associateDefaultSecurityGroup": {{boolean}},
   "bandwidthThrottling": {{number}},
   "createPublicIP": {{boolean}},
   "dataPlaneRouting": "{{string}}",
   "defaultLargeStagingDiskType": "{{string}}",
   "ebsEncryption": "{{string}}",
   "ebsEncryptionKeyArn": "{{string}}",
   "internetProtocol": "{{string}}",
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
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "useDedicatedReplicationServer": {{boolean}},
   "useFipsEndpoint": {{boolean}}
}
```

## URI Request Parameters
<a name="API_CreateReplicationConfigurationTemplate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateReplicationConfigurationTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [associateDefaultSecurityGroup](#API_CreateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-request-associateDefaultSecurityGroup"></a>
Request to associate the default Application Migration Service Security group with the Replication Settings template.
Type: Boolean
Required: Yes

 ** [bandwidthThrottling](#API_CreateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-request-bandwidthThrottling"></a>
Request to configure bandwidth throttling during Replication Settings template creation.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 10000.
Required: Yes

 ** [createPublicIP](#API_CreateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-request-createPublicIP"></a>
Request to create Public IP during Replication Settings template creation.
Type: Boolean
Required: Yes

 ** [dataPlaneRouting](#API_CreateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-request-dataPlaneRouting"></a>
Request to configure data plane routing during Replication Settings template creation.
Type: String
Valid Values: `PRIVATE_IP | PUBLIC_IP`
Required: Yes

 ** [defaultLargeStagingDiskType](#API_CreateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-request-defaultLargeStagingDiskType"></a>
Request to configure the default large staging disk EBS volume type during Replication Settings template creation.
Type: String
Valid Values: `GP2 | ST1 | GP3`
Required: Yes

 ** [ebsEncryption](#API_CreateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-request-ebsEncryption"></a>
Request to configure EBS encryption during Replication Settings template creation.
Type: String
Valid Values: `DEFAULT | CUSTOM`
Required: Yes

 ** [ebsEncryptionKeyArn](#API_CreateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-request-ebsEncryptionKeyArn"></a>
Request to configure an EBS encryption key during Replication Settings template creation.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** [internetProtocol](#API_CreateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-request-internetProtocol"></a>
Request to configure the internet protocol to IPv4 or IPv6.
Type: String
Valid Values: `IPV4 | IPV6`
Required: No

 ** [replicationServerInstanceType](#API_CreateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-request-replicationServerInstanceType"></a>
Request to configure the Replication Server instance type during Replication Settings template creation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: Yes

 ** [replicationServersSecurityGroupsIDs](#API_CreateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-request-replicationServersSecurityGroupsIDs"></a>
Request to configure the Replication Server Security group ID during Replication Settings template creation.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `sg-[0-9a-fA-F]{8,}`
Required: Yes

 ** [stagingAreaSubnetId](#API_CreateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-request-stagingAreaSubnetId"></a>
Request to configure the Staging Area subnet ID during Replication Settings template creation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `subnet-[0-9a-fA-F]{8,}`
Required: Yes

 ** [stagingAreaTags](#API_CreateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-request-stagingAreaTags"></a>
Request to configure Staging Area tags during Replication Settings template creation.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** [storageConfiguration](#API_CreateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-request-storageConfiguration"></a>
Request to configure storage during Replication Settings template creation.
Type: [StorageConfiguration](API_StorageConfiguration.md) object
Required: No

 ** [storeSnapshotOnLocalZone](#API_CreateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-request-storeSnapshotOnLocalZone"></a>
Request to store snapshot on local zone during Replication Settings template creation.
Type: Boolean
Required: No

 ** [tags](#API_CreateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-request-tags"></a>
Request to configure tags during Replication Settings template creation.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [useDedicatedReplicationServer](#API_CreateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-request-useDedicatedReplicationServer"></a>
Request to use Dedicated Replication Servers during Replication Settings template creation.
Type: Boolean
Required: Yes

 ** [useFipsEndpoint](#API_CreateReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-request-useFipsEndpoint"></a>
Request to use Fips Endpoint during Replication Settings template creation.
Type: Boolean
Required: No

## Response Syntax
<a name="API_CreateReplicationConfigurationTemplate_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateReplicationConfigurationTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-response-arn"></a>
Replication Configuration template ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [associateDefaultSecurityGroup](#API_CreateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-response-associateDefaultSecurityGroup"></a>
Replication Configuration template associate default Application Migration Service Security group.
Type: Boolean

 ** [bandwidthThrottling](#API_CreateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-response-bandwidthThrottling"></a>
Replication Configuration template bandwidth throttling.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 10000.

 ** [createPublicIP](#API_CreateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-response-createPublicIP"></a>
Replication Configuration template create Public IP.
Type: Boolean

 ** [dataPlaneRouting](#API_CreateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-response-dataPlaneRouting"></a>
Replication Configuration template data plane routing.
Type: String
Valid Values: `PRIVATE_IP | PUBLIC_IP`

 ** [defaultLargeStagingDiskType](#API_CreateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-response-defaultLargeStagingDiskType"></a>
Replication Configuration template use default large Staging Disk type.
Type: String
Valid Values: `GP2 | ST1 | GP3`

 ** [ebsEncryption](#API_CreateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-response-ebsEncryption"></a>
Replication Configuration template EBS encryption.
Type: String
Valid Values: `DEFAULT | CUSTOM`

 ** [ebsEncryptionKeyArn](#API_CreateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-response-ebsEncryptionKeyArn"></a>
Replication Configuration template EBS encryption key ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [internetProtocol](#API_CreateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-response-internetProtocol"></a>
Replication Configuration template internet protocol.
Type: String
Valid Values: `IPV4 | IPV6`

 ** [replicationConfigurationTemplateID](#API_CreateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-response-replicationConfigurationTemplateID"></a>
Replication Configuration template ID.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `rct-[0-9a-zA-Z]{17}`

 ** [replicationServerInstanceType](#API_CreateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-response-replicationServerInstanceType"></a>
Replication Configuration template server instance type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [replicationServersSecurityGroupsIDs](#API_CreateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-response-replicationServersSecurityGroupsIDs"></a>
Replication Configuration template server Security Groups IDs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `sg-[0-9a-fA-F]{8,}`

 ** [stagingAreaSubnetId](#API_CreateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-response-stagingAreaSubnetId"></a>
Replication Configuration template Staging Area subnet ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `subnet-[0-9a-fA-F]{8,}`

 ** [stagingAreaTags](#API_CreateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-response-stagingAreaTags"></a>
Replication Configuration template Staging Area Tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [storageConfiguration](#API_CreateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-response-storageConfiguration"></a>
Replication Configuration template storage configuration.
Type: [StorageConfiguration](API_StorageConfiguration.md) object

 ** [storeSnapshotOnLocalZone](#API_CreateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-response-storeSnapshotOnLocalZone"></a>
Replication Configuration template store snapshot on local zone.
Type: Boolean

 ** [tags](#API_CreateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-response-tags"></a>
Replication Configuration template Tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [useDedicatedReplicationServer](#API_CreateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-response-useDedicatedReplicationServer"></a>
Replication Configuration template use Dedicated Replication Server.
Type: Boolean

 ** [useFipsEndpoint](#API_CreateReplicationConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateReplicationConfigurationTemplate-response-useFipsEndpoint"></a>
Replication Configuration template use Fips Endpoint.
Type: Boolean

## Errors
<a name="API_CreateReplicationConfigurationTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Operation denied due to a file permission or access check error.
HTTP Status Code: 403

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
<a name="API_CreateReplicationConfigurationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/CreateReplicationConfigurationTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/CreateReplicationConfigurationTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/CreateReplicationConfigurationTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/CreateReplicationConfigurationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/CreateReplicationConfigurationTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/CreateReplicationConfigurationTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/CreateReplicationConfigurationTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/CreateReplicationConfigurationTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/CreateReplicationConfigurationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/CreateReplicationConfigurationTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
