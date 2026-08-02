---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetScheduledQuery.html
---

# GetScheduledQuery
<a name="API_GetScheduledQuery"></a>

Retrieves details about a specific scheduled query, including its configuration, execution status, and metadata.

## Request Syntax
<a name="API_GetScheduledQuery_RequestSyntax"></a>

```
{
   "identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_GetScheduledQuery_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [identifier](#API_GetScheduledQuery_RequestSyntax) **   <a name="CWL-GetScheduledQuery-request-identifier"></a>
The ARN or name of the scheduled query to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

## Response Syntax
<a name="API_GetScheduledQuery_ResponseSyntax"></a>

```
{
   "creationTime": number,
   "description": "string",
   "destinationConfiguration": {
      "s3Configuration": {
         "destinationIdentifier": "string",
         "kmsKeyId": "string",
         "ownerAccountId": "string",
         "roleArn": "string"
      }
   },
   "endTimeOffset": number,
   "executionRoleArn": "string",
   "lastExecutionStatus": "string",
   "lastTriggeredTime": number,
   "lastUpdatedTime": number,
   "logGroupIdentifiers": [ "string" ],
   "name": "string",
   "queryLanguage": "string",
   "queryString": "string",
   "scheduledQueryArn": "string",
   "scheduleEndTime": number,
   "scheduleExpression": "string",
   "scheduleStartTime": number,
   "scheduleType": "string",
   "startTimeOffset": number,
   "state": "string",
   "timezone": "string"
}
```

## Response Elements
<a name="API_GetScheduledQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_GetScheduledQuery_ResponseSyntax) **   <a name="CWL-GetScheduledQuery-response-creationTime"></a>
The timestamp when the scheduled query was created.
Type: Long
Valid Range: Minimum value of 0.

 ** [description](#API_GetScheduledQuery_ResponseSyntax) **   <a name="CWL-GetScheduledQuery-response-description"></a>
The description of the scheduled query.
Type: String
Length Constraints: Maximum length of 1024.

 ** [destinationConfiguration](#API_GetScheduledQuery_ResponseSyntax) **   <a name="CWL-GetScheduledQuery-response-destinationConfiguration"></a>
Configuration for where query results are delivered.
Type: [DestinationConfiguration](API_DestinationConfiguration.md) object

 ** [endTimeOffset](#API_GetScheduledQuery_ResponseSyntax) **   <a name="CWL-GetScheduledQuery-response-endTimeOffset"></a>
The time offset in seconds that defines the end of the lookback period for the query.
Type: Long

 ** [executionRoleArn](#API_GetScheduledQuery_ResponseSyntax) **   <a name="CWL-GetScheduledQuery-response-executionRoleArn"></a>
The ARN of the IAM role used to execute the query and deliver results.
Type: String
Length Constraints: Minimum length of 1.

 ** [lastExecutionStatus](#API_GetScheduledQuery_ResponseSyntax) **   <a name="CWL-GetScheduledQuery-response-lastExecutionStatus"></a>
The status of the most recent execution of the scheduled query.
Type: String
Valid Values: `Running | InvalidQuery | Complete | Failed | Timeout`

 ** [lastTriggeredTime](#API_GetScheduledQuery_ResponseSyntax) **   <a name="CWL-GetScheduledQuery-response-lastTriggeredTime"></a>
The timestamp when the scheduled query was last executed.
Type: Long
Valid Range: Minimum value of 0.

 ** [lastUpdatedTime](#API_GetScheduledQuery_ResponseSyntax) **   <a name="CWL-GetScheduledQuery-response-lastUpdatedTime"></a>
The timestamp when the scheduled query was last updated.
Type: Long
Valid Range: Minimum value of 0.

 ** [logGroupIdentifiers](#API_GetScheduledQuery_ResponseSyntax) **   <a name="CWL-GetScheduledQuery-response-logGroupIdentifiers"></a>
The log groups queried by the scheduled query.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w#+=/:,.@-]*`

 ** [name](#API_GetScheduledQuery_ResponseSyntax) **   <a name="CWL-GetScheduledQuery-response-name"></a>
The name of the scheduled query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.

 ** [queryLanguage](#API_GetScheduledQuery_ResponseSyntax) **   <a name="CWL-GetScheduledQuery-response-queryLanguage"></a>
The query language used by the scheduled query.
Type: String
Valid Values: `CWLI | SQL | PPL`

 ** [queryString](#API_GetScheduledQuery_ResponseSyntax) **   <a name="CWL-GetScheduledQuery-response-queryString"></a>
The query string executed by the scheduled query.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.

 ** [scheduledQueryArn](#API_GetScheduledQuery_ResponseSyntax) **   <a name="CWL-GetScheduledQuery-response-scheduledQueryArn"></a>
The ARN of the scheduled query.
Type: String

 ** [scheduleEndTime](#API_GetScheduledQuery_ResponseSyntax) **   <a name="CWL-GetScheduledQuery-response-scheduleEndTime"></a>
The end time for the scheduled query in Unix epoch format.
Type: Long
Valid Range: Minimum value of 0.

 ** [scheduleExpression](#API_GetScheduledQuery_ResponseSyntax) **   <a name="CWL-GetScheduledQuery-response-scheduleExpression"></a>
The cron expression that defines when the scheduled query runs.
Type: String
Length Constraints: Maximum length of 256.

 ** [scheduleStartTime](#API_GetScheduledQuery_ResponseSyntax) **   <a name="CWL-GetScheduledQuery-response-scheduleStartTime"></a>
The start time for the scheduled query in Unix epoch format.
Type: Long
Valid Range: Minimum value of 0.

 ** [scheduleType](#API_GetScheduledQuery_ResponseSyntax) **   <a name="CWL-GetScheduledQuery-response-scheduleType"></a>
The schedule type of the scheduled query. Valid values are `CUSTOMER_MANAGED` and `AWS_MANAGED`.
Type: String
Valid Values: `CUSTOMER_MANAGED | AWS_MANAGED`

 ** [startTimeOffset](#API_GetScheduledQuery_ResponseSyntax) **   <a name="CWL-GetScheduledQuery-response-startTimeOffset"></a>
The time offset in seconds that defines the lookback period for the query.
Type: Long

 ** [state](#API_GetScheduledQuery_ResponseSyntax) **   <a name="CWL-GetScheduledQuery-response-state"></a>
The current state of the scheduled query.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [timezone](#API_GetScheduledQuery_ResponseSyntax) **   <a name="CWL-GetScheduledQuery-response-timezone"></a>
The timezone used for evaluating the schedule expression.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_GetScheduledQuery_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred while processing the request. This exception is returned when the service encounters an unexpected condition that prevents it from fulfilling the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 400

 ** ValidationException **
One of the parameters for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_GetScheduledQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/GetScheduledQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/GetScheduledQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/GetScheduledQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/GetScheduledQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/GetScheduledQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/GetScheduledQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/GetScheduledQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/GetScheduledQuery)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/GetScheduledQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/GetScheduledQuery)
