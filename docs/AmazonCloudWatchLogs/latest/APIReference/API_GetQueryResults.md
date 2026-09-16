---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetQueryResults.html
---

# GetQueryResults
<a name="API_GetQueryResults"></a>

Returns the results from the specified query.

Only the fields requested in the query are returned, along with a `@ptr` field, which is the identifier for the log record. You can use the value of `@ptr` in a [GetLogRecord](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogRecord.html) operation to get the full log record.

 `GetQueryResults` does not start running a query. To run a query, use [StartQuery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html). For more information about how long results of previous queries are available, see [CloudWatch Logs quotas](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.html).

If the value of the `Status` field in the output is `Running`, this operation returns only partial results. If you see a value of `Scheduled` or `Running` for the status, you can retry the operation later to see the final results.

This operation is used both for retrieving results from interactive queries and from automated scheduled query executions. Scheduled queries use `GetQueryResults` internally to retrieve query results for processing and delivery to configured destinations.

You can retrieve up to 100,000 log event results from a query, if available, by using pagination. Use the `nextToken` returned in the response to request additional pages of results, with each page returning up to 10,000 log events. This is only supported for Logs Insights QL and is currently not supported for PPL and SQL query languages.

If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account to start queries in linked source accounts. For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html).

## Request Syntax
<a name="API_GetQueryResults_RequestSyntax"></a>

```
{
   "maxItems": {{number}},
   "nextToken": "{{string}}",
   "queryId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetQueryResults_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxItems](#API_GetQueryResults_RequestSyntax) **   <a name="CWL-GetQueryResults-request-maxItems"></a>
The maximum number of log events to return in the response. The maximum is 10,000 log events per request. You can retrieve up to 100,000 log event results from a query by paginating with the `nextToken`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000.
Required: No

 ** [nextToken](#API_GetQueryResults_RequestSyntax) **   <a name="CWL-GetQueryResults-request-nextToken"></a>
The token for the next set of items to return. The token expires after 1 hour.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [queryId](#API_GetQueryResults_RequestSyntax) **   <a name="CWL-GetQueryResults-request-queryId"></a>
The ID number of the query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_GetQueryResults_ResponseSyntax"></a>

```
{
   "encryptionKey": "string",
   "nextToken": "string",
   "queryLanguage": "string",
   "results": [
      [
         {
            "field": "string",
            "value": "string"
         }
      ]
   ],
   "statistics": {
      "bytesScanned": number,
      "estimatedBytesSkipped": number,
      "estimatedRecordsSkipped": number,
      "logGroupsScanned": number,
      "recordsMatched": number,
      "recordsScanned": number,
      "resultCount": number
   },
   "status": "string"
}
```

## Response Elements
<a name="API_GetQueryResults_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [encryptionKey](#API_GetQueryResults_ResponseSyntax) **   <a name="CWL-GetQueryResults-response-encryptionKey"></a>
If you associated an AWS KMS key with the CloudWatch Logs Insights query results in this account, this field displays the ARN of the key that's used to encrypt the query results when [StartQuery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html) stores them.
Type: String
Length Constraints: Maximum length of 256.

 ** [nextToken](#API_GetQueryResults_ResponseSyntax) **   <a name="CWL-GetQueryResults-response-nextToken"></a>
If there are more log events remaining in the results, the response includes a `nextToken`. You can use this token in a subsequent `GetQueryResults` request to get the next set of results. You can retrieve up to 100,000 log event results from a query by paginating with this token. This is only supported for Logs Insights QL and is currently not supported for PPL and SQL query languages.
Type: String
Length Constraints: Maximum length of 1024.

 ** [queryLanguage](#API_GetQueryResults_ResponseSyntax) **   <a name="CWL-GetQueryResults-response-queryLanguage"></a>
The query language used for this query. For more information about the query languages that CloudWatch Logs supports, see [Supported query languages](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Languages.html).
Type: String
Valid Values: `CWLI | SQL | PPL`

 ** [results](#API_GetQueryResults_ResponseSyntax) **   <a name="CWL-GetQueryResults-response-results"></a>
The log events that matched the query criteria during the most recent time it ran.
The `results` value is an array of arrays. Each log event is one object in the top-level array. Each of these log event objects is an array of `field`/`value` pairs.
Type: Array of arrays of [ResultField](API_ResultField.md) objects

 ** [statistics](#API_GetQueryResults_ResponseSyntax) **   <a name="CWL-GetQueryResults-response-statistics"></a>
Includes the number of log events scanned by the query, the number of log events that matched the query criteria, and the total number of bytes in the scanned log events. These values reflect the full raw results of the query.
Type: [QueryStatistics](API_QueryStatistics.md) object

 ** [status](#API_GetQueryResults_ResponseSyntax) **   <a name="CWL-GetQueryResults-response-status"></a>
The status of the most recent running of the query. Possible values are `Cancelled`, `Complete`, `Failed`, `Running`, `Scheduled`, `Timeout`, and `Unknown`.
Queries time out after 60 minutes of runtime. To avoid having your queries time out, reduce the time range being searched or partition your query into a number of queries.
Type: String
Valid Values: `Scheduled | Running | Complete | Failed | Cancelled | Timeout | Unknown`

## Errors
<a name="API_GetQueryResults_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## Examples
<a name="API_GetQueryResults_Examples"></a>

### Get results from a recent query
<a name="API_GetQueryResults_Example_1"></a>

The following returns the results from a specified query.

#### Sample Request
<a name="API_GetQueryResults_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: logs.<region>.<domain>
X-Amz-Date: <DATE>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Accept: application/json
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: Logs_20140328.GetQueryResults
{
   "queryId": "12ab3456-12ab-123a-789e-1234567890ab",
   "maxItems": 1000,
   "nextToken": "eEXAMPLEtoken"
}
```

#### Sample Response
<a name="API_GetQueryResults_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "results": [
        [
            {
                "field": "LogEvent1-field1-name",
                "value": "LogEvent1-field1-value"
            },
            {
                "field": "LogEvent1-field2-name",
                "value": "LogEvent1-field2-value"
            },
            ...
            {
                "field": "LogEvent1-fieldX-name",
                "value": "LogEvent1-fieldX-value"
            }
        ],
        [
            {
                "field": "LogEvent2-field1-name",
                "value": "LogEvent2-field1-value"
            },
            {
                "field": "LogEvent2-field2-name",
                "value": "LogEvent2-field2-value"
            },
            ...
            {
                "field": "LogEvent2-fieldX-name",
                "value": "LogEvent2-fieldX-value"
            }
        ],
        [
            {
                "field": "LogEventZ-field1-name",
                "value": "LogEventZ-field1-value"
            },
            {
                "field": "LogEventZ-field2-name",
                "value": "LogEventZ-field2-value"
            },
            ...
            {
                "field": "LogEventZ-fieldX-name",
                "value": "LogEventZ-fieldX-value"
            }
        ]
    ],
    "statistics": {
        "bytesScanned": 81349723,
        "recordsMatched": 360851,
        "recordsScanned": 610956
    },
    "status": "Complete",
    "nextToken": "eEXAMPLEtoken"
}
```

## See Also
<a name="API_GetQueryResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/GetQueryResults)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/GetQueryResults)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/GetQueryResults)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/GetQueryResults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/GetQueryResults)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/GetQueryResults)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/GetQueryResults)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/GetQueryResults)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/GetQueryResults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/GetQueryResults)
