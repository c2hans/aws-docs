---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetReservationPurchaseRecommendation.html
---

# GetReservationPurchaseRecommendation
<a name="API_GetReservationPurchaseRecommendation"></a>

Gets recommendations for reservation purchases. These recommendations might help you to reduce your costs. Reservations provide a discounted hourly rate (up to 75%) compared to On-Demand pricing.

 AWS generates your recommendations by identifying your On-Demand usage during a specific time period and collecting your usage into categories that are eligible for a reservation. After AWS has these categories, it simulates every combination of reservations in each category of usage to identify the best number of each type of Reserved Instance (RI) to purchase to maximize your estimated savings.

For example, AWS automatically aggregates your Amazon EC2 Linux, shared tenancy, and c4 family usage in the US West (Oregon) Region and recommends that you buy size-flexible regional reservations to apply to the c4 family usage. AWS recommends the smallest size instance in an instance family. This makes it easier to purchase a size-flexible Reserved Instance (RI). AWS also shows the equal number of normalized units. This way, you can purchase any instance size that you want. For this example, your RI recommendation is for `c4.large` because that is the smallest size instance in the c4 instance family.

## Request Syntax
<a name="API_GetReservationPurchaseRecommendation_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}",
   "AccountScope": "{{string}}",
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
   "LookbackPeriodInDays": "{{string}}",
   "NextPageToken": "{{string}}",
   "PageSize": {{number}},
   "PaymentOption": "{{string}}",
   "Service": "{{string}}",
   "ServiceSpecification": {
      "EC2Specification": {
         "OfferingClass": "{{string}}"
      }
   },
   "TermInYears": "{{string}}"
}
```

## Request Parameters
<a name="API_GetReservationPurchaseRecommendation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_GetReservationPurchaseRecommendation_RequestSyntax) **   <a name="awscostmanagement-GetReservationPurchaseRecommendation-request-AccountId"></a>
The account ID that's associated with the recommendation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** [AccountScope](#API_GetReservationPurchaseRecommendation_RequestSyntax) **   <a name="awscostmanagement-GetReservationPurchaseRecommendation-request-AccountScope"></a>
The account scope that you want your recommendations for. Amazon Web Services calculates recommendations including the management account and member accounts if the value is set to `PAYER`. If the value is `LINKED`, recommendations are calculated for individual member accounts only.
Type: String
Valid Values: `PAYER | LINKED`
Required: No

 ** [Filter](#API_GetReservationPurchaseRecommendation_RequestSyntax) **   <a name="awscostmanagement-GetReservationPurchaseRecommendation-request-Filter"></a>
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

 ** [LookbackPeriodInDays](#API_GetReservationPurchaseRecommendation_RequestSyntax) **   <a name="awscostmanagement-GetReservationPurchaseRecommendation-request-LookbackPeriodInDays"></a>
The number of previous days that you want AWS to consider when it calculates your recommendations.
Type: String
Valid Values: `SEVEN_DAYS | THIRTY_DAYS | SIXTY_DAYS`
Required: No

 ** [NextPageToken](#API_GetReservationPurchaseRecommendation_RequestSyntax) **   <a name="awscostmanagement-GetReservationPurchaseRecommendation-request-NextPageToken"></a>
The pagination token that indicates the next set of results that you want to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

 ** [PageSize](#API_GetReservationPurchaseRecommendation_RequestSyntax) **   <a name="awscostmanagement-GetReservationPurchaseRecommendation-request-PageSize"></a>
The number of recommendations that you want returned in a single response object.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 6000.
Required: No

 ** [PaymentOption](#API_GetReservationPurchaseRecommendation_RequestSyntax) **   <a name="awscostmanagement-GetReservationPurchaseRecommendation-request-PaymentOption"></a>
The reservation purchase option that you want recommendations for.
Type: String
Valid Values: `NO_UPFRONT | PARTIAL_UPFRONT | ALL_UPFRONT | LIGHT_UTILIZATION | MEDIUM_UTILIZATION | HEAVY_UTILIZATION`
Required: No

 ** [Service](#API_GetReservationPurchaseRecommendation_RequestSyntax) **   <a name="awscostmanagement-GetReservationPurchaseRecommendation-request-Service"></a>
The specific service that you want recommendations for.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

 ** [ServiceSpecification](#API_GetReservationPurchaseRecommendation_RequestSyntax) **   <a name="awscostmanagement-GetReservationPurchaseRecommendation-request-ServiceSpecification"></a>
The hardware specifications for the service instances that you want recommendations for, such as standard or convertible Amazon EC2 instances.
Type: [ServiceSpecification](API_ServiceSpecification.md) object
Required: No

 ** [TermInYears](#API_GetReservationPurchaseRecommendation_RequestSyntax) **   <a name="awscostmanagement-GetReservationPurchaseRecommendation-request-TermInYears"></a>
The reservation term that you want recommendations for.
Type: String
Valid Values: `ONE_YEAR | THREE_YEARS`
Required: No

## Response Syntax
<a name="API_GetReservationPurchaseRecommendation_ResponseSyntax"></a>

```
{
   "Metadata": {
      "AdditionalMetadata": "string",
      "GenerationTimestamp": "string",
      "RecommendationId": "string"
   },
   "NextPageToken": "string",
   "Recommendations": [
      {
         "AccountScope": "string",
         "LookbackPeriodInDays": "string",
         "PaymentOption": "string",
         "RecommendationDetails": [
            {
               "AccountId": "string",
               "AverageNormalizedUnitsUsedPerHour": "string",
               "AverageNumberOfCapacityUnitsUsedPerHour": "string",
               "AverageNumberOfInstancesUsedPerHour": "string",
               "AverageUtilization": "string",
               "CurrencyCode": "string",
               "EstimatedBreakEvenInMonths": "string",
               "EstimatedMonthlyOnDemandCost": "string",
               "EstimatedMonthlySavingsAmount": "string",
               "EstimatedMonthlySavingsPercentage": "string",
               "EstimatedReservationCostForLookbackPeriod": "string",
               "InstanceDetails": {
                  "EC2InstanceDetails": {
                     "AvailabilityZone": "string",
                     "CurrentGeneration": boolean,
                     "Family": "string",
                     "InstanceType": "string",
                     "Platform": "string",
                     "Region": "string",
                     "SizeFlexEligible": boolean,
                     "Tenancy": "string"
                  },
                  "ElastiCacheInstanceDetails": {
                     "CurrentGeneration": boolean,
                     "Family": "string",
                     "NodeType": "string",
                     "ProductDescription": "string",
                     "Region": "string",
                     "SizeFlexEligible": boolean
                  },
                  "ESInstanceDetails": {
                     "CurrentGeneration": boolean,
                     "InstanceClass": "string",
                     "InstanceSize": "string",
                     "Region": "string",
                     "SizeFlexEligible": boolean
                  },
                  "MemoryDBInstanceDetails": {
                     "CurrentGeneration": boolean,
                     "Family": "string",
                     "NodeType": "string",
                     "Region": "string",
                     "SizeFlexEligible": boolean
                  },
                  "RDSInstanceDetails": {
                     "CurrentGeneration": boolean,
                     "DatabaseEdition": "string",
                     "DatabaseEngine": "string",
                     "DeploymentModel": "string",
                     "DeploymentOption": "string",
                     "Family": "string",
                     "InstanceType": "string",
                     "LicenseModel": "string",
                     "Region": "string",
                     "SizeFlexEligible": boolean
                  },
                  "RedshiftInstanceDetails": {
                     "CurrentGeneration": boolean,
                     "Family": "string",
                     "NodeType": "string",
                     "Region": "string",
                     "SizeFlexEligible": boolean
                  }
               },
               "MaximumNormalizedUnitsUsedPerHour": "string",
               "MaximumNumberOfCapacityUnitsUsedPerHour": "string",
               "MaximumNumberOfInstancesUsedPerHour": "string",
               "MinimumNormalizedUnitsUsedPerHour": "string",
               "MinimumNumberOfCapacityUnitsUsedPerHour": "string",
               "MinimumNumberOfInstancesUsedPerHour": "string",
               "RecommendedNormalizedUnitsToPurchase": "string",
               "RecommendedNumberOfCapacityUnitsToPurchase": "string",
               "RecommendedNumberOfInstancesToPurchase": "string",
               "RecurringStandardMonthlyCost": "string",
               "ReservedCapacityDetails": {
                  "DynamoDBCapacityDetails": {
                     "CapacityUnits": "string",
                     "Region": "string"
                  }
               },
               "UpfrontCost": "string"
            }
         ],
         "RecommendationSummary": {
            "CurrencyCode": "string",
            "TotalEstimatedMonthlySavingsAmount": "string",
            "TotalEstimatedMonthlySavingsPercentage": "string"
         },
         "ServiceSpecification": {
            "EC2Specification": {
               "OfferingClass": "string"
            }
         },
         "TermInYears": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetReservationPurchaseRecommendation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Metadata](#API_GetReservationPurchaseRecommendation_ResponseSyntax) **   <a name="awscostmanagement-GetReservationPurchaseRecommendation-response-Metadata"></a>
Information about this specific recommendation call, such as the time stamp for when Cost Explorer generated this recommendation.
Type: [ReservationPurchaseRecommendationMetadata](API_ReservationPurchaseRecommendationMetadata.md) object

 ** [NextPageToken](#API_GetReservationPurchaseRecommendation_ResponseSyntax) **   <a name="awscostmanagement-GetReservationPurchaseRecommendation-response-NextPageToken"></a>
The pagination token for the next set of retrievable results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

 ** [Recommendations](#API_GetReservationPurchaseRecommendation_ResponseSyntax) **   <a name="awscostmanagement-GetReservationPurchaseRecommendation-response-Recommendations"></a>
Recommendations for reservations to purchase.
Type: Array of [ReservationPurchaseRecommendation](API_ReservationPurchaseRecommendation.md) objects

## Errors
<a name="API_GetReservationPurchaseRecommendation_Errors"></a>

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
<a name="API_GetReservationPurchaseRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/GetReservationPurchaseRecommendation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/GetReservationPurchaseRecommendation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/GetReservationPurchaseRecommendation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/GetReservationPurchaseRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/GetReservationPurchaseRecommendation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/GetReservationPurchaseRecommendation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/GetReservationPurchaseRecommendation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/GetReservationPurchaseRecommendation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/GetReservationPurchaseRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/GetReservationPurchaseRecommendation)
