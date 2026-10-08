---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlansUtilizationDetails.html
---

# GetSavingsPlansUtilizationDetails
<a name="API_GetSavingsPlansUtilizationDetails"></a>

Retrieves attribute data along with aggregate utilization and savings data for a given time period. This doesn't support granular or grouped data (daily/monthly) in response. You can't retrieve data by dates in a single response similar to `GetSavingsPlanUtilization`, but you have the option to make multiple calls to `GetSavingsPlanUtilizationDetails` by providing individual dates. You can use `GetDimensionValues` in `SAVINGS_PLANS` to determine the possible dimension values.

**Note**
 `GetSavingsPlanUtilizationDetails` internally groups data by `SavingsPlansArn`.

## Request Syntax
<a name="API_GetSavingsPlansUtilizationDetails_RequestSyntax"></a>

```
{
   "DataType": [ "{{string}}" ],
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
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
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
<a name="API_GetSavingsPlansUtilizationDetails_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DataType](#API_GetSavingsPlansUtilizationDetails_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansUtilizationDetails-request-DataType"></a>
The data type.
Type: Array of strings
Valid Values: `ATTRIBUTES | UTILIZATION | AMORTIZED_COMMITMENT | SAVINGS`
Required: No

 ** [Filter](#API_GetSavingsPlansUtilizationDetails_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansUtilizationDetails-request-Filter"></a>
Filters Savings Plans utilization coverage data for active Savings Plans dimensions. You can filter data with the following dimensions:
+  `LINKED_ACCOUNT`
+  `SAVINGS_PLAN_ARN`
+  `REGION`
+  `PAYMENT_OPTION`
+  `INSTANCE_TYPE_FAMILY`
 `GetSavingsPlansUtilizationDetails` uses the same [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html) object as the other operations, but only `AND` is supported among each dimension.
Type: [Expression](API_Expression.md) object
Required: No

 ** [MaxResults](#API_GetSavingsPlansUtilizationDetails_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansUtilizationDetails-request-MaxResults"></a>
The number of items to be returned in a response. The default is `20`, with a minimum value of `1`.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_GetSavingsPlansUtilizationDetails_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansUtilizationDetails-request-NextToken"></a>
The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

 ** [SortBy](#API_GetSavingsPlansUtilizationDetails_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansUtilizationDetails-request-SortBy"></a>
The value that you want to sort the data by.
The following values are supported for `Key`:
+  `UtilizationPercentage`
+  `TotalCommitment`
+  `UsedCommitment`
+  `UnusedCommitment`
+  `NetSavings`
+  `AmortizedRecurringCommitment`
+  `AmortizedUpfrontCommitment`
The supported values for `SortOrder` are `ASCENDING` and `DESCENDING`.
Type: [SortDefinition](API_SortDefinition.md) object
Required: No

 ** [TimePeriod](#API_GetSavingsPlansUtilizationDetails_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansUtilizationDetails-request-TimePeriod"></a>
The time period that you want the usage and costs for. The `Start` date must be within 13 months. The `End` date must be after the `Start` date, and before the current date. Future dates can't be used as an `End` date.
Type: [DateInterval](API_DateInterval.md) object
Required: Yes

## Response Syntax
<a name="API_GetSavingsPlansUtilizationDetails_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "SavingsPlansUtilizationDetails": [
      {
         "AmortizedCommitment": {
            "AmortizedRecurringCommitment": "string",
            "AmortizedUpfrontCommitment": "string",
            "TotalAmortizedCommitment": "string"
         },
         "Attributes": {
            "string" : "string"
         },
         "Savings": {
            "NetSavings": "string",
            "OnDemandCostEquivalent": "string"
         },
         "SavingsPlanArn": "string",
         "Utilization": {
            "TotalCommitment": "string",
            "UnusedCommitment": "string",
            "UsedCommitment": "string",
            "UtilizationPercentage": "string"
         }
      }
   ],
   "TimePeriod": {
      "End": "string",
      "Start": "string"
   },
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
<a name="API_GetSavingsPlansUtilizationDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetSavingsPlansUtilizationDetails_ResponseSyntax) **   <a name="awscostmanagement-GetSavingsPlansUtilizationDetails-response-NextToken"></a>
The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

 ** [SavingsPlansUtilizationDetails](#API_GetSavingsPlansUtilizationDetails_ResponseSyntax) **   <a name="awscostmanagement-GetSavingsPlansUtilizationDetails-response-SavingsPlansUtilizationDetails"></a>
Retrieves a single daily or monthly Savings Plans utilization rate and details for your account.
Type: Array of [SavingsPlansUtilizationDetail](API_SavingsPlansUtilizationDetail.md) objects

 ** [TimePeriod](#API_GetSavingsPlansUtilizationDetails_ResponseSyntax) **   <a name="awscostmanagement-GetSavingsPlansUtilizationDetails-response-TimePeriod"></a>
The time period of the request.
Type: [DateInterval](API_DateInterval.md) object

 ** [Total](#API_GetSavingsPlansUtilizationDetails_ResponseSyntax) **   <a name="awscostmanagement-GetSavingsPlansUtilizationDetails-response-Total"></a>
The total Savings Plans utilization, regardless of time period.
Type: [SavingsPlansUtilizationAggregates](API_SavingsPlansUtilizationAggregates.md) object

## Errors
<a name="API_GetSavingsPlansUtilizationDetails_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DataUnavailableException **
The requested data is unavailable.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The pagination token is invalid. Try again without a pagination token.
HTTP Status Code: 400

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

## See Also
<a name="API_GetSavingsPlansUtilizationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/GetSavingsPlansUtilizationDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/GetSavingsPlansUtilizationDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/GetSavingsPlansUtilizationDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/GetSavingsPlansUtilizationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/GetSavingsPlansUtilizationDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/GetSavingsPlansUtilizationDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/GetSavingsPlansUtilizationDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/GetSavingsPlansUtilizationDetails)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/GetSavingsPlansUtilizationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/GetSavingsPlansUtilizationDetails)
