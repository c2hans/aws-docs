---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_GetServiceGraph.html
---

# GetServiceGraph
<a name="API_GetServiceGraph"></a>

Retrieves a document that describes services that process incoming requests, and downstream services that they call as a result. Root services process incoming requests and make calls to downstream services. Root services are applications that use the [AWS X-Ray SDK](https://docs.aws.amazon.com/xray/index.html). Downstream services can be other applications, AWS resources, HTTP web APIs, or SQL databases.

## Request Syntax
<a name="API_GetServiceGraph_RequestSyntax"></a>

```
POST /ServiceGraph HTTP/1.1
Content-type: application/json

{
   "EndTime": {{number}},
   "GroupARN": "{{string}}",
   "GroupName": "{{string}}",
   "NextToken": "{{string}}",
   "StartTime": {{number}}
}
```

## URI Request Parameters
<a name="API_GetServiceGraph_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetServiceGraph_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EndTime](#API_GetServiceGraph_RequestSyntax) **   <a name="xray-GetServiceGraph-request-EndTime"></a>
The end of the timeframe for which to generate a graph, in Unix time seconds.
Type: Timestamp
Required: Yes

 ** [GroupARN](#API_GetServiceGraph_RequestSyntax) **   <a name="xray-GetServiceGraph-request-GroupARN"></a>
The Amazon Resource Name (ARN) of a group based on which you want to generate a graph.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.
Required: No

 ** [GroupName](#API_GetServiceGraph_RequestSyntax) **   <a name="xray-GetServiceGraph-request-GroupName"></a>
The name of a group based on which you want to generate a graph.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** [NextToken](#API_GetServiceGraph_RequestSyntax) **   <a name="xray-GetServiceGraph-request-NextToken"></a>
Pagination token.
Type: String
Required: No

 ** [StartTime](#API_GetServiceGraph_RequestSyntax) **   <a name="xray-GetServiceGraph-request-StartTime"></a>
The start of the time frame for which to generate a graph, in Unix time seconds.
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_GetServiceGraph_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContainsOldGroupVersions": boolean,
   "EndTime": number,
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
   ],
   "StartTime": number
}
```

## Response Elements
<a name="API_GetServiceGraph_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContainsOldGroupVersions](#API_GetServiceGraph_ResponseSyntax) **   <a name="xray-GetServiceGraph-response-ContainsOldGroupVersions"></a>
A flag indicating whether the group's filter expression has been consistent, or if the returned service graph may show traces from an older version of the group's filter expression.
Type: Boolean

 ** [EndTime](#API_GetServiceGraph_ResponseSyntax) **   <a name="xray-GetServiceGraph-response-EndTime"></a>
The end of the time frame for which the graph was generated, in Unix time seconds.
Type: Timestamp

 ** [NextToken](#API_GetServiceGraph_ResponseSyntax) **   <a name="xray-GetServiceGraph-response-NextToken"></a>
Pagination token.
Type: String

 ** [Services](#API_GetServiceGraph_ResponseSyntax) **   <a name="xray-GetServiceGraph-response-Services"></a>
The services that have processed a traced request during the specified time frame.
Type: Array of [Service](API_Service.md) objects

 ** [StartTime](#API_GetServiceGraph_ResponseSyntax) **   <a name="xray-GetServiceGraph-response-StartTime"></a>
The start of the time frame for which the graph was generated, in Unix time seconds.
Type: Timestamp

## Errors
<a name="API_GetServiceGraph_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_GetServiceGraph_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/GetServiceGraph)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/GetServiceGraph)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/GetServiceGraph)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/GetServiceGraph)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/GetServiceGraph)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/GetServiceGraph)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/GetServiceGraph)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/GetServiceGraph)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/GetServiceGraph)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/GetServiceGraph)
