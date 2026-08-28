---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html
---

# StartQuery
<a name="API_StartQuery"></a>

Starts a query of one or more log groups or data sources using CloudWatch Logs Insights. You specify the log groups or data sources and time range to query and the query string to use. You can query up to 10 data sources in a single query.

For more information, see [CloudWatch Logs Insights Query Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html).

After you run a query using `StartQuery`, the query results are stored by CloudWatch Logs. You can use [GetQueryResults](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetQueryResults.html) to retrieve the results of a query, using the `queryId` that `StartQuery` returns.

Interactive queries started with `StartQuery` share concurrency limits with automated scheduled query executions. Both types of queries count toward the same regional concurrent query quota, so high scheduled query activity may affect the availability of concurrent slots for interactive queries.

**Note**
To specify the log groups to query, a `StartQuery` operation must include one of the following:
Either exactly one of the following parameters: `logGroupName`, `logGroupNames`, or `logGroupIdentifiers`
Or the `queryString` must include a `SOURCE` command to select log groups for the query. The `SOURCE` command can select log groups based on log group name prefix, account ID, and log class, or select data sources using dataSource syntax in LogsQL, PPL, and SQL. In LogsQL, the `SOURCE` command also supports filtering by log group tags.
For more information about the `SOURCE` command, see [SOURCE](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Source.html).

If you have associated a AWS KMS key with the query results in this account, then [StartQuery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html) uses that key to encrypt the results when it stores them. If no key is associated with query results, the query results are encrypted with the default CloudWatch Logs encryption method.

Queries time out after 60 minutes of runtime. If your queries are timing out, reduce the time range being searched or partition your query into a number of queries.

If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account to start a query in a linked source account. For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html). For a cross-account `StartQuery` operation, the query definition must be defined in the monitoring account.

You can have up to 100 concurrent CloudWatch Logs insights queries, including queries that have been added to dashboards.

## Request Syntax
<a name="API_StartQuery_RequestSyntax"></a>

```
{
   "endTime": {{number}},
   "limit": {{number}},
   "logGroupIdentifiers": [ "{{string}}" ],
   "logGroupName": "{{string}}",
   "logGroupNames": [ "{{string}}" ],
   "queryLanguage": "{{string}}",
   "queryString": "{{string}}",
   "startTime": {{number}}
}
```

