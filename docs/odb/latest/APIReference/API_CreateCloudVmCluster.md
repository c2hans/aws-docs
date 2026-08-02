---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateCloudVmCluster.html
---

# CreateCloudVmCluster
<a name="API_CreateCloudVmCluster"></a>

Creates a VM cluster on the specified Exadata infrastructure.

## Request Syntax
<a name="API_CreateCloudVmCluster_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "cloudExadataInfrastructureId": "{{string}}",
   "clusterName": "{{string}}",
   "cpuCoreCount": {{number}},
   "dataCollectionOptions": {
      "isDiagnosticsEventsEnabled": {{boolean}},
      "isHealthMonitoringEnabled": {{boolean}},
      "isIncidentLogsEnabled": {{boolean}}
   },
   "dataStorageSizeInTBs": {{number}},
   "dbNodeStorageSizeInGBs": {{number}},
   "dbServers": [ "{{string}}" ],
   "displayName": "{{string}}",
   "giVersion": "{{string}}",
   "hostname": "{{string}}",
   "isLocalBackupEnabled": {{boolean}},
   "isSparseDiskgroupEnabled": {{boolean}},
   "licenseModel": "{{string}}",
   "memorySizeInGBs": {{number}},
   "odbNetworkId": "{{string}}",
   "scanListenerPortTcp": {{number}},
   "sshPublicKeys": [ "{{string}}" ],
   "systemVersion": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "timeZone": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateCloudVmCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateCloudVmCluster_RequestSyntax) **   <a name="odb-CreateCloudVmCluster-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. The client token is valid for up to 24 hours after it's first used.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 64.
