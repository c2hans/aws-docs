---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_ListAutonomousDatabaseClones.html
---

# ListAutonomousDatabaseClones
<a name="API_ListAutonomousDatabaseClones"></a>

Lists the clones of the specified Autonomous Database.

## Request Syntax
<a name="API_ListAutonomousDatabaseClones_RequestSyntax"></a>

```
{
   "autonomousDatabaseId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAutonomousDatabaseClones_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [autonomousDatabaseId](#API_ListAutonomousDatabaseClones_RequestSyntax) **   <a name="odb-ListAutonomousDatabaseClones-request-autonomousDatabaseId"></a>
The unique identifier of the source Autonomous Database whose clones you want to list.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** [maxResults](#API_ListAutonomousDatabaseClones_RequestSyntax) **   <a name="odb-ListAutonomousDatabaseClones-request-maxResults"></a>
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListAutonomousDatabaseClones_RequestSyntax) **   <a name="odb-ListAutonomousDatabaseClones-request-nextToken"></a>
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

## Response Syntax
<a name="API_ListAutonomousDatabaseClones_ResponseSyntax"></a>

```
{
   "autonomousDatabaseClones": [
      {
         "actualUsedDataStorageSizeInTBs": number,
         "adminPasswordSourceSummary": {
            "adminPasswordSource": "string",
            "adminPasswordSourceConfiguration": { ... }
         },
         "allocatedStorageSizeInTBs": number,
         "allowlistedIps": [ "string" ],
         "apexDetails": {
            "apexVersion": "string",
            "ordsVersion": "string"
         },
         "autonomousDatabaseArn": "string",
         "autonomousDatabaseId": "string",
         "autonomousMaintenanceScheduleType": "string",
         "autoRefreshFrequencyInSeconds": number,
         "autoRefreshPointLagInSeconds": number,
         "availabilityZone": "string",
         "availabilityZoneId": "string",
         "availableUpgradeVersions": [ "string" ],
         "backupRetentionPeriodInDays": number,
         "byolComputeCountLimit": number,
         "characterSet": "string",
         "cloneTableSpaceList": [ number ],
         "computeCount": number,
         "computeModel": "string",
         "connectionStringDetails": {
            "allConnectionStrings": {
               "string" : "string"
            },
            "dedicated": "string",
            "high": "string",
            "low": "string",
            "medium": "string",
            "profiles": [
               {
                  "consumerGroup": "string",
                  "displayName": "string",
                  "hostFormat": "string",
                  "isRegional": boolean,
                  "protocol": "string",
                  "sessionMode": "string",
                  "syntaxFormat": "string",
                  "tlsAuthentication": "string",
                  "value": "string"
               }
            ]
         },
         "connectionUrls": {
            "apexUrl": "string",
            "databaseTransformsUrl": "string",
            "graphStudioUrl": "string",
            "machineLearningNotebookUrl": "string",
            "machineLearningUserManagementUrl": "string",
            "mongoDbUrl": "string",
            "ordsUrl": "string",
            "spatialStudioUrl": "string",
            "sqlDevWebUrl": "string"
         },
         "cpuCoreCount": number,
         "createdAt": "string",
         "customerContacts": [
            {
               "email": "string"
            }
         ],
         "databaseEdition": "string",
         "databaseManagementStatus": "string",
         "databaseType": "string",
         "dataSafeStatus": "string",
         "dataStorageSizeInGBs": number,
         "dataStorageSizeInTBs": number,
         "dbName": "string",
         "dbToolsDetails": [
            {
               "computeCount": number,
               "isEnabled": boolean,
               "maxIdleTimeInMinutes": number,
               "name": "string"
            }
         ],
         "dbVersion": "string",
         "dbWorkload": "string",
         "displayName": "string",
         "encryptionSummary": {
            "encryptionKeyConfiguration": { ... },
            "encryptionKeyProvider": "string"
         },
         "failedDataRecoveryInSeconds": number,
         "inMemoryAreaInGBs": number,
         "isAutoScalingEnabled": boolean,
         "isAutoScalingForStorageEnabled": boolean,
         "isBackupRetentionLocked": boolean,
         "isLocalDataGuardEnabled": boolean,
         "isMtlsConnectionRequired": boolean,
         "isReconnectCloneEnabled": boolean,
         "isRefreshableClone": boolean,
         "isRemoteDataGuardEnabled": boolean,
         "licenseModel": "string",
         "localAdgAutoFailoverMaxDataLossLimit": number,
         "localDisasterRecoveryType": "string",
         "localStandbyDb": {
            "availabilityDomain": "string",
            "lagTimeInSeconds": number,
            "maintenanceTargetComponent": "string",
            "status": "string",
            "statusReason": "string",
            "timeDataGuardRoleChanged": "string",
            "timeDisasterRecoveryRoleChanged": "string",
            "timeMaintenanceBegin": "string",
            "timeMaintenanceEnd": "string"
         },
         "longTermBackupSchedule": {
            "isDisabled": boolean,
            "repeatCadence": "string",
            "retentionPeriodInDays": number,
            "timeOfBackup": "string"
         },
         "maintenanceTargetComponent": "string",
         "memoryPerOracleComputeUnitInGBs": number,
         "ncharacterSet": "string",
         "netServicesArchitecture": "string",
         "nextLongTermBackupTimeStamp": "string",
         "ocid": "string",
         "ociResourceAnchorName": "string",
         "ociUrl": "string",
         "odbNetworkArn": "string",
         "odbNetworkId": "string",
         "openMode": "string",
         "operationsInsightsStatus": "string",
         "peerDbIds": [ "string" ],
         "percentProgress": number,
         "permissionLevel": "string",
         "privateEndpoint": "string",
         "privateEndpointIp": "string",
         "privateEndpointLabel": "string",
         "provisionableCpus": [ number ],
         "refreshableMode": "string",
         "refreshableStatus": "string",
         "remoteDisasterRecoveryConfiguration": {
            "disasterRecoveryType": "string",
            "isReplicateAutomaticBackups": boolean,
            "isSnapshotStandby": boolean,
            "timeSnapshotStandbyEnabledTill": "string"
         },
         "resourcePoolLeaderId": "string",
         "resourcePoolSummary": {
            "availableComputeCapacity": number,
            "availableStorageCapacityInTBs": number,
            "isDisabled": boolean,
            "poolSize": number,
            "poolStorageSizeInTBs": number,
            "totalComputeCapacity": number
         },
         "role": "string",
         "scheduledOperations": [
            {
               "dayOfWeek": {
                  "name": "string"
               },
               "scheduledStartTime": "string",
               "scheduledStopTime": "string"
            }
         ],
         "serviceConsoleUrl": "string",
         "sourceId": "string",
         "sqlWebDeveloperUrl": "string",
         "standbyAllowlistedIps": [ "string" ],
         "standbyAllowlistedIpsSource": "string",
         "standbyDb": {
            "availabilityDomain": "string",
            "lagTimeInSeconds": number,
            "maintenanceTargetComponent": "string",
            "status": "string",
            "statusReason": "string",
            "timeDataGuardRoleChanged": "string",
            "timeDisasterRecoveryRoleChanged": "string",
            "timeMaintenanceBegin": "string",
            "timeMaintenanceEnd": "string"
         },
         "status": "string",
         "statusReason": "string",
         "timeDataGuardRoleChanged": "string",
         "timeDeletionOfFreeAutonomousDatabase": "string",
         "timeDisasterRecoveryRoleChanged": "string",
         "timeLocalDataGuardEnabled": "string",
         "timeMaintenanceBegin": "string",
         "timeMaintenanceEnd": "string",
         "timeOfAutoRefreshStart": "string",
         "timeOfLastBackup": "string",
         "timeOfLastFailover": "string",
         "timeOfLastRefresh": "string",
         "timeOfLastRefreshPoint": "string",
         "timeOfLastSwitchover": "string",
         "timeOfNextRefresh": "string",
         "timeReclamationOfFreeAutonomousDatabase": "string",
         "timeUndeleted": "string",
         "timeUntilReconnectCloneEnabled": "string",
         "totalBackupStorageSizeInGBs": number,
         "usedDataStorageSizeInGBs": number,
         "usedDataStorageSizeInTBs": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAutonomousDatabaseClones_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [autonomousDatabaseClones](#API_ListAutonomousDatabaseClones_ResponseSyntax) **   <a name="odb-ListAutonomousDatabaseClones-response-autonomousDatabaseClones"></a>
The list of Autonomous Database clones along with their properties.
Type: Array of [AutonomousDatabaseSummary](API_AutonomousDatabaseSummary.md) objects

 ** [nextToken](#API_ListAutonomousDatabaseClones_ResponseSyntax) **   <a name="odb-ListAutonomousDatabaseClones-response-nextToken"></a>
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

## Errors
<a name="API_ListAutonomousDatabaseClones_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.
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
<a name="API_ListAutonomousDatabaseClones_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/ListAutonomousDatabaseClones)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/ListAutonomousDatabaseClones)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/ListAutonomousDatabaseClones)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/ListAutonomousDatabaseClones)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/ListAutonomousDatabaseClones)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/ListAutonomousDatabaseClones)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/ListAutonomousDatabaseClones)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/ListAutonomousDatabaseClones)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/ListAutonomousDatabaseClones)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/ListAutonomousDatabaseClones)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
