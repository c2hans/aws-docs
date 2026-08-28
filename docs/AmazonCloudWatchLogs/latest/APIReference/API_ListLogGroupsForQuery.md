---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListLogGroupsForQuery.html
---

# ListLogGroupsForQuery
<a name="API_ListLogGroupsForQuery"></a>

Returns a list of the log groups that were analyzed during a single CloudWatch Logs Insights query. This can be useful for queries that use log group name prefixes or the `filterIndex` command, because the log groups are dynamically selected in these cases.

For more information about field indexes, see [Create field indexes to improve query performance and reduce costs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing.html).

## Request Syntax
<a name="API_ListLogGroupsForQuery_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "queryId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListLogGroupsForQuery_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListLogGroupsForQuery_RequestSyntax) **   <a name="CWL-ListLogGroupsForQuery-request-maxResults"></a>
Limits the number of returned log groups to the specified number.
Type: Integer
Valid Range: Minimum value of 50. Maximum value of 500.
Required: No

 ** [nextToken](#API_ListLogGroupsForQuery_RequestSyntax) **   <a name="CWL-ListLogGroupsForQuery-request-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [queryId](#API_ListLogGroupsForQuery_RequestSyntax) **   <a name="CWL-ListLogGroupsForQuery-request-queryId"></a>
The ID of the query to use. This query ID is from the response to your [StartQuery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html) operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_ListLogGroupsForQuery_ResponseSyntax"></a>

```
{
   "logGroupIdentifiers": [ "string" ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListLogGroupsForQuery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [logGroupIdentifiers](#API_ListLogGroupsForQuery_ResponseSyntax) **   <a name="CWL-ListLogGroupsForQuery-response-logGroupIdentifiers"></a>
An array of the names and ARNs of the log groups that were processed in the query.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w#+=/:,.@-]*`

 ** [nextToken](#API_ListLogGroupsForQuery_ResponseSyntax) **   <a name="CWL-ListLogGroupsForQuery-response-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_ListLogGroupsForQuery_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 400

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
<a name="API_ListLogGroupsForQuery_Examples"></a>

### To list the log groups that were analyzed during a specific query
<a name="API_ListLogGroupsForQuery_Example_1"></a>

The following examplereturns the log groups that were analyzed during the query with the `71bacb5a-30f1-4ed6-9959-2797EXAMPLE` ID.

#### Sample Request
<a name="API_ListLogGroupsForQuery_Example_1_Request"></a>

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
X-Amz-Target: Logs_20140328.ListLogGroupsForQuery
{
  "queryId": "71bacb5a-30f1-4ed6-9959-2797EXAMPLE"
}
```

#### Sample Response
<a name="API_ListLogGroupsForQuery_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "logGroupIdentifiers": [
    "arn:aws:logs:us-east-1:112233445566:log-group:/aws/lambda/applogs",
    "arn:aws:logs:us-east-1:112233445566:log-group:/aws/lambda/servicelogs",
    "arn:aws:logs:us-east-1:112233445566:log-group:/aws/lambda/errorlogs"
  ]
}
```

## See Also
<a name="API_ListLogGroupsForQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/ListLogGroupsForQuery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/ListLogGroupsForQuery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/ListLogGroupsForQuery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/ListLogGroupsForQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/ListLogGroupsForQuery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/ListLogGroupsForQuery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/ListLogGroupsForQuery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/ListLogGroupsForQuery)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/ListLogGroupsForQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/ListLogGroupsForQuery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
