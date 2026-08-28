---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetConsolidatedReport.html
---

# GetConsolidatedReport
<a name="API_GetConsolidatedReport"></a>

Get a consolidated report of your workloads.

You can optionally choose to include workloads that have been shared with you.

## Request Syntax
<a name="API_GetConsolidatedReport_RequestSyntax"></a>

```
GET /consolidatedReport?Format={{Format}}&IncludeSharedResources={{IncludeSharedResources}}&MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetConsolidatedReport_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Format](#API_GetConsolidatedReport_RequestSyntax) **   <a name="wellarchitected-GetConsolidatedReport-request-uri-Format"></a>
The format of the consolidated report.
For `PDF`, `Base64String` is returned. For `JSON`, `Metrics` is returned.
Valid Values: `PDF | JSON`
Required: Yes

 ** [IncludeSharedResources](#API_GetConsolidatedReport_RequestSyntax) **   <a name="wellarchitected-GetConsolidatedReport-request-uri-IncludeSharedResources"></a>
Set to `true` to have shared resources included in the report.

 ** [MaxResults](#API_GetConsolidatedReport_RequestSyntax) **   <a name="wellarchitected-GetConsolidatedReport-request-uri-MaxResults"></a>
The maximum number of results to return for this request.
Valid Range: Minimum value of 1. Maximum value of 15.

 ** [NextToken](#API_GetConsolidatedReport_RequestSyntax) **   <a name="wellarchitected-GetConsolidatedReport-request-uri-NextToken"></a>
The token to use to retrieve the next set of results.

## Request Body
<a name="API_GetConsolidatedReport_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetConsolidatedReport_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Base64String": "string",
   "Metrics": [
      {
         "Lenses": [
            {
               "LensArn": "string",
               "Pillars": [
                  {
                     "PillarId": "string",
                     "Questions": [
                        {
                           "BestPractices": [
                              {
                                 "ChoiceId": "string",
                                 "ChoiceTitle": "string"
                              }
                           ],
                           "QuestionId": "string",
                           "Risk": "string"
                        }
                     ],
                     "RiskCounts": {
                        "string" : number
                     }
                  }
               ],
               "RiskCounts": {
                  "string" : number
               }
            }
         ],
         "LensesAppliedCount": number,
         "MetricType": "string",
         "RiskCounts": {
            "string" : number
         },
         "UpdatedAt": number,
         "WorkloadArn": "string",
         "WorkloadId": "string",
         "WorkloadName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetConsolidatedReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Base64String](#API_GetConsolidatedReport_ResponseSyntax) **   <a name="wellarchitected-GetConsolidatedReport-response-Base64String"></a>
The Base64-encoded string representation of a lens review report.
This data can be used to create a PDF file.
Only returned by [GetConsolidatedReport](#API_GetConsolidatedReport) when `PDF` format is requested.
Type: String

 ** [Metrics](#API_GetConsolidatedReport_ResponseSyntax) **   <a name="wellarchitected-GetConsolidatedReport-response-Metrics"></a>
The metrics that make up the consolidated report.
Only returned when `JSON` format is requested.
Type: Array of [ConsolidatedReportMetric](API_ConsolidatedReportMetric.md) objects

 ** [NextToken](#API_GetConsolidatedReport_ResponseSyntax) **   <a name="wellarchitected-GetConsolidatedReport-response-NextToken"></a>
The token to use to retrieve the next set of results.
Type: String

## Errors
<a name="API_GetConsolidatedReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** ConflictException **
The resource has already been processed, was deleted, or is too large.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 409

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ThrottlingException **
Request was denied due to request throttling.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 429

 ** ValidationException **
The user input is not valid.
 ** Fields **
The fields that caused the error, if applicable.
 ** Message **
Description of the error.
 ** Reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_GetConsolidatedReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/GetConsolidatedReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/GetConsolidatedReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/GetConsolidatedReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/GetConsolidatedReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/GetConsolidatedReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/GetConsolidatedReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/GetConsolidatedReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/GetConsolidatedReport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/GetConsolidatedReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/GetConsolidatedReport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
