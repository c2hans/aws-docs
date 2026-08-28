---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_UpdateAutomationRule.html
---

# UpdateAutomationRule
<a name="API_automation_UpdateAutomationRule"></a>

 Updates an existing automation rule.

## Request Syntax
<a name="API_automation_UpdateAutomationRule_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
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
   "description": "{{string}}",
   "name": "{{string}}",
   "organizationConfiguration": {
      "accountIds": [ "{{string}}" ],
      "ruleApplyOrder": "{{string}}"
   },
   "priority": "{{string}}",
   "recommendedActionTypes": [ "{{string}}" ],
   "ruleArn": "{{string}}",
   "ruleRevision": {{number}},
   "ruleType": "{{string}}",
   "schedule": {
      "executionWindowInMinutes": {{number}},
      "scheduleExpression": "{{string}}",
      "scheduleExpressionTimezone": "{{string}}"
   },
   "status": "{{string}}"
}
```

## Request Parameters
<a name="API_automation_UpdateAutomationRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_automation_UpdateAutomationRule_RequestSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Must be 1-64 characters long and contain only alphanumeric characters, underscores, and hyphens.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,64}`
Required: No

 ** [criteria](#API_automation_UpdateAutomationRule_RequestSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-request-criteria"></a>
 A set of conditions that specify which recommended action qualify for implementation. When a rule is active and a recommended action matches these criteria, Compute Optimizer implements the action at the scheduled run time. You can specify up to 20 conditions per filter criteria and 20 values per condition.
Type: [Criteria](API_automation_Criteria.md) object
Required: No

 ** [description](#API_automation_UpdateAutomationRule_RequestSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-request-description"></a>
The updated description of the automation rule. Can be up to 1024 characters long and contain alphanumeric characters, underscores, hyphens, spaces, and certain special characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9_\-\s@\.]*`
Required: No

 ** [name](#API_automation_UpdateAutomationRule_RequestSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-request-name"></a>
The updated name of the automation rule. Must be 1-128 characters long and contain only alphanumeric characters, underscores, and hyphens.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]*`
Required: No

 ** [organizationConfiguration](#API_automation_UpdateAutomationRule_RequestSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-request-organizationConfiguration"></a>
Updated configuration settings for organization-wide rules, including rule application order and target account IDs.
Type: [OrganizationConfiguration](API_automation_OrganizationConfiguration.md) object
Required: No

 ** [priority](#API_automation_UpdateAutomationRule_RequestSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-request-priority"></a>
The updated priority level of the automation rule, used to determine execution order when multiple rules apply to the same resource.
Type: String
Required: No

 ** [recommendedActionTypes](#API_automation_UpdateAutomationRule_RequestSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-request-recommendedActionTypes"></a>
Updated list of recommended action types that this rule can execute, such as SnapshotAndDeleteUnattachedEbsVolume or UpgradeEbsVolumeType.
Type: Array of strings
Valid Values: `SnapshotAndDeleteUnattachedEbsVolume | UpgradeEbsVolumeType`
Required: No

 ** [ruleArn](#API_automation_UpdateAutomationRule_RequestSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-request-ruleArn"></a>
 The ARN of the rule to update.
Type: String
Pattern: `arn:aws:compute-optimizer::[0-9]{12}:automation-rule/[a-zA-Z0-9_-]+`
Required: Yes

 ** [ruleRevision](#API_automation_UpdateAutomationRule_RequestSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-request-ruleRevision"></a>
 The revision number of the rule to update.
Type: Long
Required: Yes

 ** [ruleType](#API_automation_UpdateAutomationRule_RequestSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-request-ruleType"></a>
The updated type of automation rule. Can be either OrganizationRule for organization-wide rules or AccountRule for account-specific rules.
Type: String
Valid Values: `OrganizationRule | AccountRule`
Required: No

 ** [schedule](#API_automation_UpdateAutomationRule_RequestSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-request-schedule"></a>
The updated schedule configuration for when the automation rule should execute, including cron expression, timezone, and execution window.
Type: [Schedule](API_automation_Schedule.md) object
Required: No

 ** [status](#API_automation_UpdateAutomationRule_RequestSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-request-status"></a>
The updated status of the automation rule. Can be Active or Inactive.
Type: String
Valid Values: `Active | Inactive`
Required: No

## Response Syntax
<a name="API_automation_UpdateAutomationRule_ResponseSyntax"></a>

```
{
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
   "ruleRevision": number,
   "ruleType": "string",
   "schedule": {
      "executionWindowInMinutes": number,
      "scheduleExpression": "string",
      "scheduleExpressionTimezone": "string"
   },
   "status": "string"
}
```

## Response Elements
<a name="API_automation_UpdateAutomationRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdTimestamp](#API_automation_UpdateAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-response-createdTimestamp"></a>
The timestamp when the automation rule was originally created.
Type: Timestamp

 ** [criteria](#API_automation_UpdateAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-response-criteria"></a>
 A set of conditions that specify which recommended action qualify for implementation. When a rule is active and a recommended action matches these criteria, Compute Optimizer implements the action at the scheduled run time. You can specify up to 20 conditions per filter criteria and 20 values per condition.
Type: [Criteria](API_automation_Criteria.md) object

 ** [description](#API_automation_UpdateAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-response-description"></a>
The updated description of the automation rule.
Type: String

 ** [lastUpdatedTimestamp](#API_automation_UpdateAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-response-lastUpdatedTimestamp"></a>
The timestamp when the automation rule was last updated.
Type: Timestamp

 ** [name](#API_automation_UpdateAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-response-name"></a>
The updated name of the automation rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]*`

 ** [organizationConfiguration](#API_automation_UpdateAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-response-organizationConfiguration"></a>
The updated organization configuration settings.
Type: [OrganizationConfiguration](API_automation_OrganizationConfiguration.md) object

 ** [priority](#API_automation_UpdateAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-response-priority"></a>
The updated priority level of the automation rule.
Type: String

 ** [recommendedActionTypes](#API_automation_UpdateAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-response-recommendedActionTypes"></a>
The updated list of recommended action types.
Type: Array of strings
Valid Values: `SnapshotAndDeleteUnattachedEbsVolume | UpgradeEbsVolumeType`

 ** [ruleArn](#API_automation_UpdateAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-response-ruleArn"></a>
 The ARN of the updated rule.
Type: String
Pattern: `arn:aws:compute-optimizer::[0-9]{12}:automation-rule/[a-zA-Z0-9_-]+`

 ** [ruleRevision](#API_automation_UpdateAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-response-ruleRevision"></a>
 The new revision number of the updated rule.
Type: Long

 ** [ruleType](#API_automation_UpdateAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-response-ruleType"></a>
The updated type of automation rule.
Type: String
Valid Values: `OrganizationRule | AccountRule`

 ** [schedule](#API_automation_UpdateAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-response-schedule"></a>
The updated schedule configuration.
Type: [Schedule](API_automation_Schedule.md) object

 ** [status](#API_automation_UpdateAutomationRule_ResponseSyntax) **   <a name="computeoptimizer-automation_UpdateAutomationRule-response-status"></a>
The updated status of the automation rule.
Type: String
Valid Values: `Active | Inactive`

## Errors
<a name="API_automation_UpdateAutomationRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You do not have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** ForbiddenException **
 You are not authorized to perform this action.
HTTP Status Code: 400

 ** IdempotencyTokenInUseException **
 The specified client token is already in use.
HTTP Status Code: 400

 ** IdempotentParameterMismatchException **
Exception thrown when the same client token is used with different parameters, indicating a mismatch in idempotent request parameters.
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
<a name="API_automation_UpdateAutomationRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-automation-2025-09-22/UpdateAutomationRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-automation-2025-09-22/UpdateAutomationRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/UpdateAutomationRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-automation-2025-09-22/UpdateAutomationRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/UpdateAutomationRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-automation-2025-09-22/UpdateAutomationRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-automation-2025-09-22/UpdateAutomationRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-automation-2025-09-22/UpdateAutomationRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-automation-2025-09-22/UpdateAutomationRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/UpdateAutomationRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
