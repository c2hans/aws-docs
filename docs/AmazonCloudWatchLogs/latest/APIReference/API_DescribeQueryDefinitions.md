---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeQueryDefinitions.html
---

# DescribeQueryDefinitions
<a name="API_DescribeQueryDefinitions"></a>

This operation returns a paginated list of your saved CloudWatch Logs Insights query definitions. You can retrieve query definitions from the current account or from a source account that is linked to the current account.

You can use the `queryDefinitionNamePrefix` parameter to limit the results to only the query definitions that have names that start with a certain string.

## Request Syntax
<a name="API_DescribeQueryDefinitions_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "queryDefinitionNamePrefix": "{{string}}",
   "queryLanguage": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeQueryDefinitions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_DescribeQueryDefinitions_RequestSyntax) **   <a name="CWL-DescribeQueryDefinitions-request-maxResults"></a>
Limits the number of returned query definitions to the specified number.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_DescribeQueryDefinitions_RequestSyntax) **   <a name="CWL-DescribeQueryDefinitions-request-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [queryDefinitionNamePrefix](#API_DescribeQueryDefinitions_RequestSyntax) **   <a name="CWL-DescribeQueryDefinitions-request-queryDefinitionNamePrefix"></a>
Use this parameter to filter your results to only the query definitions that have names that start with the prefix you specify.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [queryLanguage](#API_DescribeQueryDefinitions_RequestSyntax) **   <a name="CWL-DescribeQueryDefinitions-request-queryLanguage"></a>
The query language used for this query. For more information about the query languages that CloudWatch Logs supports, see [Supported query languages](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Languages.html).
Type: String
Valid Values: `CWLI | SQL | PPL`
Required: No

## Response Syntax
<a name="API_DescribeQueryDefinitions_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "queryDefinitions": [
      {
         "lastModified": number,
         "logGroupNames": [ "string" ],
         "name": "string",
         "parameters": [
            {
               "defaultValue": "string",
               "description": "string",
               "name": "string"
            }
         ],
         "queryDefinitionId": "string",
         "queryLanguage": "string",
         "queryString": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeQueryDefinitions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_DescribeQueryDefinitions_ResponseSyntax) **   <a name="CWL-DescribeQueryDefinitions-response-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.

 ** [queryDefinitions](#API_DescribeQueryDefinitions_ResponseSyntax) **   <a name="CWL-DescribeQueryDefinitions-response-queryDefinitions"></a>
The list of query definitions that match your request.
Type: Array of [QueryDefinition](API_QueryDefinition.md) objects

## Errors
<a name="API_DescribeQueryDefinitions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## Examples
<a name="API_DescribeQueryDefinitions_Examples"></a>

### Example
<a name="API_DescribeQueryDefinitions_Example_1"></a>

This example retrieves a list of query definitions that have names that begin with `lambda`.

#### Sample Request
<a name="API_DescribeQueryDefinitions_Example_1_Request"></a>

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
X-Amz-Target: Logs_20140328.DescribeQueryDefinitions
{
   "queryDefinitionNamePrefix": "lambda",
   "maxResults": 2
}
```

#### Sample Response
<a name="API_DescribeQueryDefinitions_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "nextToken": "abdcefghijlkmn",
   "queryDefinitions": [
      {
         "lastModified": 1549321515,
         "logGroupNames": [ "VPC_Flow_Log1", "VPC_Flow_Log2" ],
         "name": "VPC-top15-packet-transfers",
         "queryDefinitionId": "123456ab-12ab-123a-789e-1234567890ab",
         "queryString": "stats sum(packets) as packetsTransferred by srcAddr, dstAddr | sort packetsTransferred  desc | limit 15",
         "parameters": []
      },
      {
         "lastModified": 1557321299,
         "name": "ErrorsByLevel",
         "queryDefinitionId": "456789ab-abcd-1234-789e-0987654321ab",
         "queryString": "fields @timestamp, @message | filter level = {{logLevel}}",
         "parameters": [
            {
               "name": "logLevel",
               "defaultValue": "ERROR",
               "description": "Log level to filter (ERROR, WARN, INFO, DEBUG)"
            }
         ]
      }
   ]
}
```

## See Also
<a name="API_DescribeQueryDefinitions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/DescribeQueryDefinitions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/DescribeQueryDefinitions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DescribeQueryDefinitions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/DescribeQueryDefinitions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DescribeQueryDefinitions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/DescribeQueryDefinitions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/DescribeQueryDefinitions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/DescribeQueryDefinitions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/DescribeQueryDefinitions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DescribeQueryDefinitions)
