---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ReservationPurchaseRecommendation.html
---

# ReservationPurchaseRecommendation
<a name="API_ReservationPurchaseRecommendation"></a>

A specific reservation that AWS recommends for purchase.

## Contents
<a name="API_ReservationPurchaseRecommendation_Contents"></a>

 ** AccountScope **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendation-AccountScope"></a>
The account scope that AWS recommends that you purchase this instance for. For example, you can purchase this reservation for an entire organization in AWS Organizations.
Type: String
Valid Values: `PAYER | LINKED`
Required: No

 ** LookbackPeriodInDays **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendation-LookbackPeriodInDays"></a>
How many days of previous usage that AWS considers when making this recommendation.
Type: String
Valid Values: `SEVEN_DAYS | THIRTY_DAYS | SIXTY_DAYS`
Required: No

 ** PaymentOption **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendation-PaymentOption"></a>
The payment option for the reservation (for example, `AllUpfront` or `NoUpfront`).
Type: String
Valid Values: `NO_UPFRONT | PARTIAL_UPFRONT | ALL_UPFRONT | LIGHT_UTILIZATION | MEDIUM_UTILIZATION | HEAVY_UTILIZATION`
Required: No

 ** RecommendationDetails **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendation-RecommendationDetails"></a>
Details about the recommended purchases.
Type: Array of [ReservationPurchaseRecommendationDetail](API_ReservationPurchaseRecommendationDetail.md) objects
Required: No

 ** RecommendationSummary **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendation-RecommendationSummary"></a>
A summary about the recommended purchase.
Type: [ReservationPurchaseRecommendationSummary](API_ReservationPurchaseRecommendationSummary.md) object
Required: No

 ** ServiceSpecification **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendation-ServiceSpecification"></a>
Hardware specifications for the service that you want recommendations for.
Type: [ServiceSpecification](API_ServiceSpecification.md) object
Required: No

 ** TermInYears **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendation-TermInYears"></a>
The term of the reservation that you want recommendations for, in years.
Type: String
Valid Values: `ONE_YEAR | THREE_YEARS`
Required: No

## See Also
<a name="API_ReservationPurchaseRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/ReservationPurchaseRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/ReservationPurchaseRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/ReservationPurchaseRecommendation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
