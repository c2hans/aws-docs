---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_GetBackupPlan.html
---

# GetBackupPlan
<a name="API_GetBackupPlan"></a>

Returns `BackupPlan` details for the specified `BackupPlanId`. The details are the body of a backup plan in JSON format, in addition to plan metadata.

## Request Syntax
<a name="API_GetBackupPlan_RequestSyntax"></a>

```
GET /backup/plans/{{backupPlanId}}/?MaxScheduledRunsPreview={{MaxScheduledRunsPreview}}&versionId={{VersionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetBackupPlan_RequestParameters"></a>

The request uses the following URI parameters.

 ** [backupPlanId](#API_GetBackupPlan_RequestSyntax) **   <a name="Backup-GetBackupPlan-request-uri-BackupPlanId"></a>
Uniquely identifies a backup plan.
Required: Yes

 ** [MaxScheduledRunsPreview](#API_GetBackupPlan_RequestSyntax) **   <a name="Backup-GetBackupPlan-request-uri-MaxScheduledRunsPreview"></a>
Number of future scheduled backup runs to preview. When set to 0 (default), no scheduled runs preview is included in the response. Valid range is 0-10.
Valid Range: Minimum value of 0. Maximum value of 10.

 ** [VersionId](#API_GetBackupPlan_RequestSyntax) **   <a name="Backup-GetBackupPlan-request-uri-VersionId"></a>
Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.

## Request Body
<a name="API_GetBackupPlan_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBackupPlan_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AdvancedBackupSettings": [
      {
         "BackupOptions": {
            "string" : "string"
         },
         "ResourceType": "string"
      }
   ],
   "BackupPlan": {
      "AdvancedBackupSettings": [
         {
            "BackupOptions": {
               "string" : "string"
            },
            "ResourceType": "string"
         }
      ],
      "BackupPlanName": "string",
      "Rules": [
         {
            "CompletionWindowMinutes": number,
            "CopyActions": [
               {
                  "DestinationBackupVaultArn": "string",
                  "Lifecycle": {
                     "DeleteAfterDays": number,
                     "DeleteAfterEvent": "string",
                     "MoveToColdStorageAfterDays": number,
                     "OptInToArchiveForSupportedResources": boolean
                  }
               }
            ],
            "EnableContinuousBackup": boolean,
            "IndexActions": [
               {
                  "ResourceTypes": [ "string" ]
               }
            ],
            "Lifecycle": {
               "DeleteAfterDays": number,
               "DeleteAfterEvent": "string",
               "MoveToColdStorageAfterDays": number,
               "OptInToArchiveForSupportedResources": boolean
            },
            "RecoveryPointTags": {
               "string" : "string"
            },
            "RuleId": "string",
            "RuleName": "string",
            "ScanActions": [
               {
                  "MalwareScanner": "string",
                  "ScanMode": "string"
               }
            ],
            "ScheduleExpression": "string",
            "ScheduleExpressionTimezone": "string",
            "StartWindowMinutes": number,
            "TargetBackupVaultName": "string",
            "TargetLogicallyAirGappedBackupVaultArn": "string"
         }
      ],
      "ScanSettings": [
         {
            "MalwareScanner": "string",
            "ResourceTypes": [ "string" ],
            "ScannerRoleArn": "string"
         }
      ]
   },
   "BackupPlanArn": "string",
   "BackupPlanId": "string",
   "CreationDate": number,
   "CreatorRequestId": "string",
   "DeletionDate": number,
   "LastExecutionDate": number,
   "ScheduledRunsPreview": [
      {
         "ExecutionTime": number,
         "RuleExecutionType": "string",
         "RuleId": "string"
      }
   ],
   "VersionId": "string"
}
```

## Response Elements
<a name="API_GetBackupPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdvancedBackupSettings](#API_GetBackupPlan_ResponseSyntax) **   <a name="Backup-GetBackupPlan-response-AdvancedBackupSettings"></a>
Contains a list of `BackupOptions` for each resource type. The list is populated only if the advanced option is set for the backup plan.
Type: Array of [AdvancedBackupSetting](API_AdvancedBackupSetting.md) objects

 ** [BackupPlan](#API_GetBackupPlan_ResponseSyntax) **   <a name="Backup-GetBackupPlan-response-BackupPlan"></a>
Specifies the body of a backup plan. Includes a `BackupPlanName` and one or more sets of `Rules`.
Type: [BackupPlan](API_BackupPlan.md) object

 ** [BackupPlanArn](#API_GetBackupPlan_ResponseSyntax) **   <a name="Backup-GetBackupPlan-response-BackupPlanArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, `arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`.
Type: String

 ** [BackupPlanId](#API_GetBackupPlan_ResponseSyntax) **   <a name="Backup-GetBackupPlan-response-BackupPlanId"></a>
Uniquely identifies a backup plan.
Type: String

 ** [CreationDate](#API_GetBackupPlan_ResponseSyntax) **   <a name="Backup-GetBackupPlan-response-CreationDate"></a>
The date and time that a backup plan is created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp

 ** [CreatorRequestId](#API_GetBackupPlan_ResponseSyntax) **   <a name="Backup-GetBackupPlan-response-CreatorRequestId"></a>
A unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice.
Type: String

 ** [DeletionDate](#API_GetBackupPlan_ResponseSyntax) **   <a name="Backup-GetBackupPlan-response-DeletionDate"></a>
The date and time that a backup plan is deleted, in Unix format and Coordinated Universal Time (UTC). The value of `DeletionDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp

 ** [LastExecutionDate](#API_GetBackupPlan_ResponseSyntax) **   <a name="Backup-GetBackupPlan-response-LastExecutionDate"></a>
The last time this backup plan was run. A date and time, in Unix format and Coordinated Universal Time (UTC). The value of `LastExecutionDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp

 ** [ScheduledRunsPreview](#API_GetBackupPlan_ResponseSyntax) **   <a name="Backup-GetBackupPlan-response-ScheduledRunsPreview"></a>
List of upcoming scheduled backup runs. Only included when `MaxScheduledRunsPreview` parameter is greater than 0. Contains up to 10 future backup executions with their scheduled times, execution types, and associated rule IDs.
Type: Array of [ScheduledPlanExecutionMember](API_ScheduledPlanExecutionMember.md) objects

 ** [VersionId](#API_GetBackupPlan_ResponseSyntax) **   <a name="Backup-GetBackupPlan-response-VersionId"></a>
Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.
Type: String

## Errors
<a name="API_GetBackupPlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** MissingParameterValueException **
Indicates that a required parameter is missing.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource that is required for the action doesn't exist.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_GetBackupPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/GetBackupPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/GetBackupPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/GetBackupPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/GetBackupPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/GetBackupPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/GetBackupPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/GetBackupPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/GetBackupPlan)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/GetBackupPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/GetBackupPlan)
