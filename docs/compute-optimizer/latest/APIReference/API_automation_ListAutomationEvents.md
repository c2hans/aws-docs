---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListAutomationEvents.html
---

# ListAutomationEvents
<a name="API_automation_ListAutomationEvents"></a>

Lists automation events based on specified filters. You can retrieve events that were created within the past year.

## Request Syntax
<a name="API_automation_ListAutomationEvents_RequestSyntax"></a>

```
{
   "endTimeExclusive": {{number}},
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "startTimeInclusive": {{number}}
}
```

## Request Parameters
<a name="API_automation_ListAutomationEvents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [endTimeExclusive](#API_automation_ListAutomationEvents_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationEvents-request-endTimeExclusive"></a>
 The end of the time range to query for events.
Type: Timestamp
Required: No

 ** [filters](#API_automation_ListAutomationEvents_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationEvents-request-filters"></a>
 The filters to apply to the list of automation events.
Type: Array of [AutomationEventFilter](API_automation_AutomationEventFilter.md) objects
Required: No

 ** [maxResults](#API_automation_ListAutomationEvents_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationEvents-request-maxResults"></a>
 The maximum number of results to return in a single call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_automation_ListAutomationEvents_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationEvents-request-nextToken"></a>
 The token for the next page of results.
Type: String
Pattern: `[A-Za-z0-9+/=]+`
Required: No

 ** [startTimeInclusive](#API_automation_ListAutomationEvents_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationEvents-request-startTimeInclusive"></a>
 The start of the time range to query for events.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_automation_ListAutomationEvents_ResponseSyntax"></a>

```
{
   "automationEvents": [
      {
         "accountId": "string",
         "completedTimestamp": number,
         "createdTimestamp": number,
         "estimatedMonthlySavings": {
            "afterDiscountSavings": number,
            "beforeDiscountSavings": number,
            "currency": "string",
            "savingsEstimationMode": "string"
         },
         "eventDescription": "string",
         "eventId": "string",
         "eventStatus": "string",
         "eventStatusReason": "string",
         "eventType": "string",
         "recommendedActionId": "string",
         "region": "string",
         "resourceArn": "string",
         "resourceId": "string",
         "resourceType": "string",
         "ruleId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_automation_ListAutomationEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [automationEvents](#API_automation_ListAutomationEvents_ResponseSyntax) **   <a name="computeoptimizer-automation_ListAutomationEvents-response-automationEvents"></a>
 The list of automation events that match the specified criteria.
Type: Array of [AutomationEvent](API_automation_AutomationEvent.md) objects

 ** [nextToken](#API_automation_ListAutomationEvents_ResponseSyntax) **   <a name="computeoptimizer-automation_ListAutomationEvents-response-nextToken"></a>
 The token to use to retrieve the next page of results.
Type: String
Pattern: `[A-Za-z0-9+/=]+`

## Errors
<a name="API_automation_ListAutomationEvents_Errors"></a>

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
<a name="API_automation_ListAutomationEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-automation-2025-09-22/ListAutomationEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-automation-2025-09-22/ListAutomationEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/ListAutomationEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-automation-2025-09-22/ListAutomationEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/ListAutomationEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-automation-2025-09-22/ListAutomationEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-automation-2025-09-22/ListAutomationEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-automation-2025-09-22/ListAutomationEvents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-automation-2025-09-22/ListAutomationEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/ListAutomationEvents)
