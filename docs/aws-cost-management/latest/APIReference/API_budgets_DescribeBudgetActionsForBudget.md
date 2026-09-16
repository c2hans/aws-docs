---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudgetActionsForBudget.html
---

# DescribeBudgetActionsForBudget
<a name="API_budgets_DescribeBudgetActionsForBudget"></a>

 Describes all of the budget actions for a budget.

## Request Syntax
<a name="API_budgets_DescribeBudgetActionsForBudget_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}",
   "BudgetName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_budgets_DescribeBudgetActionsForBudget_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_budgets_DescribeBudgetActionsForBudget_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgetActionsForBudget-request-AccountId"></a>
The account ID of the user. It's a 12-digit number.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** [BudgetName](#API_budgets_DescribeBudgetActionsForBudget_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgetActionsForBudget-request-BudgetName"></a>
 A string that represents the budget name. The ":" and "\\" characters, and the "/action/" substring, aren't allowed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(?![^:\\]*/action/|(?i).*<script>.*</script>.*)[^:\\]+$`
Required: Yes

 ** [MaxResults](#API_budgets_DescribeBudgetActionsForBudget_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgetActionsForBudget-request-MaxResults"></a>
 An integer that represents how many entries a paginated response contains. The maximum is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_budgets_DescribeBudgetActionsForBudget_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgetActionsForBudget-request-NextToken"></a>
 A generic string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2147483647.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_budgets_DescribeBudgetActionsForBudget_ResponseSyntax"></a>

```
{
   "Actions": [
      {
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
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_budgets_DescribeBudgetActionsForBudget_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Actions](#API_budgets_DescribeBudgetActionsForBudget_ResponseSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgetActionsForBudget-response-Actions"></a>
 A list of the budget action resources information.
Type: Array of [Action](API_budgets_Action.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [NextToken](#API_budgets_DescribeBudgetActionsForBudget_ResponseSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgetActionsForBudget-response-NextToken"></a>
 A generic string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2147483647.
Pattern: `.*`

## Errors
<a name="API_budgets_DescribeBudgetActionsForBudget_Errors"></a>

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

 ** InvalidNextTokenException **
The pagination token is invalid.
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

 ** ThrottlingException **
The number of API requests has exceeded the maximum allowed API request throttling limit for the account.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

## See Also
<a name="API_budgets_DescribeBudgetActionsForBudget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/budgets-2016-10-20/DescribeBudgetActionsForBudget)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/budgets-2016-10-20/DescribeBudgetActionsForBudget)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/DescribeBudgetActionsForBudget)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/budgets-2016-10-20/DescribeBudgetActionsForBudget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/DescribeBudgetActionsForBudget)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/budgets-2016-10-20/DescribeBudgetActionsForBudget)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/budgets-2016-10-20/DescribeBudgetActionsForBudget)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/budgets-2016-10-20/DescribeBudgetActionsForBudget)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/budgets-2016-10-20/DescribeBudgetActionsForBudget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/DescribeBudgetActionsForBudget)
