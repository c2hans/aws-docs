---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudgets.html
---

# DescribeBudgets
<a name="API_budgets_DescribeBudgets"></a>

Lists the budgets that are associated with an account.

**Important**
The Request Syntax section shows the `BudgetLimit` syntax. For `PlannedBudgetLimits`, see the [Examples](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudgets.html#API_DescribeBudgets_Examples) section.

## Request Syntax
<a name="API_budgets_DescribeBudgets_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ShowFilterExpression": {{boolean}}
}
```

## Request Parameters
<a name="API_budgets_DescribeBudgets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_budgets_DescribeBudgets_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgets-request-AccountId"></a>
The `accountId` that is associated with the budgets that you want to describe.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** [MaxResults](#API_budgets_DescribeBudgets_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgets-request-MaxResults"></a>
An integer that represents how many budgets a paginated response contains. The default is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_budgets_DescribeBudgets_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgets-request-NextToken"></a>
The pagination token that you include in your request to indicate the next set of results that you want to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2147483647.
Pattern: `.*`
Required: No

 ** [ShowFilterExpression](#API_budgets_DescribeBudgets_RequestSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgets-request-ShowFilterExpression"></a>
Specifies whether the response includes the filter expression associated with the budgets. By showing the filter expression, you can see detailed filtering logic applied to the budgets, such as AWS services or tags that are being tracked.
Type: Boolean
Required: No

## Response Syntax
<a name="API_budgets_DescribeBudgets_ResponseSyntax"></a>

```
{
   "Budgets": [
      {
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
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_budgets_DescribeBudgets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Budgets](#API_budgets_DescribeBudgets_ResponseSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgets-response-Budgets"></a>
A list of budgets.
Type: Array of [Budget](API_budgets_Budget.md) objects

 ** [NextToken](#API_budgets_DescribeBudgets_ResponseSyntax) **   <a name="awscostmanagement-budgets_DescribeBudgets-response-NextToken"></a>
The pagination token in the service response that indicates the next set of results that you can retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2147483647.
Pattern: `.*`

## Errors
<a name="API_budgets_DescribeBudgets_Errors"></a>

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

## Examples
<a name="API_budgets_DescribeBudgets_Examples"></a>

### Example
<a name="API_budgets_DescribeBudgets_Example_1"></a>

The following is the `PlannedBudgetLimits` syntax.

```
{
   "Budgets": [
      {
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
   ],
   "NextToken": "string"
}
```

### Example
<a name="API_budgets_DescribeBudgets_Example_2"></a>

This example illustrates one usage of DescribeBudgets.

#### Sample Request
<a name="API_budgets_DescribeBudgets_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: awsbudgets.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSBudgetServiceGateway.DescribeBudgets

{
   "AccountId": "111122223333",
   "MaxResults": 20
}
```

#### Sample Response
<a name="API_budgets_DescribeBudgets_Example_2_Response"></a>

```
{
   "Budgets": [
      {
         "BudgetLimit": {
            "Amount": "100",
            "Unit": "USD"
         },
         "BudgetName": "Example Limit Fixed Budget",
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
      },
      {
         "BudgetLimit": {
            "Amount": "100",
            "Unit": "USD"
         },
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
         "BudgetName": "Example Planned Limits Budget",
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
   ],
   "NextToken": "exampleTokenString"
}
```

## See Also
<a name="API_budgets_DescribeBudgets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/budgets-2016-10-20/DescribeBudgets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/budgets-2016-10-20/DescribeBudgets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/DescribeBudgets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/budgets-2016-10-20/DescribeBudgets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/DescribeBudgets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/budgets-2016-10-20/DescribeBudgets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/budgets-2016-10-20/DescribeBudgets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/budgets-2016-10-20/DescribeBudgets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/budgets-2016-10-20/DescribeBudgets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/DescribeBudgets)
