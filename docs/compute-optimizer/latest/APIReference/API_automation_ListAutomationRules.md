---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListAutomationRules.html
---

# ListAutomationRules
<a name="API_automation_ListAutomationRules"></a>

 Lists the automation rules that match specified filters.

## Request Syntax
<a name="API_automation_ListAutomationRules_RequestSyntax"></a>

```
{
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_automation_ListAutomationRules_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filters](#API_automation_ListAutomationRules_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationRules-request-filters"></a>
 The filters to apply to the list of automation rules.
Type: Array of [Filter](API_automation_Filter.md) objects
Required: No

 ** [maxResults](#API_automation_ListAutomationRules_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationRules-request-maxResults"></a>
The maximum number of automation rules to return in a single response. Valid range is 1-1000.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_automation_ListAutomationRules_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationRules-request-nextToken"></a>
A token used for pagination to retrieve the next set of results when the response is truncated.
Type: String
Pattern: `[A-Za-z0-9+/=]+`
Required: No

## Response Syntax
<a name="API_automation_ListAutomationRules_ResponseSyntax"></a>

```
{
   "automationRules": [
      {
         "accountId": "string",
         "createdTimestamp": number,
         "description": "string",
         "lastUpdatedTimestamp": number,
         "name": "string",
         "organizationConfiguration": {
            "accountIds": [ "string" ],
            "ruleApplyOrder": "string"
         },
         "priority": "string",
         "recommendedActionTypes": [ "string" ],
         "ruleArn": "string",
         "ruleId": "string",
         "ruleRevision": number,
         "ruleType": "string",
         "schedule": {
            "executionWindowInMinutes": number,
            "scheduleExpression": "string",
            "scheduleExpressionTimezone": "string"
         },
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_automation_ListAutomationRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [automationRules](#API_automation_ListAutomationRules_ResponseSyntax) **   <a name="computeoptimizer-automation_ListAutomationRules-response-automationRules"></a>
 The list of automation rules that match the specified criteria.
Type: Array of [AutomationRule](API_automation_AutomationRule.md) objects

 ** [nextToken](#API_automation_ListAutomationRules_ResponseSyntax) **   <a name="computeoptimizer-automation_ListAutomationRules-response-nextToken"></a>
A token used for pagination. If present, indicates there are more results available and can be used in subsequent requests.
Type: String
Pattern: `[A-Za-z0-9+/=]+`

## Errors
<a name="API_automation_ListAutomationRules_Errors"></a>

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
<a name="API_automation_ListAutomationRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-automation-2025-09-22/ListAutomationRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-automation-2025-09-22/ListAutomationRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/ListAutomationRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-automation-2025-09-22/ListAutomationRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/ListAutomationRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-automation-2025-09-22/ListAutomationRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-automation-2025-09-22/ListAutomationRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-automation-2025-09-22/ListAutomationRules)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-automation-2025-09-22/ListAutomationRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/ListAutomationRules)
