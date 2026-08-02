---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudgetPerformanceHistory.html
---

# DescribeBudgetPerformanceHistory
<a name="API_budgets_DescribeBudgetPerformanceHistory"></a>

Describes the history for `DAILY`, `MONTHLY`, and `QUARTERLY` budgets. Budget history isn't available for `ANNUAL` budgets.

## Request Syntax
<a name="API_budgets_DescribeBudgetPerformanceHistory_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}",
   "BudgetName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "TimePeriod": {
      "End": {{number}},
      "Start": {{number}}
   }
}
```

## Request Parameters
<a name="API_budgets_DescribeBudgetPerformanceHistory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_budgets_DescribeBudgetPerformanceHistory_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgetPerformanceHistory-request-AccountId"></a>
The account ID of the user. It's a 12-digit number.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** [BudgetName](#API_budgets_DescribeBudgetPerformanceHistory_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgetPerformanceHistory-request-BudgetName"></a>
 A string that represents the budget name. The ":" and "\\" characters, and the "/action/" substring, aren't allowed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(?![^:\\]*/action/|(?i).*<script>.*</script>.*)[^:\\]+$`
Required: Yes

 ** [MaxResults](#API_budgets_DescribeBudgetPerformanceHistory_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgetPerformanceHistory-request-MaxResults"></a>
 An integer that represents how many entries a paginated response contains. The maximum is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_budgets_DescribeBudgetPerformanceHistory_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgetPerformanceHistory-request-NextToken"></a>
 A generic string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2147483647.
Pattern: `.*`
Required: No

 ** [TimePeriod](#API_budgets_DescribeBudgetPerformanceHistory_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgetPerformanceHistory-request-TimePeriod"></a>
Retrieves how often the budget went into an `ALARM` state for the specified time period.
Type: [TimePeriod](API_budgets_TimePeriod.md) object
Required: No

## Response Syntax
<a name="API_budgets_DescribeBudgetPerformanceHistory_ResponseSyntax"></a>

```
{
   "BudgetPerformanceHistory": {
      "BillingViewArn": "string",
      "BudgetedAndActualAmountsList": [
         {
            "ActualAmount": {
               "Amount": "string",
               "Unit": "string"
            },
            "BudgetedAmount": {
               "Amount": "string",
               "Unit": "string"
            },
            "TimePeriod": {
               "End": number,
               "Start": number
            }
         }
      ],
      "BudgetName": "string",
      "BudgetType": "string",
      "CostFilters": {
         "string" : [ "string" ]
      },
      "CostTypes": {
         "IncludeCredit": boolean,
         "IncludeDiscount": boolean,
         "IncludeOtherSubscription": boolean,
         "IncludeRecurring": boolean,
         "IncludeRefund": boolean,
         "IncludeSubscription": boolean,
         "IncludeSupport": boolean,
         "IncludeTax": boolean,
         "IncludeUpfront": boolean,
         "UseAmortized": boolean,
         "UseBlended": boolean
      },
      "FilterExpression": {
         "And": [
            "Expression"
         ],
         "CostCategories": {
            "Key": "string",
            "MatchOptions": [ "string" ],
            "Values": [ "string" ]
         },
         "Dimensions": {
            "Key": "string",
            "MatchOptions": [ "string" ],
            "Values": [ "string" ]
         },
         "Not": "Expression",
         "Or": [
            "Expression"
         ],
         "Tags": {
            "Key": "string",
            "MatchOptions": [ "string" ],
            "Values": [ "string" ]
         }
      },
      "Metrics": [ "string" ],
      "TimeUnit": "string"
   },
   "NextToken": "string"
}
```

## Response Elements
<a name="API_budgets_DescribeBudgetPerformanceHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BudgetPerformanceHistory](#API_budgets_DescribeBudgetPerformanceHistory_ResponseSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgetPerformanceHistory-response-BudgetPerformanceHistory"></a>
The history of how often the budget has gone into an `ALARM` state.
For `DAILY` budgets, the history saves the state of the budget for the last 60 days. For `MONTHLY` budgets, the history saves the state of the budget for the current month plus the last 12 months. For `QUARTERLY` budgets, the history saves the state of the budget for the last four quarters.
Type: [BudgetPerformanceHistory](API_budgets_BudgetPerformanceHistory.md) object

 ** [NextToken](#API_budgets_DescribeBudgetPerformanceHistory_ResponseSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgetPerformanceHistory-response-NextToken"></a>
 A generic string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2147483647.
Pattern: `.*`

## Errors
<a name="API_budgets_DescribeBudgetPerformanceHistory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to use this operation with the given parameters.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

 ** BillingViewHealthStatusException **
 The billing view status must be HEALTHY to perform this action. Try again when the status is HEALTHY.
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

## Examples
<a name="API_budgets_DescribeBudgetPerformanceHistory_Examples"></a>

### Example
<a name="API_budgets_DescribeBudgetPerformanceHistory_Example_1"></a>

The following is a sample request of the `DescribeBudgetPerformanceHistory` operation.

#### Sample Request
<a name="API_budgets_DescribeBudgetPerformanceHistory_Example_1_Request"></a>

```
GET HTTP/1.1
Host: awsbudgets.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSBudgetServiceGateway.DescribeBudgetPerformanceHistory
{
   "AccountId": "111122223333",
   "Budget": "ExampleBudget"
}
```

#### Sample Response
<a name="API_budgets_DescribeBudgetPerformanceHistory_Example_1_Response"></a>

```
{
   "BudgetPerformanceHistory": {
      "BudgetedAndActualAmountsList": [
         {
            "ActualAmount": {
               "Amount": "50",
               "Unit": "USD"
            },
            "BudgetedAmount": {
               "Amount": "100",
               "Unit": "USD"
            },
            "TimePeriod": {
               "End": 1477958399,
               "Start": 1477353600
            }
         }
      ],
      "BudgetName": "ExampleBudget",
      "BudgetType": "COST",
      "CostFilters": {
          "AZ" : [ "us-east-1" ]
      },
      "CostTypes": {
         "IncludeCredit": true,
         "IncludeDiscount": true,
         "IncludeOtherSubscription": true,
         "IncludeRecurring": true,
         "IncludeRefund": true,
         "IncludeSubscription": true,
         "IncludeSupport": true,
         "IncludeTax": true,
         "IncludeUpfront": true,
         "UseBlended": false
      },
      "TimeUnit": "MONTHLY"
   }
}
```

## See Also
<a name="API_budgets_DescribeBudgetPerformanceHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/budgets-2016-10-20/DescribeBudgetPerformanceHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/budgets-2016-10-20/DescribeBudgetPerformanceHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/DescribeBudgetPerformanceHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/budgets-2016-10-20/DescribeBudgetPerformanceHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/DescribeBudgetPerformanceHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/budgets-2016-10-20/DescribeBudgetPerformanceHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/budgets-2016-10-20/DescribeBudgetPerformanceHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/budgets-2016-10-20/DescribeBudgetPerformanceHistory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/budgets-2016-10-20/DescribeBudgetPerformanceHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/DescribeBudgetPerformanceHistory)
