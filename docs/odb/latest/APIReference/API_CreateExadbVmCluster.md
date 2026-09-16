---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateExadbVmCluster.html
---

# CreateExadbVmCluster
<a name="API_CreateExadbVmCluster"></a>

Creates an Exascale VM cluster.

## Request Syntax
<a name="API_CreateExadbVmCluster_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "clusterName": "{{string}}",
   "dataCollectionOptions": {
      "isDiagnosticsEventsEnabled": {{boolean}},
      "isHealthMonitoringEnabled": {{boolean}},
      "isIncidentLogsEnabled": {{boolean}}
   },
   "displayName": "{{string}}",
   "enabledEcpuCount": {{number}},
   "exascaleDbStorageVaultId": "{{string}}",
   "gridImageId": "{{string}}",
   "hostname": "{{string}}",
   "licenseModel": "{{string}}",
   "nodeCount": {{number}},
   "odbNetworkId": "{{string}}",
   "scanListenerPortTcp": {{number}},
   "scanListenerPortTcpSsl": {{number}},
   "shape": "{{string}}",
   "shapeAttribute": "{{string}}",
   "sshPublicKeys": [ "{{string}}" ],
   "systemVersion": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "timeZone": "{{string}}",
   "totalEcpuCount": {{number}},
   "vmFileSystemStorageTotalSizeInGBs": {{number}}
}
```

## Request Parameters
<a name="API_CreateExadbVmCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateExadbVmCluster_RequestSyntax) **   <a name="odb-CreateExadbVmCluster-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, the Amazon Web Services SDK automatically generates one and uses it for the request to ensure idempotency. The client token is valid for up to 24 hours after it's first used.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 64.
Pattern: `[a-zA-Z0-9_\/.=-]+`
Required: No

 ** [clusterName](#API_CreateExadbVmCluster_RequestSyntax) **   <a name="odb-CreateExadbVmCluster-request-clusterName"></a>
A name for the Grid Infrastructure cluster. The name isn't case sensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 11.
Pattern: `[a-zA-Z][a-zA-Z0-9-]*`
Required: No

 ** [dataCollectionOptions](#API_CreateExadbVmCluster_RequestSyntax) **   <a name="odb-CreateExadbVmCluster-request-dataCollectionOptions"></a>
The set of preferences for the various diagnostic collection options for the Exascale VM cluster.
Type: [DataCollectionOptions](API_DataCollectionOptions.md) object
Required: No

 ** [displayName](#API_CreateExadbVmCluster_RequestSyntax) **   <a name="odb-CreateExadbVmCluster-request-displayName"></a>
A user-friendly name for the Exascale VM cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_](?!.*--)[a-zA-Z0-9_-]*`
Required: Yes

 ** [enabledEcpuCount](#API_CreateExadbVmCluster_RequestSyntax) **   <a name="odb-CreateExadbVmCluster-request-enabledEcpuCount"></a>
The number of ECPUs to enable for the Exascale VM cluster.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** [exascaleDbStorageVaultId](#API_CreateExadbVmCluster_RequestSyntax) **   <a name="odb-CreateExadbVmCluster-request-exascaleDbStorageVaultId"></a>
The unique identifier of the Exascale storage vault for this Exascale VM cluster.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** [gridImageId](#API_CreateExadbVmCluster_RequestSyntax) **   <a name="odb-CreateExadbVmCluster-request-gridImageId"></a>
The Grid Infrastructure software image ID for the Exascale VM cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [hostname](#API_CreateExadbVmCluster_RequestSyntax) **   <a name="odb-CreateExadbVmCluster-request-hostname"></a>
The host name for the Exascale VM cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `[a-zA-Z][a-zA-Z0-9-]*[a-zA-Z0-9]`
Required: Yes

 ** [licenseModel](#API_CreateExadbVmCluster_RequestSyntax) **   <a name="odb-CreateExadbVmCluster-request-licenseModel"></a>
The Oracle license model to apply to the Exascale VM cluster.
Type: String
Valid Values: `BRING_YOUR_OWN_LICENSE | LICENSE_INCLUDED`
Required: No

 ** [nodeCount](#API_CreateExadbVmCluster_RequestSyntax) **   <a name="odb-CreateExadbVmCluster-request-nodeCount"></a>
The number of nodes in the Exascale VM cluster.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** [odbNetworkId](#API_CreateExadbVmCluster_RequestSyntax) **   <a name="odb-CreateExadbVmCluster-request-odbNetworkId"></a>
The unique identifier of the ODB network for the Exascale VM cluster.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** [scanListenerPortTcp](#API_CreateExadbVmCluster_RequestSyntax) **   <a name="odb-CreateExadbVmCluster-request-scanListenerPortTcp"></a>
The port number for TCP connections to the single client access name (SCAN) listener.
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 8999.
Required: No

 ** [scanListenerPortTcpSsl](#API_CreateExadbVmCluster_RequestSyntax) **   <a name="odb-CreateExadbVmCluster-request-scanListenerPortTcpSsl"></a>
The port number for TCP connections with SSL to the single client access name (SCAN) listener.
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 8999.
Required: No

 ** [shape](#API_CreateExadbVmCluster_RequestSyntax) **   <a name="odb-CreateExadbVmCluster-request-shape"></a>
The shape of the Exascale VM cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [shapeAttribute](#API_CreateExadbVmCluster_RequestSyntax) **   <a name="odb-CreateExadbVmCluster-request-shapeAttribute"></a>
The shape attribute for the Exascale VM cluster.
Type: String
Valid Values: `SMART_STORAGE | BLOCK_STORAGE`
Required: No

 ** [sshPublicKeys](#API_CreateExadbVmCluster_RequestSyntax) **   <a name="odb-CreateExadbVmCluster-request-sshPublicKeys"></a>
The public key portion of one or more key pairs used for SSH access to the Exascale VM cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: Yes

 ** [systemVersion](#API_CreateExadbVmCluster_RequestSyntax) **   <a name="odb-CreateExadbVmCluster-request-systemVersion"></a>
The version of the operating system of the image for the Exascale VM cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [tags](#API_CreateExadbVmCluster_RequestSyntax) **   <a name="odb-CreateExadbVmCluster-request-tags"></a>
The list of resource tags to apply to the Exascale VM cluster.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [timeZone](#API_CreateExadbVmCluster_RequestSyntax) **   <a name="odb-CreateExadbVmCluster-request-timeZone"></a>
The time zone for the Exascale VM cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [totalEcpuCount](#API_CreateExadbVmCluster_RequestSyntax) **   <a name="odb-CreateExadbVmCluster-request-totalEcpuCount"></a>
The total number of ECPUs for the Exascale VM cluster.
Type: Integer
Valid Range: Minimum value of 2.
Required: Yes

 ** [vmFileSystemStorageTotalSizeInGBs](#API_CreateExadbVmCluster_RequestSyntax) **   <a name="odb-CreateExadbVmCluster-request-vmFileSystemStorageTotalSizeInGBs"></a>
The total amount of file system storage, in gigabytes (GB), for the Exascale VM cluster.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

## Response Syntax
<a name="API_CreateExadbVmCluster_ResponseSyntax"></a>

```
{
   "displayName": "string",
   "exadbVmClusterId": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_CreateExadbVmCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [displayName](#API_CreateExadbVmCluster_ResponseSyntax) **   <a name="odb-CreateExadbVmCluster-response-displayName"></a>
The user-friendly name for the Exascale VM cluster.
Type: String

 ** [exadbVmClusterId](#API_CreateExadbVmCluster_ResponseSyntax) **   <a name="odb-CreateExadbVmCluster-response-exadbVmClusterId"></a>
The unique identifier of the Exascale VM cluster.
Type: String

 ** [status](#API_CreateExadbVmCluster_ResponseSyntax) **   <a name="odb-CreateExadbVmCluster-response-status"></a>
The current status of the Exascale VM cluster.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`

 ** [statusReason](#API_CreateExadbVmCluster_ResponseSyntax) **   <a name="odb-CreateExadbVmCluster-response-statusReason"></a>
Additional information about the status of the Exascale VM cluster.
Type: String

## Errors
<a name="API_CreateExadbVmCluster_Errors"></a>

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
<a name="API_CreateExadbVmCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/CreateExadbVmCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/CreateExadbVmCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/CreateExadbVmCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/CreateExadbVmCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/CreateExadbVmCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/CreateExadbVmCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/CreateExadbVmCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/CreateExadbVmCluster)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/CreateExadbVmCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/CreateExadbVmCluster)
