---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_GetInsightImpactGraph.html
---

# GetInsightImpactGraph
<a name="API_GetInsightImpactGraph"></a>

Retrieves a service graph structure filtered by the specified insight. The service graph is limited to only structural information. For a complete service graph, use this API with the GetServiceGraph API.

## Request Syntax
<a name="API_GetInsightImpactGraph_RequestSyntax"></a>

```
POST /InsightImpactGraph HTTP/1.1
Content-type: application/json

{
   "EndTime": {{number}},
   "InsightId": "{{string}}",
   "NextToken": "{{string}}",
   "StartTime": {{number}}
}
```

## URI Request Parameters
<a name="API_GetInsightImpactGraph_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetInsightImpactGraph_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EndTime](#API_GetInsightImpactGraph_RequestSyntax) **   <a name="xray-GetInsightImpactGraph-request-EndTime"></a>
The estimated end time of the insight, in Unix time seconds. The EndTime is exclusive of the value provided. The time range between the start time and end time can't be more than six hours.
Type: Timestamp
Required: Yes

 ** [InsightId](#API_GetInsightImpactGraph_RequestSyntax) **   <a name="xray-GetInsightImpactGraph-request-InsightId"></a>
The insight's unique identifier. Use the GetInsightSummaries action to retrieve an InsightId.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}`
Required: Yes

 ** [NextToken](#API_GetInsightImpactGraph_RequestSyntax) **   <a name="xray-GetInsightImpactGraph-request-NextToken"></a>
Specify the pagination token returned by a previous request to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

 ** [StartTime](#API_GetInsightImpactGraph_RequestSyntax) **   <a name="xray-GetInsightImpactGraph-request-StartTime"></a>
The estimated start time of the insight, in Unix time seconds. The StartTime is inclusive of the value provided and can't be more than 30 days old.
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_GetInsightImpactGraph_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EndTime": number,
   "InsightId": "string",
   "NextToken": "string",
   "ServiceGraphEndTime": number,
   "ServiceGraphStartTime": number,
   "Services": [
      {
         "AccountId": "string",
         "Edges": [
            {
               "ReferenceId": number
            }
         ],
         "Name": "string",
         "Names": [ "string" ],
         "ReferenceId": number,
         "Type": "string"
      }
   ],
   "StartTime": number
}
```

## Response Elements
<a name="API_GetInsightImpactGraph_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndTime](#API_GetInsightImpactGraph_ResponseSyntax) **   <a name="xray-GetInsightImpactGraph-response-EndTime"></a>
The provided end time.
Type: Timestamp

 ** [InsightId](#API_GetInsightImpactGraph_ResponseSyntax) **   <a name="xray-GetInsightImpactGraph-response-InsightId"></a>
The insight's unique identifier.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}`

 ** [NextToken](#API_GetInsightImpactGraph_ResponseSyntax) **   <a name="xray-GetInsightImpactGraph-response-NextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [ServiceGraphEndTime](#API_GetInsightImpactGraph_ResponseSyntax) **   <a name="xray-GetInsightImpactGraph-response-ServiceGraphEndTime"></a>
The time, in Unix seconds, at which the service graph ended.
Type: Timestamp

 ** [ServiceGraphStartTime](#API_GetInsightImpactGraph_ResponseSyntax) **   <a name="xray-GetInsightImpactGraph-response-ServiceGraphStartTime"></a>
The time, in Unix seconds, at which the service graph started.
Type: Timestamp

 ** [Services](#API_GetInsightImpactGraph_ResponseSyntax) **   <a name="xray-GetInsightImpactGraph-response-Services"></a>
The AWS instrumented services related to the insight.
Type: Array of [InsightImpactGraphService](API_InsightImpactGraphService.md) objects

 ** [StartTime](#API_GetInsightImpactGraph_ResponseSyntax) **   <a name="xray-GetInsightImpactGraph-response-StartTime"></a>
The provided start time.
Type: Timestamp

## Errors
<a name="API_GetInsightImpactGraph_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_GetInsightImpactGraph_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/GetInsightImpactGraph)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/GetInsightImpactGraph)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/GetInsightImpactGraph)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/GetInsightImpactGraph)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/GetInsightImpactGraph)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/GetInsightImpactGraph)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/GetInsightImpactGraph)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/GetInsightImpactGraph)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/GetInsightImpactGraph)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/GetInsightImpactGraph)
