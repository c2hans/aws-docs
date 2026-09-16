---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudget.html
---

# DescribeBudget
<a name="API_budgets_DescribeBudget"></a>

Describes a budget.

**Important**
The Request Syntax section shows the `BudgetLimit` syntax. For `PlannedBudgetLimits`, see the [Examples](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudget.html#API_DescribeBudget_Examples) section.

## Request Syntax
<a name="API_budgets_DescribeBudget_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}",
   "BudgetName": "{{string}}",
   "ShowFilterExpression": {{boolean}}
}
```

## Request Parameters
<a name="API_budgets_DescribeBudget_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_budgets_DescribeBudget_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeBudget-request-AccountId"></a>
The `accountId` that is associated with the budget that you want a description of.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** [BudgetName](#API_budgets_DescribeBudget_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeBudget-request-BudgetName"></a>
The name of the budget that you want a description of.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(?![^:\\]*/action/|(?i).*<script>.*</script>.*)[^:\\]+$`
Required: Yes

 ** [ShowFilterExpression](#API_budgets_DescribeBudget_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeBudget-request-ShowFilterExpression"></a>
Specifies whether the response includes the filter expression associated with the budget. By showing the filter expression, you can see detailed filtering logic applied to the budget, such as AWS services or tags that are being tracked.
Type: Boolean
Required: No

## Response Syntax
<a name="API_budgets_DescribeBudget_ResponseSyntax"></a>

```
{
   "Budget": {
      "AutoAdjustData": {
         "AutoAdjustType": "string",
         "HistoricalOptions": {
            "BudgetAdjustmentPeriod": number,
            "LookBackAvailablePeriods": number
         },
         "LastAutoAdjustTime": number
      },
      "BillingViewArn": "string",
      "BudgetLimit": {
         "Amount": "string",
         "Unit": "string"
      },
      "BudgetName": "string",
      "BudgetType": "string",
      "CalculatedSpend": {
         "ActualSpend": {
            "Amount": "string",
            "Unit": "string"
         },
         "ForecastedSpend": {
            "Amount": "string",
            "Unit": "string"
         }
      },
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
      "HealthStatus": {
         "LastUpdatedTime": number,
         "Status": "string",
         "StatusReason": "string"
      },
      "LastUpdatedTime": number,
      "Metrics": [ "string" ],
      "PlannedBudgetLimits": {
         "string" : {
            "Amount": "string",
            "Unit": "string"
         }
      },
      "TimePeriod": {
         "End": number,
         "Start": number
      },
      "TimeUnit": "string"
   }
}
```

## Response Elements
<a name="API_budgets_DescribeBudget_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Budget](#API_budgets_DescribeBudget_ResponseSyntax) **   <a name="awscostmanagement-budgets_DescribeBudget-response-Budget"></a>
The description of the budget.
Type: [Budget](API_budgets_Budget.md) object

## Errors
<a name="API_budgets_DescribeBudget_Errors"></a>

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

 ** ThrottlingException **
The number of API requests has exceeded the maximum allowed API request throttling limit for the account.
 ** Message **
The error message the exception carries.
HTTP Status Code: 400

## Examples
<a name="API_budgets_DescribeBudget_Examples"></a>

### Example
<a name="API_budgets_DescribeBudget_Example_1"></a>

The following is the `PlannedBudgetLimits` syntax.

```
{
   "Budget": {
      "BudgetLimit": {
         "Amount": "string",
         "Unit": "string"
      },
      "PlannedBudgetLimits": {
         "string": {
            "Amount": "string",
            "Unit": "string"
         }
      },
      "BudgetName": "string",
      "BudgetType": "string",
      "CalculatedSpend": {
         "ActualSpend": {
            "Amount": "string",
            "Unit": "string"
         },
         "ForecastedSpend": {
            "Amount": "string",
            "Unit": "string"
         }
      },
      "FilterExpression": {
         "And": [
            "Expression"
         ],
         "Dimensions": {
            "Key": "string",
            "Values": ["string"]
         },
         "Not": "Expression",
         "Or": [
            "Expression"
         ],
         "Tags": {
            "Key": "string",
            "Values": ["string"]
         }
      },
      "Metrics": ["string"],
      "LastUpdatedTime": number,
      "TimePeriod": {
         "End": number,
         "Start": number
      },
      "TimeUnit": "string"
   }
}
```

### Example
<a name="API_budgets_DescribeBudget_Example_2"></a>

The following is a sample request and response of the `DescribeBudget` operation using `BudgetLimit`

#### Sample Request
<a name="API_budgets_DescribeBudget_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: awsbudgets.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSBudgetServiceGateway.DescribeBudget

{
   "AccountId": "111122223333",
   "BudgetName": "Example Budget"
}
```

#### Sample Response
<a name="API_budgets_DescribeBudget_Example_2_Response"></a>

```
{
   "Budget": {
      "BudgetLimit": {
         "Amount": "100",
         "Unit": "USD"
      },
      "BudgetName": "Example Budget",
      "BudgetType": "COST",
      "CalculatedSpend": {
         "ActualSpend": {
            "Amount": "50",
            "Unit": "USD"
         },
         "ForecastedSpend": {
            "Amount": "100",
            "Unit": "USD"
         }
      },
      "FilterExpression": {
         "Dimensions": {
            "Key": "AZ",
            "Values": ["us-east-1"]
         }
      },
      "Metrics": ["UNBLENDED_COST"],
      "TimePeriod": {
         "Start": 1477353600,
         "End": 1477958399
      },
      "TimeUnit": "MONTHLY"
   }
}
```

### Example
<a name="API_budgets_DescribeBudget_Example_3"></a>

The following is a sample response of the `DescribeBudget` operation, using `PlannedBudgetLimits`.

#### Sample Response
<a name="API_budgets_DescribeBudget_Example_3_Response"></a>

```
{
   "Budget": {
      "PlannedBudgetLimits":{
         "1583020800": {
            "Amount": "100",
            "Unit": "USD"
         },
         "1564617600": {
            "Amount": "200",
            "Unit": "USD"
         },
         "1569888000": {
            "Amount": "300",
            "Unit": "USD"
         },
         "1556668800": {
            "Amount": "400",
            "Unit": "USD"
         },
         "1575158400": {
            "Amount": "500",
            "Unit": "USD"
         },
         "1580515200": {
            "Amount": "200",
            "Unit": "USD"
         }
      },
      "BudgetName": "Example Budget",
      "BudgetType": "COST",
      "CalculatedSpend": {
         "ActualSpend": {
            "Amount": "50",
            "Unit": "USD"
         },
         "ForecastedSpend": {
            "Amount": "100",
            "Unit": "USD"
         }
      },
      "FilterExpression": {
         "Dimensions": {
            "Key": "AZ",
            "Values": ["us-east-1"]
         }
      },
      "Metrics": ["UNBLENDED_COST"],
      "TimePeriod": {
         "Start": 1477353600,
         "End": 1477958399
      },
      "TimeUnit": "MONTHLY"
   }
}
```

## See Also
<a name="API_budgets_DescribeBudget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/budgets-2016-10-20/DescribeBudget)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/budgets-2016-10-20/DescribeBudget)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/DescribeBudget)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/budgets-2016-10-20/DescribeBudget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/DescribeBudget)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/budgets-2016-10-20/DescribeBudget)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/budgets-2016-10-20/DescribeBudget)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/budgets-2016-10-20/DescribeBudget)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/budgets-2016-10-20/DescribeBudget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/DescribeBudget)
