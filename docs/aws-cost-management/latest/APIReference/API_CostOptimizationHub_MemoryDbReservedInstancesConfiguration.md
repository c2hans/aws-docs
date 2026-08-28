---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_MemoryDbReservedInstancesConfiguration.html
---

# MemoryDbReservedInstancesConfiguration
<a name="API_CostOptimizationHub_MemoryDbReservedInstancesConfiguration"></a>

The MemoryDB reserved instances configuration used for recommendations.

**Note**
While the API reference uses "MemoryDB reserved instances", the user guide and other documentation refer to them as "MemoryDB reserved nodes", as the terms are used interchangeably.

## Contents
<a name="API_CostOptimizationHub_MemoryDbReservedInstancesConfiguration_Contents"></a>

 ** accountScope **   <a name="awscostmanagement-Type-CostOptimizationHub_MemoryDbReservedInstancesConfiguration-accountScope"></a>
The account scope for which you want recommendations.
Type: String
Required: No

 ** currentGeneration **   <a name="awscostmanagement-Type-CostOptimizationHub_MemoryDbReservedInstancesConfiguration-currentGeneration"></a>
Determines whether the recommendation is for a current generation instance.
Type: String
Required: No

 ** instanceFamily **   <a name="awscostmanagement-Type-CostOptimizationHub_MemoryDbReservedInstancesConfiguration-instanceFamily"></a>
The instance family of the recommended reservation.
Type: String
Required: No

 ** instanceType **   <a name="awscostmanagement-Type-CostOptimizationHub_MemoryDbReservedInstancesConfiguration-instanceType"></a>
The type of instance that AWS recommends.
Type: String
Required: No

 ** monthlyRecurringCost **   <a name="awscostmanagement-Type-CostOptimizationHub_MemoryDbReservedInstancesConfiguration-monthlyRecurringCost"></a>
How much purchasing these reserved instances costs you on a monthly basis.
Type: String
Required: No

 ** normalizedUnitsToPurchase **   <a name="awscostmanagement-Type-CostOptimizationHub_MemoryDbReservedInstancesConfiguration-normalizedUnitsToPurchase"></a>
The number of normalized units that AWS recommends that you purchase.
Type: String
Required: No

 ** numberOfInstancesToPurchase **   <a name="awscostmanagement-Type-CostOptimizationHub_MemoryDbReservedInstancesConfiguration-numberOfInstancesToPurchase"></a>
The number of instances that AWS recommends that you purchase.
Type: String
Required: No

 ** paymentOption **   <a name="awscostmanagement-Type-CostOptimizationHub_MemoryDbReservedInstancesConfiguration-paymentOption"></a>
The payment option for the commitment.
Type: String
Required: No

 ** reservedInstancesRegion **   <a name="awscostmanagement-Type-CostOptimizationHub_MemoryDbReservedInstancesConfiguration-reservedInstancesRegion"></a>
The AWS Region of the commitment.
Type: String
Required: No

 ** service **   <a name="awscostmanagement-Type-CostOptimizationHub_MemoryDbReservedInstancesConfiguration-service"></a>
The service for which you want recommendations.
Type: String
Required: No

 ** sizeFlexEligible **   <a name="awscostmanagement-Type-CostOptimizationHub_MemoryDbReservedInstancesConfiguration-sizeFlexEligible"></a>
Determines whether the recommendation is size flexible.
Type: Boolean
Required: No

 ** term **   <a name="awscostmanagement-Type-CostOptimizationHub_MemoryDbReservedInstancesConfiguration-term"></a>
The reserved instances recommendation term in years.
Type: String
Required: No

 ** upfrontCost **   <a name="awscostmanagement-Type-CostOptimizationHub_MemoryDbReservedInstancesConfiguration-upfrontCost"></a>
How much purchasing these reserved instances costs you upfront.
Type: String
Required: No

## See Also
<a name="API_CostOptimizationHub_MemoryDbReservedInstancesConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cost-optimization-hub-2022-07-26/MemoryDbReservedInstancesConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cost-optimization-hub-2022-07-26/MemoryDbReservedInstancesConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cost-optimization-hub-2022-07-26/MemoryDbReservedInstancesConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
