---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlansCoverage.html
---

# GetSavingsPlansCoverage
<a name="API_GetSavingsPlansCoverage"></a>

Retrieves the Savings Plans covered for your account. This enables you to see how much of your cost is covered by a Savings Plan. An organization’s management account can see the coverage of the associated member accounts. This supports dimensions, cost categories, and nested expressions. For any time period, you can filter data for Savings Plans usage with the following dimensions:
+  `LINKED_ACCOUNT`
+  `REGION`
+  `SERVICE`
+  `INSTANCE_FAMILY`

To determine valid values for a dimension, use the `GetDimensionValues` operation.

## Request Syntax
<a name="API_GetSavingsPlansCoverage_RequestSyntax"></a>

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
      "Tags": {
         "Key": "{{string}}",
         "MatchOptions": [ "{{string}}" ],
         "Values": [ "{{string}}" ]
      }
   },
   "Granularity": "{{string}}",
   "GroupBy": [
      {
         "Key": "{{string}}",
         "Type": "{{string}}"
      }
   ],
   "MaxResults": {{number}},
   "Metrics": [ "{{string}}" ],
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
<a name="API_GetSavingsPlansCoverage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filter](#API_GetSavingsPlansCoverage_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansCoverage-request-Filter"></a>
Filters Savings Plans coverage data by dimensions. You can filter data for Savings Plans usage with the following dimensions:
+  `LINKED_ACCOUNT`
+  `REGION`
+  `SERVICE`
+  `INSTANCE_FAMILY`
 `GetSavingsPlansCoverage` uses the same [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html) object as the other operations, but only `AND` is supported among each dimension. If there are multiple values for a dimension, they are OR'd together.
Cost category is also supported.
Type: [Expression](API_Expression.md) object
Required: No

 ** [Granularity](#API_GetSavingsPlansCoverage_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansCoverage-request-Granularity"></a>
The granularity of the Amazon Web Services cost data for your Savings Plans. `Granularity` can't be set if `GroupBy` is set.
The `GetSavingsPlansCoverage` operation supports only `DAILY` and `MONTHLY` granularities.
Type: String
Valid Values: `DAILY | MONTHLY | HOURLY`
Required: No

 ** [GroupBy](#API_GetSavingsPlansCoverage_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansCoverage-request-GroupBy"></a>
You can group the data using the attributes `INSTANCE_FAMILY`, `REGION`, or `SERVICE`.
Type: Array of [GroupDefinition](API_GroupDefinition.md) objects
Required: No

 ** [MaxResults](#API_GetSavingsPlansCoverage_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansCoverage-request-MaxResults"></a>
The number of items to be returned in a response. The default is `20`, with a minimum value of `1`.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [Metrics](#API_GetSavingsPlansCoverage_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansCoverage-request-Metrics"></a>
The measurement that you want your Savings Plans coverage reported in. The only valid value is `SpendCoveredBySavingsPlans`.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** [NextToken](#API_GetSavingsPlansCoverage_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansCoverage-request-NextToken"></a>
The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

 ** [SortBy](#API_GetSavingsPlansCoverage_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansCoverage-request-SortBy"></a>
The value that you want to sort the data by.
The following values are supported for `Key`:
+  `SpendCoveredBySavingsPlan`
+  `OnDemandCost`
+  `CoveragePercentage`
+  `TotalCost`
+  `InstanceFamily`
+  `Region`
+  `Service`
The supported values for `SortOrder` are `ASCENDING` and `DESCENDING`.
Type: [SortDefinition](API_SortDefinition.md) object
Required: No

 ** [TimePeriod](#API_GetSavingsPlansCoverage_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansCoverage-request-TimePeriod"></a>
The time period that you want the usage and costs for. The `Start` date must be within 13 months. The `End` date must be after the `Start` date, and before the current date. Future dates can't be used as an `End` date.
Type: [DateInterval](API_DateInterval.md) object
Required: Yes

## Response Syntax
<a name="API_GetSavingsPlansCoverage_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "SavingsPlansCoverages": [
      {
         "Attributes": {
            "string" : "string"
         },
         "Coverage": {
            "CoveragePercentage": "string",
            "OnDemandCost": "string",
            "SpendCoveredBySavingsPlans": "string",
            "TotalCost": "string"
         },
         "TimePeriod": {
            "End": "string",
            "Start": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_GetSavingsPlansCoverage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetSavingsPlansCoverage_ResponseSyntax) **   <a name="awscostmanagement-GetSavingsPlansCoverage-response-NextToken"></a>
The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

 ** [SavingsPlansCoverages](#API_GetSavingsPlansCoverage_ResponseSyntax) **   <a name="awscostmanagement-GetSavingsPlansCoverage-response-SavingsPlansCoverages"></a>
The amount of spend that your Savings Plans covered.
Type: Array of [SavingsPlansCoverage](API_SavingsPlansCoverage.md) objects

## Errors
<a name="API_GetSavingsPlansCoverage_Errors"></a>

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
<a name="API_GetSavingsPlansCoverage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/GetSavingsPlansCoverage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/GetSavingsPlansCoverage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/GetSavingsPlansCoverage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/GetSavingsPlansCoverage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/GetSavingsPlansCoverage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/GetSavingsPlansCoverage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/GetSavingsPlansCoverage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/GetSavingsPlansCoverage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/GetSavingsPlansCoverage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/GetSavingsPlansCoverage)
