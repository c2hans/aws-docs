---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_GetInsight.html
---

# GetInsight
<a name="API_GetInsight"></a>

Retrieves the summary information of an insight. This includes impact to clients and root cause services, the top anomalous services, the category, the state of the insight, and the start and end time of the insight.

## Request Syntax
<a name="API_GetInsight_RequestSyntax"></a>

```
POST /Insight HTTP/1.1
Content-type: application/json

{
   "InsightId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetInsight_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetInsight_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InsightId](#API_GetInsight_RequestSyntax) **   <a name="xray-GetInsight-request-InsightId"></a>
The insight's unique identifier. Use the GetInsightSummaries action to retrieve an InsightId.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}`
Required: Yes

## Response Syntax
<a name="API_GetInsight_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Insight": {
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
}
```

## Response Elements
<a name="API_GetInsight_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Insight](#API_GetInsight_ResponseSyntax) **   <a name="xray-GetInsight-response-Insight"></a>
The summary information of an insight.
Type: [Insight](API_Insight.md) object

## Errors
<a name="API_GetInsight_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_GetInsight_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/GetInsight)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/GetInsight)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/GetInsight)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/GetInsight)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/GetInsight)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/GetInsight)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/GetInsight)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/GetInsight)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/GetInsight)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/GetInsight)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
