---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_GetInsightSummaries.html
---

# GetInsightSummaries
<a name="API_GetInsightSummaries"></a>

Retrieves the summaries of all insights in the specified group matching the provided filter values.

## Request Syntax
<a name="API_GetInsightSummaries_RequestSyntax"></a>

```
POST /InsightSummaries HTTP/1.1
Content-type: application/json

{
   "EndTime": {{number}},
   "GroupARN": "{{string}}",
   "GroupName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "StartTime": {{number}},
   "States": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_GetInsightSummaries_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetInsightSummaries_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EndTime](#API_GetInsightSummaries_RequestSyntax) **   <a name="xray-GetInsightSummaries-request-EndTime"></a>
The end of the time frame in which the insights ended. The end time can't be more than 30 days old.
Type: Timestamp
Required: Yes

 ** [GroupARN](#API_GetInsightSummaries_RequestSyntax) **   <a name="xray-GetInsightSummaries-request-GroupARN"></a>
The Amazon Resource Name (ARN) of the group. Required if the GroupName isn't provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.
Required: No

 ** [GroupName](#API_GetInsightSummaries_RequestSyntax) **   <a name="xray-GetInsightSummaries-request-GroupName"></a>
The name of the group. Required if the GroupARN isn't provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** [MaxResults](#API_GetInsightSummaries_RequestSyntax) **   <a name="xray-GetInsightSummaries-request-MaxResults"></a>
The maximum number of results to display.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetInsightSummaries_RequestSyntax) **   <a name="xray-GetInsightSummaries-request-NextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

 ** [StartTime](#API_GetInsightSummaries_RequestSyntax) **   <a name="xray-GetInsightSummaries-request-StartTime"></a>
The beginning of the time frame in which the insights started. The start time can't be more than 30 days old.
Type: Timestamp
Required: Yes

 ** [States](#API_GetInsightSummaries_RequestSyntax) **   <a name="xray-GetInsightSummaries-request-States"></a>
The list of insight states.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Valid Values: `ACTIVE | CLOSED`
Required: No

## Response Syntax
<a name="API_GetInsightSummaries_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "InsightSummaries": [
      {
         "Categories": [ "string" ],
         "ClientRequestImpactStatistics": {
            "FaultCount": number,
            "OkCount": number,
            "TotalCount": number
         },
         "EndTime": number,
         "GroupARN": "string",
         "GroupName": "string",
         "InsightId": "string",
         "LastUpdateTime": number,
         "RootCauseServiceId": {
            "AccountId": "string",
            "Name": "string",
            "Names": [ "string" ],
            "Type": "string"
         },
         "RootCauseServiceRequestImpactStatistics": {
            "FaultCount": number,
            "OkCount": number,
            "TotalCount": number
         },
         "StartTime": number,
         "State": "string",
         "Summary": "string",
         "TopAnomalousServices": [
            {
               "ServiceId": {
                  "AccountId": "string",
                  "Name": "string",
                  "Names": [ "string" ],
                  "Type": "string"
               }
            }
         ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetInsightSummaries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InsightSummaries](#API_GetInsightSummaries_ResponseSyntax) **   <a name="xray-GetInsightSummaries-response-InsightSummaries"></a>
The summary of each insight within the group matching the provided filters. The summary contains the InsightID, start and end time, the root cause service, the root cause and client impact statistics, the top anomalous services, and the status of the insight.
Type: Array of [InsightSummary](API_InsightSummary.md) objects

 ** [NextToken](#API_GetInsightSummaries_ResponseSyntax) **   <a name="xray-GetInsightSummaries-response-NextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

## Errors
<a name="API_GetInsightSummaries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_GetInsightSummaries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/GetInsightSummaries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/GetInsightSummaries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/GetInsightSummaries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/GetInsightSummaries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/GetInsightSummaries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/GetInsightSummaries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/GetInsightSummaries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/GetInsightSummaries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/GetInsightSummaries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/GetInsightSummaries)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
