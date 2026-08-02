---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_CreateBackupPlan.html
---

# CreateBackupPlan
<a name="API_CreateBackupPlan"></a>

Creates a backup plan using a backup plan name and backup rules. A backup plan is a document that contains information that AWS Backup uses to schedule tasks that create recovery points for resources.

If you call `CreateBackupPlan` with a plan that already exists, you receive an `AlreadyExistsException` exception.

## Request Syntax
<a name="API_CreateBackupPlan_RequestSyntax"></a>

```
PUT /backup/plans/ HTTP/1.1
Content-type: application/json

{
   "BackupPlan": {
      "AdvancedBackupSettings": [
         {
            "BackupOptions": {
               "{{string}}" : "{{string}}"
            },
            "ResourceType": "{{string}}"
         }
      ],
      "BackupPlanName": "{{string}}",
      "Rules": [
         {
            "CompletionWindowMinutes": {{number}},
            "CopyActions": [
               {
                  "DestinationBackupVaultArn": "{{string}}",
                  "Lifecycle": {
                     "DeleteAfterDays": {{number}},
                     "DeleteAfterEvent": "{{string}}",
                     "MoveToColdStorageAfterDays": {{number}},
                     "OptInToArchiveForSupportedResources": {{boolean}}
                  }
               }
            ],
            "EnableContinuousBackup": {{boolean}},
            "IndexActions": [
               {
                  "ResourceTypes": [ "{{string}}" ]
               }
            ],
            "Lifecycle": {
               "DeleteAfterDays": {{number}},
               "DeleteAfterEvent": "{{string}}",
               "MoveToColdStorageAfterDays": {{number}},
               "OptInToArchiveForSupportedResources": {{boolean}}
            },
            "RecoveryPointTags": {
               "{{string}}" : "{{string}}"
            },
            "RuleName": "{{string}}",
            "ScanActions": [
               {
                  "MalwareScanner": "{{string}}",
                  "ScanMode": "{{string}}"
               }
            ],
            "ScheduleExpression": "{{string}}",
            "ScheduleExpressionTimezone": "{{string}}",
            "StartWindowMinutes": {{number}},
            "TargetBackupVaultName": "{{string}}",
            "TargetLogicallyAirGappedBackupVaultArn": "{{string}}"
         }
      ],
      "ScanSettings": [
         {
            "MalwareScanner": "{{string}}",
            "ResourceTypes": [ "{{string}}" ],
            "ScannerRoleArn": "{{string}}"
         }
      ]
   },
   "BackupPlanTags": {
      "{{string}}" : "{{string}}"
   },
   "CreatorRequestId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateBackupPlan_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateBackupPlan_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [BackupPlan](#API_CreateBackupPlan_RequestSyntax) **   <a name="Backup-CreateBackupPlan-request-BackupPlan"></a>
The body of a backup plan. Includes a `BackupPlanName` and one or more sets of `Rules`.
Type: [BackupPlanInput](API_BackupPlanInput.md) object
Required: Yes

 ** [BackupPlanTags](#API_CreateBackupPlan_RequestSyntax) **   <a name="Backup-CreateBackupPlan-request-BackupPlanTags"></a>
The tags to assign to the backup plan.
Type: String to string map
Required: No

 ** [CreatorRequestId](#API_CreateBackupPlan_RequestSyntax) **   <a name="Backup-CreateBackupPlan-request-CreatorRequestId"></a>
Identifies the request and allows failed requests to be retried without the risk of running the operation twice. If the request includes a `CreatorRequestId` that matches an existing backup plan, that plan is returned. This parameter is optional.
If used, this parameter must contain 1 to 50 alphanumeric or '-\_.' characters.
Type: String
Required: No

## Response Syntax
<a name="API_CreateBackupPlan_ResponseSyntax"></a>

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
   "BackupPlanArn": "string",
   "BackupPlanId": "string",
   "CreationDate": number,
   "VersionId": "string"
}
```

## Response Elements
<a name="API_CreateBackupPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdvancedBackupSettings](#API_CreateBackupPlan_ResponseSyntax) **   <a name="Backup-CreateBackupPlan-response-AdvancedBackupSettings"></a>
The settings for a resource type. This option is only available for Windows Volume Shadow Copy Service (VSS) backup jobs.
Type: Array of [AdvancedBackupSetting](API_AdvancedBackupSetting.md) objects

 ** [BackupPlanArn](#API_CreateBackupPlan_ResponseSyntax) **   <a name="Backup-CreateBackupPlan-response-BackupPlanArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, `arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`.
Type: String

 ** [BackupPlanId](#API_CreateBackupPlan_ResponseSyntax) **   <a name="Backup-CreateBackupPlan-response-BackupPlanId"></a>
The ID of the backup plan.
Type: String

 ** [CreationDate](#API_CreateBackupPlan_ResponseSyntax) **   <a name="Backup-CreateBackupPlan-response-CreationDate"></a>
The date and time that a backup plan is created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp

 ** [VersionId](#API_CreateBackupPlan_ResponseSyntax) **   <a name="Backup-CreateBackupPlan-response-VersionId"></a>
Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. They cannot be edited.
Type: String

## Errors
<a name="API_CreateBackupPlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **
The required resource already exists.
 ** Arn **

 ** Context **

 ** CreatorRequestId **

 ** Type **

HTTP Status Code: 400

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** LimitExceededException **
A limit in the request has been exceeded; for example, a maximum number of items allowed in a request.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** MissingParameterValueException **
Indicates that a required parameter is missing.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_CreateBackupPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/CreateBackupPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/CreateBackupPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/CreateBackupPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/CreateBackupPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/CreateBackupPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/CreateBackupPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/CreateBackupPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/CreateBackupPlan)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/CreateBackupPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/CreateBackupPlan)
