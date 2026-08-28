---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_GetTraceGraph.html
---

# GetTraceGraph
<a name="API_GetTraceGraph"></a>

Retrieves a service graph for one or more specific trace IDs.

## Request Syntax
<a name="API_GetTraceGraph_RequestSyntax"></a>

```
POST /TraceGraph HTTP/1.1
Content-type: application/json

{
   "NextToken": "{{string}}",
   "TraceIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_GetTraceGraph_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetTraceGraph_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [NextToken](#API_GetTraceGraph_RequestSyntax) **   <a name="xray-GetTraceGraph-request-NextToken"></a>
Pagination token.
Type: String
Required: No

 ** [TraceIds](#API_GetTraceGraph_RequestSyntax) **   <a name="xray-GetTraceGraph-request-TraceIds"></a>
Trace IDs of requests for which to generate a service graph.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 35.
Required: Yes

## Response Syntax
<a name="API_GetTraceGraph_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Services": [
      {
         "AccountId": "string",
         "DurationHistogram": [
            {
               "Count": number,
               "Value": number
            }
         ],
         "Edges": [
            {
               "Aliases": [
                  {
                     "Name": "string",
                     "Names": [ "string" ],
                     "Type": "string"
                  }
               ],
               "EdgeType": "string",
               "EndTime": number,
               "ReceivedEventAgeHistogram": [
                  {
                     "Count": number,
                     "Value": number
                  }
               ],
               "ReferenceId": number,
               "ResponseTimeHistogram": [
                  {
                     "Count": number,
                     "Value": number
                  }
               ],
               "StartTime": number,
               "SummaryStatistics": {
                  "ErrorStatistics": {
                     "OtherCount": number,
                     "ThrottleCount": number,
                     "TotalCount": number
                  },
                  "FaultStatistics": {
                     "OtherCount": number,
                     "TotalCount": number
                  },
                  "OkCount": number,
                  "TotalCount": number,
                  "TotalResponseTime": number
               }
            }
         ],
         "EndTime": number,
         "Name": "string",
         "Names": [ "string" ],
         "ReferenceId": number,
         "ResponseTimeHistogram": [
            {
               "Count": number,
               "Value": number
            }
         ],
         "Root": boolean,
         "StartTime": number,
         "State": "string",
         "SummaryStatistics": {
            "ErrorStatistics": {
               "OtherCount": number,
               "ThrottleCount": number,
               "TotalCount": number
            },
            "FaultStatistics": {
               "OtherCount": number,
               "TotalCount": number
            },
            "OkCount": number,
            "TotalCount": number,
            "TotalResponseTime": number
         },
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetTraceGraph_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetTraceGraph_ResponseSyntax) **   <a name="xray-GetTraceGraph-response-NextToken"></a>
Pagination token.
Type: String

 ** [Services](#API_GetTraceGraph_ResponseSyntax) **   <a name="xray-GetTraceGraph-response-Services"></a>
The services that have processed one of the specified requests.
Type: Array of [Service](API_Service.md) objects

## Errors
<a name="API_GetTraceGraph_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_GetTraceGraph_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/GetTraceGraph)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/GetTraceGraph)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/GetTraceGraph)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/GetTraceGraph)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/GetTraceGraph)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/GetTraceGraph)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/GetTraceGraph)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/GetTraceGraph)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/GetTraceGraph)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/GetTraceGraph)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
