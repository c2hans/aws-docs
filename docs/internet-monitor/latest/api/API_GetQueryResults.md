---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_GetQueryResults.html
---

# GetQueryResults
<a name="API_GetQueryResults"></a>

Return the data for a query with the Internet Monitor query interface. Specify the query that you want to return results for by providing a `QueryId` and a monitor name.

For more information about using the query interface, including examples, see [Using the Internet Monitor query interface](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html) in the Internet Monitor User Guide.

## Request Syntax
<a name="API_GetQueryResults_RequestSyntax"></a>

```
GET /v20210603/Monitors/{{MonitorName}}/Queries/{{QueryId}}/Results?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetQueryResults_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_GetQueryResults_RequestSyntax) **   <a name="internetmonitor-GetQueryResults-request-uri-MaxResults"></a>
The number of query results that you want to return with this call.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [MonitorName](#API_GetQueryResults_RequestSyntax) **   <a name="internetmonitor-GetQueryResults-request-uri-MonitorName"></a>
The name of the monitor to return data for.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [NextToken](#API_GetQueryResults_RequestSyntax) **   <a name="internetmonitor-GetQueryResults-request-uri-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.

 ** [QueryId](#API_GetQueryResults_RequestSyntax) **   <a name="internetmonitor-GetQueryResults-request-uri-QueryId"></a>
The ID of the query that you want to return data results for. A `QueryId` is an internally-generated identifier for a specific query.
Required: Yes

## Request Body
<a name="API_GetQueryResults_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetQueryResults_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Data": [
      [ "string" ]
   ],
   "Fields": [
      {
         "Name": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetQueryResults_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Data](#API_GetQueryResults_ResponseSyntax) **   <a name="internetmonitor-GetQueryResults-response-Data"></a>
The data results that the query returns. Data is returned in arrays, aligned with the `Fields` for the query, which creates a repository of Internet Monitor information for your application. Then, you can filter the information in the repository by using `FilterParameters` that you define.
Type: Array of arrays of strings

 ** [Fields](#API_GetQueryResults_ResponseSyntax) **   <a name="internetmonitor-GetQueryResults-response-Fields"></a>
The fields that the query returns data for. Fields are name-data type pairs, such as `availability_score`-`float`.
Type: Array of [QueryField](API_QueryField.md) objects

 ** [NextToken](#API_GetQueryResults_ResponseSyntax) **   <a name="internetmonitor-GetQueryResults-response-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.
Type: String

## Errors
<a name="API_GetQueryResults_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal error occurred.
HTTP Status Code: 500

 ** LimitExceededException **
The request exceeded a service quota.
HTTP Status Code: 403

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
Invalid request.
HTTP Status Code: 400

## See Also
<a name="API_GetQueryResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/internetmonitor-2021-06-03/GetQueryResults)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/internetmonitor-2021-06-03/GetQueryResults)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/GetQueryResults)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/internetmonitor-2021-06-03/GetQueryResults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/GetQueryResults)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/internetmonitor-2021-06-03/GetQueryResults)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/internetmonitor-2021-06-03/GetQueryResults)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/internetmonitor-2021-06-03/GetQueryResults)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/internetmonitor-2021-06-03/GetQueryResults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/GetQueryResults)
