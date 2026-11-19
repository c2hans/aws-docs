---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlansUtilization.html
---

# GetSavingsPlansUtilization

Retrieves the Savings Plans utilization for your account across date ranges with daily or monthly granularity. Management account in an organization have access to member accounts. You can use `GetDimensionValues` in `SAVINGS_PLANS` to determine the possible dimension values.

**Note**
You can't group by any dimension values for `GetSavingsPlansUtilization`.

## Request Syntax
<a name="API_GetSavingsPlansUtilization_RequestSyntax"></a>

```
{
   "Filter": {
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
      "ProductAttributes": {
         "Key": "{{string}}",
         "MatchOptions": [ "{{string}}" ],
         "Values": [ "{{string}}" ]
      },
      "Tags": {
         "Key": "{{string}}",
         "MatchOptions": [ "{{string}}" ],
         "Values": [ "{{string}}" ]
      }
   },
   "Granularity": "{{string}}",
   "SortBy": {
      "Key": "{{string}}",
      "SortOrder": "{{string}}"
   },
   "TimePeriod": {
      "End": "{{string}}",
      "Start": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_GetSavingsPlansUtilization_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filter](#API_GetSavingsPlansUtilization_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansUtilization-request-Filter"></a>
Filters Savings Plans utilization coverage data for active Savings Plans dimensions. You can filter data with the following dimensions:
+  `LINKED_ACCOUNT`
+  `SAVINGS_PLAN_ARN`
+  `SAVINGS_PLANS_TYPE`
+  `REGION`
+  `PAYMENT_OPTION`
+  `INSTANCE_TYPE_FAMILY`
 `GetSavingsPlansUtilization` uses the same [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html) object as the other operations. The filter must have one of the following shapes:
+ A `Dimensions` expression.
+ A `Not` expression that contains one `Dimensions` expression.
+ An `And` expression with two or more operands, where each operand has one of the two shapes above.
 `Or`, `Tags`, and `CostCategories` expressions aren't supported. An `And` expression can't contain another `And`, and a `Not` expression can't contain an `And` or another `Not`.
Each dimension can appear only once in the filter, including inside `Not`. To filter on several values of a dimension, put all of the values in one expression. Cost Explorer combines the values in one expression with OR.
Type: [Expression](API_Expression.md) object
Required: No

 ** [Granularity](#API_GetSavingsPlansUtilization_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansUtilization-request-Granularity"></a>
The granularity of the Amazon Web Services utilization data for your Savings Plans.
The `GetSavingsPlansUtilization` operation supports only `DAILY` and `MONTHLY` granularities.
With `MONTHLY`, each result's `TimePeriod` shows a full calendar month, but its amounts include only the days inside the requested `TimePeriod`. If `TimePeriod` doesn't start on the first day of a month, the first result covers only part of that month. The same applies to the last result if `TimePeriod` doesn't end on the first day of a month. For the current month, the result's `End` is the first day without complete data.
Type: String
Valid Values: `DAILY | MONTHLY | HOURLY`
Required: No

 ** [SortBy](#API_GetSavingsPlansUtilization_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansUtilization-request-SortBy"></a>
The value that you want to sort the data by.
The following values are supported for `Key`:
+  `UtilizationPercentage`
+  `TotalCommitment`
+  `UsedCommitment`
+  `UnusedCommitment`
+  `NetSavings`
The supported values for `SortOrder` are `ASCENDING` and `DESCENDING`.
Type: [SortDefinition](API_SortDefinition.md) object
Required: No

 ** [TimePeriod](#API_GetSavingsPlansUtilization_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansUtilization-request-TimePeriod"></a>
The time period that you want the usage and costs for. The `Start` date must be within 13 months. The `End` date must be after the `Start` date, and before the current date. Future dates can't be used as an `End` date.
Type: [DateInterval](API_DateInterval.md) object
Required: Yes

## Response Syntax
<a name="API_GetSavingsPlansUtilization_ResponseSyntax"></a>

```
{
   "SavingsPlansUtilizationsByTime": [
      {
         "AmortizedCommitment": {
            "AmortizedRecurringCommitment": "string",
            "AmortizedUpfrontCommitment": "string",
            "TotalAmortizedCommitment": "string"
         },
         "Savings": {
            "NetSavings": "string",
            "OnDemandCostEquivalent": "string"
         },
         "TimePeriod": {
            "End": "string",
            "Start": "string"
         },
         "Utilization": {
            "TotalCommitment": "string",
            "UnusedCommitment": "string",
            "UsedCommitment": "string",
            "UtilizationPercentage": "string"
         }
      }
   ],
   "Total": {
      "AmortizedCommitment": {
         "AmortizedRecurringCommitment": "string",
         "AmortizedUpfrontCommitment": "string",
         "TotalAmortizedCommitment": "string"
      },
      "Savings": {
         "NetSavings": "string",
         "OnDemandCostEquivalent": "string"
      },
      "Utilization": {
         "TotalCommitment": "string",
         "UnusedCommitment": "string",
         "UsedCommitment": "string",
         "UtilizationPercentage": "string"
      }
   }
}
```

## Response Elements
<a name="API_GetSavingsPlansUtilization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SavingsPlansUtilizationsByTime](#API_GetSavingsPlansUtilization_ResponseSyntax) **   <a name="awscostmanagement-GetSavingsPlansUtilization-response-SavingsPlansUtilizationsByTime"></a>
The amount of cost/commitment that you used your Savings Plans. You can use it to specify date ranges.
Type: Array of [SavingsPlansUtilizationByTime](API_SavingsPlansUtilizationByTime.md) objects

 ** [Total](#API_GetSavingsPlansUtilization_ResponseSyntax) **   <a name="awscostmanagement-GetSavingsPlansUtilization-response-Total"></a>
The total amount of cost/commitment that you used your Savings Plans, regardless of date ranges.
Type: [SavingsPlansUtilizationAggregates](API_SavingsPlansUtilizationAggregates.md) object

## Errors
<a name="API_GetSavingsPlansUtilization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DataUnavailableException **
The requested data is unavailable.
HTTP Status Code: 400

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

## See Also
<a name="API_GetSavingsPlansUtilization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/GetSavingsPlansUtilization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/GetSavingsPlansUtilization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/GetSavingsPlansUtilization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/GetSavingsPlansUtilization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/GetSavingsPlansUtilization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/GetSavingsPlansUtilization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/GetSavingsPlansUtilization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/GetSavingsPlansUtilization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/GetSavingsPlansUtilization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/GetSavingsPlansUtilization)
