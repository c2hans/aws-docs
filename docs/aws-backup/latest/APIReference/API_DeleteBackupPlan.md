---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DeleteBackupPlan.html
---

# DeleteBackupPlan
<a name="API_DeleteBackupPlan"></a>

Deletes a backup plan. A backup plan can only be deleted after all associated selections of resources have been deleted. Deleting a backup plan deletes the current version of a backup plan. Previous versions, if any, will still exist.

## Request Syntax
<a name="API_DeleteBackupPlan_RequestSyntax"></a>

```
DELETE /backup/plans/{{backupPlanId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteBackupPlan_RequestParameters"></a>

The request uses the following URI parameters.

 ** [backupPlanId](#API_DeleteBackupPlan_RequestSyntax) **   <a name="Backup-DeleteBackupPlan-request-uri-BackupPlanId"></a>
Uniquely identifies a backup plan.
Required: Yes

## Request Body
<a name="API_DeleteBackupPlan_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteBackupPlan_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "BackupPlanArn": "string",
   "BackupPlanId": "string",
   "DeletionDate": number,
   "VersionId": "string"
}
```

## Response Elements
<a name="API_DeleteBackupPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BackupPlanArn](#API_DeleteBackupPlan_ResponseSyntax) **   <a name="Backup-DeleteBackupPlan-response-BackupPlanArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, `arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`.
Type: String

 ** [BackupPlanId](#API_DeleteBackupPlan_ResponseSyntax) **   <a name="Backup-DeleteBackupPlan-response-BackupPlanId"></a>
Uniquely identifies a backup plan.
Type: String

 ** [DeletionDate](#API_DeleteBackupPlan_ResponseSyntax) **   <a name="Backup-DeleteBackupPlan-response-DeletionDate"></a>
The date and time a backup plan is deleted, in Unix format and Coordinated Universal Time (UTC). The value of `DeletionDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp

 ** [VersionId](#API_DeleteBackupPlan_ResponseSyntax) **   <a name="Backup-DeleteBackupPlan-response-VersionId"></a>
Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.
Type: String

## Errors
<a name="API_DeleteBackupPlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.
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
<a name="API_DeleteBackupPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/DeleteBackupPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/DeleteBackupPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/DeleteBackupPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/DeleteBackupPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/DeleteBackupPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/DeleteBackupPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/DeleteBackupPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/DeleteBackupPlan)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/DeleteBackupPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/DeleteBackupPlan)
