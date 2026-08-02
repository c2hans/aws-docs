---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateCloudAutonomousVmCluster.html
---

# CreateCloudAutonomousVmCluster
<a name="API_CreateCloudAutonomousVmCluster"></a>

Creates a new Autonomous VM cluster in the specified Exadata infrastructure.

## Request Syntax
<a name="API_CreateCloudAutonomousVmCluster_RequestSyntax"></a>

```
{
   "autonomousDataStorageSizeInTBs": {{number}},
   "clientToken": "{{string}}",
   "cloudExadataInfrastructureId": "{{string}}",
   "cpuCoreCountPerNode": {{number}},
   "dbServers": [ "{{string}}" ],
   "description": "{{string}}",
   "displayName": "{{string}}",
   "isMtlsEnabledVmCluster": {{boolean}},
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
   "memoryPerOracleComputeUnitInGBs": {{number}},
   "odbNetworkId": "{{string}}",
   "scanListenerPortNonTls": {{number}},
   "scanListenerPortTls": {{number}},
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "timeZone": "{{string}}",
   "totalContainerDatabases": {{number}}
}
```

## Request Parameters
<a name="API_CreateCloudAutonomousVmCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [autonomousDataStorageSizeInTBs](#API_CreateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-CreateCloudAutonomousVmCluster-request-autonomousDataStorageSizeInTBs"></a>
The data disk group size to be allocated for Autonomous Databases, in terabytes (TB).
Type: Double
Valid Range: Minimum value of 0.
Required: Yes

 ** [clientToken](#API_CreateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-CreateCloudAutonomousVmCluster-request-clientToken"></a>
A client-provided token to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 64.
Pattern: `[a-zA-Z0-9_\/.=-]+`
Required: No

 ** [cloudExadataInfrastructureId](#API_CreateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-CreateCloudAutonomousVmCluster-request-cloudExadataInfrastructureId"></a>
The unique identifier of the Exadata infrastructure where the VM cluster will be created.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** [cpuCoreCountPerNode](#API_CreateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-CreateCloudAutonomousVmCluster-request-cpuCoreCountPerNode"></a>
The number of CPU cores to be enabled per VM cluster node.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** [dbServers](#API_CreateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-CreateCloudAutonomousVmCluster-request-dbServers"></a>
The list of database servers to be used for the Autonomous VM cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** [description](#API_CreateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-CreateCloudAutonomousVmCluster-request-description"></a>
A user-provided description of the Autonomous VM cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.
Required: No

 ** [displayName](#API_CreateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-CreateCloudAutonomousVmCluster-request-displayName"></a>
The display name for the Autonomous VM cluster. The name does not need to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_](?!.*--)[a-zA-Z0-9_-]*`
Required: Yes

 ** [isMtlsEnabledVmCluster](#API_CreateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-CreateCloudAutonomousVmCluster-request-isMtlsEnabledVmCluster"></a>
Specifies whether to enable mutual TLS (mTLS) authentication for the Autonomous VM cluster.
Type: Boolean
Required: No

 ** [licenseModel](#API_CreateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-CreateCloudAutonomousVmCluster-request-licenseModel"></a>
The Oracle license model to apply to the Autonomous VM cluster.
Type: String
Valid Values: `BRING_YOUR_OWN_LICENSE | LICENSE_INCLUDED`
Required: No

 ** [maintenanceWindow](#API_CreateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-CreateCloudAutonomousVmCluster-request-maintenanceWindow"></a>
The scheduling details for the maintenance window. Patching and system updates take place during the maintenance window.
Type: [MaintenanceWindow](API_MaintenanceWindow.md) object
Required: No

 ** [memoryPerOracleComputeUnitInGBs](#API_CreateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-CreateCloudAutonomousVmCluster-request-memoryPerOracleComputeUnitInGBs"></a>
The amount of memory to be allocated per OCPU, in GB.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** [odbNetworkId](#API_CreateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-CreateCloudAutonomousVmCluster-request-odbNetworkId"></a>
The unique identifier of the ODB network to be used for the VM cluster.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** [scanListenerPortNonTls](#API_CreateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-CreateCloudAutonomousVmCluster-request-scanListenerPortNonTls"></a>
The SCAN listener port for non-TLS (TCP) protocol.
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 8999.
Required: No

 ** [scanListenerPortTls](#API_CreateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-CreateCloudAutonomousVmCluster-request-scanListenerPortTls"></a>
The SCAN listener port for TLS (TCP) protocol.
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 8999.
Required: No

 ** [tags](#API_CreateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-CreateCloudAutonomousVmCluster-request-tags"></a>
Free-form tags for this resource. Each tag is a key-value pair with no predefined name, type, or namespace.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [timeZone](#API_CreateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-CreateCloudAutonomousVmCluster-request-timeZone"></a>
The time zone to use for the Autonomous VM cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [totalContainerDatabases](#API_CreateCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-CreateCloudAutonomousVmCluster-request-totalContainerDatabases"></a>
The total number of Autonomous CDBs that you can create in the Autonomous VM cluster.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

## Response Syntax
<a name="API_CreateCloudAutonomousVmCluster_ResponseSyntax"></a>

```
{
   "cloudAutonomousVmClusterId": "string",
   "displayName": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_CreateCloudAutonomousVmCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cloudAutonomousVmClusterId](#API_CreateCloudAutonomousVmCluster_ResponseSyntax) **   <a name="odb-CreateCloudAutonomousVmCluster-response-cloudAutonomousVmClusterId"></a>
The unique identifier of the created Autonomous VM cluster.
Type: String

 ** [displayName](#API_CreateCloudAutonomousVmCluster_ResponseSyntax) **   <a name="odb-CreateCloudAutonomousVmCluster-response-displayName"></a>
The display name of the created Autonomous VM cluster.
Type: String

 ** [status](#API_CreateCloudAutonomousVmCluster_ResponseSyntax) **   <a name="odb-CreateCloudAutonomousVmCluster-response-status"></a>
The current status of the Autonomous VM cluster creation process.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`

 ** [statusReason](#API_CreateCloudAutonomousVmCluster_ResponseSyntax) **   <a name="odb-CreateCloudAutonomousVmCluster-response-statusReason"></a>
Additional information about the current status of the Autonomous VM cluster creation process, if applicable.
Type: String

## Errors
<a name="API_CreateCloudAutonomousVmCluster_Errors"></a>

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
<a name="API_CreateCloudAutonomousVmCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/CreateCloudAutonomousVmCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/CreateCloudAutonomousVmCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/CreateCloudAutonomousVmCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/CreateCloudAutonomousVmCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/CreateCloudAutonomousVmCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/CreateCloudAutonomousVmCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/CreateCloudAutonomousVmCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/CreateCloudAutonomousVmCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/CreateCloudAutonomousVmCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/CreateCloudAutonomousVmCluster)
