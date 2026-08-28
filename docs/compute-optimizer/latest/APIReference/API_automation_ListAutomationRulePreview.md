---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListAutomationRulePreview.html
---

# ListAutomationRulePreview
<a name="API_automation_ListAutomationRulePreview"></a>

Returns a preview of the recommended actions that match your Automation rule's configuration and criteria.

## Request Syntax
<a name="API_automation_ListAutomationRulePreview_RequestSyntax"></a>

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
<a name="API_automation_ListAutomationRulePreview_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [criteria](#API_automation_ListAutomationRulePreview_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationRulePreview-request-criteria"></a>
A set of conditions that specify which recommended action qualify for implementation. When a rule is active and a recommended action matches these criteria, Compute Optimizer implements the action at the scheduled run time.
Type: [Criteria](API_automation_Criteria.md) object
Required: No

 ** [maxResults](#API_automation_ListAutomationRulePreview_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationRulePreview-request-maxResults"></a>
The maximum number of automation rule preview results to return in a single response. Valid range is 1-1000.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_automation_ListAutomationRulePreview_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationRulePreview-request-nextToken"></a>
A token used for pagination to retrieve the next set of results when the response is truncated.
Type: String
Pattern: `[A-Za-z0-9+/=]+`
Required: No

 ** [organizationScope](#API_automation_ListAutomationRulePreview_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationRulePreview-request-organizationScope"></a>
 The organizational scope for the rule preview.
Type: [OrganizationScope](API_automation_OrganizationScope.md) object
Required: No

 ** [recommendedActionTypes](#API_automation_ListAutomationRulePreview_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationRulePreview-request-recommendedActionTypes"></a>
 The types of recommended actions to include in the preview.
Type: Array of strings
Valid Values: `SnapshotAndDeleteUnattachedEbsVolume | UpgradeEbsVolumeType`
Required: Yes

 ** [ruleType](#API_automation_ListAutomationRulePreview_RequestSyntax) **   <a name="computeoptimizer-automation_ListAutomationRulePreview-request-ruleType"></a>
 The type of rule.
Only the management account or a delegated administrator can set the ruleType to be OrganizationRule.
Type: String
Valid Values: `OrganizationRule | AccountRule`
Required: Yes

## Response Syntax
<a name="API_automation_ListAutomationRulePreview_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "previewResults": [
      {
         "accountId": "string",
         "currentResourceDetails": { ... },
         "currentResourceSummary": "string",
         "estimatedMonthlySavings": {
            "afterDiscountSavings": number,
            "beforeDiscountSavings": number,
            "currency": "string",
            "savingsEstimationMode": "string"
         },
         "lookBackPeriodInDays": number,
         "recommendedActionId": "string",
         "recommendedActionType": "string",
         "recommendedResourceDetails": { ... },
         "recommendedResourceSummary": "string",
         "region": "string",
         "resourceArn": "string",
         "resourceId": "string",
         "resourceTags": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "resourceType": "string",
         "restartNeeded": boolean
      }
   ]
}
```

## Response Elements
<a name="API_automation_ListAutomationRulePreview_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_automation_ListAutomationRulePreview_ResponseSyntax) **   <a name="computeoptimizer-automation_ListAutomationRulePreview-response-nextToken"></a>
A token used for pagination. If present, indicates there are more results available and can be used in subsequent requests.
Type: String
Pattern: `[A-Za-z0-9+/=]+`

 ** [previewResults](#API_automation_ListAutomationRulePreview_ResponseSyntax) **   <a name="computeoptimizer-automation_ListAutomationRulePreview-response-previewResults"></a>
 The list of actions that would be taken based on the specified criteria.
Type: Array of [PreviewResult](API_automation_PreviewResult.md) objects

## Errors
<a name="API_automation_ListAutomationRulePreview_Errors"></a>

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
<a name="API_automation_ListAutomationRulePreview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-automation-2025-09-22/ListAutomationRulePreview)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-automation-2025-09-22/ListAutomationRulePreview)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/ListAutomationRulePreview)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-automation-2025-09-22/ListAutomationRulePreview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/ListAutomationRulePreview)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-automation-2025-09-22/ListAutomationRulePreview)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-automation-2025-09-22/ListAutomationRulePreview)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-automation-2025-09-22/ListAutomationRulePreview)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-automation-2025-09-22/ListAutomationRulePreview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/ListAutomationRulePreview)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
