---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ElastiCacheReservedInstancesConfiguration.html
---

# ElastiCacheReservedInstancesConfiguration
<a name="API_CostOptimizationHub_ElastiCacheReservedInstancesConfiguration"></a>

The ElastiCache reserved instances configuration used for recommendations.

## Contents
<a name="API_CostOptimizationHub_ElastiCacheReservedInstancesConfiguration_Contents"></a>

 ** accountScope **   <a name="awscostmanagement-Type-CostOptimizationHub_ElastiCacheReservedInstancesConfiguration-accountScope"></a>
The account scope for which you want recommendations.
Type: String
Required: No

 ** currentGeneration **   <a name="awscostmanagement-Type-CostOptimizationHub_ElastiCacheReservedInstancesConfiguration-currentGeneration"></a>
Determines whether the recommendation is for a current generation instance.
Type: String
Required: No

 ** instanceFamily **   <a name="awscostmanagement-Type-CostOptimizationHub_ElastiCacheReservedInstancesConfiguration-instanceFamily"></a>
The instance family of the recommended reservation.
Type: String
Required: No

 ** instanceType **   <a name="awscostmanagement-Type-CostOptimizationHub_ElastiCacheReservedInstancesConfiguration-instanceType"></a>
The type of instance that AWS recommends.
Type: String
Required: No

 ** monthlyRecurringCost **   <a name="awscostmanagement-Type-CostOptimizationHub_ElastiCacheReservedInstancesConfiguration-monthlyRecurringCost"></a>
How much purchasing these reserved instances costs you on a monthly basis.
Type: String
Required: No

 ** normalizedUnitsToPurchase **   <a name="awscostmanagement-Type-CostOptimizationHub_ElastiCacheReservedInstancesConfiguration-normalizedUnitsToPurchase"></a>
The number of normalized units that AWS recommends that you purchase.
Type: String
Required: No

 ** numberOfInstancesToPurchase **   <a name="awscostmanagement-Type-CostOptimizationHub_ElastiCacheReservedInstancesConfiguration-numberOfInstancesToPurchase"></a>
The number of instances that AWS recommends that you purchase.
Type: String
Required: No

 ** paymentOption **   <a name="awscostmanagement-Type-CostOptimizationHub_ElastiCacheReservedInstancesConfiguration-paymentOption"></a>
The payment option for the commitment.
Type: String
Required: No

 ** reservedInstancesRegion **   <a name="awscostmanagement-Type-CostOptimizationHub_ElastiCacheReservedInstancesConfiguration-reservedInstancesRegion"></a>
The AWS Region of the commitment.
Type: String
Required: No

 ** service **   <a name="awscostmanagement-Type-CostOptimizationHub_ElastiCacheReservedInstancesConfiguration-service"></a>
The service for which you want recommendations.
Type: String
Required: No

 ** sizeFlexEligible **   <a name="awscostmanagement-Type-CostOptimizationHub_ElastiCacheReservedInstancesConfiguration-sizeFlexEligible"></a>
Determines whether the recommendation is size flexible.
Type: Boolean
Required: No

 ** term **   <a name="awscostmanagement-Type-CostOptimizationHub_ElastiCacheReservedInstancesConfiguration-term"></a>
The reserved instances recommendation term in years.
Type: String
Required: No

 ** upfrontCost **   <a name="awscostmanagement-Type-CostOptimizationHub_ElastiCacheReservedInstancesConfiguration-upfrontCost"></a>
How much purchasing this instance costs you upfront.
Type: String
Required: No

## See Also
<a name="API_CostOptimizationHub_ElastiCacheReservedInstancesConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cost-optimization-hub-2022-07-26/ElastiCacheReservedInstancesConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cost-optimization-hub-2022-07-26/ElastiCacheReservedInstancesConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cost-optimization-hub-2022-07-26/ElastiCacheReservedInstancesConfiguration)
