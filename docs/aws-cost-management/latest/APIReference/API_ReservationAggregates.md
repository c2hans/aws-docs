---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ReservationAggregates.html
---

# ReservationAggregates
<a name="API_ReservationAggregates"></a>

The aggregated numbers for your reservation usage.

## Contents
<a name="API_ReservationAggregates_Contents"></a>

 ** AmortizedRecurringFee **   <a name="awscostmanagement-Type-ReservationAggregates-AmortizedRecurringFee"></a>
The monthly cost of your reservation. It's amortized over the reservation period.
Type: String
Required: No

 ** AmortizedUpfrontFee **   <a name="awscostmanagement-Type-ReservationAggregates-AmortizedUpfrontFee"></a>
The upfront cost of your reservation. It's amortized over the reservation period.
Type: String
Required: No

 ** NetRISavings **   <a name="awscostmanagement-Type-ReservationAggregates-NetRISavings"></a>
How much you saved due to purchasing and utilizing reservation. AWS calculates this by subtracting `TotalAmortizedFee` from `OnDemandCostOfRIHoursUsed`.
Type: String
Required: No

 ** OnDemandCostOfRIHoursUsed **   <a name="awscostmanagement-Type-ReservationAggregates-OnDemandCostOfRIHoursUsed"></a>
How much your reservation costs if charged On-Demand rates.
Type: String
Required: No

 ** PurchasedHours **   <a name="awscostmanagement-Type-ReservationAggregates-PurchasedHours"></a>
How many reservation hours that you purchased.
Type: String
Required: No

 ** PurchasedUnits **   <a name="awscostmanagement-Type-ReservationAggregates-PurchasedUnits"></a>
The number of Amazon EC2 reservation hours that you purchased. It's converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.
Type: String
Required: No

 ** RealizedSavings **   <a name="awscostmanagement-Type-ReservationAggregates-RealizedSavings"></a>
The realized savings because of purchasing and using a reservation.
Type: String
Required: No

 ** RICostForUnusedHours **   <a name="awscostmanagement-Type-ReservationAggregates-RICostForUnusedHours"></a>
The cost of unused hours for your reservation.
Type: String
Required: No

 ** TotalActualHours **   <a name="awscostmanagement-Type-ReservationAggregates-TotalActualHours"></a>
The total number of reservation hours that you used.
Type: String
Required: No

 ** TotalActualUnits **   <a name="awscostmanagement-Type-ReservationAggregates-TotalActualUnits"></a>
The total number of Amazon EC2 reservation hours that you used. It's converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.
Type: String
Required: No

 ** TotalAmortizedFee **   <a name="awscostmanagement-Type-ReservationAggregates-TotalAmortizedFee"></a>
The total cost of your reservation. It's amortized over the reservation period.
Type: String
Required: No

 ** TotalPotentialRISavings **   <a name="awscostmanagement-Type-ReservationAggregates-TotalPotentialRISavings"></a>
How much you might save if you use your entire reservation.
Type: String
Required: No

 ** UnrealizedSavings **   <a name="awscostmanagement-Type-ReservationAggregates-UnrealizedSavings"></a>
The unrealized savings because of purchasing and using a reservation.
Type: String
Required: No

 ** UnusedHours **   <a name="awscostmanagement-Type-ReservationAggregates-UnusedHours"></a>
The number of reservation hours that you didn't use.
Type: String
Required: No

 ** UnusedUnits **   <a name="awscostmanagement-Type-ReservationAggregates-UnusedUnits"></a>
The number of Amazon EC2 reservation hours that you didn't use. It's converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.
Type: String
Required: No

 ** UtilizationPercentage **   <a name="awscostmanagement-Type-ReservationAggregates-UtilizationPercentage"></a>
The percentage of reservation time that you used.
Type: String
Required: No

 ** UtilizationPercentageInUnits **   <a name="awscostmanagement-Type-ReservationAggregates-UtilizationPercentageInUnits"></a>
The percentage of Amazon EC2 reservation time that you used. It's converted to normalized units. Normalized units are available only for Amazon EC2 usage after November 11, 2017.
Type: String
Required: No

## See Also
<a name="API_ReservationAggregates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/ReservationAggregates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/ReservationAggregates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/ReservationAggregates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
