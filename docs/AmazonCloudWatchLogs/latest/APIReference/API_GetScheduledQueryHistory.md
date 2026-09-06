---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetScheduledQueryHistory.html
---

# GetScheduledQueryHistory
<a name="API_GetScheduledQueryHistory"></a>

Retrieves the execution history of a scheduled query within a specified time range, including query results and destination processing status.

## Request Syntax
<a name="API_GetScheduledQueryHistory_RequestSyntax"></a>

```
{
   "endTime": {{number}},
   "executionStatuses": [ "{{string}}" ],
   "identifier": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "startTime": {{number}}
}
```

## Request Parameters
<a name="API_GetScheduledQueryHistory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [endTime](#API_GetScheduledQueryHistory_RequestSyntax) **   <a name="CWL-GetScheduledQueryHistory-request-endTime"></a>
The end time for the history query in Unix epoch format.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** [executionStatuses](#API_GetScheduledQueryHistory_RequestSyntax) **   <a name="CWL-GetScheduledQueryHistory-request-executionStatuses"></a>
An array of execution statuses to filter the history results. Only executions with the specified statuses are returned.
Type: Array of strings
Valid Values: `Running | InvalidQuery | Complete | Failed | Timeout`
Required: No

 ** [identifier](#API_GetScheduledQueryHistory_RequestSyntax) **   <a name="CWL-GetScheduledQueryHistory-request-identifier"></a>
The ARN or name of the scheduled query to retrieve history for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [maxResults](#API_GetScheduledQueryHistory_RequestSyntax) **   <a name="CWL-GetScheduledQueryHistory-request-maxResults"></a>
The maximum number of history records to return. Valid range is 1 to 1000.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_GetScheduledQueryHistory_RequestSyntax) **   <a name="CWL-GetScheduledQueryHistory-request-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [startTime](#API_GetScheduledQueryHistory_RequestSyntax) **   <a name="CWL-GetScheduledQueryHistory-request-startTime"></a>
The start time for the history query in Unix epoch format.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

## Response Syntax
<a name="API_GetScheduledQueryHistory_ResponseSyntax"></a>

```
{
   "name": "string",
   "nextToken": "string",
   "scheduledQueryArn": "string",
   "triggerHistory": [
      {
         "destinations": [
            {
               "destinationIdentifier": "string",
               "destinationType": "string",
               "errorMessage": "string",
               "processedIdentifier": "string",
               "status": "string"
            }
         ],
         "errorMessage": "string",
         "executionStatus": "string",
         "queryId": "string",
         "triggeredTimestamp": number
      }
   ]
}
```

## Response Elements
<a name="API_GetScheduledQueryHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [name](#API_GetScheduledQueryHistory_ResponseSyntax) **   <a name="CWL-GetScheduledQueryHistory-response-name"></a>
The name of the scheduled query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.

 ** [nextToken](#API_GetScheduledQueryHistory_ResponseSyntax) **   <a name="CWL-GetScheduledQueryHistory-response-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.

 ** [scheduledQueryArn](#API_GetScheduledQueryHistory_ResponseSyntax) **   <a name="CWL-GetScheduledQueryHistory-response-scheduledQueryArn"></a>
The ARN of the scheduled query.
Type: String

 ** [triggerHistory](#API_GetScheduledQueryHistory_ResponseSyntax) **   <a name="CWL-GetScheduledQueryHistory-response-triggerHistory"></a>
An array of execution history records for the scheduled query.
Type: Array of [TriggerHistoryRecord](API_TriggerHistoryRecord.md) objects

## Errors
<a name="API_GetScheduledQueryHistory_Errors"></a>

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
<a name="API_GetScheduledQueryHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/GetScheduledQueryHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/GetScheduledQueryHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/GetScheduledQueryHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/GetScheduledQueryHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/GetScheduledQueryHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/GetScheduledQueryHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/GetScheduledQueryHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/GetScheduledQueryHistory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/GetScheduledQueryHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/GetScheduledQueryHistory)
