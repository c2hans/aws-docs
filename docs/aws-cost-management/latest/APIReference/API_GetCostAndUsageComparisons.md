---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostAndUsageComparisons.html
---

# GetCostAndUsageComparisons
<a name="API_GetCostAndUsageComparisons"></a>

Retrieves cost and usage comparisons for your account between two periods within the last 13 months. If you have enabled multi-year data at monthly granularity, you can go back up to 38 months.

## Request Syntax
<a name="API_GetCostAndUsageComparisons_RequestSyntax"></a>

```
{
   "BaselineTimePeriod": {
      "End": "{{string}}",
      "Start": "{{string}}"
   },
   "BillingViewArn": "{{string}}",
   "ComparisonTimePeriod": {
      "End": "{{string}}",
      "Start": "{{string}}"
   },
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
   "GroupBy": [
      {
         "Key": "{{string}}",
         "Type": "{{string}}"
      }
   ],
   "MaxResults": {{number}},
   "MetricForComparison": "{{string}}",
   "NextPageToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCostAndUsageComparisons_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BaselineTimePeriod](#API_GetCostAndUsageComparisons_RequestSyntax) **   <a name="awscostmanagement-GetCostAndUsageComparisons-request-BaselineTimePeriod"></a>
The reference time period for comparison. This time period serves as the baseline against which other cost and usage data will be compared. The interval must start and end on the first day of a month, with a duration of exactly one month.
Type: [DateInterval](API_DateInterval.md) object
Required: Yes

 ** [BillingViewArn](#API_GetCostAndUsageComparisons_RequestSyntax) **   <a name="awscostmanagement-GetCostAndUsageComparisons-request-BillingViewArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to AWS Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z-]*:(billing)::[0-9]{12}:billingview/[-a-zA-Z0-9/:_+=.-@]{1,43}$`
