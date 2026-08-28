---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListScanJobs.html
---

# ListScanJobs
<a name="API_ListScanJobs"></a>

Returns a list of existing scan jobs for an authenticated account for the last 30 days.

## Request Syntax
<a name="API_ListScanJobs_RequestSyntax"></a>

```
GET /scan/jobs?ByAccountId={{ByAccountId}}&ByBackupVaultName={{ByBackupVaultName}}&ByCompleteAfter={{ByCompleteAfter}}&ByCompleteBefore={{ByCompleteBefore}}&ByMalwareScanner={{ByMalwareScanner}}&ByRecoveryPointArn={{ByRecoveryPointArn}}&ByResourceArn={{ByResourceArn}}&ByResourceType={{ByResourceType}}&ByScanResultStatus={{ByScanResultStatus}}&ByState={{ByState}}&MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListScanJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ByAccountId](#API_ListScanJobs_RequestSyntax) **   <a name="Backup-ListScanJobs-request-uri-ByAccountId"></a>
The account ID to list the jobs from. Returns only backup jobs associated with the specified account ID.
If used from an AWS Organizations management account, passing `*` returns all jobs across the organization.
Pattern: `^[0-9]{12}$`

 ** [ByBackupVaultName](#API_ListScanJobs_RequestSyntax) **   <a name="Backup-ListScanJobs-request-uri-ByBackupVaultName"></a>
Returns only scan jobs that will be stored in the specified backup vault. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created.
Pattern: `^[a-zA-Z0-9\-\_\.]{2,50}$`

 ** [ByCompleteAfter](#API_ListScanJobs_RequestSyntax) **   <a name="Backup-ListScanJobs-request-uri-ByCompleteAfter"></a>
Returns only scan jobs completed after a date expressed in Unix format and Coordinated Universal Time (UTC).

 ** [ByCompleteBefore](#API_ListScanJobs_RequestSyntax) **   <a name="Backup-ListScanJobs-request-uri-ByCompleteBefore"></a>
Returns only backup jobs completed before a date expressed in Unix format and Coordinated Universal Time (UTC).

 ** [ByMalwareScanner](#API_ListScanJobs_RequestSyntax) **   <a name="Backup-ListScanJobs-request-uri-ByMalwareScanner"></a>
Returns only the scan jobs for the specified malware scanner. Currently only supports `GUARDDUTY`.
Valid Values: `GUARDDUTY`

 ** [ByRecoveryPointArn](#API_ListScanJobs_RequestSyntax) **   <a name="Backup-ListScanJobs-request-uri-ByRecoveryPointArn"></a>
Returns only the scan jobs that are ran against the specified recovery point.

 ** [ByResourceArn](#API_ListScanJobs_RequestSyntax) **   <a name="Backup-ListScanJobs-request-uri-ByResourceArn"></a>
Returns only scan jobs that match the specified resource Amazon Resource Name (ARN).

 ** [ByResourceType](#API_ListScanJobs_RequestSyntax) **   <a name="Backup-ListScanJobs-request-uri-ByResourceType"></a>
Returns restore testing selections by the specified restore testing plan name.
+  `EBS`for Amazon Elastic Block Store
+  `EC2`for Amazon Elastic Compute Cloud
+  `S3`for Amazon Simple Storage Service (Amazon S3)
Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`
Valid Values: `EBS | EC2 | S3`

 ** [ByScanResultStatus](#API_ListScanJobs_RequestSyntax) **   <a name="Backup-ListScanJobs-request-uri-ByScanResultStatus"></a>
Returns only the scan jobs for the specified scan results:
+  `THREATS_FOUND`
+  `NO_THREATS_FOUND`
Valid Values: `NO_THREATS_FOUND | THREATS_FOUND | UNKNOWN`

 ** [ByState](#API_ListScanJobs_RequestSyntax) **   <a name="Backup-ListScanJobs-request-uri-ByState"></a>
Returns only the scan jobs for the specified scanning job state.
Valid Values: `CANCELED | COMPLETED | COMPLETED_WITH_ISSUES | CREATED | FAILED | RUNNING`

 ** [MaxResults](#API_ListScanJobs_RequestSyntax) **   <a name="Backup-ListScanJobs-request-uri-MaxResults"></a>
The maximum number of items to be returned.
Valid Range: Minimum value of 1. Maximum value of 1000.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListScanJobs_RequestSyntax) **   <a name="Backup-ListScanJobs-request-uri-NextToken"></a>
The next item following a partial list of returned items. For example, if a request is made to return `MaxResults` number of items, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.

## Request Body
<a name="API_ListScanJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListScanJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ScanJobs": [
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
   ]
}
```

## Response Elements
<a name="API_ListScanJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListScanJobs_ResponseSyntax) **   <a name="Backup-ListScanJobs-response-NextToken"></a>
The next item following a partial list of returned items. For example, if a request is made to return `MaxResults` number of items, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.
Type: String

 ** [ScanJobs](#API_ListScanJobs_ResponseSyntax) **   <a name="Backup-ListScanJobs-response-ScanJobs"></a>
An array of structures containing metadata about your scan jobs returned in JSON format.
Type: Array of [ScanJob](API_ScanJob.md) objects

## Errors
<a name="API_ListScanJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_ListScanJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/ListScanJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/ListScanJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ListScanJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/ListScanJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ListScanJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/ListScanJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/ListScanJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/ListScanJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/ListScanJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ListScanJobs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
