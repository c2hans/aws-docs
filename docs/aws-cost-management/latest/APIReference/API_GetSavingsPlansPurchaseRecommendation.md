---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlansPurchaseRecommendation.html
---

# GetSavingsPlansPurchaseRecommendation
<a name="API_GetSavingsPlansPurchaseRecommendation"></a>

Retrieves the Savings Plans recommendations for your account. First use `StartSavingsPlansPurchaseRecommendationGeneration` to generate a new set of recommendations, and then use `GetSavingsPlansPurchaseRecommendation` to retrieve them.

## Request Syntax
<a name="API_GetSavingsPlansPurchaseRecommendation_RequestSyntax"></a>

```
{
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
   "SavingsPlansType": "{{string}}",
   "TermInYears": "{{string}}"
}
```

## Request Parameters
<a name="API_GetSavingsPlansPurchaseRecommendation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountScope](#API_GetSavingsPlansPurchaseRecommendation_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansPurchaseRecommendation-request-AccountScope"></a>
The account scope that you want your recommendations for. Amazon Web Services calculates recommendations including the management account and member accounts if the value is set to `PAYER`. If the value is `LINKED`, recommendations are calculated for individual member accounts only.
Type: String
Valid Values: `PAYER | LINKED`
Required: No

 ** [Filter](#API_GetSavingsPlansPurchaseRecommendation_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansPurchaseRecommendation-request-Filter"></a>
You can filter your recommendations by Account ID with the `LINKED_ACCOUNT` dimension. To filter your recommendations by Account ID, specify `Key` as `LINKED_ACCOUNT` and `Value` as the comma-separated Acount ID(s) that you want to see Savings Plans purchase recommendations for.
For GetSavingsPlansPurchaseRecommendation, the `Filter` doesn't include `CostCategories` or `Tags`. It only includes `Dimensions`. With `Dimensions`, `Key` must be `LINKED_ACCOUNT` and `Value` can be a single Account ID or multiple comma-separated Account IDs that you want to see Savings Plans Purchase Recommendations for. `AND` and `OR` operators are not supported.
Type: [Expression](API_Expression.md) object
Required: No

 ** [LookbackPeriodInDays](#API_GetSavingsPlansPurchaseRecommendation_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansPurchaseRecommendation-request-LookbackPeriodInDays"></a>
The lookback period that's used to generate the recommendation.
Type: String
Valid Values: `SEVEN_DAYS | THIRTY_DAYS | SIXTY_DAYS`
Required: Yes

 ** [NextPageToken](#API_GetSavingsPlansPurchaseRecommendation_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansPurchaseRecommendation-request-NextPageToken"></a>
The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

 ** [PageSize](#API_GetSavingsPlansPurchaseRecommendation_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansPurchaseRecommendation-request-PageSize"></a>
The number of recommendations that you want returned in a single response object.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 6000.
Required: No

 ** [PaymentOption](#API_GetSavingsPlansPurchaseRecommendation_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansPurchaseRecommendation-request-PaymentOption"></a>
The payment option that's used to generate these recommendations.
Type: String
Valid Values: `NO_UPFRONT | PARTIAL_UPFRONT | ALL_UPFRONT | LIGHT_UTILIZATION | MEDIUM_UTILIZATION | HEAVY_UTILIZATION`
Required: Yes

 ** [SavingsPlansType](#API_GetSavingsPlansPurchaseRecommendation_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansPurchaseRecommendation-request-SavingsPlansType"></a>
The Savings Plans recommendation type that's requested.
Type: String
Valid Values: `COMPUTE_SP | EC2_INSTANCE_SP | SAGEMAKER_SP | DATABASE_SP`
Required: Yes

 ** [TermInYears](#API_GetSavingsPlansPurchaseRecommendation_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlansPurchaseRecommendation-request-TermInYears"></a>
The savings plan recommendation term that's used to generate these recommendations.
Type: String
Valid Values: `ONE_YEAR | THREE_YEARS`
Required: Yes

## Response Syntax
<a name="API_GetSavingsPlansPurchaseRecommendation_ResponseSyntax"></a>

```
{
   "Metadata": {
      "AdditionalMetadata": "string",
      "GenerationTimestamp": "string",
      "RecommendationId": "string"
   },
   "NextPageToken": "string",
   "SavingsPlansPurchaseRecommendation": {
      "AccountScope": "string",
      "LookbackPeriodInDays": "string",
      "PaymentOption": "string",
      "SavingsPlansPurchaseRecommendationDetails": [
         {
            "AccountId": "string",
            "CurrencyCode": "string",
            "CurrentAverageHourlyOnDemandSpend": "string",
            "CurrentMaximumHourlyOnDemandSpend": "string",
            "CurrentMinimumHourlyOnDemandSpend": "string",
            "EstimatedAverageUtilization": "string",
            "EstimatedMonthlySavingsAmount": "string",
            "EstimatedOnDemandCost": "string",
            "EstimatedOnDemandCostWithCurrentCommitment": "string",
            "EstimatedROI": "string",
            "EstimatedSavingsAmount": "string",
            "EstimatedSavingsPercentage": "string",
            "EstimatedSPCost": "string",
            "HourlyCommitmentToPurchase": "string",
            "RecommendationDetailId": "string",
            "SavingsPlansDetails": {
               "InstanceFamily": "string",
               "OfferingId": "string",
               "Region": "string"
            },
            "UpfrontCost": "string"
         }
      ],
      "SavingsPlansPurchaseRecommendationSummary": {
         "CurrencyCode": "string",
         "CurrentOnDemandSpend": "string",
         "DailyCommitmentToPurchase": "string",
         "EstimatedMonthlySavingsAmount": "string",
         "EstimatedOnDemandCostWithCurrentCommitment": "string",
         "EstimatedROI": "string",
         "EstimatedSavingsAmount": "string",
         "EstimatedSavingsPercentage": "string",
         "EstimatedTotalCost": "string",
         "HourlyCommitmentToPurchase": "string",
         "TotalRecommendationCount": "string"
      },
      "SavingsPlansType": "string",
      "TermInYears": "string"
   }
}
```

## Response Elements
<a name="API_GetSavingsPlansPurchaseRecommendation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Metadata](#API_GetSavingsPlansPurchaseRecommendation_ResponseSyntax) **   <a name="awscostmanagement-GetSavingsPlansPurchaseRecommendation-response-Metadata"></a>
Information that regards this specific recommendation set.
Type: [SavingsPlansPurchaseRecommendationMetadata](API_SavingsPlansPurchaseRecommendationMetadata.md) object

 ** [NextPageToken](#API_GetSavingsPlansPurchaseRecommendation_ResponseSyntax) **   <a name="awscostmanagement-GetSavingsPlansPurchaseRecommendation-response-NextPageToken"></a>
The token for the next set of retrievable results. AWS provides the token when the response from a previous call has more results than the maximum page size.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

 ** [SavingsPlansPurchaseRecommendation](#API_GetSavingsPlansPurchaseRecommendation_ResponseSyntax) **   <a name="awscostmanagement-GetSavingsPlansPurchaseRecommendation-response-SavingsPlansPurchaseRecommendation"></a>
Contains your request parameters, Savings Plan Recommendations Summary, and Details.
Type: [SavingsPlansPurchaseRecommendation](API_SavingsPlansPurchaseRecommendation.md) object

## Errors
<a name="API_GetSavingsPlansPurchaseRecommendation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The pagination token is invalid. Try again without a pagination token.
HTTP Status Code: 400

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

## See Also
<a name="API_GetSavingsPlansPurchaseRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/GetSavingsPlansPurchaseRecommendation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/GetSavingsPlansPurchaseRecommendation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/GetSavingsPlansPurchaseRecommendation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/GetSavingsPlansPurchaseRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/GetSavingsPlansPurchaseRecommendation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/GetSavingsPlansPurchaseRecommendation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/GetSavingsPlansPurchaseRecommendation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/GetSavingsPlansPurchaseRecommendation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/GetSavingsPlansPurchaseRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/GetSavingsPlansPurchaseRecommendation)
