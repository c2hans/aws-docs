---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutQueryDefinition.html
---

# PutQueryDefinition
<a name="API_PutQueryDefinition"></a>

Creates or updates a query definition for CloudWatch Logs Insights. For more information, see [Analyzing Log Data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html).

To update a query definition, specify its `queryDefinitionId` in your request. The values of `name`, `queryString`, and `logGroupNames` are changed to the values that you specify in your update operation. No current values are retained from the current query definition. For example, imagine updating a current query definition that includes log groups. If you don't specify the `logGroupNames` parameter in your update operation, the query definition changes to contain no log groups.

You must have the `logs:PutQueryDefinition` permission to be able to perform this operation.

## Request Syntax
<a name="API_PutQueryDefinition_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "logGroupNames": [ "{{string}}" ],
   "name": "{{string}}",
   "parameters": [
      {
         "defaultValue": "{{string}}",
         "description": "{{string}}",
         "name": "{{string}}"
      }
   ],
   "queryDefinitionId": "{{string}}",
   "queryLanguage": "{{string}}",
   "queryString": "{{string}}"
}
```

## Request Parameters
<a name="API_PutQueryDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_PutQueryDefinition_RequestSyntax) **   <a name="CWL-PutQueryDefinition-request-clientToken"></a>
Used as an idempotency token, to avoid returning an exception if the service receives the same request twice because of a network error.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 128.
Pattern: `\S{36,128}`
Required: No

 ** [logGroupNames](#API_PutQueryDefinition_RequestSyntax) **   <a name="CWL-PutQueryDefinition-request-logGroupNames"></a>
Use this parameter to include specific log groups as part of your query definition. If your query uses the OpenSearch Service query language, you specify the log group names inside the `querystring` instead of here.
If you are updating an existing query definition for the Logs Insights QL or OpenSearch Service PPL and you omit this parameter, then the updated definition will contain no log groups.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** [name](#API_PutQueryDefinition_RequestSyntax) **   <a name="CWL-PutQueryDefinition-request-name"></a>
A name for the query definition. If you are saving numerous query definitions, we recommend that you name them. This way, you can find the ones you want by using the first part of the name as a filter in the `queryDefinitionNamePrefix` parameter of [DescribeQueryDefinitions](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeQueryDefinitions.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [parameters](#API_PutQueryDefinition_RequestSyntax) **   <a name="CWL-PutQueryDefinition-request-parameters"></a>
Use this parameter to include specific query parameters as part of your query definition. Query parameters are supported only for Logs Insights QL queries. Query parameters allow you to use placeholder variables in your query string that are substituted with values at execution time. Use the `{{parameterName}}` syntax in your query string to reference a parameter.
Type: Array of [QueryParameter](API_QueryParameter.md) objects
Array Members: Maximum number of 20 items.
Required: No

 ** [queryDefinitionId](#API_PutQueryDefinition_RequestSyntax) **   <a name="CWL-PutQueryDefinition-request-queryDefinitionId"></a>
If you are updating a query definition, use this parameter to specify the ID of the query definition that you want to update. You can use [DescribeQueryDefinitions](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeQueryDefinitions.html) to retrieve the IDs of your saved query definitions.
If you are creating a query definition, do not specify this parameter. CloudWatch generates a unique ID for the new query definition and include it in the response to this operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [queryLanguage](#API_PutQueryDefinition_RequestSyntax) **   <a name="CWL-PutQueryDefinition-request-queryLanguage"></a>
Specify the query language to use for this query. The options are Logs Insights QL, OpenSearch PPL, and OpenSearch SQL. For more information about the query languages that CloudWatch Logs supports, see [Supported query languages](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Languages.html).
Type: String
Valid Values: `CWLI | SQL | PPL`
Required: No

 ** [queryString](#API_PutQueryDefinition_RequestSyntax) **   <a name="CWL-PutQueryDefinition-request-queryString"></a>
The query string to use for this definition. For more information, see [CloudWatch Logs Insights Query Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Required: Yes

## Response Syntax
<a name="API_PutQueryDefinition_ResponseSyntax"></a>

```
{
   "queryDefinitionId": "string"
}
```

## Response Elements
<a name="API_PutQueryDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [queryDefinitionId](#API_PutQueryDefinition_ResponseSyntax) **   <a name="CWL-PutQueryDefinition-response-queryDefinitionId"></a>
The ID of the query definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_PutQueryDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** LimitExceededException **
You have reached the maximum number of resources that can be created.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## Examples
<a name="API_PutQueryDefinition_Examples"></a>

### Create a new query definition
<a name="API_PutQueryDefinition_Example_1"></a>

This example creates a query definition.

#### Sample Request
<a name="API_PutQueryDefinition_Example_1_Request"></a>

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
X-Amz-Target: Logs_20140328.PutQueryDefinition
{
   "querystring": "stats sum(packets) as packetsTransferred by srcAddr, dstAddr | sort packetsTransferred  desc | limit 15",
   "name": "VPC-top15-packet-transfers",
   "logGroupNames": [ "VPC_Flow_Log1", "VPC_Flow_Log2" ],
}
```

#### Sample Response
<a name="API_PutQueryDefinition_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "queryDefinitionId": "123456ab-12ab-123a-789e-1234567890ab"
}
```

### Update a query definition
<a name="API_PutQueryDefinition_Example_2"></a>

This example updates the query definition that was created in the previous example. The query is changed to show the top 25 responses instead of the top 15, and the name of the query is changed to reflect this.

#### Sample Request
<a name="API_PutQueryDefinition_Example_2_Request"></a>

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
X-Amz-Target: Logs_20140328.PutQueryDefinition
{
   "queryDefinitionId": "123456ab-12ab-123a-789e-1234567890ab",
   "querystring": "stats sum(packets) as packetsTransferred by srcAddr, dstAddr | sort packetsTransferred  desc | limit 25",
   "name": "VPC-top25-packet-transfers",
}
```

#### Sample Response
<a name="API_PutQueryDefinition_Example_2_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "success": True
}
```

### Create a query definition with parameters
<a name="API_PutQueryDefinition_Example_3"></a>

This example creates a parameterized query definition. The query string includes parameter placeholders that are substituted at execution time.

#### Sample Request
<a name="API_PutQueryDefinition_Example_3_Request"></a>

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
X-Amz-Target: Logs_20140328.PutQueryDefinition
{
   "name": "ErrorsByLevel",
   "queryString": "fields @timestamp, @message | filter level = {{logLevel}}",
   "logGroupNames": [ "/aws/lambda/my-function" ],
   "parameters": [
      {
         "name": "logLevel",
         "defaultValue": "ERROR",
         "description": "Log level to filter (ERROR, WARN, INFO, DEBUG)"
      }
   ]
}
```

#### Sample Response
<a name="API_PutQueryDefinition_Example_3_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "queryDefinitionId": "12345678-1234-1234-1234-123456789012"
}
```

## See Also
<a name="API_PutQueryDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/PutQueryDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/PutQueryDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/PutQueryDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/PutQueryDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/PutQueryDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/PutQueryDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/PutQueryDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/PutQueryDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/PutQueryDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/PutQueryDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
