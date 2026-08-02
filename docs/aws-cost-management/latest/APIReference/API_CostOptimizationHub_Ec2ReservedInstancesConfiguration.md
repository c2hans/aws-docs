---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_Ec2ReservedInstancesConfiguration.html
---

# Ec2ReservedInstancesConfiguration
<a name="API_CostOptimizationHub_Ec2ReservedInstancesConfiguration"></a>

The EC2 reserved instances configuration used for recommendations.

## Contents
<a name="API_CostOptimizationHub_Ec2ReservedInstancesConfiguration_Contents"></a>

 ** accountScope **   <a name="awscostmanagement-Type-CostOptimizationHub_Ec2ReservedInstancesConfiguration-accountScope"></a>
The account scope for which you want recommendations.
Type: String
Required: No

 ** currentGeneration **   <a name="awscostmanagement-Type-CostOptimizationHub_Ec2ReservedInstancesConfiguration-currentGeneration"></a>
Determines whether the recommendation is for a current generation instance.
Type: String
Required: No

 ** instanceFamily **   <a name="awscostmanagement-Type-CostOptimizationHub_Ec2ReservedInstancesConfiguration-instanceFamily"></a>
The instance family of the recommended reservation.
Type: String
Required: No

 ** instanceType **   <a name="awscostmanagement-Type-CostOptimizationHub_Ec2ReservedInstancesConfiguration-instanceType"></a>
The type of instance that AWS recommends.
Type: String
Required: No

 ** monthlyRecurringCost **   <a name="awscostmanagement-Type-CostOptimizationHub_Ec2ReservedInstancesConfiguration-monthlyRecurringCost"></a>
How much purchasing these reserved instances costs you on a monthly basis.
Type: String
Required: No

 ** normalizedUnitsToPurchase **   <a name="awscostmanagement-Type-CostOptimizationHub_Ec2ReservedInstancesConfiguration-normalizedUnitsToPurchase"></a>
The number of normalized units that AWS recommends that you purchase.
Type: String
Required: No

 ** numberOfInstancesToPurchase **   <a name="awscostmanagement-Type-CostOptimizationHub_Ec2ReservedInstancesConfiguration-numberOfInstancesToPurchase"></a>
The number of instances that AWS recommends that you purchase.
Type: String
Required: No

 ** offeringClass **   <a name="awscostmanagement-Type-CostOptimizationHub_Ec2ReservedInstancesConfiguration-offeringClass"></a>
Indicates whether the recommendation is for standard or convertible reservations.
Type: String
Required: No

 ** paymentOption **   <a name="awscostmanagement-Type-CostOptimizationHub_Ec2ReservedInstancesConfiguration-paymentOption"></a>
The payment option for the commitment.
Type: String
Required: No

 ** platform **   <a name="awscostmanagement-Type-CostOptimizationHub_Ec2ReservedInstancesConfiguration-platform"></a>
The platform of the recommended reservation. The platform is the specific combination of operating system, license model, and software on an instance.
Type: String
Required: No

 ** reservedInstancesRegion **   <a name="awscostmanagement-Type-CostOptimizationHub_Ec2ReservedInstancesConfiguration-reservedInstancesRegion"></a>
The AWS Region of the commitment.
Type: String
Required: No

 ** service **   <a name="awscostmanagement-Type-CostOptimizationHub_Ec2ReservedInstancesConfiguration-service"></a>
The service for which you want recommendations.
Type: String
Required: No

 ** sizeFlexEligible **   <a name="awscostmanagement-Type-CostOptimizationHub_Ec2ReservedInstancesConfiguration-sizeFlexEligible"></a>
Determines whether the recommendation is size flexible.
Type: Boolean
Required: No

 ** tenancy **   <a name="awscostmanagement-Type-CostOptimizationHub_Ec2ReservedInstancesConfiguration-tenancy"></a>
Determines whether the recommended reservation is dedicated or shared.
Type: String
Required: No

 ** term **   <a name="awscostmanagement-Type-CostOptimizationHub_Ec2ReservedInstancesConfiguration-term"></a>
The reserved instances recommendation term in years.
Type: String
Required: No

 ** upfrontCost **   <a name="awscostmanagement-Type-CostOptimizationHub_Ec2ReservedInstancesConfiguration-upfrontCost"></a>
How much purchasing this instance costs you upfront.
Type: String
Required: No

## See Also
<a name="API_CostOptimizationHub_Ec2ReservedInstancesConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cost-optimization-hub-2022-07-26/Ec2ReservedInstancesConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cost-optimization-hub-2022-07-26/Ec2ReservedInstancesConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cost-optimization-hub-2022-07-26/Ec2ReservedInstancesConfiguration)
