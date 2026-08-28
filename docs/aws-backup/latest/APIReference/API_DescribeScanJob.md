---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DescribeScanJob.html
---

# DescribeScanJob
<a name="API_DescribeScanJob"></a>

Returns scan job details for the specified ScanJobID.

## Request Syntax
<a name="API_DescribeScanJob_RequestSyntax"></a>

```
GET /scan/jobs/{{ScanJobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeScanJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ScanJobId](#API_DescribeScanJob_RequestSyntax) **   <a name="Backup-DescribeScanJob-request-uri-ScanJobId"></a>
Uniquely identifies a request to AWS Backup to scan a resource.
Required: Yes

## Request Body
<a name="API_DescribeScanJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeScanJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AccountId": "string",
   "BackupVaultArn": "string",
   "BackupVaultName": "string",
   "CompletionDate": number,
   "ContinuousScanEndTime": number,
   "ContinuousScanStartTime": number,
   "CreatedBy": {
      "BackupPlanArn": "string",
      "BackupPlanId": "string",
      "BackupPlanVersion": "string",
      "BackupRuleId": "string"
   },
   "CreationDate": number,
   "IamRoleArn": "string",
   "MalwareScanner": "string",
   "RecoveryPointArn": "string",
   "ResourceArn": "string",
   "ResourceName": "string",
   "ResourceType": "string",
   "ScanBaseRecoveryPointArn": "string",
   "ScanId": "string",
   "ScanJobId": "string",
   "ScanMode": "string",
   "ScannerRoleArn": "string",
   "ScanResult": {
      "ScanResultStatus": "string"
   },
   "State": "string",
   "StatusMessage": "string"
}
```

