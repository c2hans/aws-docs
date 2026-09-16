---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_UpdateExadbVmCluster.html
---

# UpdateExadbVmCluster
<a name="API_UpdateExadbVmCluster"></a>

Updates the specified Exascale VM cluster.

## Request Syntax
<a name="API_UpdateExadbVmCluster_RequestSyntax"></a>

```
{
   "dataCollectionOptions": {
      "isDiagnosticsEventsEnabled": {{boolean}},
      "isHealthMonitoringEnabled": {{boolean}},
      "isIncidentLogsEnabled": {{boolean}}
   },
   "displayName": "{{string}}",
   "enabledEcpuCount": {{number}},
   "exadbVmClusterId": "{{string}}",
   "gridImageId": "{{string}}",
   "licenseModel": "{{string}}",
   "sshPublicKeys": [ "{{string}}" ],
   "systemVersion": "{{string}}",
   "totalEcpuCount": {{number}},
   "updateAction": "{{string}}",
   "vmFileSystemStorageTotalSizeInGBs": {{number}}
}
```

## Request Parameters
<a name="API_UpdateExadbVmCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [dataCollectionOptions](#API_UpdateExadbVmCluster_RequestSyntax) **   <a name="odb-UpdateExadbVmCluster-request-dataCollectionOptions"></a>
The set of preferences for the various diagnostic collection options for the Exascale VM cluster.
Type: [DataCollectionOptions](API_DataCollectionOptions.md) object
Required: No

 ** [displayName](#API_UpdateExadbVmCluster_RequestSyntax) **   <a name="odb-UpdateExadbVmCluster-request-displayName"></a>
A new user-friendly name for the Exascale VM cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_](?!.*--)[a-zA-Z0-9_-]*`
Required: No

 ** [enabledEcpuCount](#API_UpdateExadbVmCluster_RequestSyntax) **   <a name="odb-UpdateExadbVmCluster-request-enabledEcpuCount"></a>
The number of ECPUs to enable for the Exascale VM cluster.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [exadbVmClusterId](#API_UpdateExadbVmCluster_RequestSyntax) **   <a name="odb-UpdateExadbVmCluster-request-exadbVmClusterId"></a>
The unique identifier of the Exascale VM cluster to update.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** [gridImageId](#API_UpdateExadbVmCluster_RequestSyntax) **   <a name="odb-UpdateExadbVmCluster-request-gridImageId"></a>
The Grid Infrastructure software image ID for the Exascale VM cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [licenseModel](#API_UpdateExadbVmCluster_RequestSyntax) **   <a name="odb-UpdateExadbVmCluster-request-licenseModel"></a>
The Oracle license model to apply to the Exascale VM cluster.
Type: String
Valid Values: `BRING_YOUR_OWN_LICENSE | LICENSE_INCLUDED`
Required: No

 ** [sshPublicKeys](#API_UpdateExadbVmCluster_RequestSyntax) **   <a name="odb-UpdateExadbVmCluster-request-sshPublicKeys"></a>
The public key portion of one or more key pairs used for SSH access to the Exascale VM cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** [systemVersion](#API_UpdateExadbVmCluster_RequestSyntax) **   <a name="odb-UpdateExadbVmCluster-request-systemVersion"></a>
The version of the operating system of the image for the Exascale VM cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [totalEcpuCount](#API_UpdateExadbVmCluster_RequestSyntax) **   <a name="odb-UpdateExadbVmCluster-request-totalEcpuCount"></a>
The total number of ECPUs for the Exascale VM cluster.
Type: Integer
Valid Range: Minimum value of 2.
Required: No

 ** [updateAction](#API_UpdateExadbVmCluster_RequestSyntax) **   <a name="odb-UpdateExadbVmCluster-request-updateAction"></a>
The update action to perform on the Exascale VM cluster.
Type: String
Valid Values: `ROLLING_APPLY | NON_ROLLING_APPLY | PRECHECK | ROLLBACK`
Required: No

 ** [vmFileSystemStorageTotalSizeInGBs](#API_UpdateExadbVmCluster_RequestSyntax) **   <a name="odb-UpdateExadbVmCluster-request-vmFileSystemStorageTotalSizeInGBs"></a>
The total amount of file system storage, in gigabytes (GB), for the Exascale VM cluster.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## Response Syntax
<a name="API_UpdateExadbVmCluster_ResponseSyntax"></a>

```
{
   "displayName": "string",
   "exadbVmClusterId": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_UpdateExadbVmCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [displayName](#API_UpdateExadbVmCluster_ResponseSyntax) **   <a name="odb-UpdateExadbVmCluster-response-displayName"></a>
The user-friendly name for the Exascale VM cluster.
Type: String

 ** [exadbVmClusterId](#API_UpdateExadbVmCluster_ResponseSyntax) **   <a name="odb-UpdateExadbVmCluster-response-exadbVmClusterId"></a>
The unique identifier of the Exascale VM cluster.
Type: String

 ** [status](#API_UpdateExadbVmCluster_ResponseSyntax) **   <a name="odb-UpdateExadbVmCluster-response-status"></a>
The current status of the Exascale VM cluster.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`

 ** [statusReason](#API_UpdateExadbVmCluster_ResponseSyntax) **   <a name="odb-UpdateExadbVmCluster-response-statusReason"></a>
Additional information about the status of the Exascale VM cluster.
Type: String

## Errors
<a name="API_UpdateExadbVmCluster_Errors"></a>

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
<a name="API_UpdateExadbVmCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/UpdateExadbVmCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/UpdateExadbVmCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/UpdateExadbVmCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/UpdateExadbVmCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/UpdateExadbVmCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/UpdateExadbVmCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/UpdateExadbVmCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/UpdateExadbVmCluster)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/UpdateExadbVmCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/UpdateExadbVmCluster)
