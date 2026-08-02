---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_UpdateBudget.html
---

# UpdateBudget
<a name="API_budgets_UpdateBudget"></a>

Updates a budget. You can change every part of a budget except for the `budgetName` and the `calculatedSpend`. When you modify a budget, the `calculatedSpend` drops to zero until AWS has new usage data to use for forecasting.

**Important**
Only one of `BudgetLimit` or `PlannedBudgetLimits` can be present in the syntax at one time. Use the syntax that matches your case. The Request Syntax section shows the `BudgetLimit` syntax. For `PlannedBudgetLimits`, see the [Examples](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_UpdateBudget.html#API_UpdateBudget_Examples) section.
Similarly, only one set of filter and metric selections can be present in the syntax at one time. Either `FilterExpression` and `Metrics` or `CostFilters` and `CostTypes`, not both or a different combination. We recommend using `FilterExpression` and `Metrics` as they provide more flexible and powerful filtering capabilities. The Request Syntax section shows the `FilterExpression`/`Metrics` syntax.

## Request Syntax
<a name="API_budgets_UpdateBudget_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}",
   "NewBudget": {
      "AutoAdjustData": {
         "AutoAdjustType": "{{string}}",
         "HistoricalOptions": {
            "BudgetAdjustmentPeriod": {{number}},
            "LookBackAvailablePeriods": {{number}}
         },
         "LastAutoAdjustTime": {{number}}
      },
      "BillingViewArn": "{{string}}",
      "BudgetLimit": {
         "Amount": "{{string}}",
         "Unit": "{{string}}"
      },
      "BudgetName": "{{string}}",
      "BudgetType": "{{string}}",
      "CalculatedSpend": {
         "ActualSpend": {
            "Amount": "{{string}}",
            "Unit": "{{string}}"
         },
         "ForecastedSpend": {
            "Amount": "{{string}}",
            "Unit": "{{string}}"
         }
      },
      "CostFilters": {
         "{{string}}" : [ "{{string}}" ]
      },
      "CostTypes": {
         "IncludeCredit": {{boolean}},
         "IncludeDiscount": {{boolean}},
         "IncludeOtherSubscription": {{boolean}},
         "IncludeRecurring": {{boolean}},
         "IncludeRefund": {{boolean}},
         "IncludeSubscription": {{boolean}},
         "IncludeSupport": {{boolean}},
         "IncludeTax": {{boolean}},
         "IncludeUpfront": {{boolean}},
         "UseAmortized": {{boolean}},
         "UseBlended": {{boolean}}
      },
      "FilterExpression": {
         "And": [
            "Expression"
         ],
         "CostCategories": {
            "Key": "{{string}}",
            "MatchOptions": [ "{{string}}" ],
            "Values": [ "{{string}}" ]
         },
         "Dimensions": {
            "Key": "{{string}}",
            "MatchOptions": [ "{{string}}" ],
            "Values": [ "{{string}}" ]
         },
         "Not": "Expression",
         "Or": [
            "Expression"
         ],
         "Tags": {
            "Key": "{{string}}",
            "MatchOptions": [ "{{string}}" ],
            "Values": [ "{{string}}" ]
         }
      },
      "HealthStatus": {
         "LastUpdatedTime": {{number}},
         "Status": "{{string}}",
         "StatusReason": "{{string}}"
      },
      "LastUpdatedTime": {{number}},
      "Metrics": [ "{{string}}" ],
      "PlannedBudgetLimits": {
         "{{string}}" : {
            "Amount": "{{string}}",
            "Unit": "{{string}}"
         }
      },
      "TimePeriod": {
         "End": {{number}},
         "Start": {{number}}
      },
      "TimeUnit": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_budgets_UpdateBudget_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_budgets_UpdateBudget_RequestSyntax) **   <a name="awscostmanagement-budgets_UpdateBudget-request-AccountId"></a>
The `accountId` that is associated with the budget that you want to update.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** [NewBudget](#API_budgets_UpdateBudget_RequestSyntax) **   <a name="awscostmanagement-budgets_UpdateBudget-request-NewBudget"></a>
The budget that you want to update your budget to.
Type: [Budget](API_budgets_Budget.md) object
Required: Yes

## Response Elements
<a name="API_budgets_UpdateBudget_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_budgets_UpdateBudget_Errors"></a>

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

## Examples
<a name="API_budgets_UpdateBudget_Examples"></a>

### Example
<a name="API_budgets_UpdateBudget_Example_1"></a>

The following is the `PlannedBudgetLimits` syntax.

```
{
   "AccountId": "string",
   "NewBudget": {
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
<a name="API_budgets_UpdateBudget_Example_2"></a>

The following is a sample request of the `UpdateBudget` operation using `BudgetLimit`.

#### Sample Request
<a name="API_budgets_UpdateBudget_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: awsbudgets.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSBudgetServiceGateway.UpdateBudget

{
   "AccountId": "111122223333",
   "NewBudget": {
      "BudgetLimit": {
         "Amount": "100",
         "Unit": "USD"
      },
      "BudgetName": "Example Budget",
      "BudgetType": "COST",
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
      "TimeUnit": "MONTHLY",
      "NotificationsWithSubscribers": [
         {
            "Notification": {
               "ComparisonOperator": "GREATER_THAN",
               "NotificationType": "ACTUAL",
               "Threshold": 80,
               "ThresholdType": "PERCENTAGE"
            },
            "Subscribers": [
               {
                  "Address": "budget-alerts@example.com",
                  "SubscriptionType": "EMAIL"
               }
            ]
         },
         {
            "Notification": {
               "ComparisonOperator": "GREATER_THAN",
               "NotificationType": "FORECASTED",
               "Threshold": 90,
               "ThresholdType": "PERCENTAGE"
            },
            "Subscribers": [
               {
                  "Address": "budget-forecasts@example.com",
                  "SubscriptionType": "EMAIL"
               }
            ]
         }
      ]
   }
}
```

### Example
<a name="API_budgets_UpdateBudget_Example_3"></a>

The following is an example of transitioning from `CostFilters`/`CostTypes` to `FilterExpression`/`Metrics`.

```
POST / HTTP/1.1
Host: awsbudgets.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSBudgetServiceGateway.UpdateBudget

{
   "AccountId": "111122223333",
   "NewBudget": {
      "BudgetLimit": {
         "Amount": "100",
         "Unit": "USD"
      },
      "BudgetName": "Example Budget",
      "BudgetType": "COST",
      // Replacing these fields:
      /*
      "CostFilters": {
         "Service": ["Amazon Simple Storage Service"],
         "Region": ["us-east-1"]
      },
      "CostTypes": {
         "IncludeCredit": true,
         "IncludeDiscount": true,
         "UseBlended": false
      },
      */
      // With these new fields:
      "FilterExpression": {
         "Dimensions": {
            "Key": "SERVICE",
            "Values": ["Amazon Simple Storage Service"]
         },
         "And": [{
            "Dimensions": {
               "Key": "REGION",
               "Values": ["us-east-1"]
            }
         }]
      },
      "Metrics": ["UNBLENDED_COST"],
      "TimePeriod": {
         "Start": 1477353600,
         "End": 1477958399
      },
      "TimeUnit": "MONTHLY",
      "NotificationsWithSubscribers": [
         {
            "Notification": {
               "ComparisonOperator": "GREATER_THAN",
               "NotificationType": "ACTUAL",
               "Threshold": 85,
               "ThresholdType": "PERCENTAGE"
            },
            "Subscribers": [
               {
                  "Address": "migration-alerts@example.com",
                  "SubscriptionType": "EMAIL"
               }
            ]
         }
      ]
   }
}
```

### Example
<a name="API_budgets_UpdateBudget_Example_4"></a>

The following is an example of updating a budget to use exclusion capabilities.

```
POST / HTTP/1.1
Host: awsbudgets.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSBudgetServiceGateway.UpdateBudget

{
   "AccountId": "111122223333",
   "NewBudget": {
      "BudgetLimit": {
         "Amount": "1000",
         "Unit": "USD"
      },
      "BudgetName": "Example Budget",
      "BudgetType": "COST",
      "FilterExpression": {
         "Not": {
            "Dimensions": {
               "Key": "SERVICE",
               "Values": ["AWS Shield", "AWS Support (Enterprise)"]
            }
         }
      },
      "Metrics": ["NET_UNBLENDED_COST"],
      "TimePeriod": {
         "Start": 1477353600,
         "End": 1477958399
      },
      "TimeUnit": "MONTHLY",
      "NotificationsWithSubscribers": [
         {
            "Notification": {
               "ComparisonOperator": "GREATER_THAN",
               "NotificationType": "ACTUAL",
               "Threshold": 70,
               "ThresholdType": "PERCENTAGE"
            },
            "Subscribers": [
               {
                  "Address": "exclusion-alerts@example.com",
                  "SubscriptionType": "EMAIL"
               }
            ]
         },
         {
            "Notification": {
               "ComparisonOperator": "GREATER_THAN",
               "NotificationType": "FORECASTED",
               "Threshold": 100,
               "ThresholdType": "PERCENTAGE"
            },
            "Subscribers": [
               {
                  "Address": "exclusion-forecasts@example.com",
                  "SubscriptionType": "EMAIL"
               }
            ]
         }
      ]
   }
}
```

### Example
<a name="API_budgets_UpdateBudget_Example_5"></a>

The following is a sample request of the `UpdateBudget` operation using `PlannedBudgetLimits`.

#### Sample Request
<a name="API_budgets_UpdateBudget_Example_5_Request"></a>

```
POST / HTTP/1.1
Host: awsbudgets.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSBudgetServiceGateway.UpdateBudget

{
   "AccountId": "111122223333",
   "NewBudget": {
      "PlannedBudgetLimits":{
         "1712019600": {
            "Amount": "100",
            "Unit": "USD"
         },
         "1714611600": {
            "Amount": "200",
            "Unit": "USD"
         },
         "1717203600": {
            "Amount": "300",
            "Unit": "USD"
         }
      },
      "BudgetName": "Example Budget",
      "BudgetType": "COST",
      "FilterExpression": {
         "Dimensions": {
            "Key": "AZ",
            "Values": ["us-east-1"]
         },
         "And": [{
            "Dimensions": {
               "Key": "SERVICE",
               "Values": ["Amazon Simple Storage Service", "Amazon FSx"]
            }
         }]
      },
      "Metrics": ["NET_UNBLENDED_COST"],
      "TimePeriod": {
         "Start": 1712019600,
         "End": 1717203600
      },
      "TimeUnit": "MONTHLY",
      "NotificationsWithSubscribers": [
         {
            "Notification": {
               "ComparisonOperator": "GREATER_THAN",
               "NotificationType": "ACTUAL",
               "Threshold": 50,
               "ThresholdType": "PERCENTAGE"
            },
            "Subscribers": [
               {
                  "Address": "planned-budget-alerts-1@example.com",
                  "SubscriptionType": "EMAIL"
               }
            ]
         },
         {
            "Notification": {
               "ComparisonOperator": "GREATER_THAN",
               "NotificationType": "ACTUAL",
               "Threshold": 75,
               "ThresholdType": "PERCENTAGE"
            },
            "Subscribers": [
               {
                  "Address": "planned-budget-alerts-2@example.com",
                  "SubscriptionType": "EMAIL"
               }
            ]
         },
         {
            "Notification": {
               "ComparisonOperator": "GREATER_THAN",
               "NotificationType": "ACTUAL",
               "Threshold": 90,
               "ThresholdType": "PERCENTAGE"
            },
            "Subscribers": [
               {
                  "Address": "planned-budget-alerts-3@example.com",
                  "SubscriptionType": "EMAIL"
               }
            ]
         }
      ]
   }
}
```

## See Also
<a name="API_budgets_UpdateBudget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/budgets-2016-10-20/UpdateBudget)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/budgets-2016-10-20/UpdateBudget)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/UpdateBudget)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/budgets-2016-10-20/UpdateBudget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/UpdateBudget)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/budgets-2016-10-20/UpdateBudget)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/budgets-2016-10-20/UpdateBudget)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/budgets-2016-10-20/UpdateBudget)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/budgets-2016-10-20/UpdateBudget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/UpdateBudget)
