---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_GetAutomationRule.html
---

# GetAutomationRule
<a name="API_automation_GetAutomationRule"></a>

 Retrieves details about a specific automation rule.

## Request Syntax
<a name="API_automation_GetAutomationRule_RequestSyntax"></a>

```
{
   "ruleArn": "{{string}}"
}
```

## Request Parameters
<a name="API_automation_GetAutomationRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ruleArn](#API_automation_GetAutomationRule_RequestSyntax) **   <a name="computeoptimizer-automation_GetAutomationRule-request-ruleArn"></a>
 The ARN of the rule to retrieve.
Type: String
Pattern: `arn:aws:compute-optimizer::[0-9]{12}:automation-rule/[a-zA-Z0-9_-]+`
Required: Yes

## Response Syntax
<a name="API_automation_GetAutomationRule_ResponseSyntax"></a>

```
{
   "accountId": "string",
   "createdTimestamp": number,
   "criteria": {
      "ebsVolumeSizeInGib": [
         {
            "comparison": "string",
            "values": [ number ]
         }
      ],
      "ebsVolumeType": [
         {
            "comparison": "string",
            "values": [ "string" ]
         }
      ],
      "estimatedMonthlySavings": [
         {
            "comparison": "string",
            "values": [ number ]
         }
      ],
      "lookBackPeriodInDays": [
         {
            "comparison": "string",
            "values": [ number ]
         }
      ],
      "region": [
         {
            "comparison": "string",
            "values": [ "string" ]
         }
      ],
      "resourceArn": [
         {
            "comparison": "string",
            "values": [ "string" ]
         }
      ],
      "resourceTag": [
         {
            "comparison": "string",
            "key": "string",
            "values": [ "string" ]
         }
      ],
      "restartNeeded": [
         {
            "comparison": "string",
            "values": [ "string" ]
         }
      ]
   },
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
   "status": "string",
   "tags": [
      {
         "key": "string",
         "value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_automation_GetAutomationRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountId](#API_automation_GetAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationRule-response-accountId"></a>
The 12-digit AWS account ID that owns this automation rule.
Type: String
Pattern: `[0-9]{12}`

 ** [createdTimestamp](#API_automation_GetAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationRule-response-createdTimestamp"></a>
The timestamp when the automation rule was created.
Type: Timestamp

 ** [criteria](#API_automation_GetAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationRule-response-criteria"></a>
 A set of conditions that specify which recommended action qualify for implementation. When a rule is active and a recommended action matches these criteria, Compute Optimizer implements the action at the scheduled run time. You can specify up to 20 conditions per filter criteria and 20 values per condition.
Type: [Criteria](API_automation_Criteria.md) object

 ** [description](#API_automation_GetAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationRule-response-description"></a>
A description of the automation rule.
Type: String

 ** [lastUpdatedTimestamp](#API_automation_GetAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationRule-response-lastUpdatedTimestamp"></a>
The timestamp when the automation rule was last updated.
Type: Timestamp

 ** [name](#API_automation_GetAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationRule-response-name"></a>
The name of the automation rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]*`

 ** [organizationConfiguration](#API_automation_GetAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationRule-response-organizationConfiguration"></a>
Configuration settings for organization-wide automation rules.
Type: [OrganizationConfiguration](API_automation_OrganizationConfiguration.md) object

 ** [priority](#API_automation_GetAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationRule-response-priority"></a>
A string representation of a decimal number between 0 and 1 (having up to 30 digits after the decimal point) that determines the priority of the rule.
Type: String

 ** [recommendedActionTypes](#API_automation_GetAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationRule-response-recommendedActionTypes"></a>
List of recommended action types that this rule can execute.
Type: Array of strings
Valid Values: `SnapshotAndDeleteUnattachedEbsVolume | UpgradeEbsVolumeType`

 ** [ruleArn](#API_automation_GetAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationRule-response-ruleArn"></a>
The Amazon Resource Name (ARN) of the automation rule.
Type: String
Pattern: `arn:aws:compute-optimizer::[0-9]{12}:automation-rule/[a-zA-Z0-9_-]+`

 ** [ruleId](#API_automation_GetAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationRule-response-ruleId"></a>
The unique identifier of the automation rule.
Type: String
Pattern: `[0-9A-Za-z]{16}`

 ** [ruleRevision](#API_automation_GetAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationRule-response-ruleRevision"></a>
The revision number of the automation rule.
Type: Long

 ** [ruleType](#API_automation_GetAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationRule-response-ruleType"></a>
The type of automation rule.
Type: String
Valid Values: `OrganizationRule | AccountRule`

 ** [schedule](#API_automation_GetAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationRule-response-schedule"></a>
Configuration for scheduling when automation rules should execute, including timing and execution windows.
Type: [Schedule](API_automation_Schedule.md) object

 ** [status](#API_automation_GetAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationRule-response-status"></a>
The current status of the automation rule (Active or Inactive).
Type: String
Valid Values: `Active | Inactive`

 ** [tags](#API_automation_GetAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_GetAutomationRule-response-tags"></a>
The tags associated with the automation rule.
Type: Array of [Tag](API_automation_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

## Errors
<a name="API_automation_GetAutomationRule_Errors"></a>

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

 ** ResourceNotFoundException **
 The specified resource was not found.
HTTP Status Code: 400

 ** ServiceUnavailableException **
 The service is temporarily unavailable.
HTTP Status Code: 500

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_automation_GetAutomationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-automation-2025-09-22/GetAutomationRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-automation-2025-09-22/GetAutomationRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/GetAutomationRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-automation-2025-09-22/GetAutomationRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/GetAutomationRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-automation-2025-09-22/GetAutomationRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-automation-2025-09-22/GetAutomationRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-automation-2025-09-22/GetAutomationRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-automation-2025-09-22/GetAutomationRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/GetAutomationRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
