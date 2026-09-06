---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateScheduledQuery.html
---

# CreateScheduledQuery
<a name="API_CreateScheduledQuery"></a>

Creates a scheduled query that runs CloudWatch Logs Insights queries at regular intervals. Scheduled queries enable proactive monitoring by automatically executing queries to detect patterns and anomalies in your log data. Query results can be delivered to Amazon S3 for analysis or further processing.

## Request Syntax
<a name="API_CreateScheduledQuery_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "destinationConfiguration": {
      "lookupTableConfiguration": {
         "description": "{{string}}",
         "kmsKeyId": "{{string}}",
         "roleArn": "{{string}}",
         "tableName": "{{string}}",
         "tags": {
            "{{string}}" : "{{string}}"
         }
      },
      "s3Configuration": {
         "destinationIdentifier": "{{string}}",
         "kmsKeyId": "{{string}}",
         "ownerAccountId": "{{string}}",
         "roleArn": "{{string}}"
      }
   },
   "endTimeOffset": {{number}},
   "executionRoleArn": "{{string}}",
   "logGroupIdentifiers": [ "{{string}}" ],
   "name": "{{string}}",
   "queryLanguage": "{{string}}",
   "queryString": "{{string}}",
   "scheduleEndTime": {{number}},
   "scheduleExpression": "{{string}}",
   "scheduleStartTime": {{number}},
   "startTimeOffset": {{number}},
   "state": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "timezone": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateScheduledQuery_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_CreateScheduledQuery_RequestSyntax) **   <a name="CWL-CreateScheduledQuery-request-description"></a>
An optional description for the scheduled query to help identify its purpose and functionality.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [destinationConfiguration](#API_CreateScheduledQuery_RequestSyntax) **   <a name="CWL-CreateScheduledQuery-request-destinationConfiguration"></a>
Configuration for where to deliver query results. Supports Amazon S3 destinations for storing query output and lookup table destinations for automatically refreshing lookup tables with query results. You can configure one or both destination types.
Type: [DestinationConfiguration](API_DestinationConfiguration.md) object
Required: No

 ** [endTimeOffset](#API_CreateScheduledQuery_RequestSyntax) **   <a name="CWL-CreateScheduledQuery-request-endTimeOffset"></a>
The time offset in seconds that defines the end of the lookback period for the query. Together with `startTimeOffset`, this determines the time window relative to the execution time over which the query runs.
Type: Long
Required: No

 ** [executionRoleArn](#API_CreateScheduledQuery_RequestSyntax) **   <a name="CWL-CreateScheduledQuery-request-executionRoleArn"></a>
The ARN of the IAM role that grants permissions to execute the query and deliver results to the specified destination. The role must have permissions to read from the specified log groups and write to the destination.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [logGroupIdentifiers](#API_CreateScheduledQuery_RequestSyntax) **   <a name="CWL-CreateScheduledQuery-request-logGroupIdentifiers"></a>
An array of log group names or ARNs to query. You can specify between 1 and 50 log groups. Log groups can be identified by name or full ARN.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w#+=/:,.@-]*`
Required: No

 ** [name](#API_CreateScheduledQuery_RequestSyntax) **   <a name="CWL-CreateScheduledQuery-request-name"></a>
The name of the scheduled query. The name must be unique within your account and region. Length must be between 1 and 300 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [queryLanguage](#API_CreateScheduledQuery_RequestSyntax) **   <a name="CWL-CreateScheduledQuery-request-queryLanguage"></a>
The query language to use for the scheduled query. Valid values are `CWLI`, `PPL`, and `SQL`.
Type: String
Valid Values: `CWLI | SQL | PPL`
Required: Yes

 ** [queryString](#API_CreateScheduledQuery_RequestSyntax) **   <a name="CWL-CreateScheduledQuery-request-queryString"></a>
The query string to execute. This is the same query syntax used in CloudWatch Logs Insights. Maximum length is 10,000 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Required: Yes

 ** [scheduleEndTime](#API_CreateScheduledQuery_RequestSyntax) **   <a name="CWL-CreateScheduledQuery-request-scheduleEndTime"></a>
The end time for the scheduled query in Unix epoch format. The query will stop executing after this time.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** [scheduleExpression](#API_CreateScheduledQuery_RequestSyntax) **   <a name="CWL-CreateScheduledQuery-request-scheduleExpression"></a>
A cron expression that defines when the scheduled query runs. The expression uses standard cron syntax and supports minute-level precision. Maximum length is 256 characters.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

 ** [scheduleStartTime](#API_CreateScheduledQuery_RequestSyntax) **   <a name="CWL-CreateScheduledQuery-request-scheduleStartTime"></a>
The start time for the scheduled query in Unix epoch format. The query will not execute before this time.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** [startTimeOffset](#API_CreateScheduledQuery_RequestSyntax) **   <a name="CWL-CreateScheduledQuery-request-startTimeOffset"></a>
The time offset in seconds that defines the lookback period for the query. This determines how far back in time the query searches from the execution time.
Type: Long
Required: No

 ** [state](#API_CreateScheduledQuery_RequestSyntax) **   <a name="CWL-CreateScheduledQuery-request-state"></a>
The initial state of the scheduled query. Valid values are `ENABLED` and `DISABLED`. Default is `ENABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [tags](#API_CreateScheduledQuery_RequestSyntax) **   <a name="CWL-CreateScheduledQuery-request-tags"></a>
Key-value pairs to associate with the scheduled query for resource management and cost allocation.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]+)$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** [timezone](#API_CreateScheduledQuery_RequestSyntax) **   <a name="CWL-CreateScheduledQuery-request-timezone"></a>
The timezone for evaluating the schedule expression. This determines when the scheduled query executes relative to the specified timezone.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_CreateScheduledQuery_ResponseSyntax"></a>

```
{
   "scheduledQueryArn": "string",
   "state": "string"
}
```

## Response Elements
<a name="API_CreateScheduledQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [scheduledQueryArn](#API_CreateScheduledQuery_ResponseSyntax) **   <a name="CWL-CreateScheduledQuery-response-scheduledQueryArn"></a>
The ARN of the created scheduled query.
Type: String

 ** [state](#API_CreateScheduledQuery_ResponseSyntax) **   <a name="CWL-CreateScheduledQuery-response-state"></a>
The current state of the scheduled query.
Type: String
Valid Values: `ENABLED | DISABLED`

## Errors
<a name="API_CreateScheduledQuery_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** ConflictException **
This operation attempted to create a resource that already exists.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred while processing the request. This exception is returned when the service encounters an unexpected condition that prevents it from fulfilling the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
This request exceeds a service quota.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 400

 ** ValidationException **
One of the parameters for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_CreateScheduledQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/CreateScheduledQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/CreateScheduledQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/CreateScheduledQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/CreateScheduledQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/CreateScheduledQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/CreateScheduledQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/CreateScheduledQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/CreateScheduledQuery)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/CreateScheduledQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/CreateScheduledQuery)
