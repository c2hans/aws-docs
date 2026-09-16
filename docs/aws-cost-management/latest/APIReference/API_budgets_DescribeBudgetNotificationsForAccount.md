---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudgetNotificationsForAccount.html
---

# DescribeBudgetNotificationsForAccount
<a name="API_budgets_DescribeBudgetNotificationsForAccount"></a>

 Lists the budget names and notifications that are associated with an account.

## Request Syntax
<a name="API_budgets_DescribeBudgetNotificationsForAccount_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_budgets_DescribeBudgetNotificationsForAccount_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_budgets_DescribeBudgetNotificationsForAccount_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgetNotificationsForAccount-request-AccountId"></a>
The account ID of the user. It's a 12-digit number.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** [MaxResults](#API_budgets_DescribeBudgetNotificationsForAccount_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgetNotificationsForAccount-request-MaxResults"></a>
 An integer that represents how many budgets a paginated response contains. The default is 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_budgets_DescribeBudgetNotificationsForAccount_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgetNotificationsForAccount-request-NextToken"></a>
 A generic string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2147483647.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_budgets_DescribeBudgetNotificationsForAccount_ResponseSyntax"></a>

```
{
   "BudgetNotificationsForAccount": [
      {
         "BudgetName": "string",
         "Notifications": [
            {
               "ComparisonOperator": "string",
               "NotificationState": "string",
               "NotificationType": "string",
               "Threshold": number,
               "ThresholdType": "string"
            }
         ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_budgets_DescribeBudgetNotificationsForAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BudgetNotificationsForAccount](#API_budgets_DescribeBudgetNotificationsForAccount_ResponseSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgetNotificationsForAccount-response-BudgetNotificationsForAccount"></a>
 A list of budget names and associated notifications for an account.
Type: Array of [BudgetNotificationsForAccount](API_budgets_BudgetNotificationsForAccount.md) objects
Array Members: Maximum number of 1000 items.

 ** [NextToken](#API_budgets_DescribeBudgetNotificationsForAccount_ResponseSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgetNotificationsForAccount-response-NextToken"></a>
 A generic string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2147483647.
Pattern: `.*`

## Errors
<a name="API_budgets_DescribeBudgetNotificationsForAccount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to use this operation with the given parameters.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

 ** ExpiredNextTokenException **
The pagination token expired.
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
<a name="API_budgets_DescribeBudgetNotificationsForAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/budgets-2016-10-20/DescribeBudgetNotificationsForAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/budgets-2016-10-20/DescribeBudgetNotificationsForAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/DescribeBudgetNotificationsForAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/budgets-2016-10-20/DescribeBudgetNotificationsForAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/DescribeBudgetNotificationsForAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/budgets-2016-10-20/DescribeBudgetNotificationsForAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/budgets-2016-10-20/DescribeBudgetNotificationsForAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/budgets-2016-10-20/DescribeBudgetNotificationsForAccount)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/budgets-2016-10-20/DescribeBudgetNotificationsForAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/DescribeBudgetNotificationsForAccount)
