---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_CreateBudgetAction.html
---

# CreateBudgetAction
<a name="API_budgets_CreateBudgetAction"></a>

 Creates a budget action.

## Request Syntax
<a name="API_budgets_CreateBudgetAction_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}",
   "ActionThreshold": {
      "ActionThresholdType": "{{string}}",
      "ActionThresholdValue": {{number}}
   },
   "ActionType": "{{string}}",
   "ApprovalModel": "{{string}}",
   "BudgetName": "{{string}}",
   "Definition": {
      "IamActionDefinition": {
         "Groups": [ "{{string}}" ],
         "PolicyArn": "{{string}}",
         "Roles": [ "{{string}}" ],
         "Users": [ "{{string}}" ]
      },
      "ScpActionDefinition": {
         "PolicyId": "{{string}}",
         "TargetIds": [ "{{string}}" ]
      },
      "SsmActionDefinition": {
         "ActionSubType": "{{string}}",
         "InstanceIds": [ "{{string}}" ],
         "Region": "{{string}}"
      }
   },
   "ExecutionRoleArn": "{{string}}",
   "NotificationType": "{{string}}",
   "ResourceTags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Subscribers": [
      {
         "Address": "{{string}}",
         "SubscriptionType": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_budgets_CreateBudgetAction_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_budgets_CreateBudgetAction_RequestSyntax) **   <a name="awscostmanagement-budgets_CreateBudgetAction-request-AccountId"></a>
The account ID of the user. It's a 12-digit number.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** [ActionThreshold](#API_budgets_CreateBudgetAction_RequestSyntax) **   <a name="awscostmanagement-budgets_CreateBudgetAction-request-ActionThreshold"></a>
The trigger threshold of the action.
Type: [ActionThreshold](API_budgets_ActionThreshold.md) object
Required: Yes

 ** [ActionType](#API_budgets_CreateBudgetAction_RequestSyntax) **   <a name="awscostmanagement-budgets_CreateBudgetAction-request-ActionType"></a>
 The type of action. This defines the type of tasks that can be carried out by this action. This field also determines the format for definition.
Type: String
Valid Values: `APPLY_IAM_POLICY | APPLY_SCP_POLICY | RUN_SSM_DOCUMENTS`
Required: Yes

 ** [ApprovalModel](#API_budgets_CreateBudgetAction_RequestSyntax) **   <a name="awscostmanagement-budgets_CreateBudgetAction-request-ApprovalModel"></a>
 This specifies if the action needs manual or automatic approval.
Type: String
Valid Values: `AUTOMATIC | MANUAL`
Required: Yes

 ** [BudgetName](#API_budgets_CreateBudgetAction_RequestSyntax) **   <a name="awscostmanagement-budgets_CreateBudgetAction-request-BudgetName"></a>
 A string that represents the budget name. The ":" and "\\" characters, and the "/action/" substring, aren't allowed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(?![^:\\]*/action/|(?i).*<script>.*</script>.*)[^:\\]+$`
Required: Yes

 ** [Definition](#API_budgets_CreateBudgetAction_RequestSyntax) **   <a name="awscostmanagement-budgets_CreateBudgetAction-request-Definition"></a>
Specifies all of the type-specific parameters.
Type: [Definition](API_budgets_Definition.md) object
Required: Yes

 ** [ExecutionRoleArn](#API_budgets_CreateBudgetAction_RequestSyntax) **   <a name="awscostmanagement-budgets_CreateBudgetAction-request-ExecutionRoleArn"></a>
 The role passed for action execution and reversion. Roles and actions must be in the same account.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 618.
Pattern: `^arn:aws(-eusc|-cn|-us-gov|-iso|-iso-[a-z]{1})?:iam::\d{12}:role(\u002F[\u0021-\u007F]+\u002F|\u002F)[\w+=,.@-]+$`
Required: Yes

 ** [NotificationType](#API_budgets_CreateBudgetAction_RequestSyntax) **   <a name="awscostmanagement-budgets_CreateBudgetAction-request-NotificationType"></a>
 The type of a notification. It must be ACTUAL or FORECASTED.
Type: String
Valid Values: `ACTUAL | FORECASTED`
Required: Yes

 ** [ResourceTags](#API_budgets_CreateBudgetAction_RequestSyntax) **   <a name="awscostmanagement-budgets_CreateBudgetAction-request-ResourceTags"></a>
An optional list of tags to associate with the specified budget action. Each tag consists of a key and a value, and each key must be unique for the resource.
Type: Array of [ResourceTag](API_budgets_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [Subscribers](#API_budgets_CreateBudgetAction_RequestSyntax) **   <a name="awscostmanagement-budgets_CreateBudgetAction-request-Subscribers"></a>
 A list of subscribers.
Type: Array of [Subscriber](API_budgets_Subscriber.md) objects
Array Members: Minimum number of 1 item. Maximum number of 11 items.
Required: Yes

## Response Syntax
<a name="API_budgets_CreateBudgetAction_ResponseSyntax"></a>

```
{
   "AccountId": "string",
   "ActionId": "string",
   "BudgetName": "string"
}
```

## Response Elements
<a name="API_budgets_CreateBudgetAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountId](#API_budgets_CreateBudgetAction_ResponseSyntax) **   <a name="awscostmanagement-budgets_CreateBudgetAction-response-AccountId"></a>
The account ID of the user. It's a 12-digit number.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`

 ** [ActionId](#API_budgets_CreateBudgetAction_ResponseSyntax) **   <a name="awscostmanagement-budgets_CreateBudgetAction-response-ActionId"></a>
 A system-generated universally unique identifier (UUID) for the action.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$`

 ** [BudgetName](#API_budgets_CreateBudgetAction_ResponseSyntax) **   <a name="awscostmanagement-budgets_CreateBudgetAction-response-BudgetName"></a>
 A string that represents the budget name. The ":" and "\\" characters, and the "/action/" substring, aren't allowed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(?![^:\\]*/action/|(?i).*<script>.*</script>.*)[^:\\]+$`

## Errors
<a name="API_budgets_CreateBudgetAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to use this operation with the given parameters.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

 ** CreationLimitExceededException **
You've exceeded the notification or subscriber limit.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

 ** DuplicateRecordException **
The budget name already exists. Budget names must be unique within an account.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

 ** InternalErrorException **
An error on the server occurred during the processing of your request. Try again later.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

 ** InvalidParameterException **
An error on the client occurred. Typically, the cause is an invalid input value.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

 ** NotFoundException **
We can’t locate the resource that you specified.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
You've reached a Service Quota limit on this resource.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

 ** ThrottlingException **
The number of API requests has exceeded the maximum allowed API request throttling limit for the account.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

## See Also
<a name="API_budgets_CreateBudgetAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/budgets-2016-10-20/CreateBudgetAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/budgets-2016-10-20/CreateBudgetAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/CreateBudgetAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/budgets-2016-10-20/CreateBudgetAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/CreateBudgetAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/budgets-2016-10-20/CreateBudgetAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/budgets-2016-10-20/CreateBudgetAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/budgets-2016-10-20/CreateBudgetAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/budgets-2016-10-20/CreateBudgetAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/CreateBudgetAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
