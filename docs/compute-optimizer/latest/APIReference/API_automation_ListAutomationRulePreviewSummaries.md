---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListAutomationRulePreviewSummaries.html
---

# ListAutomationRulePreviewSummaries
<a name="API_automation_ListAutomationRulePreviewSummaries"></a>

Returns a summary of the recommended actions that match your rule preview configuration and criteria.

## Request Syntax
<a name="API_automation_ListAutomationRulePreviewSummaries_RequestSyntax"></a>

```
{
   "criteria": {
      "ebsVolumeSizeInGib": [
         {
            "comparison": "{{string}}",
            "values": [ {{number}} ]
         }
      ],
      "ebsVolumeType": [
         {
            "comparison": "{{string}}",
            "values": [ "{{string}}" ]
         }
      ],
      "estimatedMonthlySavings": [
         {
            "comparison": "{{string}}",
            "values": [ {{number}} ]
         }
      ],
      "lookBackPeriodInDays": [
         {
            "comparison": "{{string}}",
            "values": [ {{number}} ]
         }
      ],
      "region": [
         {
            "comparison": "{{string}}",
            "values": [ "{{string}}" ]
         }
      ],
      "resourceArn": [
         {
            "comparison": "{{string}}",
            "values": [ "{{string}}" ]
         }
      ],
      "resourceTag": [
         {
            "comparison": "{{string}}",
            "key": "{{string}}",
            "values": [ "{{string}}" ]
         }
      ],
      "restartNeeded": [
         {
            "comparison": "{{string}}",
            "values": [ "{{string}}" ]
         }
      ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "organizationScope": {
      "accountIds": [ "{{string}}" ]
   },
   "recommendedActionTypes": [ "{{string}}" ],
   "ruleType": "{{string}}"
}
```

## Request Parameters
<a name="API_automation_ListAutomationRulePreviewSummaries_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [criteria](#API_automation_ListAutomationRulePreviewSummaries_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationRulePreviewSummaries-request-criteria"></a>
 A set of conditions that specify which recommended action qualify for implementation. When a rule is active and a recommended action matches these criteria, Compute Optimizer implements the action at the scheduled run time. You can specify up to 20 conditions per filter criteria and 20 values per condition.
Type: [Criteria](API_automation_Criteria.md) object
Required: No

 ** [maxResults](#API_automation_ListAutomationRulePreviewSummaries_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationRulePreviewSummaries-request-maxResults"></a>
The maximum number of automation rule preview summaries to return in a single response. Valid range is 1-1000.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_automation_ListAutomationRulePreviewSummaries_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationRulePreviewSummaries-request-nextToken"></a>
A token used for pagination to retrieve the next set of results when the response is truncated.
Type: String
Pattern: `[A-Za-z0-9+/=]+`
Required: No

 ** [organizationScope](#API_automation_ListAutomationRulePreviewSummaries_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationRulePreviewSummaries-request-organizationScope"></a>
The organizational scope for the rule preview.
Type: [OrganizationScope](API_automation_OrganizationScope.md) object
Required: No

 ** [recommendedActionTypes](#API_automation_ListAutomationRulePreviewSummaries_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationRulePreviewSummaries-request-recommendedActionTypes"></a>
The types of recommended actions to include in the preview.
Type: Array of strings
Valid Values: `SnapshotAndDeleteUnattachedEbsVolume | UpgradeEbsVolumeType`
Required: Yes

 ** [ruleType](#API_automation_ListAutomationRulePreviewSummaries_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationRulePreviewSummaries-request-ruleType"></a>
The type of rule.
Type: String
Valid Values: `OrganizationRule | AccountRule`
Required: Yes

## Response Syntax
<a name="API_automation_ListAutomationRulePreviewSummaries_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "previewResultSummaries": [
      {
         "key": "string",
         "total": {
            "estimatedMonthlySavings": {
               "afterDiscountSavings": number,
               "beforeDiscountSavings": number,
               "currency": "string",
               "savingsEstimationMode": "string"
            },
            "recommendedActionCount": number
         }
      }
   ]
}
```

## Response Elements
<a name="API_automation_ListAutomationRulePreviewSummaries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_automation_ListAutomationRulePreviewSummaries_ResponseSyntax) **   <a name="computeoptimizer-automation_ListAutomationRulePreviewSummaries-response-nextToken"></a>
A token used for pagination. If present, indicates there are more results available and can be used in subsequent requests.
Type: String
Pattern: `[A-Za-z0-9+/=]+`

 ** [previewResultSummaries](#API_automation_ListAutomationRulePreviewSummaries_ResponseSyntax) **   <a name="computeoptimizer-automation_ListAutomationRulePreviewSummaries-response-previewResultSummaries"></a>
The list of automation rule preview summaries that match the specified criteria.
Type: Array of [PreviewResultSummary](API_automation_PreviewResultSummary.md) objects

## Errors
<a name="API_automation_ListAutomationRulePreviewSummaries_Errors"></a>

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
<a name="API_automation_ListAutomationRulePreviewSummaries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-automation-2025-09-22/ListAutomationRulePreviewSummaries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-automation-2025-09-22/ListAutomationRulePreviewSummaries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/ListAutomationRulePreviewSummaries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-automation-2025-09-22/ListAutomationRulePreviewSummaries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/ListAutomationRulePreviewSummaries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-automation-2025-09-22/ListAutomationRulePreviewSummaries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-automation-2025-09-22/ListAutomationRulePreviewSummaries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-automation-2025-09-22/ListAutomationRulePreviewSummaries)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-automation-2025-09-22/ListAutomationRulePreviewSummaries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/ListAutomationRulePreviewSummaries)
