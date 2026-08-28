---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_StartScanJob.html
---

# StartScanJob
<a name="API_StartScanJob"></a>

Starts scanning jobs for specific resources.

## Request Syntax
<a name="API_StartScanJob_RequestSyntax"></a>

```
PUT /scan/job HTTP/1.1
Content-type: application/json

{
   "BackupVaultName": "{{string}}",
   "ContinuousScanEndTime": {{number}},
   "IamRoleArn": "{{string}}",
   "IdempotencyToken": "{{string}}",
   "MalwareScanner": "{{string}}",
   "RecoveryPointArn": "{{string}}",
   "ScanBaseRecoveryPointArn": "{{string}}",
   "ScanMode": "{{string}}",
   "ScannerRoleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartScanJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartScanJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [BackupVaultName](#API_StartScanJob_RequestSyntax) **   <a name="Backup-StartScanJob-request-BackupVaultName"></a>
The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created.
Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`
Type: String
Required: Yes

 ** [ContinuousScanEndTime](#API_StartScanJob_RequestSyntax) **   <a name="Backup-StartScanJob-request-ContinuousScanEndTime"></a>
The point in time the scan job will scan up to for a continuous backup.
Type: Timestamp
Required: No

 ** [IamRoleArn](#API_StartScanJob_RequestSyntax) **   <a name="Backup-StartScanJob-request-IamRoleArn"></a>
Specifies the IAM role ARN used to create the target recovery point; for example, `arn:aws:iam::123456789012:role/S3Access`.
Type: String
Required: Yes

 ** [IdempotencyToken](#API_StartScanJob_RequestSyntax) **   <a name="Backup-StartScanJob-request-IdempotencyToken"></a>
A customer-chosen string that you can use to distinguish between otherwise identical calls to `StartScanJob`. Retrying a successful request with the same idempotency token results in a success message with no action taken.
Type: String
Required: No

 ** [MalwareScanner](#API_StartScanJob_RequestSyntax) **   <a name="Backup-StartScanJob-request-MalwareScanner"></a>
Specifies the malware scanner used during the scan job. Currently only supports `GUARDDUTY`.
Type: String
Valid Values: `GUARDDUTY`
Required: Yes

 ** [RecoveryPointArn](#API_StartScanJob_RequestSyntax) **   <a name="Backup-StartScanJob-request-RecoveryPointArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a recovery point. This is your target recovery point for a full scan. If you are running an incremental scan, this will be your a recovery point which has been created after your base recovery point selection.
Type: String
Required: Yes

 ** [ScanBaseRecoveryPointArn](#API_StartScanJob_RequestSyntax) **   <a name="Backup-StartScanJob-request-ScanBaseRecoveryPointArn"></a>
An ARN that uniquely identifies the base recovery point to be used for incremental scanning.
Type: String
Required: No

 ** [ScanMode](#API_StartScanJob_RequestSyntax) **   <a name="Backup-StartScanJob-request-ScanMode"></a>
Specifies the scan type use for the scan job.
Includes:
+  `FULL_SCAN` will scan the entire data lineage within the backup.
+  `INCREMENTAL_SCAN` will scan the data difference between the target recovery point and base recovery point ARN.
Type: String
Valid Values: `FULL_SCAN | INCREMENTAL_SCAN`
Required: Yes

 ** [ScannerRoleArn](#API_StartScanJob_RequestSyntax) **   <a name="Backup-StartScanJob-request-ScannerRoleArn"></a>
Specified the IAM scanner role ARN.
Type: String
Required: Yes

## Response Syntax
<a name="API_StartScanJob_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "CreationDate": number,
   "ScanJobId": "string"
}
```

## Response Elements
<a name="API_StartScanJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [CreationDate](#API_StartScanJob_ResponseSyntax) **   <a name="Backup-StartScanJob-response-CreationDate"></a>
The date and time that a backup job is created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp

 ** [ScanJobId](#API_StartScanJob_ResponseSyntax) **   <a name="Backup-StartScanJob-response-ScanJobId"></a>
Uniquely identifies a request to AWS Backup to back up a resource.
Type: String

## Errors
<a name="API_StartScanJob_Errors"></a>

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
<a name="API_StartScanJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/StartScanJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/StartScanJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/StartScanJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/StartScanJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/StartScanJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/StartScanJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/StartScanJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/StartScanJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/StartScanJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/StartScanJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
