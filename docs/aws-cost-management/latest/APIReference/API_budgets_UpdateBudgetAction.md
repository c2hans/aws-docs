---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_UpdateBudgetAction.html
---

# UpdateBudgetAction
<a name="API_budgets_UpdateBudgetAction"></a>

 Updates a budget action.

## Request Syntax
<a name="API_budgets_UpdateBudgetAction_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}",
   "ActionId": "{{string}}",
   "ActionThreshold": {
      "ActionThresholdType": "{{string}}",
      "ActionThresholdValue": {{number}}
   },
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
   "Subscribers": [
      {
         "Address": "{{string}}",
         "SubscriptionType": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_budgets_UpdateBudgetAction_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_budgets_UpdateBudgetAction_RequestSyntax) **   <a name="awscostmanagement-budgets_UpdateBudgetAction-request-AccountId"></a>
The account ID of the user. It's a 12-digit number.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** [ActionId](#API_budgets_UpdateBudgetAction_RequestSyntax) **   <a name="awscostmanagement-budgets_UpdateBudgetAction-request-ActionId"></a>
 A system-generated universally unique identifier (UUID) for the action.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$`
Required: Yes

 ** [ActionThreshold](#API_budgets_UpdateBudgetAction_RequestSyntax) **   <a name="awscostmanagement-budgets_UpdateBudgetAction-request-ActionThreshold"></a>
The trigger threshold of the action.
Type: [ActionThreshold](API_budgets_ActionThreshold.md) object
Required: No

 ** [ApprovalModel](#API_budgets_UpdateBudgetAction_RequestSyntax) **   <a name="awscostmanagement-budgets_UpdateBudgetAction-request-ApprovalModel"></a>
 This specifies if the action needs manual or automatic approval.
Type: String
Valid Values: `AUTOMATIC | MANUAL`
Required: No

 ** [BudgetName](#API_budgets_UpdateBudgetAction_RequestSyntax) **   <a name="awscostmanagement-budgets_UpdateBudgetAction-request-BudgetName"></a>
 A string that represents the budget name. The ":" and "\\" characters, and the "/action/" substring, aren't allowed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(?![^:\\]*/action/|(?i).*<script>.*</script>.*)[^:\\]+$`
Required: Yes

 ** [Definition](#API_budgets_UpdateBudgetAction_RequestSyntax) **   <a name="awscostmanagement-budgets_UpdateBudgetAction-request-Definition"></a>
Specifies all of the type-specific parameters.
Type: [Definition](API_budgets_Definition.md) object
Required: No

 ** [ExecutionRoleArn](#API_budgets_UpdateBudgetAction_RequestSyntax) **   <a name="awscostmanagement-budgets_UpdateBudgetAction-request-ExecutionRoleArn"></a>
 The role passed for action execution and reversion. Roles and actions must be in the same account.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 618.
Pattern: `^arn:aws(-eusc|-cn|-us-gov|-iso|-iso-[a-z]{1})?:iam::\d{12}:role(\u002F[\u0021-\u007F]+\u002F|\u002F)[\w+=,.@-]+$`
Required: No

 ** [NotificationType](#API_budgets_UpdateBudgetAction_RequestSyntax) **   <a name="awscostmanagement-budgets_UpdateBudgetAction-request-NotificationType"></a>
 The type of a notification. It must be ACTUAL or FORECASTED.
Type: String
Valid Values: `ACTUAL | FORECASTED`
Required: No

 ** [Subscribers](#API_budgets_UpdateBudgetAction_RequestSyntax) **   <a name="awscostmanagement-budgets_UpdateBudgetAction-request-Subscribers"></a>
 A list of subscribers.
Type: Array of [Subscriber](API_budgets_Subscriber.md) objects
Array Members: Minimum number of 1 item. Maximum number of 11 items.
Required: No

## Response Syntax
<a name="API_budgets_UpdateBudgetAction_ResponseSyntax"></a>

```
{
   "AccountId": "string",
   "BudgetName": "string",
   "NewAction": {
      "ActionId": "string",
      "ActionThreshold": {
         "ActionThresholdType": "string",
         "ActionThresholdValue": number
      },
      "ActionType": "string",
      "ApprovalModel": "string",
      "BudgetName": "string",
      "Definition": {
         "IamActionDefinition": {
            "Groups": [ "string" ],
            "PolicyArn": "string",
            "Roles": [ "string" ],
            "Users": [ "string" ]
         },
         "ScpActionDefinition": {
            "PolicyId": "string",
            "TargetIds": [ "string" ]
         },
         "SsmActionDefinition": {
            "ActionSubType": "string",
            "InstanceIds": [ "string" ],
            "Region": "string"
         }
      },
      "ExecutionRoleArn": "string",
      "NotificationType": "string",
      "Status": "string",
      "Subscribers": [
         {
            "Address": "string",
            "SubscriptionType": "string"
         }
      ]
   },
   "OldAction": {
      "ActionId": "string",
      "ActionThreshold": {
         "ActionThresholdType": "string",
         "ActionThresholdValue": number
      },
      "ActionType": "string",
      "ApprovalModel": "string",
      "BudgetName": "string",
      "Definition": {
         "IamActionDefinition": {
            "Groups": [ "string" ],
            "PolicyArn": "string",
            "Roles": [ "string" ],
            "Users": [ "string" ]
         },
         "ScpActionDefinition": {
            "PolicyId": "string",
            "TargetIds": [ "string" ]
         },
         "SsmActionDefinition": {
            "ActionSubType": "string",
            "InstanceIds": [ "string" ],
            "Region": "string"
         }
      },
      "ExecutionRoleArn": "string",
      "NotificationType": "string",
      "Status": "string",
      "Subscribers": [
         {
            "Address": "string",
            "SubscriptionType": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_budgets_UpdateBudgetAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountId](#API_budgets_UpdateBudgetAction_ResponseSyntax) **   <a name="awscostmanagement-budgets_UpdateBudgetAction-response-AccountId"></a>
The account ID of the user. It's a 12-digit number.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`

 ** [BudgetName](#API_budgets_UpdateBudgetAction_ResponseSyntax) **   <a name="awscostmanagement-budgets_UpdateBudgetAction-response-BudgetName"></a>
 A string that represents the budget name. The ":" and "\\" characters, and the "/action/" substring, aren't allowed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(?![^:\\]*/action/|(?i).*<script>.*</script>.*)[^:\\]+$`

 ** [NewAction](#API_budgets_UpdateBudgetAction_ResponseSyntax) **   <a name="awscostmanagement-budgets_UpdateBudgetAction-response-NewAction"></a>
 The updated action resource information.
Type: [Action](API_budgets_Action.md) object

 ** [OldAction](#API_budgets_UpdateBudgetAction_ResponseSyntax) **   <a name="awscostmanagement-budgets_UpdateBudgetAction-response-OldAction"></a>
 The previous action resource information.
Type: [Action](API_budgets_Action.md) object

## Errors
<a name="API_budgets_UpdateBudgetAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to use this operation with the given parameters.
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

 ** ResourceLockedException **
The request was received and recognized by the server, but the server rejected that particular method for the requested resource.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

 ** ThrottlingException **
The number of API requests has exceeded the maximum allowed API request throttling limit for the account.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

## See Also
<a name="API_budgets_UpdateBudgetAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/budgets-2016-10-20/UpdateBudgetAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/budgets-2016-10-20/UpdateBudgetAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/UpdateBudgetAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/budgets-2016-10-20/UpdateBudgetAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/UpdateBudgetAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/budgets-2016-10-20/UpdateBudgetAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/budgets-2016-10-20/UpdateBudgetAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/budgets-2016-10-20/UpdateBudgetAction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/budgets-2016-10-20/UpdateBudgetAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/UpdateBudgetAction)