## Response Elements
<a name="API_DescribeScanJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountId](#API_DescribeScanJob_ResponseSyntax) **   <a name="Backup-DescribeScanJob-response-AccountId"></a>
Returns the account ID that owns the scan job.
Pattern: `^[0-9]{12}$`
Type: String

 ** [BackupVaultArn](#API_DescribeScanJob_ResponseSyntax) **   <a name="Backup-DescribeScanJob-response-BackupVaultArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, `arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`
Type: String

 ** [BackupVaultName](#API_DescribeScanJob_ResponseSyntax) **   <a name="Backup-DescribeScanJob-response-BackupVaultName"></a>
The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created.
Pattern: `^[a-zA-Z0-9\-\_\.]{2,50}$`
Type: String

 ** [CompletionDate](#API_DescribeScanJob_ResponseSyntax) **   <a name="Backup-DescribeScanJob-response-CompletionDate"></a>
The date and time that a backup index finished creation, in Unix format and Coordinated Universal Time (UTC). The value of `CompletionDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp

 ** [ContinuousScanEndTime](#API_DescribeScanJob_ResponseSyntax) **   <a name="Backup-DescribeScanJob-response-ContinuousScanEndTime"></a>
The point in time the scan job scanned up to for a continuous backup.
Type: Timestamp

 ** [ContinuousScanStartTime](#API_DescribeScanJob_ResponseSyntax) **   <a name="Backup-DescribeScanJob-response-ContinuousScanStartTime"></a>
The point in time the scan job started scan from for a continuous backup.
Type: Timestamp

 ** [CreatedBy](#API_DescribeScanJob_ResponseSyntax) **   <a name="Backup-DescribeScanJob-response-CreatedBy"></a>
Contains identifying information about the creation of a scan job, including the backup plan and rule that initiated the scan.
Type: [ScanJobCreator](API_ScanJobCreator.md) object

 ** [CreationDate](#API_DescribeScanJob_ResponseSyntax) **   <a name="Backup-DescribeScanJob-response-CreationDate"></a>
The date and time that a backup index finished creation, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp

 ** [IamRoleArn](#API_DescribeScanJob_ResponseSyntax) **   <a name="Backup-DescribeScanJob-response-IamRoleArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, `arn:aws:iam::123456789012:role/S3Access`.
Type: String

 ** [MalwareScanner](#API_DescribeScanJob_ResponseSyntax) **   <a name="Backup-DescribeScanJob-response-MalwareScanner"></a>
The scanning engine used for the corresponding scan job. Currently only `GUARDUTY` is supported.
Type: String
Valid Values: `GUARDDUTY`

 ** [RecoveryPointArn](#API_DescribeScanJob_ResponseSyntax) **   <a name="Backup-DescribeScanJob-response-RecoveryPointArn"></a>
An ARN that uniquely identifies the target recovery point for scanning.; for example, `arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.
Type: String

 ** [ResourceArn](#API_DescribeScanJob_ResponseSyntax) **   <a name="Backup-DescribeScanJob-response-ResourceArn"></a>
An ARN that uniquely identifies the source resource of the corresponding recovery point ARN.
Type: String

 ** [ResourceName](#API_DescribeScanJob_ResponseSyntax) **   <a name="Backup-DescribeScanJob-response-ResourceName"></a>
The non-unique name of the resource that belongs to the specified backup.
Type: String

 ** [ResourceType](#API_DescribeScanJob_ResponseSyntax) **   <a name="Backup-DescribeScanJob-response-ResourceType"></a>
The type of AWS Resource to be backed up; for example, an Amazon Elastic Block Store (Amazon EBS) volume.
Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`
Type: String
Valid Values: `EBS | EC2 | S3`

 ** [ScanBaseRecoveryPointArn](#API_DescribeScanJob_ResponseSyntax) **   <a name="Backup-DescribeScanJob-response-ScanBaseRecoveryPointArn"></a>
An ARN that uniquely identifies the base recovery point for scanning. This field will only be populated when an incremental scan job has taken place.
Type: String

 ** [ScanId](#API_DescribeScanJob_ResponseSyntax) **   <a name="Backup-DescribeScanJob-response-ScanId"></a>
The scan ID generated by Amazon GuardDuty for the corresponding Scan Job ID request from AWS Backup.
Type: String

 ** [ScanJobId](#API_DescribeScanJob_ResponseSyntax) **   <a name="Backup-DescribeScanJob-response-ScanJobId"></a>
The scan job ID that uniquely identified the request to AWS Backup.
Type: String

 ** [ScanMode](#API_DescribeScanJob_ResponseSyntax) **   <a name="Backup-DescribeScanJob-response-ScanMode"></a>
Specifies the scan type used for the scan job.
Type: String
Valid Values: `FULL_SCAN | INCREMENTAL_SCAN`

 ** [ScannerRoleArn](#API_DescribeScanJob_ResponseSyntax) **   <a name="Backup-DescribeScanJob-response-ScannerRoleArn"></a>
Specifies the scanner IAM role ARN used to for the scan job.
Type: String

 ** [ScanResult](#API_DescribeScanJob_ResponseSyntax) **   <a name="Backup-DescribeScanJob-response-ScanResult"></a>
 Contains the `ScanResultsStatus` for the scanning job and returns `THREATS_FOUND` or `NO_THREATS_FOUND` for completed jobs.
Type: [ScanResultInfo](API_ScanResultInfo.md) object

 ** [State](#API_DescribeScanJob_ResponseSyntax) **   <a name="Backup-DescribeScanJob-response-State"></a>
The current state of a scan job.
Type: String
Valid Values: `CANCELED | COMPLETED | COMPLETED_WITH_ISSUES | CREATED | FAILED | RUNNING`

 ** [StatusMessage](#API_DescribeScanJob_ResponseSyntax) **   <a name="Backup-DescribeScanJob-response-StatusMessage"></a>
A detailed message explaining the status of the job to back up a resource.
Type: String

## Errors
<a name="API_DescribeScanJob_Errors"></a>

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
<a name="API_DescribeScanJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/DescribeScanJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/DescribeScanJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/DescribeScanJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/DescribeScanJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/DescribeScanJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/DescribeScanJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/DescribeScanJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/DescribeScanJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/DescribeScanJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/DescribeScanJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
