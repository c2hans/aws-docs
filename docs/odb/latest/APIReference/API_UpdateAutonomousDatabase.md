---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_UpdateAutonomousDatabase.html
---

# UpdateAutonomousDatabase
<a name="API_UpdateAutonomousDatabase"></a>

Updates the properties of an Autonomous Database.

## Request Syntax
<a name="API_UpdateAutonomousDatabase_RequestSyntax"></a>

```
{
   "adminPassword": "{{string}}",
   "adminPasswordSource": "{{string}}",
   "adminPasswordSourceConfiguration": { ... },
   "allowlistedIps": [ "{{string}}" ],
   "autonomousDatabaseId": "{{string}}",
   "autonomousMaintenanceScheduleType": "{{string}}",
   "autoRefreshFrequencyInSeconds": {{number}},
   "autoRefreshPointLagInSeconds": {{number}},
   "backupRetentionPeriodInDays": {{number}},
   "byolComputeCountLimit": {{number}},
   "computeCount": {{number}},
   "cpuCoreCount": {{number}},
   "customerContactsToSendToOCI": [
      {
         "email": "{{string}}"
      }
   ],
   "databaseEdition": "{{string}}",
   "dataStorageSizeInGBs": {{number}},
   "dataStorageSizeInTBs": {{number}},
   "dbName": "{{string}}",
   "dbToolsDetails": [
      {
         "computeCount": {{number}},
         "isEnabled": {{boolean}},
         "maxIdleTimeInMinutes": {{number}},
         "name": "{{string}}"
      }
   ],
   "dbVersion": "{{string}}",
   "dbWorkload": "{{string}}",
   "displayName": "{{string}}",
   "encryptionKeyConfiguration": { ... },
   "encryptionKeyProvider": "{{string}}",
   "isAutoScalingEnabled": {{boolean}},
   "isAutoScalingForStorageEnabled": {{boolean}},
   "isBackupRetentionLocked": {{boolean}},
   "isDisconnectPeer": {{boolean}},
   "isLocalDataGuardEnabled": {{boolean}},
   "isMtlsConnectionRequired": {{boolean}},
   "isRefreshableClone": {{boolean}},
   "licenseModel": "{{string}}",
   "localAdgAutoFailoverMaxDataLossLimit": {{number}},
   "longTermBackupSchedule": {
      "isDisabled": {{boolean}},
      "repeatCadence": "{{string}}",
      "retentionPeriodInDays": {{number}},
      "timeOfBackup": "{{string}}"
   },
   "openMode": "{{string}}",
   "peerDbId": "{{string}}",
   "permissionLevel": "{{string}}",
   "privateEndpointIp": "{{string}}",
   "privateEndpointLabel": "{{string}}",
   "refreshableMode": "{{string}}",
   "resourcePoolLeaderId": "{{string}}",
   "resourcePoolSummary": {
      "availableComputeCapacity": {{number}},
      "availableStorageCapacityInTBs": {{number}},
      "isDisabled": {{boolean}},
      "poolSize": {{number}},
      "poolStorageSizeInTBs": {{number}},
      "totalComputeCapacity": {{number}}
   },
   "scheduledOperations": [
      {
         "dayOfWeek": {
            "name": "{{string}}"
         },
         "scheduledStartTime": "{{string}}",
         "scheduledStopTime": "{{string}}"
      }
   ],
   "standbyAllowlistedIps": [ "{{string}}" ],
   "standbyAllowlistedIpsSource": "{{string}}",
   "timeOfAutoRefreshStart": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateAutonomousDatabase_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [adminPassword](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-adminPassword"></a>
The new password for the `ADMIN` user of the Autonomous Database.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 30.
Required: No

 ** [adminPasswordSource](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-adminPasswordSource"></a>
The source of the admin password for the Autonomous Database. When set to `CUSTOMER_MANAGED_AWS_SECRET`, the admin password is retrieved from an AWS Secrets Manager secret.
Type: String
Valid Values: `CUSTOMER_MANAGED_AWS_SECRET | API_REQUEST_PARAMETER`
Required: No

 ** [adminPasswordSourceConfiguration](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-adminPasswordSourceConfiguration"></a>
The configuration of the admin password source for the Autonomous Database.
Type: [AdminPasswordSourceConfigurationInput](API_AdminPasswordSourceConfigurationInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [allowlistedIps](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-allowlistedIps"></a>
The list of IP addresses that are allowed to access the Autonomous Database.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** [autonomousDatabaseId](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-autonomousDatabaseId"></a>
The unique identifier of the Autonomous Database to update.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** [autonomousMaintenanceScheduleType](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-autonomousMaintenanceScheduleType"></a>
The maintenance schedule type for the Autonomous Database.
Type: String
Valid Values: `EARLY | REGULAR`
Required: No

 ** [autoRefreshFrequencyInSeconds](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-autoRefreshFrequencyInSeconds"></a>
The frequency, in seconds, at which the refreshable clone Autonomous Database is automatically refreshed.
Type: Integer
Valid Range: Minimum value of 3600. Maximum value of 604800.
Required: No

 ** [autoRefreshPointLagInSeconds](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-autoRefreshPointLagInSeconds"></a>
The time lag, in seconds, between the refreshable clone and its source Autonomous Database.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 604800.
Required: No

 ** [backupRetentionPeriodInDays](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-backupRetentionPeriodInDays"></a>
The retention period, in days, for automatic backups of the Autonomous Database.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 60.
Required: No

 ** [byolComputeCountLimit](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-byolComputeCountLimit"></a>
The maximum number of compute resources that you can allocate to the Autonomous Database under the bring-your-own-license (BYOL) model.
Type: Double
Valid Range: Minimum value of 2.
Required: No

 ** [computeCount](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-computeCount"></a>
The compute capacity, in number of ECPUs or OCPUs, to assign to the Autonomous Database.
Type: Double
Valid Range: Minimum value of 0.1. Maximum value of 512.
Required: No

 ** [cpuCoreCount](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-cpuCoreCount"></a>
The number of CPU cores to allocate to the Autonomous Database.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 128.
Required: No

 ** [customerContactsToSendToOCI](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-customerContactsToSendToOCI"></a>
The list of customer contacts to receive operational notifications from OCI for the Autonomous Database.
Type: Array of [CustomerContact](API_CustomerContact.md) objects
Required: No

 ** [databaseEdition](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-databaseEdition"></a>
The Oracle Database edition to apply to the Autonomous Database.
Type: String
Valid Values: `STANDARD_EDITION | ENTERPRISE_EDITION`
Required: No

 ** [dataStorageSizeInGBs](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-dataStorageSizeInGBs"></a>
The size, in gigabytes (GB), of the data volume to allocate for the Autonomous Database.
Type: Integer
Valid Range: Minimum value of 20. Maximum value of 393216.
Required: No

 ** [dataStorageSizeInTBs](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-dataStorageSizeInTBs"></a>
The size, in terabytes (TB), of the data volume to allocate for the Autonomous Database.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 384.
Required: No

 ** [dbName](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-dbName"></a>
The new name of the Autonomous Database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Required: No

 ** [dbToolsDetails](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-dbToolsDetails"></a>
The list of database management tools to enable for the Autonomous Database.
Type: Array of [DatabaseTool](API_DatabaseTool.md) objects
Required: No

 ** [dbVersion](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-dbVersion"></a>
The Oracle Database software version to use for the Autonomous Database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [dbWorkload](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-dbWorkload"></a>
The intended use of the Autonomous Database, such as transaction processing, data warehouse, JSON database, or APEX.
Type: String
Valid Values: `OLTP | AJD | APEX | LH`
Required: No

 ** [displayName](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-displayName"></a>
The new user-friendly name for the Autonomous Database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_](?!.*--)[a-zA-Z0-9_-]*`
Required: No

 ** [encryptionKeyConfiguration](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-encryptionKeyConfiguration"></a>
The configuration of the encryption key to use for the Autonomous Database.
Type: [EncryptionKeyConfigurationInput](API_EncryptionKeyConfigurationInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [encryptionKeyProvider](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-encryptionKeyProvider"></a>
The provider of the encryption key to use for the Autonomous Database.
Type: String
Valid Values: `ORACLE_MANAGED | AWS_KMS`
Required: No

 ** [isAutoScalingEnabled](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-isAutoScalingEnabled"></a>
Specifies whether to enable automatic scaling of the compute resources for the Autonomous Database.
Type: Boolean
Required: No

 ** [isAutoScalingForStorageEnabled](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-isAutoScalingForStorageEnabled"></a>
Specifies whether to enable automatic scaling of the storage for the Autonomous Database.
Type: Boolean
Required: No

 ** [isBackupRetentionLocked](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-isBackupRetentionLocked"></a>
Specifies whether to lock the backup retention period of the Autonomous Database to prevent it from being shortened.
Type: Boolean
Required: No

 ** [isDisconnectPeer](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-isDisconnectPeer"></a>
Specifies whether to disconnect the Autonomous Database from its peer database.
Type: Boolean
Required: No

 ** [isLocalDataGuardEnabled](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-isLocalDataGuardEnabled"></a>
Specifies whether to enable local Oracle Data Guard for the Autonomous Database.
Type: Boolean
Required: No

 ** [isMtlsConnectionRequired](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-isMtlsConnectionRequired"></a>
Specifies whether mutual TLS (mTLS) authentication is required to connect to the Autonomous Database.
Type: Boolean
Required: No

 ** [isRefreshableClone](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-isRefreshableClone"></a>
Specifies whether the Autonomous Database is a refreshable clone.
Type: Boolean
Required: No

 ** [licenseModel](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-licenseModel"></a>
The Oracle license model to apply to the Autonomous Database.
Type: String
Valid Values: `BRING_YOUR_OWN_LICENSE | LICENSE_INCLUDED`
Required: No

 ** [localAdgAutoFailoverMaxDataLossLimit](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-localAdgAutoFailoverMaxDataLossLimit"></a>
The maximum data loss limit, in seconds, for automatic failover to the local Oracle Data Guard standby database.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 3600.
Required: No

 ** [longTermBackupSchedule](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-longTermBackupSchedule"></a>
The long-term backup schedule for the Autonomous Database.
Type: [LongTermBackupSchedule](API_LongTermBackupSchedule.md) object
Required: No

 ** [openMode](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-openMode"></a>
The mode in which to open the Autonomous Database, either read-only or read/write.
Type: String
Valid Values: `READ_ONLY | READ_WRITE`
Required: No

 ** [peerDbId](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-peerDbId"></a>
The unique identifier of the peer Autonomous Database.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: No

 ** [permissionLevel](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-permissionLevel"></a>
The permission level of the Autonomous Database.
Type: String
Valid Values: `RESTRICTED | UNRESTRICTED`
Required: No

 ** [privateEndpointIp](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-privateEndpointIp"></a>
The private endpoint IP address for the Autonomous Database.
Type: String
Required: No

 ** [privateEndpointLabel](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-privateEndpointLabel"></a>
The private endpoint label for the Autonomous Database.
Type: String
Required: No

 ** [refreshableMode](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-refreshableMode"></a>
The refresh mode of the refreshable clone Autonomous Database.
Type: String
Valid Values: `AUTOMATIC | MANUAL`
Required: No

 ** [resourcePoolLeaderId](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-resourcePoolLeaderId"></a>
The unique identifier of the resource pool leader Autonomous Database.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: No

 ** [resourcePoolSummary](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-resourcePoolSummary"></a>
The configuration of the resource pool for the Autonomous Database.
Type: [ResourcePoolSummary](API_ResourcePoolSummary.md) object
Required: No

 ** [scheduledOperations](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-scheduledOperations"></a>
The list of scheduled start and stop times for the Autonomous Database.
Type: Array of [ScheduledOperationDetails](API_ScheduledOperationDetails.md) objects
Required: No

 ** [standbyAllowlistedIps](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-standbyAllowlistedIps"></a>
The list of IP addresses that are allowed to access the standby Autonomous Database.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** [standbyAllowlistedIpsSource](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-standbyAllowlistedIpsSource"></a>
The source of the allowlisted IP addresses for the standby Autonomous Database.
Type: String
Valid Values: `PRIMARY | SEPARATE | NOT_APPLICABLE`
Required: No

 ** [timeOfAutoRefreshStart](#API_UpdateAutonomousDatabase_RequestSyntax) **   <a name="odb-UpdateAutonomousDatabase-request-timeOfAutoRefreshStart"></a>
The date and time at which the automatic refresh of the refreshable clone Autonomous Database starts.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_UpdateAutonomousDatabase_ResponseSyntax"></a>

```
{
   "autonomousDatabaseId": "string",
   "displayName": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_UpdateAutonomousDatabase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [autonomousDatabaseId](#API_UpdateAutonomousDatabase_ResponseSyntax) **   <a name="odb-UpdateAutonomousDatabase-response-autonomousDatabaseId"></a>
The unique identifier of the Autonomous Database that was updated.
Type: String

 ** [displayName](#API_UpdateAutonomousDatabase_ResponseSyntax) **   <a name="odb-UpdateAutonomousDatabase-response-displayName"></a>
The user-friendly name of the Autonomous Database that was updated.
Type: String

 ** [status](#API_UpdateAutonomousDatabase_ResponseSyntax) **   <a name="odb-UpdateAutonomousDatabase-response-status"></a>
The current status of the Autonomous Database.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS | STOPPING | STOPPED | STARTING | UNAVAILABLE | RESTORE_IN_PROGRESS | RESTORE_FAILED | BACKUP_IN_PROGRESS | SCALE_IN_PROGRESS | AVAILABLE_NEEDS_ATTENTION | RESTARTING | RECREATING | ROLE_CHANGE_IN_PROGRESS | UPGRADING | INACCESSIBLE | STANDBY`

 ** [statusReason](#API_UpdateAutonomousDatabase_ResponseSyntax) **   <a name="odb-UpdateAutonomousDatabase-response-statusReason"></a>
Additional information about the current status of the Autonomous Database, if applicable.
Type: String

## Errors
<a name="API_UpdateAutonomousDatabase_Errors"></a>

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
<a name="API_UpdateAutonomousDatabase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/UpdateAutonomousDatabase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/UpdateAutonomousDatabase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/UpdateAutonomousDatabase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/UpdateAutonomousDatabase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/UpdateAutonomousDatabase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/UpdateAutonomousDatabase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/UpdateAutonomousDatabase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/UpdateAutonomousDatabase)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/UpdateAutonomousDatabase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/UpdateAutonomousDatabase)
