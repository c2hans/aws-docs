---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlanPurchaseRecommendationDetails.html
---

# GetSavingsPlanPurchaseRecommendationDetails
<a name="API_GetSavingsPlanPurchaseRecommendationDetails"></a>

Retrieves the details for a Savings Plan recommendation. These details include the hourly data-points that construct the cost, coverage, and utilization charts.

## Request Syntax
<a name="API_GetSavingsPlanPurchaseRecommendationDetails_RequestSyntax"></a>

```
{
   "RecommendationDetailId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetSavingsPlanPurchaseRecommendationDetails_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RecommendationDetailId](#API_GetSavingsPlanPurchaseRecommendationDetails_RequestSyntax) **   <a name="awscostmanagement-GetSavingsPlanPurchaseRecommendationDetails-request-RecommendationDetailId"></a>
The ID that is associated with the Savings Plan recommendation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[\S\s]{8}-[\S\s]{4}-[\S\s]{4}-[\S\s]{4}-[\S\s]{12}$`
Required: Yes

## Response Syntax
<a name="API_GetSavingsPlanPurchaseRecommendationDetails_ResponseSyntax"></a>

```
{
   "RecommendationDetailData": {
      "AccountId": "string",
      "AccountScope": "string",
      "CurrencyCode": "string",
      "CurrentAverageCoverage": "string",
      "CurrentAverageHourlyOnDemandSpend": "string",
      "CurrentMaximumHourlyOnDemandSpend": "string",
      "CurrentMinimumHourlyOnDemandSpend": "string",
      "EstimatedAverageCoverage": "string",
      "EstimatedAverageUtilization": "string",
      "EstimatedMonthlySavingsAmount": "string",
      "EstimatedOnDemandCost": "string",
      "EstimatedOnDemandCostWithCurrentCommitment": "string",
      "EstimatedROI": "string",
      "EstimatedSavingsAmount": "string",
      "EstimatedSavingsPercentage": "string",
      "EstimatedSPCost": "string",
      "ExistingHourlyCommitment": "string",
      "GenerationTimestamp": "string",
      "HourlyCommitmentToPurchase": "string",
      "InstanceFamily": "string",
      "LatestUsageTimestamp": "string",
      "LookbackPeriodInDays": "string",
      "MetricsOverLookbackPeriod": [
         {
            "CurrentCoverage": "string",
            "EstimatedCoverage": "string",
            "EstimatedNewCommitmentUtilization": "string",
            "EstimatedOnDemandCost": "string",
            "StartTime": "string"
         }
      ],
      "OfferingId": "string",
      "PaymentOption": "string",
      "Region": "string",
      "SavingsPlansType": "string",
      "TermInYears": "string",
      "UpfrontCost": "string"
   },
   "RecommendationDetailId": "string"
}
```

## Response Elements
<a name="API_GetSavingsPlanPurchaseRecommendationDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RecommendationDetailData](#API_GetSavingsPlanPurchaseRecommendationDetails_ResponseSyntax) **   <a name="awscostmanagement-GetSavingsPlanPurchaseRecommendationDetails-response-RecommendationDetailData"></a>
Contains detailed information about a specific Savings Plan recommendation.
Type: [RecommendationDetailData](API_RecommendationDetailData.md) object

 ** [RecommendationDetailId](#API_GetSavingsPlanPurchaseRecommendationDetails_ResponseSyntax) **   <a name="awscostmanagement-GetSavingsPlanPurchaseRecommendationDetails-response-RecommendationDetailId"></a>
The ID that is associated with the Savings Plan recommendation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[\S\s]{8}-[\S\s]{4}-[\S\s]{4}-[\S\s]{4}-[\S\s]{12}$`

## Errors
<a name="API_GetSavingsPlanPurchaseRecommendationDetails_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DataUnavailableException **
The requested data is unavailable.
HTTP Status Code: 400

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

## See Also
<a name="API_GetSavingsPlanPurchaseRecommendationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/GetSavingsPlanPurchaseRecommendationDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/GetSavingsPlanPurchaseRecommendationDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/GetSavingsPlanPurchaseRecommendationDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/GetSavingsPlanPurchaseRecommendationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/GetSavingsPlanPurchaseRecommendationDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/GetSavingsPlanPurchaseRecommendationDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/GetSavingsPlanPurchaseRecommendationDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/GetSavingsPlanPurchaseRecommendationDetails)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/GetSavingsPlanPurchaseRecommendationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/GetSavingsPlanPurchaseRecommendationDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
