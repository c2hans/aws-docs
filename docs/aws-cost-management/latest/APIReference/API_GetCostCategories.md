---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostCategories.html
---

# GetCostCategories
<a name="API_GetCostCategories"></a>

Retrieves an array of cost category names and values incurred cost.

**Note**
If some cost category names and values are not associated with any cost, they will not be returned by this API.

## Request Syntax
<a name="API_GetCostCategories_RequestSyntax"></a>

```
{
   "BillingViewArn": "{{string}}",
   "CostCategoryName": "{{string}}",
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
   "NextPageToken": "{{string}}",
   "SearchString": "{{string}}",
   "SortBy": [
      {
         "Key": "{{string}}",
         "SortOrder": "{{string}}"
      }
   ],
   "TimePeriod": {
      "End": "{{string}}",
      "Start": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_GetCostCategories_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BillingViewArn](#API_GetCostCategories_RequestSyntax) **   <a name="awscostmanagement-GetCostCategories-request-BillingViewArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to AWS Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z-]*:(billing)::[0-9]{12}:billingview/[-a-zA-Z0-9/:_+=.-@]{1,43}$`
Required: No

 ** [CostCategoryName](#API_GetCostCategories_RequestSyntax) **   <a name="awscostmanagement-GetCostCategories-request-CostCategoryName"></a>
The unique name of the cost category.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )$`
Required: No

 ** [Filter](#API_GetCostCategories_RequestSyntax) **   <a name="awscostmanagement-GetCostCategories-request-Filter"></a>
Use `Expression` to filter in various Cost Explorer APIs.
Not all `Expression` types are supported in each API. Refer to the documentation for each specific API to see what is supported.
There are two patterns:
+ Simple dimension values.
  + There are four types of simple dimension values: `CostCategories`, `Tags`, `Dimensions`, and `ProductAttributes`.
    + Specify the `CostCategories` field to define a filter that acts on Cost Categories.
    + Specify the `Tags` field to define a filter that acts on Cost Allocation Tags.
    + Specify the `Dimensions` field to define a filter that acts on the [`DimensionValues`](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DimensionValues.html).
    + Specify the `ProductAttributes` field to define a filter that acts on the product attributes of supported services, such as Amazon Bedrock. Only `GetCostAndUsage`, `GetCostAndUsageWithResources`, `GetDimensionValues` (in the `COST_AND_USAGE` context), `GetTags`, and `GetCostCategories` support `ProductAttributes`. For the supported services, keys and `SERVICE` filter rules, see [`ProductAttributeValues`](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ProductAttributeValues.html).
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

 ** [MaxResults](#API_GetCostCategories_RequestSyntax) **   <a name="awscostmanagement-GetCostCategories-request-MaxResults"></a>
This field is only used when the `SortBy` value is provided in the request.
The maximum number of objects that are returned for this request. If `MaxResults` isn't specified with the `SortBy` value, the request returns 1000 results as the default value for this parameter.
For `GetCostCategories`, MaxResults has an upper quota of 1000.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextPageToken](#API_GetCostCategories_RequestSyntax) **   <a name="awscostmanagement-GetCostCategories-request-NextPageToken"></a>
If the number of objects that are still available for retrieval exceeds the quota, AWS returns a NextPageToken value in the response. To retrieve the next batch of objects, provide the NextPageToken from the previous call in your next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

 ** [SearchString](#API_GetCostCategories_RequestSyntax) **   <a name="awscostmanagement-GetCostCategories-request-SearchString"></a>
The value that you want to search the filter values for.
If you don't specify a `CostCategoryName`, `SearchString` is used to filter cost category names that match the `SearchString` pattern. If you specify a `CostCategoryName`, `SearchString` is used to filter cost category values that match the `SearchString` pattern.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** [SortBy](#API_GetCostCategories_RequestSyntax) **   <a name="awscostmanagement-GetCostCategories-request-SortBy"></a>
The value that you sort the data by.
The key represents the cost and usage metrics. The following values are supported:
+  `BlendedCost`
+  `UnblendedCost`
+  `AmortizedCost`
+  `NetAmortizedCost`
+  `NetUnblendedCost`
+  `UsageQuantity`
+  `NormalizedUsageAmount`
The supported key values for the `SortOrder` value are `ASCENDING` and `DESCENDING`.
When you use the `SortBy` value, the `NextPageToken` and `SearchString` key values aren't supported.
Type: Array of [SortDefinition](API_SortDefinition.md) objects
Required: No

 ** [TimePeriod](#API_GetCostCategories_RequestSyntax) **   <a name="awscostmanagement-GetCostCategories-request-TimePeriod"></a>
The time period of the request.
Type: [DateInterval](API_DateInterval.md) object
Required: Yes

## Response Syntax
<a name="API_GetCostCategories_ResponseSyntax"></a>

```
{
   "CostCategoryNames": [ "string" ],
   "CostCategoryValues": [ "string" ],
   "NextPageToken": "string",
   "ReturnSize": number,
   "TotalSize": number
}
```

## Response Elements
<a name="API_GetCostCategories_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CostCategoryNames](#API_GetCostCategories_ResponseSyntax) **   <a name="awscostmanagement-GetCostCategories-response-CostCategoryNames"></a>
The names of the cost categories.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )$`

 ** [CostCategoryValues](#API_GetCostCategories_ResponseSyntax) **   <a name="awscostmanagement-GetCostCategories-response-CostCategoryValues"></a>
The cost category values.
If the `CostCategoryName` key isn't specified in the request, the `CostCategoryValues` fields aren't returned.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )$`

 ** [NextPageToken](#API_GetCostCategories_ResponseSyntax) **   <a name="awscostmanagement-GetCostCategories-response-NextPageToken"></a>
If the number of objects that are still available for retrieval exceeds the quota, AWS returns a NextPageToken value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

 ** [ReturnSize](#API_GetCostCategories_ResponseSyntax) **   <a name="awscostmanagement-GetCostCategories-response-ReturnSize"></a>
The number of objects that are returned.
Type: Integer

 ** [TotalSize](#API_GetCostCategories_ResponseSyntax) **   <a name="awscostmanagement-GetCostCategories-response-TotalSize"></a>
The total number of objects.
Type: Integer

## Errors
<a name="API_GetCostCategories_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BillExpirationException **
The requested report expired. Update the date interval and try again.
HTTP Status Code: 400

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

 ** RequestChangedException **
Your request parameters changed between pages. Try again with the old parameters or without a pagination token.
HTTP Status Code: 400

 ** ResourceNotFoundException **
 The specified ARN in the request doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_GetCostCategories_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/GetCostCategories)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/GetCostCategories)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/GetCostCategories)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/GetCostCategories)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/GetCostCategories)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/GetCostCategories)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/GetCostCategories)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/GetCostCategories)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/GetCostCategories)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/GetCostCategories)
