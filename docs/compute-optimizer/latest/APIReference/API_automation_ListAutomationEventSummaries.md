---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListAutomationEventSummaries.html
---

# ListAutomationEventSummaries
<a name="API_automation_ListAutomationEventSummaries"></a>

Provides a summary of automation events based on specified filters. Only events created within the past year will be included in the summary.

## Request Syntax
<a name="API_automation_ListAutomationEventSummaries_RequestSyntax"></a>

```
{
   "endDateExclusive": "{{string}}",
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "startDateInclusive": "{{string}}"
}
```

## Request Parameters
<a name="API_automation_ListAutomationEventSummaries_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [endDateExclusive](#API_automation_ListAutomationEventSummaries_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationEventSummaries-request-endDateExclusive"></a>
The end date for filtering automation event summaries, exclusive. Events created before this date will be included.
Type: String
Required: No

 ** [filters](#API_automation_ListAutomationEventSummaries_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationEventSummaries-request-filters"></a>
 The filters to apply to the list of automation event summaries.
Type: Array of [AutomationEventFilter](API_automation_AutomationEventFilter.md) objects
Required: No

 ** [maxResults](#API_automation_ListAutomationEventSummaries_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationEventSummaries-request-maxResults"></a>
The maximum number of automation event summaries to return in a single response. Valid range is 1-1000.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_automation_ListAutomationEventSummaries_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationEventSummaries-request-nextToken"></a>
A token used for pagination to retrieve the next set of results when the response is truncated.
Type: String
Pattern: `[A-Za-z0-9+/=]+`
Required: No

 ** [startDateInclusive](#API_automation_ListAutomationEventSummaries_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationEventSummaries-request-startDateInclusive"></a>
The start date for filtering automation event summaries, inclusive. Events created on or after this date will be included.
Type: String
Required: No

## Response Syntax
<a name="API_automation_ListAutomationEventSummaries_ResponseSyntax"></a>

```
{
   "automationEventSummaries": [
      {
         "dimensions": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "key": "string",
         "timePeriod": {
            "endTimeExclusive": number,
            "startTimeInclusive": number
         },
         "total": {
            "automationEventCount": number,
            "estimatedMonthlySavings": {
               "afterDiscountSavings": number,
               "beforeDiscountSavings": number,
               "currency": "string",
               "savingsEstimationMode": "string"
            }
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_automation_ListAutomationEventSummaries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [automationEventSummaries](#API_automation_ListAutomationEventSummaries_ResponseSyntax) **   <a name="computeoptimizer-automation_ListAutomationEventSummaries-response-automationEventSummaries"></a>
 The list of automation event summaries that match the specified criteria.
Type: Array of [AutomationEventSummary](API_automation_AutomationEventSummary.md) objects

 ** [nextToken](#API_automation_ListAutomationEventSummaries_ResponseSyntax) **   <a name="computeoptimizer-automation_ListAutomationEventSummaries-response-nextToken"></a>
A token used for pagination. If present, indicates there are more results available and can be used in subsequent requests.
Type: String
Pattern: `[A-Za-z0-9+/=]+`

## Errors
<a name="API_automation_ListAutomationEventSummaries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You do not have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** ForbiddenException **
 You are not authorized to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
 An internal error occurred while processing the request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
 One or more parameter values are not valid.
HTTP Status Code: 400

 ** OptInRequiredException **
 The account must be opted in to Compute Optimizer Automation before performing this action.
HTTP Status Code: 400

 ** ServiceUnavailableException **
 The service is temporarily unavailable.
HTTP Status Code: 500

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_automation_ListAutomationEventSummaries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-automation-2025-09-22/ListAutomationEventSummaries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-automation-2025-09-22/ListAutomationEventSummaries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/ListAutomationEventSummaries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-automation-2025-09-22/ListAutomationEventSummaries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/ListAutomationEventSummaries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-automation-2025-09-22/ListAutomationEventSummaries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-automation-2025-09-22/ListAutomationEventSummaries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-automation-2025-09-22/ListAutomationEventSummaries)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-automation-2025-09-22/ListAutomationEventSummaries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/ListAutomationEventSummaries)
