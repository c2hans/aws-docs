---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_ExecuteBudgetAction.html
---

# ExecuteBudgetAction
<a name="API_budgets_ExecuteBudgetAction"></a>

 Executes a budget action.

## Request Syntax
<a name="API_budgets_ExecuteBudgetAction_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}",
   "ActionId": "{{string}}",
   "BudgetName": "{{string}}",
   "ExecutionType": "{{string}}"
}
```

## Request Parameters
<a name="API_budgets_ExecuteBudgetAction_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_budgets_ExecuteBudgetAction_RequestSyntax) **   <a name="awscostmanagement-budgets_ExecuteBudgetAction-request-AccountId"></a>
The account ID of the user. It's a 12-digit number.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** [ActionId](#API_budgets_ExecuteBudgetAction_RequestSyntax) **   <a name="awscostmanagement-budgets_ExecuteBudgetAction-request-ActionId"></a>
 A system-generated universally unique identifier (UUID) for the action.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$`
Required: Yes

 ** [BudgetName](#API_budgets_ExecuteBudgetAction_RequestSyntax) **   <a name="awscostmanagement-budgets_ExecuteBudgetAction-request-BudgetName"></a>
 A string that represents the budget name. The ":" and "\\" characters, and the "/action/" substring, aren't allowed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(?![^:\\]*/action/|(?i).*<script>.*</script>.*)[^:\\]+$`
Required: Yes

 ** [ExecutionType](#API_budgets_ExecuteBudgetAction_RequestSyntax) **   <a name="awscostmanagement-budgets_ExecuteBudgetAction-request-ExecutionType"></a>
 The type of execution.
Type: String
Valid Values: `APPROVE_BUDGET_ACTION | RETRY_BUDGET_ACTION | REVERSE_BUDGET_ACTION | RESET_BUDGET_ACTION`
Required: Yes

## Response Syntax
<a name="API_budgets_ExecuteBudgetAction_ResponseSyntax"></a>

```
{
   "AccountId": "string",
   "ActionId": "string",
   "BudgetName": "string",
   "ExecutionType": "string"
}
```

## Response Elements
<a name="API_budgets_ExecuteBudgetAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountId](#API_budgets_ExecuteBudgetAction_ResponseSyntax) **   <a name="awscostmanagement-budgets_ExecuteBudgetAction-response-AccountId"></a>
The account ID of the user. It's a 12-digit number.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`

 ** [ActionId](#API_budgets_ExecuteBudgetAction_ResponseSyntax) **   <a name="awscostmanagement-budgets_ExecuteBudgetAction-response-ActionId"></a>
 A system-generated universally unique identifier (UUID) for the action.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$`

 ** [BudgetName](#API_budgets_ExecuteBudgetAction_ResponseSyntax) **   <a name="awscostmanagement-budgets_ExecuteBudgetAction-response-BudgetName"></a>
 A string that represents the budget name. The ":" and "\\" characters, and the "/action/" substring, aren't allowed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(?![^:\\]*/action/|(?i).*<script>.*</script>.*)[^:\\]+$`

 ** [ExecutionType](#API_budgets_ExecuteBudgetAction_ResponseSyntax) **   <a name="awscostmanagement-budgets_ExecuteBudgetAction-response-ExecutionType"></a>
 The type of execution.
Type: String
Valid Values: `APPROVE_BUDGET_ACTION | RETRY_BUDGET_ACTION | REVERSE_BUDGET_ACTION | RESET_BUDGET_ACTION`

## Errors
<a name="API_budgets_ExecuteBudgetAction_Errors"></a>

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
<a name="API_budgets_ExecuteBudgetAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/budgets-2016-10-20/ExecuteBudgetAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/budgets-2016-10-20/ExecuteBudgetAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/ExecuteBudgetAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/budgets-2016-10-20/ExecuteBudgetAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/ExecuteBudgetAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/budgets-2016-10-20/ExecuteBudgetAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/budgets-2016-10-20/ExecuteBudgetAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/budgets-2016-10-20/ExecuteBudgetAction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/budgets-2016-10-20/ExecuteBudgetAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/ExecuteBudgetAction)
