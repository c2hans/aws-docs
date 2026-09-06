---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListBackupJobSummaries.html
---

# ListBackupJobSummaries
<a name="API_ListBackupJobSummaries"></a>

This is a request for a summary of backup jobs created or running within the most recent 14 days. You can include parameters AccountID, State, ResourceType, MessageCategory, AggregationPeriod, MaxResults, or NextToken to filter results.

This request returns a summary that contains Region, Account, State, ResourceType, MessageCategory, StartTime, EndTime, and Count of included jobs.

## Request Syntax
<a name="API_ListBackupJobSummaries_RequestSyntax"></a>

```
GET /audit/backup-job-summaries?AccountId={{AccountId}}&AggregationPeriod={{AggregationPeriod}}&MaxResults={{MaxResults}}&MessageCategory={{MessageCategory}}&NextToken={{NextToken}}&ResourceType={{ResourceType}}&State={{State}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListBackupJobSummaries_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AccountId](#API_ListBackupJobSummaries_RequestSyntax) **   <a name="Backup-ListBackupJobSummaries-request-uri-AccountId"></a>
Returns the job count for the specified account.
If the request is sent from a member account or an account not part of AWS Organizations, jobs within requestor's account will be returned.
Root, admin, and delegated administrator accounts can use the value ANY to return job counts from every account in the organization.
 `AGGREGATE_ALL` aggregates job counts from all accounts within the authenticated organization, then returns the sum.
Pattern: `^[0-9]{12}$`

 ** [AggregationPeriod](#API_ListBackupJobSummaries_RequestSyntax) **   <a name="Backup-ListBackupJobSummaries-request-uri-AggregationPeriod"></a>
The period for the returned results.
+  `ONE_DAY` - The daily job count for the prior 14 days.
+  `SEVEN_DAYS` - The aggregated job count for the prior 7 days.
+  `FOURTEEN_DAYS` - The aggregated job count for prior 14 days.
Valid Values: `ONE_DAY | SEVEN_DAYS | FOURTEEN_DAYS`

 ** [MaxResults](#API_ListBackupJobSummaries_RequestSyntax) **   <a name="Backup-ListBackupJobSummaries-request-uri-MaxResults"></a>
The maximum number of items to be returned.
The value is an integer. Range of accepted values is from 1 to 500.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [MessageCategory](#API_ListBackupJobSummaries_RequestSyntax) **   <a name="Backup-ListBackupJobSummaries-request-uri-MessageCategory"></a>
This parameter returns the job count for the specified message category.
Example accepted strings include `AccessDenied`, `Success`, and `InvalidParameters`. See [Monitoring](https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html) for a list of accepted MessageCategory strings.
The the value ANY returns count of all message categories.
 `AGGREGATE_ALL` aggregates job counts for all message categories and returns the sum.

 ** [NextToken](#API_ListBackupJobSummaries_RequestSyntax) **   <a name="Backup-ListBackupJobSummaries-request-uri-NextToken"></a>
The next item following a partial list of returned resources. For example, if a request is made to return `MaxResults` number of resources, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.

 ** [ResourceType](#API_ListBackupJobSummaries_RequestSyntax) **   <a name="Backup-ListBackupJobSummaries-request-uri-ResourceType"></a>
Returns the job count for the specified resource type. Use request `GetSupportedResourceTypes` to obtain strings for supported resource types.
The the value ANY returns count of all resource types.
 `AGGREGATE_ALL` aggregates job counts for all resource types and returns the sum.
The type of AWS resource to be backed up; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.
Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

 ** [State](#API_ListBackupJobSummaries_RequestSyntax) **   <a name="Backup-ListBackupJobSummaries-request-uri-State"></a>
This parameter returns the job count for jobs with the specified state.
The the value ANY returns count of all states.
 `AGGREGATE_ALL` aggregates job counts for all states and returns the sum.
 `Completed with issues` is a status found only in the AWS Backup console. For API, this status refers to jobs with a state of `COMPLETED` and a `MessageCategory` with a value other than `SUCCESS`; that is, the status is completed but comes with a status message. To obtain the job count for `Completed with issues`, run two GET requests, and subtract the second, smaller number:
GET /audit/backup-job-summaries?AggregationPeriod=FOURTEEN\_DAYS&State=COMPLETED
GET /audit/backup-job-summaries?AggregationPeriod=FOURTEEN\_DAYS&MessageCategory=SUCCESS&State=COMPLETED
Valid Values: `CREATED | PENDING | RUNNING | ABORTING | ABORTED | COMPLETED | FAILED | EXPIRED | PARTIAL | AGGREGATE_ALL | ANY`

## Request Body
<a name="API_ListBackupJobSummaries_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListBackupJobSummaries_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AggregationPeriod": "string",
   "BackupJobSummaries": [
      {
         "AccountId": "string",
         "Count": number,
         "EndTime": number,
         "MessageCategory": "string",
         "Region": "string",
         "ResourceType": "string",
         "StartTime": number,
         "State": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListBackupJobSummaries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AggregationPeriod](#API_ListBackupJobSummaries_ResponseSyntax) **   <a name="Backup-ListBackupJobSummaries-response-AggregationPeriod"></a>
The period for the returned results.
+  `ONE_DAY` - The daily job count for the prior 14 days.
+  `SEVEN_DAYS` - The aggregated job count for the prior 7 days.
+  `FOURTEEN_DAYS` - The aggregated job count for prior 14 days.
Type: String

 ** [BackupJobSummaries](#API_ListBackupJobSummaries_ResponseSyntax) **   <a name="Backup-ListBackupJobSummaries-response-BackupJobSummaries"></a>
The summary information.
Type: Array of [BackupJobSummary](API_BackupJobSummary.md) objects

 ** [NextToken](#API_ListBackupJobSummaries_ResponseSyntax) **   <a name="Backup-ListBackupJobSummaries-response-NextToken"></a>
The next item following a partial list of returned resources. For example, if a request is made to return `MaxResults` number of resources, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.
Type: String

## Errors
<a name="API_ListBackupJobSummaries_Errors"></a>

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
<a name="API_ListBackupJobSummaries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/ListBackupJobSummaries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/ListBackupJobSummaries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ListBackupJobSummaries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/ListBackupJobSummaries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ListBackupJobSummaries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/ListBackupJobSummaries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/ListBackupJobSummaries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/ListBackupJobSummaries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/ListBackupJobSummaries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ListBackupJobSummaries)