Pattern: `[a-zA-Z0-9_\/.=-]+`
Required: No

 ** [cloudExadataInfrastructureId](#API_CreateCloudVmCluster_RequestSyntax) **   <a name="odb-CreateCloudVmCluster-request-cloudExadataInfrastructureId"></a>
The unique identifier of the Exadata infrastructure for this VM cluster.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** [clusterName](#API_CreateCloudVmCluster_RequestSyntax) **   <a name="odb-CreateCloudVmCluster-request-clusterName"></a>
A name for the Grid Infrastructure cluster. The name isn't case sensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 11.
Pattern: `[a-zA-Z][a-zA-Z0-9-]*`
Required: No

 ** [cpuCoreCount](#API_CreateCloudVmCluster_RequestSyntax) **   <a name="odb-CreateCloudVmCluster-request-cpuCoreCount"></a>
The number of CPU cores to enable on the VM cluster.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000.
Required: Yes

 ** [dataCollectionOptions](#API_CreateCloudVmCluster_RequestSyntax) **   <a name="odb-CreateCloudVmCluster-request-dataCollectionOptions"></a>
The set of preferences for the various diagnostic collection options for the VM cluster.
Type: [DataCollectionOptions](API_DataCollectionOptions.md) object
Required: No

 ** [dataStorageSizeInTBs](#API_CreateCloudVmCluster_RequestSyntax) **   <a name="odb-CreateCloudVmCluster-request-dataStorageSizeInTBs"></a>
The size of the data disk group, in terabytes (TBs), to allocate for the VM cluster.
Type: Double
Required: No

 ** [dbNodeStorageSizeInGBs](#API_CreateCloudVmCluster_RequestSyntax) **   <a name="odb-CreateCloudVmCluster-request-dbNodeStorageSizeInGBs"></a>
The amount of local node storage, in gigabytes (GBs), to allocate for the VM cluster.
Type: Integer
Required: No

 ** [dbServers](#API_CreateCloudVmCluster_RequestSyntax) **   <a name="odb-CreateCloudVmCluster-request-dbServers"></a>
The list of database servers for the VM cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** [displayName](#API_CreateCloudVmCluster_RequestSyntax) **   <a name="odb-CreateCloudVmCluster-request-displayName"></a>
A user-friendly name for the VM cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_](?!.*--)[a-zA-Z0-9_-]*`
Required: Yes

 ** [giVersion](#API_CreateCloudVmCluster_RequestSyntax) **   <a name="odb-CreateCloudVmCluster-request-giVersion"></a>
A valid software version of Oracle Grid Infrastructure (GI). To get the list of valid values, use the `ListGiVersions` operation and specify the shape of the Exadata infrastructure.
Example: `19.0.0.0`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [hostname](#API_CreateCloudVmCluster_RequestSyntax) **   <a name="odb-CreateCloudVmCluster-request-hostname"></a>
The host name for the VM cluster.
Constraints:
+ Can't be "localhost" or "hostname".
+ Can't contain "-version".
+ The maximum length of the combined hostname and domain is 63 characters.
+ The hostname must be unique within the subnet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `[a-zA-Z][a-zA-Z0-9-]*[a-zA-Z0-9]`
Required: Yes

 ** [isLocalBackupEnabled](#API_CreateCloudVmCluster_RequestSyntax) **   <a name="odb-CreateCloudVmCluster-request-isLocalBackupEnabled"></a>
Specifies whether to enable database backups to local Exadata storage for the VM cluster.
Type: Boolean
Required: No

 ** [isSparseDiskgroupEnabled](#API_CreateCloudVmCluster_RequestSyntax) **   <a name="odb-CreateCloudVmCluster-request-isSparseDiskgroupEnabled"></a>
Specifies whether to create a sparse disk group for the VM cluster.
Type: Boolean
Required: No

 ** [licenseModel](#API_CreateCloudVmCluster_RequestSyntax) **   <a name="odb-CreateCloudVmCluster-request-licenseModel"></a>
The Oracle license model to apply to the VM cluster.
Default: `LICENSE_INCLUDED`
Type: String
Valid Values: `BRING_YOUR_OWN_LICENSE | LICENSE_INCLUDED`
Required: No

 ** [memorySizeInGBs](#API_CreateCloudVmCluster_RequestSyntax) **   <a name="odb-CreateCloudVmCluster-request-memorySizeInGBs"></a>
The amount of memory, in gigabytes (GBs), to allocate for the VM cluster.
Type: Integer
Required: No

 ** [odbNetworkId](#API_CreateCloudVmCluster_RequestSyntax) **   <a name="odb-CreateCloudVmCluster-request-odbNetworkId"></a>
The unique identifier of the ODB network for the VM cluster.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** [scanListenerPortTcp](#API_CreateCloudVmCluster_RequestSyntax) **   <a name="odb-CreateCloudVmCluster-request-scanListenerPortTcp"></a>
The port number for TCP connections to the single client access name (SCAN) listener.
Valid values: `1024–8999` with the following exceptions: `2484`, `6100`, `6200`, `7060`, `7070`, `7085`, and `7879`
Default: `1521`
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 8999.
Required: No

 ** [sshPublicKeys](#API_CreateCloudVmCluster_RequestSyntax) **   <a name="odb-CreateCloudVmCluster-request-sshPublicKeys"></a>
The public key portion of one or more key pairs used for SSH access to the VM cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: Yes

 ** [systemVersion](#API_CreateCloudVmCluster_RequestSyntax) **   <a name="odb-CreateCloudVmCluster-request-systemVersion"></a>
The version of the operating system of the image for the VM cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [tags](#API_CreateCloudVmCluster_RequestSyntax) **   <a name="odb-CreateCloudVmCluster-request-tags"></a>
The list of resource tags to apply to the VM cluster.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [timeZone](#API_CreateCloudVmCluster_RequestSyntax) **   <a name="odb-CreateCloudVmCluster-request-timeZone"></a>
The time zone for the VM cluster. For a list of valid values for time zone, you can check the options in the console.
Default: UTC
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## Response Syntax
<a name="API_CreateCloudVmCluster_ResponseSyntax"></a>

```
{
   "cloudVmClusterId": "string",
   "displayName": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_CreateCloudVmCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cloudVmClusterId](#API_CreateCloudVmCluster_ResponseSyntax) **   <a name="odb-CreateCloudVmCluster-response-cloudVmClusterId"></a>
The unique identifier for the VM cluster.
Type: String

 ** [displayName](#API_CreateCloudVmCluster_ResponseSyntax) **   <a name="odb-CreateCloudVmCluster-response-displayName"></a>
The user-friendly name for the VM cluster.
Type: String

 ** [status](#API_CreateCloudVmCluster_ResponseSyntax) **   <a name="odb-CreateCloudVmCluster-response-status"></a>
The current status of the VM cluster.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`

 ** [statusReason](#API_CreateCloudVmCluster_ResponseSyntax) **   <a name="odb-CreateCloudVmCluster-response-statusReason"></a>
Additional information about the status of the VM cluster.
Type: String

## Errors
<a name="API_CreateCloudVmCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.
HTTP Status Code: 400

 ** ConflictException **
Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.
 ** resourceId **
The identifier of the resource that caused the conflict.
 ** resourceType **
The type of resource that caused the conflict.
HTTP Status Code: 400

 ** InternalServerException **
Occurs when there is an internal failure in the Oracle Database@AWS service. Wait and try again.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of resource that was not found.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
You have exceeded the service quota.
 ** quotaCode **
The unqiue identifier of the service quota that was exceeded.
 ** resourceId **
The identifier of the resource that exceeded the service quota.
 ** resourceType **
The type of resource that exceeded the service quota.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after being throttled.
HTTP Status Code: 400

 ** ValidationException **
The request has failed validation because it is missing required fields or has invalid inputs.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason why the validation failed.
HTTP Status Code: 400

## See Also
<a name="API_CreateCloudVmCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/CreateCloudVmCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/CreateCloudVmCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/CreateCloudVmCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/CreateCloudVmCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/CreateCloudVmCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/CreateCloudVmCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/CreateCloudVmCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/CreateCloudVmCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/CreateCloudVmCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/CreateCloudVmCluster)
