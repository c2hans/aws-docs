---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_OpenSearchReservedInstancesConfiguration.html
---

# OpenSearchReservedInstancesConfiguration
<a name="API_CostOptimizationHub_OpenSearchReservedInstancesConfiguration"></a>

The OpenSearch reserved instances configuration used for recommendations.

## Contents
<a name="API_CostOptimizationHub_OpenSearchReservedInstancesConfiguration_Contents"></a>

 ** accountScope **   <a name="awscostmanagement-Type-CostOptimizationHub_OpenSearchReservedInstancesConfiguration-accountScope"></a>
The account scope for which you want recommendations.
Type: String
Required: No

 ** currentGeneration **   <a name="awscostmanagement-Type-CostOptimizationHub_OpenSearchReservedInstancesConfiguration-currentGeneration"></a>
Determines whether the recommendation is for a current generation instance.
Type: String
Required: No

 ** instanceType **   <a name="awscostmanagement-Type-CostOptimizationHub_OpenSearchReservedInstancesConfiguration-instanceType"></a>
The type of instance that AWS recommends.
Type: String
Required: No

 ** monthlyRecurringCost **   <a name="awscostmanagement-Type-CostOptimizationHub_OpenSearchReservedInstancesConfiguration-monthlyRecurringCost"></a>
How much purchasing these reserved instances costs you on a monthly basis.
Type: String
Required: No

 ** normalizedUnitsToPurchase **   <a name="awscostmanagement-Type-CostOptimizationHub_OpenSearchReservedInstancesConfiguration-normalizedUnitsToPurchase"></a>
The number of normalized units that AWS recommends that you purchase.
Type: String
Required: No

 ** numberOfInstancesToPurchase **   <a name="awscostmanagement-Type-CostOptimizationHub_OpenSearchReservedInstancesConfiguration-numberOfInstancesToPurchase"></a>
The number of instances that AWS recommends that you purchase.
Type: String
Required: No

 ** paymentOption **   <a name="awscostmanagement-Type-CostOptimizationHub_OpenSearchReservedInstancesConfiguration-paymentOption"></a>
The payment option for the commitment.
Type: String
Required: No

 ** reservedInstancesRegion **   <a name="awscostmanagement-Type-CostOptimizationHub_OpenSearchReservedInstancesConfiguration-reservedInstancesRegion"></a>
The AWS Region of the commitment.
Type: String
Required: No

 ** service **   <a name="awscostmanagement-Type-CostOptimizationHub_OpenSearchReservedInstancesConfiguration-service"></a>
The service for which you want recommendations.
Type: String
Required: No

 ** sizeFlexEligible **   <a name="awscostmanagement-Type-CostOptimizationHub_OpenSearchReservedInstancesConfiguration-sizeFlexEligible"></a>
Determines whether the recommendation is size flexible.
Type: Boolean
Required: No

 ** term **   <a name="awscostmanagement-Type-CostOptimizationHub_OpenSearchReservedInstancesConfiguration-term"></a>
The reserved instances recommendation term in years.
Type: String
Required: No

 ** upfrontCost **   <a name="awscostmanagement-Type-CostOptimizationHub_OpenSearchReservedInstancesConfiguration-upfrontCost"></a>
How much purchasing this instance costs you upfront.
Type: String
Required: No

## See Also
<a name="API_CostOptimizationHub_OpenSearchReservedInstancesConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cost-optimization-hub-2022-07-26/OpenSearchReservedInstancesConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cost-optimization-hub-2022-07-26/OpenSearchReservedInstancesConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cost-optimization-hub-2022-07-26/OpenSearchReservedInstancesConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