## Request Parameters
<a name="API_StartQuery_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [endTime](#API_StartQuery_RequestSyntax) **   <a name="CWL-StartQuery-request-endTime"></a>
The end of the time range to query. The range is inclusive, so the specified end time is included in the query. Specified as epoch time, the number of seconds since `January 1, 1970, 00:00:00 UTC`.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** [limit](#API_StartQuery_RequestSyntax) **   <a name="CWL-StartQuery-request-limit"></a>
The maximum number of log events to return from the query. The maximum limit is 100,000. The maximum events returned in a single GetQueryResults API call is 10,000 log events per request. You can retrieve up to 100,000 log event results from a query by paginating with the `nextToken`. 100,000 limit is only supported for Logs Insights QL and is currently not supported for PPL and SQL query languages.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100000.
Required: No

 ** [logGroupIdentifiers](#API_StartQuery_RequestSyntax) **   <a name="CWL-StartQuery-request-logGroupIdentifiers"></a>
The list of log groups to query. You can include up to 50 log groups.
You can specify them by the log group name or ARN. If a log group that you're querying is in a source account and you're using a monitoring account, you must specify the ARN of the log group here. The query definition must also be defined in the monitoring account.
If you specify an ARN, use the format arn:aws:logs:*region*:*account-id*:log-group:*log\_group\_name* Don't include an \* at the end.
A `StartQuery` operation must include exactly one of the following parameters: `logGroupName`, `logGroupNames`, or `logGroupIdentifiers`. The exception is queries using the OpenSearch Service SQL query language, where you specify the log group names inside the `querystring` instead of here.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w#+=/:,.@-]*`
Required: No

 ** [logGroupName](#API_StartQuery_RequestSyntax) **   <a name="CWL-StartQuery-request-logGroupName"></a>
The log group on which to perform the query.
A `StartQuery` operation must include exactly one of the following parameters: `logGroupName`, `logGroupNames`, or `logGroupIdentifiers`. The exception is queries using the OpenSearch Service SQL query language, where you specify the log group names inside the `querystring` instead of here.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** [logGroupNames](#API_StartQuery_RequestSyntax) **   <a name="CWL-StartQuery-request-logGroupNames"></a>
The list of log groups to be queried. You can include up to 50 log groups.
A `StartQuery` operation must include exactly one of the following parameters: `logGroupName`, `logGroupNames`, or `logGroupIdentifiers`. The exception is queries using the OpenSearch Service SQL query language, where you specify the log group names inside the `querystring` instead of here.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** [queryLanguage](#API_StartQuery_RequestSyntax) **   <a name="CWL-StartQuery-request-queryLanguage"></a>
Specify the query language to use for this query. The options are Logs Insights QL, OpenSearch PPL, and OpenSearch SQL. For more information about the query languages that CloudWatch Logs supports, see [Supported query languages](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Languages.html).
Type: String
Valid Values: `CWLI | SQL | PPL`
Required: No

 ** [queryString](#API_StartQuery_RequestSyntax) **   <a name="CWL-StartQuery-request-queryString"></a>
The query string to use. For more information, see [CloudWatch Logs Insights Query Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Required: Yes

 ** [startTime](#API_StartQuery_RequestSyntax) **   <a name="CWL-StartQuery-request-startTime"></a>
The beginning of the time range to query. The range is inclusive, so the specified start time is included in the query. Specified as epoch time, the number of seconds since `January 1, 1970, 00:00:00 UTC`.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

## Response Syntax
<a name="API_StartQuery_ResponseSyntax"></a>

```
{
   "queryId": "string"
}
```

## Response Elements
<a name="API_StartQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [queryId](#API_StartQuery_ResponseSyntax) **   <a name="CWL-StartQuery-response-queryId"></a>
The unique ID of the query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_StartQuery_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** LimitExceededException **
You have reached the maximum number of resources that can be created.
HTTP Status Code: 400

 ** MalformedQueryException **
The query string is not valid. Details about this error are displayed in a `QueryCompileError` object. For more information, see [QueryCompileError](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_QueryCompileError.html).
For more information about valid query syntax, see [CloudWatch Logs Insights Query Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html).
 ** queryCompileError **
Reserved.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## Examples
<a name="API_StartQuery_Examples"></a>

### Example: Start a query
<a name="API_StartQuery_Example_1"></a>

This example starts a query of three log groups, specifying the query string and start time. It also limits the results to the most recent 100 matching events.

#### Sample Request
<a name="API_StartQuery_Example_1_Request"></a>

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
X-Amz-Target: Logs_20140328.StartQuery
{
    "limit": 100,
    "logGroupNames": [
        "LogGroupName1",
        "LogGroupName2",
        "LogGroupName3"
    ],
    "queryString": "stats count(*) by eventSource, eventName, awsRegion",
    "startTime": 1546300800,
    "endTime": 1546309800
}
```

#### Sample Response
<a name="API_StartQuery_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "queryId": "12ab3456-12ab-123a-789e-1234567890ab"
}
```

### Example: Start a query
<a name="API_StartQuery_Example_2"></a>

 This example starts a query for a log group ARN and specifies a query string. It also specifies the request start and end times.

#### Sample Request
<a name="API_StartQuery_Example_2_Request"></a>

```
{
    "limit": 100,
    "logGroupIdentifiers": [
        "arn:aws:logs:us-east-1:123456789012:log-group:monitoring-logGroup-1234"
     ],
    "queryString": "stats count(*) by eventSource, eventName, awsRegion",
    "startTime": 1546300800,
    "endTime": 1546309800
}
```

#### Sample Response
<a name="API_StartQuery_Example_2_Response"></a>

```
{
    "queryId": "12ab3456-12ab-123a-789e-1234567890ab"
}
```

### Example: Start a query using field indexing and the source command
<a name="API_StartQuery_Example_3"></a>

This example queries all log groups in the `111122223333` account that have log group names that start with `my-log`. It leverages field indexing so that only log groups and log events known to match the indexed field `transactionId` are processed. Only log events that include the value `tx-001` for the `transactionId` field will be returned.

#### Sample Request
<a name="API_StartQuery_Example_3_Request"></a>

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
X-Amz-Target: Logs_20140328.StartQuery
{
 "queryString":
  "source logGroups(namePrefix: ['my-log'], accountIdentifiers: ['accountId' = '111122223333'])
 | filterIndex transactionId = 'tx-001'",
    "startTime": 1722704400000,
    "endTime": 1722705229849
}
```

## See Also
<a name="API_StartQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/StartQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/StartQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/StartQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/StartQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/StartQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/StartQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/StartQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/StartQuery)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/StartQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/StartQuery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
