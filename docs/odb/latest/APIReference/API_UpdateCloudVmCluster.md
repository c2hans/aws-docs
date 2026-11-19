---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_UpdateCloudVmCluster.html
---

# UpdateCloudVmCluster

Updates the properties of the specified VM cluster.

## Request Syntax
<a name="API_UpdateCloudVmCluster_RequestSyntax"></a>

```
{
   "cloudVmClusterId": "{{string}}",
   "cpuCoreCount": {{number}},
   "dataCollectionOptions": {
      "isDiagnosticsEventsEnabled": {{boolean}},
      "isHealthMonitoringEnabled": {{boolean}},
      "isIncidentLogsEnabled": {{boolean}}
   },
   "dataStorageSizeInTBs": {{number}},
   "dbNodeStorageSizeInGBs": {{number}},
   "displayName": "{{string}}",
   "licenseModel": "{{string}}",
   "memorySizeInGBs": {{number}},
   "sshPublicKeys": [ "{{string}}" ],
   "storageSizeInGBs": {{number}}
}
```

## Request Parameters
<a name="API_UpdateCloudVmCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cloudVmClusterId](#API_UpdateCloudVmCluster_RequestSyntax) **   <a name="odb-UpdateCloudVmCluster-request-cloudVmClusterId"></a>
The unique identifier of the VM cluster to update.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: Yes

 ** [cpuCoreCount](#API_UpdateCloudVmCluster_RequestSyntax) **   <a name="odb-UpdateCloudVmCluster-request-cpuCoreCount"></a>
The number of CPU cores to enable on the VM cluster. If you don't specify a value, the existing number of CPU cores is retained.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [dataCollectionOptions](#API_UpdateCloudVmCluster_RequestSyntax) **   <a name="odb-UpdateCloudVmCluster-request-dataCollectionOptions"></a>
The set of preferences for the diagnostic collection options for the VM cluster.
Type: [DataCollectionOptions](API_DataCollectionOptions.md) object
Required: No

 ** [dataStorageSizeInTBs](#API_UpdateCloudVmCluster_RequestSyntax) **   <a name="odb-UpdateCloudVmCluster-request-dataStorageSizeInTBs"></a>
The size of the data disk group, in terabytes (TB), to allocate for the VM cluster.
Type: Double
Valid Range: Minimum value of 0.
Required: No

 ** [dbNodeStorageSizeInGBs](#API_UpdateCloudVmCluster_RequestSyntax) **   <a name="odb-UpdateCloudVmCluster-request-dbNodeStorageSizeInGBs"></a>
The amount of local node storage, in gigabytes (GB), to allocate for the VM cluster.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [displayName](#API_UpdateCloudVmCluster_RequestSyntax) **   <a name="odb-UpdateCloudVmCluster-request-displayName"></a>
A new user-friendly name for the VM cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_](?!.*--)[a-zA-Z0-9_-]*`
Required: No

 ** [licenseModel](#API_UpdateCloudVmCluster_RequestSyntax) **   <a name="odb-UpdateCloudVmCluster-request-licenseModel"></a>
The Oracle license model to apply to the VM cluster.
Type: String
Valid Values: `BRING_YOUR_OWN_LICENSE | LICENSE_INCLUDED`
Required: No

 ** [memorySizeInGBs](#API_UpdateCloudVmCluster_RequestSyntax) **   <a name="odb-UpdateCloudVmCluster-request-memorySizeInGBs"></a>
The amount of memory, in gigabytes (GB), to allocate for the VM cluster.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [sshPublicKeys](#API_UpdateCloudVmCluster_RequestSyntax) **   <a name="odb-UpdateCloudVmCluster-request-sshPublicKeys"></a>
The public key portion of one or more key pairs used for SSH access to the VM cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** [storageSizeInGBs](#API_UpdateCloudVmCluster_RequestSyntax) **   <a name="odb-UpdateCloudVmCluster-request-storageSizeInGBs"></a>
The amount of local node storage, in gigabytes (GB), to allocate to the VM cluster.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## Response Syntax
<a name="API_UpdateCloudVmCluster_ResponseSyntax"></a>

```
{
   "cloudVmClusterId": "string",
   "displayName": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_UpdateCloudVmCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cloudVmClusterId](#API_UpdateCloudVmCluster_ResponseSyntax) **   <a name="odb-UpdateCloudVmCluster-response-cloudVmClusterId"></a>
The unique identifier of the updated VM cluster.
Type: String

 ** [displayName](#API_UpdateCloudVmCluster_ResponseSyntax) **   <a name="odb-UpdateCloudVmCluster-response-displayName"></a>
The user-friendly name of the updated VM cluster.
Type: String

 ** [status](#API_UpdateCloudVmCluster_ResponseSyntax) **   <a name="odb-UpdateCloudVmCluster-response-status"></a>
The current status of the VM cluster.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`

 ** [statusReason](#API_UpdateCloudVmCluster_ResponseSyntax) **   <a name="odb-UpdateCloudVmCluster-response-statusReason"></a>
Additional information about the current status of the VM cluster, if applicable.
Type: String

## Errors
<a name="API_UpdateCloudVmCluster_Errors"></a>

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
<a name="API_UpdateCloudVmCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/UpdateCloudVmCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/UpdateCloudVmCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/UpdateCloudVmCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/UpdateCloudVmCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/UpdateCloudVmCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/UpdateCloudVmCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/UpdateCloudVmCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/UpdateCloudVmCluster)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/UpdateCloudVmCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/UpdateCloudVmCluster)