Required: No

 ** [ComparisonTimePeriod](#API_GetCostAndUsageComparisons_RequestSyntax) **   <a name="awscostmanagement-GetCostAndUsageComparisons-request-ComparisonTimePeriod"></a>
The comparison time period for analysis. This time period's cost and usage data will be compared against the baseline time period. The interval must start and end on the first day of a month, with a duration of exactly one month.
Type: [DateInterval](API_DateInterval.md) object
Required: Yes

 ** [Filter](#API_GetCostAndUsageComparisons_RequestSyntax) **   <a name="awscostmanagement-GetCostAndUsageComparisons-request-Filter"></a>
Use `Expression` to filter in various Cost Explorer APIs.
Not all `Expression` types are supported in each API. Refer to the documentation for each specific API to see what is supported.
There are two patterns:
+ Simple dimension values.
  + There are three types of simple dimension values: `CostCategories`, `Tags`, and `Dimensions`.
    + Specify the `CostCategories` field to define a filter that acts on Cost Categories.
    + Specify the `Tags` field to define a filter that acts on Cost Allocation Tags.
    + Specify the `Dimensions` field to define a filter that acts on the [https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DimensionValues.html](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DimensionValues.html).
  + For each filter type, you can set the dimension name and values for the filters that you plan to use.
    + For example, you can filter for `REGION==us-east-1 OR REGION==us-west-1`. For `GetRightsizingRecommendation`, the Region is a full name (for example, `REGION==US East (N. Virginia)`.
    + The corresponding `Expression` for this example is as follows: `{ "Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] } }`
    + As shown in the previous example, lists of dimension values are combined with `OR` when applying the filter.
  + You can also set different match options to further control how the filter behaves. Not all APIs support match options. Refer to the documentation for each specific API to see what is supported.
    + For example, you can filter for linked account names that start with "a".
    + The corresponding `Expression` for this example is as follows: `{ "Dimensions": { "Key": "LINKED_ACCOUNT_NAME", "MatchOptions": [ "STARTS_WITH" ], "Values": [ "a" ] } }`
+ Compound `Expression` types with logical operations.
  + You can use multiple `Expression` types and the logical operators `AND/OR/NOT` to create a list of one or more `Expression` objects. By doing this, you can filter by more advanced options.
  + For example, you can filter by `((REGION == us-east-1 OR REGION == us-west-1) OR (TAG.Type == Type1)) AND (USAGE_TYPE != DataTransfer)`.
  + The corresponding `Expression` for this example is as follows: `{ "And": [ {"Or": [ {"Dimensions": { "Key": "REGION", "Values": [ "us-east-1", "us-west-1" ] }}, {"Tags": { "Key": "TagName", "Values": ["Value1"] } } ]}, {"Not": {"Dimensions": { "Key": "USAGE_TYPE", "Values": ["DataTransfer"] }}} ] } `
**Note**
Because each `Expression` can have only one operator, the service returns an error if more than one is specified. The following example shows an `Expression` object that creates an error: ` { "And": [ ... ], "Dimensions": { "Key": "USAGE_TYPE", "Values": [ "DataTransfer" ] } } `
The following is an example of the corresponding error message: `"Expression has more than one roots. Only one root operator is allowed for each expression: And, Or, Not, Dimensions, Tags, CostCategories"`
For the `GetRightsizingRecommendation` action, a combination of OR and NOT isn't supported. OR isn't supported between different dimensions, or dimensions and tags. NOT operators aren't supported. Dimensions are also limited to `LINKED_ACCOUNT`, `REGION`, or `RIGHTSIZING_TYPE`.
For the `GetReservationPurchaseRecommendation` action, only NOT is supported. AND and OR aren't supported. Dimensions are limited to `LINKED_ACCOUNT`.
Type: [Expression](API_Expression.md) object
Required: No

 ** [GroupBy](#API_GetCostAndUsageComparisons_RequestSyntax) **   <a name="awscostmanagement-GetCostAndUsageComparisons-request-GroupBy"></a>
You can group results using the attributes `DIMENSION`, `TAG`, and `COST_CATEGORY`.
Type: Array of [GroupDefinition](API_GroupDefinition.md) objects
Required: No

 ** [MaxResults](#API_GetCostAndUsageComparisons_RequestSyntax) **   <a name="awscostmanagement-GetCostAndUsageComparisons-request-MaxResults"></a>
The maximum number of results that are returned for the request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2000.
Required: No

 ** [MetricForComparison](#API_GetCostAndUsageComparisons_RequestSyntax) **   <a name="awscostmanagement-GetCostAndUsageComparisons-request-MetricForComparison"></a>
The cost and usage metric to compare. Valid values are `AmortizedCost`, `BlendedCost`, `NetAmortizedCost`, `NetUnblendedCost`, `NormalizedUsageAmount`, `UnblendedCost`, and `UsageQuantity`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

 ** [NextPageToken](#API_GetCostAndUsageComparisons_RequestSyntax) **   <a name="awscostmanagement-GetCostAndUsageComparisons-request-NextPageToken"></a>
The token to retrieve the next set of paginated results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

## Response Syntax
<a name="API_GetCostAndUsageComparisons_ResponseSyntax"></a>

```
{
   "CostAndUsageComparisons": [
      {
         "CostAndUsageSelector": {
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
         "Metrics": {
            "string" : {
               "BaselineTimePeriodAmount": "string",
               "ComparisonTimePeriodAmount": "string",
               "Difference": "string",
               "Unit": "string"
            }
         }
      }
   ],
   "NextPageToken": "string",
   "TotalCostAndUsage": {
      "string" : {
         "BaselineTimePeriodAmount": "string",
         "ComparisonTimePeriodAmount": "string",
         "Difference": "string",
         "Unit": "string"
      }
   }
}
```

## Response Elements
<a name="API_GetCostAndUsageComparisons_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CostAndUsageComparisons](#API_GetCostAndUsageComparisons_ResponseSyntax) **   <a name="awscostmanagement-GetCostAndUsageComparisons-response-CostAndUsageComparisons"></a>
An array of comparison results showing cost and usage metrics between `BaselineTimePeriod` and `ComparisonTimePeriod`.
Type: Array of [CostAndUsageComparison](API_CostAndUsageComparison.md) objects

 ** [NextPageToken](#API_GetCostAndUsageComparisons_ResponseSyntax) **   <a name="awscostmanagement-GetCostAndUsageComparisons-response-NextPageToken"></a>
The token to retrieve the next set of paginated results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

 ** [TotalCostAndUsage](#API_GetCostAndUsageComparisons_ResponseSyntax) **   <a name="awscostmanagement-GetCostAndUsageComparisons-response-TotalCostAndUsage"></a>
A summary of the total cost and usage, comparing amounts between `BaselineTimePeriod` and `ComparisonTimePeriod` and their differences. This total represents the aggregate total across all paginated results, if the response spans multiple pages.
Type: String to [ComparisonMetricValue](API_ComparisonMetricValue.md) object map
Key Length Constraints: Minimum length of 0. Maximum length of 1024.
Key Pattern: `[\S\s]*`

## Errors
<a name="API_GetCostAndUsageComparisons_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BillingViewHealthStatusException **
 The billing view status must be `HEALTHY` to perform this action. Try again when the status is `HEALTHY`.
HTTP Status Code: 400

 ** DataUnavailableException **
The requested data is unavailable.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The pagination token is invalid. Try again without a pagination token.
HTTP Status Code: 400

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

 ** ResourceNotFoundException **
 The specified ARN in the request doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_GetCostAndUsageComparisons_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/GetCostAndUsageComparisons)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/GetCostAndUsageComparisons)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/GetCostAndUsageComparisons)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/GetCostAndUsageComparisons)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/GetCostAndUsageComparisons)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/GetCostAndUsageComparisons)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/GetCostAndUsageComparisons)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/GetCostAndUsageComparisons)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/GetCostAndUsageComparisons)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/GetCostAndUsageComparisons)
