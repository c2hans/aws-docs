---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetRightsizingRecommendation.html
---

# GetRightsizingRecommendation
<a name="API_GetRightsizingRecommendation"></a>

Creates recommendations that help you save cost by identifying idle and underutilized Amazon EC2 instances.

Recommendations are generated to either downsize or terminate instances, along with providing savings detail and metrics. For more information about calculation and function, see [Optimizing Your Cost with Rightsizing Recommendations](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-rightsizing.html) in the * AWS Billing and Cost Management User Guide*.

## Request Syntax
<a name="API_GetRightsizingRecommendation_RequestSyntax"></a>

```
{
   "Configuration": {
      "BenefitsConsidered": {{boolean}},
      "RecommendationTarget": "{{string}}"
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
   "NextPageToken": "{{string}}",
   "PageSize": {{number}},
   "Service": "{{string}}"
}
```

## Request Parameters
<a name="API_GetRightsizingRecommendation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Configuration](#API_GetRightsizingRecommendation_RequestSyntax) **   <a name="awscostmanagement-GetRightsizingRecommendation-request-Configuration"></a>
You can use Configuration to customize recommendations across two attributes. You can choose to view recommendations for instances within the same instance families or across different instance families. You can also choose to view your estimated savings that are associated with recommendations with consideration of existing Savings Plans or RI benefits, or neither.
Type: [RightsizingRecommendationConfiguration](API_RightsizingRecommendationConfiguration.md) object
Required: No

 ** [Filter](#API_GetRightsizingRecommendation_RequestSyntax) **   <a name="awscostmanagement-GetRightsizingRecommendation-request-Filter"></a>
Use `Expression` to filter in various Cost Explorer APIs.
Not all `Expression` types are supported in each API. Refer to the documentation for each specific API to see what is supported.
There are two patterns:
+ Simple dimension values.
  + There are three types of simple dimension values: `CostCategories`, `Tags`, and `Dimensions`.
    + Specify the `CostCategories` field to define a filter that acts on Cost Categories.
    + Specify the `Tags` field to define a filter that acts on Cost Allocation Tags.
    + Specify the `Dimensions` field to define a filter that acts on the [`DimensionValues`](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DimensionValues.html).
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

 ** [NextPageToken](#API_GetRightsizingRecommendation_RequestSyntax) **   <a name="awscostmanagement-GetRightsizingRecommendation-request-NextPageToken"></a>
The pagination token that indicates the next set of results that you want to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

 ** [PageSize](#API_GetRightsizingRecommendation_RequestSyntax) **   <a name="awscostmanagement-GetRightsizingRecommendation-request-PageSize"></a>
The number of recommendations that you want returned in a single response object.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 6000.
Required: No

 ** [Service](#API_GetRightsizingRecommendation_RequestSyntax) **   <a name="awscostmanagement-GetRightsizingRecommendation-request-Service"></a>
The specific service that you want recommendations for. The only valid value for `GetRightsizingRecommendation` is "`AmazonEC2`".
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

## Response Syntax
<a name="API_GetRightsizingRecommendation_ResponseSyntax"></a>

```
{
   "Configuration": {
      "BenefitsConsidered": boolean,
      "RecommendationTarget": "string"
   },
   "Metadata": {
      "AdditionalMetadata": "string",
      "GenerationTimestamp": "string",
      "LookbackPeriodInDays": "string",
      "RecommendationId": "string"
   },
   "NextPageToken": "string",
   "RightsizingRecommendations": [
      {
         "AccountId": "string",
         "CurrentInstance": {
            "CurrencyCode": "string",
            "InstanceName": "string",
            "MonthlyCost": "string",
            "OnDemandHoursInLookbackPeriod": "string",
            "ReservationCoveredHoursInLookbackPeriod": "string",
            "ResourceDetails": {
               "EC2ResourceDetails": {
                  "HourlyOnDemandRate": "string",
                  "InstanceType": "string",
                  "Memory": "string",
                  "NetworkPerformance": "string",
                  "Platform": "string",
                  "Region": "string",
                  "Sku": "string",
                  "Storage": "string",
                  "Vcpu": "string"
               }
            },
            "ResourceId": "string",
            "ResourceUtilization": {
               "EC2ResourceUtilization": {
                  "DiskResourceUtilization": {
                     "DiskReadBytesPerSecond": "string",
                     "DiskReadOpsPerSecond": "string",
                     "DiskWriteBytesPerSecond": "string",
                     "DiskWriteOpsPerSecond": "string"
                  },
                  "EBSResourceUtilization": {
                     "EbsReadBytesPerSecond": "string",
                     "EbsReadOpsPerSecond": "string",
                     "EbsWriteBytesPerSecond": "string",
                     "EbsWriteOpsPerSecond": "string"
                  },
                  "MaxCpuUtilizationPercentage": "string",
                  "MaxMemoryUtilizationPercentage": "string",
                  "MaxStorageUtilizationPercentage": "string",
                  "NetworkResourceUtilization": {
                     "NetworkInBytesPerSecond": "string",
                     "NetworkOutBytesPerSecond": "string",
                     "NetworkPacketsInPerSecond": "string",
                     "NetworkPacketsOutPerSecond": "string"
                  }
               }
            },
            "SavingsPlansCoveredHoursInLookbackPeriod": "string",
            "Tags": [
               {
                  "Key": "string",
                  "MatchOptions": [ "string" ],
                  "Values": [ "string" ]
               }
            ],
            "TotalRunningHoursInLookbackPeriod": "string"
         },
         "FindingReasonCodes": [ "string" ],
         "ModifyRecommendationDetail": {
            "TargetInstances": [
               {
                  "CurrencyCode": "string",
                  "DefaultTargetInstance": boolean,
                  "EstimatedMonthlyCost": "string",
                  "EstimatedMonthlySavings": "string",
                  "ExpectedResourceUtilization": {
                     "EC2ResourceUtilization": {
                        "DiskResourceUtilization": {
                           "DiskReadBytesPerSecond": "string",
                           "DiskReadOpsPerSecond": "string",
                           "DiskWriteBytesPerSecond": "string",
                           "DiskWriteOpsPerSecond": "string"
                        },
                        "EBSResourceUtilization": {
                           "EbsReadBytesPerSecond": "string",
                           "EbsReadOpsPerSecond": "string",
                           "EbsWriteBytesPerSecond": "string",
                           "EbsWriteOpsPerSecond": "string"
                        },
                        "MaxCpuUtilizationPercentage": "string",
                        "MaxMemoryUtilizationPercentage": "string",
                        "MaxStorageUtilizationPercentage": "string",
                        "NetworkResourceUtilization": {
                           "NetworkInBytesPerSecond": "string",
                           "NetworkOutBytesPerSecond": "string",
                           "NetworkPacketsInPerSecond": "string",
                           "NetworkPacketsOutPerSecond": "string"
                        }
                     }
                  },
                  "PlatformDifferences": [ "string" ],
                  "ResourceDetails": {
                     "EC2ResourceDetails": {
                        "HourlyOnDemandRate": "string",
                        "InstanceType": "string",
                        "Memory": "string",
                        "NetworkPerformance": "string",
                        "Platform": "string",
                        "Region": "string",
                        "Sku": "string",
                        "Storage": "string",
                        "Vcpu": "string"
                     }
                  }
               }
            ]
         },
         "RightsizingType": "string",
         "TerminateRecommendationDetail": {
            "CurrencyCode": "string",
            "EstimatedMonthlySavings": "string"
         }
      }
   ],
   "Summary": {
      "EstimatedTotalMonthlySavingsAmount": "string",
      "SavingsCurrencyCode": "string",
      "SavingsPercentage": "string",
      "TotalRecommendationCount": "string"
   }
}
```

## Response Elements
<a name="API_GetRightsizingRecommendation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Configuration](#API_GetRightsizingRecommendation_ResponseSyntax) **   <a name="awscostmanagement-GetRightsizingRecommendation-response-Configuration"></a>
You can use Configuration to customize recommendations across two attributes. You can choose to view recommendations for instances within the same instance families or across different instance families. You can also choose to view your estimated savings that are associated with recommendations with consideration of existing Savings Plans or RI benefits, or neither.
Type: [RightsizingRecommendationConfiguration](API_RightsizingRecommendationConfiguration.md) object

 ** [Metadata](#API_GetRightsizingRecommendation_ResponseSyntax) **   <a name="awscostmanagement-GetRightsizingRecommendation-response-Metadata"></a>
Information regarding this specific recommendation set.
Type: [RightsizingRecommendationMetadata](API_RightsizingRecommendationMetadata.md) object

 ** [NextPageToken](#API_GetRightsizingRecommendation_ResponseSyntax) **   <a name="awscostmanagement-GetRightsizingRecommendation-response-NextPageToken"></a>
The token to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

 ** [RightsizingRecommendations](#API_GetRightsizingRecommendation_ResponseSyntax) **   <a name="awscostmanagement-GetRightsizingRecommendation-response-RightsizingRecommendations"></a>
Recommendations to rightsize resources.
Type: Array of [RightsizingRecommendation](API_RightsizingRecommendation.md) objects

 ** [Summary](#API_GetRightsizingRecommendation_ResponseSyntax) **   <a name="awscostmanagement-GetRightsizingRecommendation-response-Summary"></a>
Summary of this recommendation set.
Type: [RightsizingRecommendationSummary](API_RightsizingRecommendationSummary.md) object

## Errors
<a name="API_GetRightsizingRecommendation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The pagination token is invalid. Try again without a pagination token.
HTTP Status Code: 400

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

## See Also
<a name="API_GetRightsizingRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/GetRightsizingRecommendation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/GetRightsizingRecommendation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/GetRightsizingRecommendation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/GetRightsizingRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/GetRightsizingRecommendation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/GetRightsizingRecommendation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/GetRightsizingRecommendation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/GetRightsizingRecommendation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/GetRightsizingRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/GetRightsizingRecommendation)
