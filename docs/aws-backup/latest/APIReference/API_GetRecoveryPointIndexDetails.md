---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_GetRecoveryPointIndexDetails.html
---

# GetRecoveryPointIndexDetails
<a name="API_GetRecoveryPointIndexDetails"></a>

This operation returns the metadata and details specific to the backup index associated with the specified recovery point.

## Request Syntax
<a name="API_GetRecoveryPointIndexDetails_RequestSyntax"></a>

```
GET /backup-vaults/{{backupVaultName}}/recovery-points/{{recoveryPointArn}}/index HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRecoveryPointIndexDetails_RequestParameters"></a>

The request uses the following URI parameters.

 ** [backupVaultName](#API_GetRecoveryPointIndexDetails_RequestSyntax) **   <a name="Backup-GetRecoveryPointIndexDetails-request-uri-BackupVaultName"></a>
The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created.
Accepted characters include lowercase letters, numbers, and hyphens.
Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`
Required: Yes

 ** [recoveryPointArn](#API_GetRecoveryPointIndexDetails_RequestSyntax) **   <a name="Backup-GetRecoveryPointIndexDetails-request-uri-RecoveryPointArn"></a>
An ARN that uniquely identifies a recovery point; for example, `arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.
Required: Yes

## Request Body
<a name="API_GetRecoveryPointIndexDetails_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRecoveryPointIndexDetails_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "BackupVaultArn": "string",
   "IndexCompletionDate": number,
   "IndexCreationDate": number,
   "IndexDeletionDate": number,
   "IndexStatus": "string",
   "IndexStatusMessage": "string",
   "RecoveryPointArn": "string",
   "SourceResourceArn": "string",
   "TotalItemsIndexed": number
}
```

## Response Elements
<a name="API_GetRecoveryPointIndexDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BackupVaultArn](#API_GetRecoveryPointIndexDetails_ResponseSyntax) **   <a name="Backup-GetRecoveryPointIndexDetails-response-BackupVaultArn"></a>
An ARN that uniquely identifies the backup vault where the recovery point index is stored.
For example, `arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`.
Type: String

 ** [IndexCompletionDate](#API_GetRecoveryPointIndexDetails_ResponseSyntax) **   <a name="Backup-GetRecoveryPointIndexDetails-response-IndexCompletionDate"></a>
The date and time that a backup index finished creation, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp

 ** [IndexCreationDate](#API_GetRecoveryPointIndexDetails_ResponseSyntax) **   <a name="Backup-GetRecoveryPointIndexDetails-response-IndexCreationDate"></a>
The date and time that a backup index was created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp

 ** [IndexDeletionDate](#API_GetRecoveryPointIndexDetails_ResponseSyntax) **   <a name="Backup-GetRecoveryPointIndexDetails-response-IndexDeletionDate"></a>
The date and time that a backup index was deleted, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp

 ** [IndexStatus](#API_GetRecoveryPointIndexDetails_ResponseSyntax) **   <a name="Backup-GetRecoveryPointIndexDetails-response-IndexStatus"></a>
This is the current status for the backup index associated with the specified recovery point.
Statuses are: `PENDING` \| `ACTIVE` \| `FAILED` \| `DELETING`
A recovery point with an index that has the status of `ACTIVE` can be included in a search.
Type: String
Valid Values: `PENDING | ACTIVE | FAILED | DELETING`

 ** [IndexStatusMessage](#API_GetRecoveryPointIndexDetails_ResponseSyntax) **   <a name="Backup-GetRecoveryPointIndexDetails-response-IndexStatusMessage"></a>
A detailed message explaining the status of a backup index associated with the recovery point.
Type: String

 ** [RecoveryPointArn](#API_GetRecoveryPointIndexDetails_ResponseSyntax) **   <a name="Backup-GetRecoveryPointIndexDetails-response-RecoveryPointArn"></a>
An ARN that uniquely identifies a recovery point; for example, `arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.
Type: String

 ** [SourceResourceArn](#API_GetRecoveryPointIndexDetails_ResponseSyntax) **   <a name="Backup-GetRecoveryPointIndexDetails-response-SourceResourceArn"></a>
A string of the Amazon Resource Name (ARN) that uniquely identifies the source resource.
Type: String

 ** [TotalItemsIndexed](#API_GetRecoveryPointIndexDetails_ResponseSyntax) **   <a name="Backup-GetRecoveryPointIndexDetails-response-TotalItemsIndexed"></a>
Count of items within the backup index associated with the recovery point.
Type: Long

## Errors
<a name="API_GetRecoveryPointIndexDetails_Errors"></a>

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
<a name="API_GetRecoveryPointIndexDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/GetRecoveryPointIndexDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/GetRecoveryPointIndexDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/GetRecoveryPointIndexDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/GetRecoveryPointIndexDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/GetRecoveryPointIndexDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/GetRecoveryPointIndexDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/GetRecoveryPointIndexDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/GetRecoveryPointIndexDetails)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/GetRecoveryPointIndexDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/GetRecoveryPointIndexDetails)
