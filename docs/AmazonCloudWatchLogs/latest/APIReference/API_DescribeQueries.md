---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeQueries.html
---

# DescribeQueries
<a name="API_DescribeQueries"></a>

Returns a list of CloudWatch Logs Insights queries that are scheduled, running, or have been run recently in this account. You can request all queries or limit it to queries of a specific log group or queries with a certain status.

This operation includes both interactive queries started directly by users and automated queries executed by scheduled query configurations. Scheduled query executions appear in the results alongside manually initiated queries, providing visibility into all query activity in your account.

## Request Syntax
<a name="API_DescribeQueries_RequestSyntax"></a>

```
{
   "logGroupName": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "queryLanguage": "{{string}}",
   "status": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeQueries_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [logGroupName](#API_DescribeQueries_RequestSyntax) **   <a name="CWL-DescribeQueries-request-logGroupName"></a>
Limits the returned queries to only those for the specified log group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** [maxResults](#API_DescribeQueries_RequestSyntax) **   <a name="CWL-DescribeQueries-request-maxResults"></a>
Limits the number of returned queries to the specified number.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_DescribeQueries_RequestSyntax) **   <a name="CWL-DescribeQueries-request-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [queryLanguage](#API_DescribeQueries_RequestSyntax) **   <a name="CWL-DescribeQueries-request-queryLanguage"></a>
Limits the returned queries to only the queries that use the specified query language.
Type: String
Valid Values: `CWLI | SQL | PPL`
Required: No

 ** [status](#API_DescribeQueries_RequestSyntax) **   <a name="CWL-DescribeQueries-request-status"></a>
Limits the returned queries to only those that have the specified status. Valid values are `Cancelled`, `Complete`, `Failed`, `Running`, and `Scheduled`.
Type: String
Valid Values: `Scheduled | Running | Complete | Failed | Cancelled | Timeout | Unknown`
Required: No

## Response Syntax
<a name="API_DescribeQueries_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "queries": [
      {
         "bytesScanned": number,
         "createTime": number,
         "logGroupName": "string",
         "queryDuration": number,
         "queryId": "string",
         "queryLanguage": "string",
         "queryString": "string",
         "status": "string",
         "userIdentity": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeQueries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_DescribeQueries_ResponseSyntax) **   <a name="CWL-DescribeQueries-response-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.

 ** [queries](#API_DescribeQueries_ResponseSyntax) **   <a name="CWL-DescribeQueries-response-queries"></a>
The list of queries that match the request.
Type: Array of [QueryInfo](API_QueryInfo.md) objects

## Errors
<a name="API_DescribeQueries_Errors"></a>

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
<a name="API_DescribeQueries_Examples"></a>

### List the CloudWatch Logs Insights queries for a specific log group
<a name="API_DescribeQueries_Example_1"></a>

The following example lists the successfully completed queries of the log group named `MyLogGroup`.

#### Sample Request
<a name="API_DescribeQueries_Example_1_Request"></a>

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
X-Amz-Target: Logs_20140328.DescribeQueries
{
   "logGroupName": "MyLogGroup",
   "status": "Completed"
}
```

#### Sample Response
<a name="API_DescribeQueries_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "nextToken": "string",
    "queries": [
        {
            "createTime": 1540923785,
            "logGroupName": "MyLogGroup",
            "queryId": "12ab3456-12ab-123a-789e-1234567890ab",
            "queryString": "filter @message like /Exception/ | stats count(*) as @exceptionCount by date_floor(@timestamp, 5m) | sort @exceptionCount desc",
            "status": "Completed",
            "queryDuration": 5200,
            "bytesScanned": 1048576.0,
            "userIdentity": "arn:aws:iam::123456789012:user/example-user"
        },
        {
            "createTime": 1540025601,
            "logGroupName": "MyLogGroup",
            "queryId": "98ab3456-12ab-123a-789e-1234567890ab",
            "queryString": "stats count(*) by eventSource, eventName, awsRegion",
            "status": "Running",
            "queryDuration": 1500,
            "bytesScanned": 524288.0,
            "userIdentity": "arn:aws:iam::123456789012:user/example-user"
        }
    ]
}
```

## See Also
<a name="API_DescribeQueries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/DescribeQueries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/DescribeQueries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DescribeQueries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/DescribeQueries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DescribeQueries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/DescribeQueries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/DescribeQueries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/DescribeQueries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/DescribeQueries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DescribeQueries)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
