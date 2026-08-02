---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateAutonomousDatabase.html
---

# CreateAutonomousDatabase
<a name="API_CreateAutonomousDatabase"></a>

Creates a new Autonomous Database.

## Request Syntax
<a name="API_CreateAutonomousDatabase_RequestSyntax"></a>

```
{
   "adminPassword": "{{string}}",
   "adminPasswordSource": "{{string}}",
   "adminPasswordSourceConfiguration": { ... },
   "allowlistedIps": [ "{{string}}" ],
   "autonomousMaintenanceScheduleType": "{{string}}",
   "backupRetentionPeriodInDays": {{number}},
   "byolComputeCountLimit": {{number}},
   "characterSet": "{{string}}",
   "clientToken": "{{string}}",
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
   "isLocalDataGuardEnabled": {{boolean}},
   "isMtlsConnectionRequired": {{boolean}},
   "licenseModel": "{{string}}",
   "ncharacterSet": "{{string}}",
   "odbNetworkId": "{{string}}",
   "privateEndpointIp": "{{string}}",
   "privateEndpointLabel": "{{string}}",
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
   "source": "{{string}}",
   "sourceConfiguration": { ... },
   "standbyAllowlistedIps": [ "{{string}}" ],
   "standbyAllowlistedIpsSource": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "transportableTablespace": {
      "ttsBundleUrl": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateAutonomousDatabase_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [adminPassword](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-adminPassword"></a>
The password for the `ADMIN` user of the Autonomous Database.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 30.
Required: No

 ** [adminPasswordSource](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-adminPasswordSource"></a>
The source of the admin password for the Autonomous Database. When set to `CUSTOMER_MANAGED_AWS_SECRET`, the admin password is retrieved from an AWS Secrets Manager secret.
Type: String
Valid Values: `CUSTOMER_MANAGED_AWS_SECRET | API_REQUEST_PARAMETER`
Required: No

 ** [adminPasswordSourceConfiguration](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-adminPasswordSourceConfiguration"></a>
The configuration of the admin password source for the Autonomous Database.
Type: [AdminPasswordSourceConfigurationInput](API_AdminPasswordSourceConfigurationInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [allowlistedIps](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-allowlistedIps"></a>
The list of IP addresses that are allowed to access the Autonomous Database.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** [autonomousMaintenanceScheduleType](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-autonomousMaintenanceScheduleType"></a>
The maintenance schedule type for the Autonomous Database.
Type: String
Valid Values: `EARLY | REGULAR`
Required: No

 ** [backupRetentionPeriodInDays](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-backupRetentionPeriodInDays"></a>
The retention period, in days, for automatic backups of the Autonomous Database.
Type: Integer
Required: No

 ** [byolComputeCountLimit](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-byolComputeCountLimit"></a>
The maximum number of compute resources that you can allocate to the Autonomous Database under the bring-your-own-license (BYOL) model.
Type: Double
Valid Range: Minimum value of 2.
Required: No

 ** [characterSet](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-characterSet"></a>
The character set to use for the Autonomous Database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [clientToken](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-clientToken"></a>
A client-provided token to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 64.
Pattern: `[a-zA-Z0-9_\/.=-]+`
Required: No

 ** [computeCount](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-computeCount"></a>
The compute capacity, in number of Elastic CPUs (ECPUs) or Oracle CPUs (OCPUs), to assign to the Autonomous Database.
Type: Double
Valid Range: Minimum value of 0.1. Maximum value of 512.
Required: No

 ** [cpuCoreCount](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-cpuCoreCount"></a>
The number of CPU cores to allocate to the Autonomous Database.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 128.
Required: No

 ** [customerContactsToSendToOCI](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-customerContactsToSendToOCI"></a>
The list of customer contacts to receive operational notifications from Oracle Cloud Infrastructure (OCI) for the Autonomous Database.
Type: Array of [CustomerContact](API_CustomerContact.md) objects
Required: No

 ** [databaseEdition](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-databaseEdition"></a>
The Oracle Database edition to apply to the Autonomous Database.
Type: String
Valid Values: `STANDARD_EDITION | ENTERPRISE_EDITION`
Required: No

 ** [dataStorageSizeInGBs](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-dataStorageSizeInGBs"></a>
The size, in gigabytes (GB), of the data volume to allocate for the Autonomous Database.
Type: Integer
Valid Range: Minimum value of 20. Maximum value of 393216.
Required: No

 ** [dataStorageSizeInTBs](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-dataStorageSizeInTBs"></a>
The size, in terabytes (TB), of the data volume to allocate for the Autonomous Database.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 384.
Required: No

 ** [dbName](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-dbName"></a>
The name of the Autonomous Database. The name must begin with an alphabetic character and can contain a maximum of 30 alphanumeric characters. Special characters are not permitted. The name must be unique in the AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Required: No

 ** [dbToolsDetails](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-dbToolsDetails"></a>
The list of database management tools to enable for the Autonomous Database.
Type: Array of [DatabaseTool](API_DatabaseTool.md) objects
Required: No

 ** [dbVersion](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-dbVersion"></a>
The Oracle Database software version to use for the Autonomous Database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [dbWorkload](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-dbWorkload"></a>
The intended use of the Autonomous Database, such as transaction processing, data warehouse, JSON database, or APEX.
Type: String
Valid Values: `OLTP | AJD | APEX | LH`
Required: No

 ** [displayName](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-displayName"></a>
The user-friendly name for the Autonomous Database. The name does not have to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_](?!.*--)[a-zA-Z0-9_-]*`
Required: No

 ** [encryptionKeyConfiguration](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-encryptionKeyConfiguration"></a>
The configuration of the encryption key to use for the Autonomous Database.
Type: [EncryptionKeyConfigurationInput](API_EncryptionKeyConfigurationInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [encryptionKeyProvider](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-encryptionKeyProvider"></a>
The provider of the encryption key to use for the Autonomous Database.
Type: String
Valid Values: `ORACLE_MANAGED | AWS_KMS`
Required: No

 ** [isAutoScalingEnabled](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-isAutoScalingEnabled"></a>
Specifies whether to enable automatic scaling of the compute resources for the Autonomous Database.
Type: Boolean
Required: No

 ** [isAutoScalingForStorageEnabled](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-isAutoScalingForStorageEnabled"></a>
Specifies whether to enable automatic scaling of the storage for the Autonomous Database.
Type: Boolean
Required: No

 ** [isBackupRetentionLocked](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-isBackupRetentionLocked"></a>
Specifies whether to lock the backup retention period of the Autonomous Database to prevent it from being shortened.
Type: Boolean
Required: No

 ** [isLocalDataGuardEnabled](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-isLocalDataGuardEnabled"></a>
Specifies whether to enable local Oracle Data Guard for the Autonomous Database.
Type: Boolean
Required: No

 ** [isMtlsConnectionRequired](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-isMtlsConnectionRequired"></a>
Specifies whether mutual TLS (mTLS) authentication is required to connect to the Autonomous Database.
Type: Boolean
Required: No

 ** [licenseModel](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-licenseModel"></a>
The Oracle license model to apply to the Autonomous Database.
Type: String
Valid Values: `BRING_YOUR_OWN_LICENSE | LICENSE_INCLUDED`
Required: No

 ** [ncharacterSet](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-ncharacterSet"></a>
The national character set to use for the Autonomous Database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [odbNetworkId](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-odbNetworkId"></a>
The unique identifier of the ODB network to be used for the Autonomous Database.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: No

 ** [privateEndpointIp](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-privateEndpointIp"></a>
The private endpoint IP address for the Autonomous Database.
Type: String
Required: No

 ** [privateEndpointLabel](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-privateEndpointLabel"></a>
The private endpoint label for the Autonomous Database.
Type: String
Required: No

 ** [resourcePoolLeaderId](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-resourcePoolLeaderId"></a>
The unique identifier of the resource pool leader Autonomous Database.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: No

 ** [resourcePoolSummary](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-resourcePoolSummary"></a>
The configuration of the resource pool for the Autonomous Database.
Type: [ResourcePoolSummary](API_ResourcePoolSummary.md) object
Required: No

 ** [scheduledOperations](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-scheduledOperations"></a>
The list of scheduled start and stop times for the Autonomous Database.
Type: Array of [ScheduledOperationDetails](API_ScheduledOperationDetails.md) objects
Required: No

 ** [source](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-source"></a>
The source from which to create the Autonomous Database, such as a clone, backup, or cross-Region copy.
Type: String
Valid Values: `NONE | DATABASE | BACKUP_FROM_ID | BACKUP_FROM_TIMESTAMP | CROSS_REGION_DATAGUARD | CROSS_REGION_DISASTER_RECOVERY | CLONE_TO_REFRESHABLE`
Required: No

 ** [sourceConfiguration](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-sourceConfiguration"></a>
The configuration details for the source used to create the Autonomous Database.
Type: [SourceConfiguration](API_SourceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [standbyAllowlistedIps](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-standbyAllowlistedIps"></a>
The list of IP addresses that are allowed to access the standby Autonomous Database.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** [standbyAllowlistedIpsSource](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-standbyAllowlistedIpsSource"></a>
The source of the allowlisted IP addresses for the standby Autonomous Database.
Type: String
Valid Values: `PRIMARY | SEPARATE | NOT_APPLICABLE`
Required: No

 ** [tags](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-tags"></a>
The list of resource tags to apply to the Autonomous Database. Each tag is a key-value pair with no predefined name, type, or namespace.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [transportableTablespace](#API_CreateAutonomousDatabase_RequestSyntax) **   <a name="odb-CreateAutonomousDatabase-request-transportableTablespace"></a>
The transportable tablespace configuration to use when creating the Autonomous Database.
Type: [TransportableTablespace](API_TransportableTablespace.md) object
Required: No

## Response Syntax
<a name="API_CreateAutonomousDatabase_ResponseSyntax"></a>

```
{
   "autonomousDatabaseId": "string",
   "displayName": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_CreateAutonomousDatabase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [autonomousDatabaseId](#API_CreateAutonomousDatabase_ResponseSyntax) **   <a name="odb-CreateAutonomousDatabase-response-autonomousDatabaseId"></a>
The unique identifier of the Autonomous Database that was created.
Type: String

 ** [displayName](#API_CreateAutonomousDatabase_ResponseSyntax) **   <a name="odb-CreateAutonomousDatabase-response-displayName"></a>
The user-friendly name of the Autonomous Database that was created.
Type: String

 ** [status](#API_CreateAutonomousDatabase_ResponseSyntax) **   <a name="odb-CreateAutonomousDatabase-response-status"></a>
The current status of the Autonomous Database.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS | STOPPING | STOPPED | STARTING | UNAVAILABLE | RESTORE_IN_PROGRESS | RESTORE_FAILED | BACKUP_IN_PROGRESS | SCALE_IN_PROGRESS | AVAILABLE_NEEDS_ATTENTION | RESTARTING | RECREATING | ROLE_CHANGE_IN_PROGRESS | UPGRADING | INACCESSIBLE | STANDBY`

 ** [statusReason](#API_CreateAutonomousDatabase_ResponseSyntax) **   <a name="odb-CreateAutonomousDatabase-response-statusReason"></a>
Additional information about the current status of the Autonomous Database, if applicable.
Type: String

## Errors
<a name="API_CreateAutonomousDatabase_Errors"></a>

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
<a name="API_CreateAutonomousDatabase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/CreateAutonomousDatabase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/CreateAutonomousDatabase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/CreateAutonomousDatabase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/CreateAutonomousDatabase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/CreateAutonomousDatabase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/CreateAutonomousDatabase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/CreateAutonomousDatabase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/CreateAutonomousDatabase)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/CreateAutonomousDatabase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/CreateAutonomousDatabase)
