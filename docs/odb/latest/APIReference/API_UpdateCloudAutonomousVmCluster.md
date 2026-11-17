---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_UpdateCloudAutonomousVmCluster.html
---

# UpdateCloudAutonomousVmCluster
<a name="API_UpdateCloudAutonomousVmCluster"></a>

Updates the properties of the specified Autonomous VM cluster.

## Request Syntax
<a name="API_UpdateCloudAutonomousVmCluster_RequestSyntax"></a>

```
{
   "autonomousDataStorageSizeInTBs": {{number}},
   "cloudAutonomousVmClusterId": "{{string}}",
   "cpuCoreCountPerNode": {{number}},
   "description": "{{string}}",
   "displayName": "{{string}}",
   "licenseModel": "{{string}}",
   "maintenanceWindow": {
      "customActionTimeoutInMins": {{number}},
      "daysOfWeek": [
         {
            "name": "{{string}}"
         }
      ],
      "hoursOfDay": [ {{number}} ],
      "isCustomActionTimeoutEnabled": {{boolean}},
      "leadTimeInWeeks": {{number}},
      "months": [
         {
            "name": "{{string}}"
         }
      ],
      "patchingMode": "{{string}}",
      "preference": "{{string}}",
      "skipRu": {{boolean}},
      "weeksOfMonth": [ {{number}} ]
   },
   "totalContainerDatabases": {{number}}
}
```

## Request Parameters
<a name="API_UpdateCloudAutonomousVmCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [autonomousDataStorageSizeInTBs](#API_UpdateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-UpdateCloudAutonomousVmCluster-request-autonomousDataStorageSizeInTBs"></a>
The data storage size to allocate for Autonomous Databases in the Autonomous VM cluster, in terabytes (TB).
Type: Double
Valid Range: Minimum value of 0.
Required: No

 ** [cloudAutonomousVmClusterId](#API_UpdateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-UpdateCloudAutonomousVmCluster-request-cloudAutonomousVmClusterId"></a>
The unique identifier of the Autonomous VM cluster to update.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: Yes

 ** [cpuCoreCountPerNode](#API_UpdateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-UpdateCloudAutonomousVmCluster-request-cpuCoreCountPerNode"></a>
The number of CPU cores to enable per node in the Autonomous VM cluster. If you don't specify a value, the existing number of CPU cores per node is retained.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [description](#API_UpdateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-UpdateCloudAutonomousVmCluster-request-description"></a>
A user-provided description of the Autonomous VM cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.
Required: No

 ** [displayName](#API_UpdateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-UpdateCloudAutonomousVmCluster-request-displayName"></a>
A new user-friendly name for the Autonomous VM cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_](?!.*--)[a-zA-Z0-9_-]*`
Required: No

 ** [licenseModel](#API_UpdateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-UpdateCloudAutonomousVmCluster-request-licenseModel"></a>
The Oracle license model to apply to the Autonomous VM cluster.
Type: String
Valid Values: `BRING_YOUR_OWN_LICENSE | LICENSE_INCLUDED`
Required: No

 ** [maintenanceWindow](#API_UpdateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-UpdateCloudAutonomousVmCluster-request-maintenanceWindow"></a>
The scheduling details for the maintenance window. Patching and system updates take place during the maintenance window.
Type: [MaintenanceWindow](API_MaintenanceWindow.md) object
Required: No

 ** [totalContainerDatabases](#API_UpdateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-UpdateCloudAutonomousVmCluster-request-totalContainerDatabases"></a>
The total number of Autonomous Container Databases that can be created in the Autonomous VM cluster.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## Response Syntax
<a name="API_UpdateCloudAutonomousVmCluster_ResponseSyntax"></a>

```
{
   "cloudAutonomousVmClusterId": "string",
   "displayName": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_UpdateCloudAutonomousVmCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cloudAutonomousVmClusterId](#API_UpdateCloudAutonomousVmCluster_ResponseSyntax) **   <a name="odb-UpdateCloudAutonomousVmCluster-response-cloudAutonomousVmClusterId"></a>
The unique identifier of the updated Autonomous VM cluster.
Type: String

 ** [displayName](#API_UpdateCloudAutonomousVmCluster_ResponseSyntax) **   <a name="odb-UpdateCloudAutonomousVmCluster-response-displayName"></a>
The user-friendly name of the updated Autonomous VM cluster.
Type: String

 ** [status](#API_UpdateCloudAutonomousVmCluster_ResponseSyntax) **   <a name="odb-UpdateCloudAutonomousVmCluster-response-status"></a>
The current status of the Autonomous VM cluster.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`

 ** [statusReason](#API_UpdateCloudAutonomousVmCluster_ResponseSyntax) **   <a name="odb-UpdateCloudAutonomousVmCluster-response-statusReason"></a>
Additional information about the current status of the Autonomous VM cluster, if applicable.
Type: String

## Errors
<a name="API_UpdateCloudAutonomousVmCluster_Errors"></a>

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
<a name="API_UpdateCloudAutonomousVmCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/UpdateCloudAutonomousVmCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/UpdateCloudAutonomousVmCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/UpdateCloudAutonomousVmCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/UpdateCloudAutonomousVmCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/UpdateCloudAutonomousVmCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/UpdateCloudAutonomousVmCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/UpdateCloudAutonomousVmCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/UpdateCloudAutonomousVmCluster)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/UpdateCloudAutonomousVmCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/UpdateCloudAutonomousVmCluster)
