---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ReservationPurchaseRecommendationDetail.html
---

# ReservationPurchaseRecommendationDetail
<a name="API_ReservationPurchaseRecommendationDetail"></a>

Details about your recommended reservation purchase.

## Contents
<a name="API_ReservationPurchaseRecommendationDetail_Contents"></a>

 ** AccountId **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-AccountId"></a>
The account that this Reserved Instance (RI) recommendation is for.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** AverageNormalizedUnitsUsedPerHour **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-AverageNormalizedUnitsUsedPerHour"></a>
The average number of normalized units that you used in an hour during the historical period. AWS uses this to calculate your recommended reservation purchases.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** AverageNumberOfCapacityUnitsUsedPerHour **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-AverageNumberOfCapacityUnitsUsedPerHour"></a>
The average number of provisioned capacity units that you used in an hour during the historical period. AWS uses this to calculate your recommended reservation purchases.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** AverageNumberOfInstancesUsedPerHour **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-AverageNumberOfInstancesUsedPerHour"></a>
The average number of instances that you used in an hour during the historical period. AWS uses this to calculate your recommended reservation purchases.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** AverageUtilization **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-AverageUtilization"></a>
The average utilization of your instances. AWS uses this to calculate your recommended reservation purchases.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** CurrencyCode **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-CurrencyCode"></a>
The currency code that AWS used to calculate the costs for this instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedBreakEvenInMonths **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-EstimatedBreakEvenInMonths"></a>
How long AWS estimates that it takes for this instance to start saving you money, in months.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedMonthlyOnDemandCost **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-EstimatedMonthlyOnDemandCost"></a>
How much AWS estimates that you spend on On-Demand Instances in a month.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedMonthlySavingsAmount **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-EstimatedMonthlySavingsAmount"></a>
How much AWS estimates that this specific recommendation might save you in a month.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedMonthlySavingsPercentage **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-EstimatedMonthlySavingsPercentage"></a>
How much AWS estimates that this specific recommendation might save you in a month, as a percentage of your overall costs.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** EstimatedReservationCostForLookbackPeriod **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-EstimatedReservationCostForLookbackPeriod"></a>
How much AWS estimates that you might spend for all usage during the specified historical period if you had a reservation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** InstanceDetails **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-InstanceDetails"></a>
Details about the reservations that AWS recommends that you purchase.
Type: [InstanceDetails](API_InstanceDetails.md) object
Required: No

 ** MaximumNormalizedUnitsUsedPerHour **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-MaximumNormalizedUnitsUsedPerHour"></a>
The maximum number of normalized units that you used in an hour during the historical period. AWS uses this to calculate your recommended reservation purchases.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** MaximumNumberOfCapacityUnitsUsedPerHour **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-MaximumNumberOfCapacityUnitsUsedPerHour"></a>
The maximum number of provisioned capacity units that you used in an hour during the historical period. AWS uses this to calculate your recommended reservation purchases.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** MaximumNumberOfInstancesUsedPerHour **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-MaximumNumberOfInstancesUsedPerHour"></a>
The maximum number of instances that you used in an hour during the historical period. AWS uses this to calculate your recommended reservation purchases.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** MinimumNormalizedUnitsUsedPerHour **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-MinimumNormalizedUnitsUsedPerHour"></a>
The minimum number of normalized units that you used in an hour during the historical period. AWS uses this to calculate your recommended reservation purchases.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** MinimumNumberOfCapacityUnitsUsedPerHour **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-MinimumNumberOfCapacityUnitsUsedPerHour"></a>
The minimum number of provisioned capacity units that you used in an hour during the historical period. AWS uses this to calculate your recommended reservation purchases.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** MinimumNumberOfInstancesUsedPerHour **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-MinimumNumberOfInstancesUsedPerHour"></a>
The minimum number of instances that you used in an hour during the historical period. AWS uses this to calculate your recommended reservation purchases.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** RecommendedNormalizedUnitsToPurchase **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-RecommendedNormalizedUnitsToPurchase"></a>
The number of normalized units that AWS recommends that you purchase.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** RecommendedNumberOfCapacityUnitsToPurchase **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-RecommendedNumberOfCapacityUnitsToPurchase"></a>
The number of reserved capacity units that AWS recommends that you purchase.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** RecommendedNumberOfInstancesToPurchase **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-RecommendedNumberOfInstancesToPurchase"></a>
The number of instances that AWS recommends that you purchase.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** RecurringStandardMonthlyCost **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-RecurringStandardMonthlyCost"></a>
How much purchasing this instance costs you on a monthly basis.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** ReservedCapacityDetails **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-ReservedCapacityDetails"></a>
Details about the reservations that AWS recommends that you purchase.
Type: [ReservedCapacityDetails](API_ReservedCapacityDetails.md) object
Required: No

 ** UpfrontCost **   <a name="awscostmanagement-Type-ReservationPurchaseRecommendationDetail-UpfrontCost"></a>
How much purchasing this instance costs you upfront.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_ReservationPurchaseRecommendationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/ReservationPurchaseRecommendationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/ReservationPurchaseRecommendationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/ReservationPurchaseRecommendationDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
