---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListRestoreJobSummaries.html
---

# ListRestoreJobSummaries
<a name="API_ListRestoreJobSummaries"></a>

This request obtains a summary of restore jobs created or running within the the most recent 30 days. You can include parameters AccountID, State, ResourceType, AggregationPeriod, MaxResults, or NextToken to filter results.

This request returns a summary that contains Region, Account, State, RestourceType, MessageCategory, StartTime, EndTime, and Count of included jobs.

## Request Syntax
<a name="API_ListRestoreJobSummaries_RequestSyntax"></a>

```
GET /audit/restore-job-summaries?AccountId={{AccountId}}&AggregationPeriod={{AggregationPeriod}}&MaxResults={{MaxResults}}&NextToken={{NextToken}}&ResourceType={{ResourceType}}&State={{State}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRestoreJobSummaries_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AccountId](#API_ListRestoreJobSummaries_RequestSyntax) **   <a name="Backup-ListRestoreJobSummaries-request-uri-AccountId"></a>
Returns the job count for the specified account.
If the request is sent from a member account or an account not part of AWS Organizations, jobs within requestor's account will be returned.
Root, admin, and delegated administrator accounts can use the value ANY to return job counts from every account in the organization.
 `AGGREGATE_ALL` aggregates job counts from all accounts within the authenticated organization, then returns the sum.
Pattern: `^[0-9]{12}$`

 ** [AggregationPeriod](#API_ListRestoreJobSummaries_RequestSyntax) **   <a name="Backup-ListRestoreJobSummaries-request-uri-AggregationPeriod"></a>
The period for the returned results.
+  `ONE_DAY` - The daily job count for the prior 14 days.
+  `SEVEN_DAYS` - The aggregated job count for the prior 7 days.
+  `FOURTEEN_DAYS` - The aggregated job count for prior 14 days.
Valid Values: `ONE_DAY | SEVEN_DAYS | FOURTEEN_DAYS`

 ** [MaxResults](#API_ListRestoreJobSummaries_RequestSyntax) **   <a name="Backup-ListRestoreJobSummaries-request-uri-MaxResults"></a>
This parameter sets the maximum number of items to be returned.
The value is an integer. Range of accepted values is from 1 to 500.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListRestoreJobSummaries_RequestSyntax) **   <a name="Backup-ListRestoreJobSummaries-request-uri-NextToken"></a>
The next item following a partial list of returned resources. For example, if a request is made to return `MaxResults` number of resources, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.

 ** [ResourceType](#API_ListRestoreJobSummaries_RequestSyntax) **   <a name="Backup-ListRestoreJobSummaries-request-uri-ResourceType"></a>
Returns the job count for the specified resource type. Use request `GetSupportedResourceTypes` to obtain strings for supported resource types.
The the value ANY returns count of all resource types.
 `AGGREGATE_ALL` aggregates job counts for all resource types and returns the sum.
The type of AWS resource to be backed up; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.
Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

 ** [State](#API_ListRestoreJobSummaries_RequestSyntax) **   <a name="Backup-ListRestoreJobSummaries-request-uri-State"></a>
This parameter returns the job count for jobs with the specified state.
The the value ANY returns count of all states.
 `AGGREGATE_ALL` aggregates job counts for all states and returns the sum.
Valid Values: `CREATED | PENDING | RUNNING | ABORTED | COMPLETED | FAILED | AGGREGATE_ALL | ANY`

## Request Body
<a name="API_ListRestoreJobSummaries_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRestoreJobSummaries_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AggregationPeriod": "string",
   "NextToken": "string",
   "RestoreJobSummaries": [
      {
         "AccountId": "string",
         "Count": number,
         "EndTime": number,
         "Region": "string",
         "ResourceType": "string",
         "StartTime": number,
         "State": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRestoreJobSummaries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AggregationPeriod](#API_ListRestoreJobSummaries_ResponseSyntax) **   <a name="Backup-ListRestoreJobSummaries-response-AggregationPeriod"></a>
The period for the returned results.
+  `ONE_DAY` - The daily job count for the prior 14 days.
+  `SEVEN_DAYS` - The aggregated job count for the prior 7 days.
+  `FOURTEEN_DAYS` - The aggregated job count for prior 14 days.
Type: String

 ** [NextToken](#API_ListRestoreJobSummaries_ResponseSyntax) **   <a name="Backup-ListRestoreJobSummaries-response-NextToken"></a>
The next item following a partial list of returned resources. For example, if a request is made to return `MaxResults` number of resources, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.
Type: String

 ** [RestoreJobSummaries](#API_ListRestoreJobSummaries_ResponseSyntax) **   <a name="Backup-ListRestoreJobSummaries-response-RestoreJobSummaries"></a>
This return contains a summary that contains Region, Account, State, ResourceType, MessageCategory, StartTime, EndTime, and Count of included jobs.
Type: Array of [RestoreJobSummary](API_RestoreJobSummary.md) objects

## Errors
<a name="API_ListRestoreJobSummaries_Errors"></a>

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
<a name="API_ListRestoreJobSummaries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/ListRestoreJobSummaries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/ListRestoreJobSummaries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ListRestoreJobSummaries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/ListRestoreJobSummaries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ListRestoreJobSummaries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/ListRestoreJobSummaries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/ListRestoreJobSummaries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/ListRestoreJobSummaries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/ListRestoreJobSummaries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ListRestoreJobSummaries)
