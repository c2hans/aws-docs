---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_GetTraceSummaries.html
---

# GetTraceSummaries
<a name="API_GetTraceSummaries"></a>

Retrieves IDs and annotations for traces available for a specified time frame using an optional filter. To get the full traces, pass the trace IDs to `BatchGetTraces`.

A filter expression can target traced requests that hit specific service nodes or edges, have errors, or come from a known user. For example, the following filter expression targets traces that pass through `api.example.com`:

 `service("api.example.com")`

This filter expression finds traces that have an annotation named `account` with the value `12345`:

 `annotation.account = "12345"`

For a full list of indexed fields and keywords that you can use in filter expressions, see [Use filter expressions](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray-interface-console.html#xray-console-filters) in the * AWS X-Ray Developer Guide*.

## Request Syntax
<a name="API_GetTraceSummaries_RequestSyntax"></a>

```
POST /TraceSummaries HTTP/1.1
Content-type: application/json

{
   "EndTime": {{number}},
   "FilterExpression": "{{string}}",
   "NextToken": "{{string}}",
   "Sampling": {{boolean}},
   "SamplingStrategy": {
      "Name": "{{string}}",
      "Value": {{number}}
   },
   "StartTime": {{number}},
   "TimeRangeType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetTraceSummaries_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetTraceSummaries_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EndTime](#API_GetTraceSummaries_RequestSyntax) **   <a name="xray-GetTraceSummaries-request-EndTime"></a>
The end of the time frame for which to retrieve traces, in Unix time seconds.
Type: Timestamp
Required: Yes

 ** [FilterExpression](#API_GetTraceSummaries_RequestSyntax) **   <a name="xray-GetTraceSummaries-request-FilterExpression"></a>
Specify a filter expression to retrieve trace summaries for services or requests that meet certain requirements.
Type: String
Required: No

 ** [NextToken](#API_GetTraceSummaries_RequestSyntax) **   <a name="xray-GetTraceSummaries-request-NextToken"></a>
Specify the pagination token returned by a previous request to retrieve the next page of results.
Type: String
Required: No

 ** [Sampling](#API_GetTraceSummaries_RequestSyntax) **   <a name="xray-GetTraceSummaries-request-Sampling"></a>
Set to `true` to get summaries for only a subset of available traces.
Type: Boolean
Required: No

 ** [SamplingStrategy](#API_GetTraceSummaries_RequestSyntax) **   <a name="xray-GetTraceSummaries-request-SamplingStrategy"></a>
A parameter to indicate whether to enable sampling on trace summaries. Input parameters are Name and Value.
Type: [SamplingStrategy](API_SamplingStrategy.md) object
Required: No

 ** [StartTime](#API_GetTraceSummaries_RequestSyntax) **   <a name="xray-GetTraceSummaries-request-StartTime"></a>
The start of the time frame for which to retrieve traces, in Unix time seconds.
Type: Timestamp
Required: Yes

 ** [TimeRangeType](#API_GetTraceSummaries_RequestSyntax) **   <a name="xray-GetTraceSummaries-request-TimeRangeType"></a>
Query trace summaries by TraceId (trace start time), Event (trace update time), or Service (trace segment end time).
Type: String
Valid Values: `TraceId | Event | Service`
Required: No

## Response Syntax
<a name="API_GetTraceSummaries_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApproximateTime": number,
   "NextToken": "string",
   "TracesProcessedCount": number,
   "TraceSummaries": [
      {
         "Annotations": {
            "string" : [
               {
                  "AnnotationValue": {
                     "BooleanValue": boolean,
                     "NumberValue": number,
                     "StringValue": "string"
                  },
                  "ServiceIds": [
                     {
                        "AccountId": "string",
                        "Name": "string",
                        "Names": [ "string" ],
                        "Type": "string"
                     }
                  ]
               }
            ]
         },
         "AvailabilityZones": [
            {
               "Name": "string"
            }
         ],
         "Duration": number,
         "EntryPoint": {
            "AccountId": "string",
            "Name": "string",
            "Names": [ "string" ],
            "Type": "string"
         },
         "ErrorRootCauses": [
            {
               "ClientImpacting": boolean,
               "Services": [
                  {
                     "AccountId": "string",
                     "EntityPath": [
                        {
                           "Exceptions": [
                              {
                                 "Message": "string",
                                 "Name": "string"
                              }
                           ],
                           "Name": "string",
                           "Remote": boolean
                        }
                     ],
                     "Inferred": boolean,
                     "Name": "string",
                     "Names": [ "string" ],
                     "Type": "string"
                  }
               ]
            }
         ],
         "FaultRootCauses": [
            {
               "ClientImpacting": boolean,
               "Services": [
                  {
                     "AccountId": "string",
                     "EntityPath": [
                        {
                           "Exceptions": [
                              {
                                 "Message": "string",
                                 "Name": "string"
                              }
                           ],
                           "Name": "string",
                           "Remote": boolean
                        }
                     ],
                     "Inferred": boolean,
                     "Name": "string",
                     "Names": [ "string" ],
                     "Type": "string"
                  }
               ]
            }
         ],
         "HasError": boolean,
         "HasFault": boolean,
         "HasThrottle": boolean,
         "Http": {
            "ClientIp": "string",
            "HttpMethod": "string",
            "HttpStatus": number,
            "HttpURL": "string",
            "UserAgent": "string"
         },
         "Id": "string",
         "InstanceIds": [
            {
               "Id": "string"
            }
         ],
         "IsPartial": boolean,
         "MatchedEventTime": number,
         "ResourceARNs": [
            {
               "ARN": "string"
            }
         ],
         "ResponseTime": number,
         "ResponseTimeRootCauses": [
            {
               "ClientImpacting": boolean,
               "Services": [
                  {
                     "AccountId": "string",
                     "EntityPath": [
                        {
                           "Coverage": number,
                           "Name": "string",
                           "Remote": boolean
                        }
                     ],
                     "Inferred": boolean,
                     "Name": "string",
                     "Names": [ "string" ],
                     "Type": "string"
                  }
               ]
            }
         ],
         "Revision": number,
         "ServiceIds": [
            {
               "AccountId": "string",
               "Name": "string",
               "Names": [ "string" ],
               "Type": "string"
            }
         ],
         "StartTime": number,
         "Users": [
            {
               "ServiceIds": [
                  {
                     "AccountId": "string",
                     "Name": "string",
                     "Names": [ "string" ],
                     "Type": "string"
                  }
               ],
               "UserName": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_GetTraceSummaries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApproximateTime](#API_GetTraceSummaries_ResponseSyntax) **   <a name="xray-GetTraceSummaries-response-ApproximateTime"></a>
The start time of this page of results.
Type: Timestamp

 ** [NextToken](#API_GetTraceSummaries_ResponseSyntax) **   <a name="xray-GetTraceSummaries-response-NextToken"></a>
If the requested time frame contained more than one page of results, you can use this token to retrieve the next page. The first page contains the most recent results, closest to the end of the time frame.
Type: String

 ** [TracesProcessedCount](#API_GetTraceSummaries_ResponseSyntax) **   <a name="xray-GetTraceSummaries-response-TracesProcessedCount"></a>
The total number of traces processed, including traces that did not match the specified filter expression.
Type: Long

 ** [TraceSummaries](#API_GetTraceSummaries_ResponseSyntax) **   <a name="xray-GetTraceSummaries-response-TraceSummaries"></a>
Trace IDs and annotations for traces that were found in the specified time frame.
Type: Array of [TraceSummary](API_TraceSummary.md) objects

## Errors
<a name="API_GetTraceSummaries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_GetTraceSummaries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/GetTraceSummaries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/GetTraceSummaries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/GetTraceSummaries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/GetTraceSummaries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/GetTraceSummaries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/GetTraceSummaries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/GetTraceSummaries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/GetTraceSummaries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/GetTraceSummaries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/GetTraceSummaries)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
