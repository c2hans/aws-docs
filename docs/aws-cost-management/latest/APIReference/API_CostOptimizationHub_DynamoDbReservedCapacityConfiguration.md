---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_DynamoDbReservedCapacityConfiguration.html
---

# DynamoDbReservedCapacityConfiguration
<a name="API_CostOptimizationHub_DynamoDbReservedCapacityConfiguration"></a>

The DynamoDB reserved capacity configuration used for recommendations.

## Contents
<a name="API_CostOptimizationHub_DynamoDbReservedCapacityConfiguration_Contents"></a>

 ** accountScope **   <a name="awscostmanagement-Type-CostOptimizationHub_DynamoDbReservedCapacityConfiguration-accountScope"></a>
The account scope for which you want recommendations.
Type: String
Required: No

 ** capacityUnits **   <a name="awscostmanagement-Type-CostOptimizationHub_DynamoDbReservedCapacityConfiguration-capacityUnits"></a>
The capacity unit of the recommended reservation.
Type: String
Required: No

 ** monthlyRecurringCost **   <a name="awscostmanagement-Type-CostOptimizationHub_DynamoDbReservedCapacityConfiguration-monthlyRecurringCost"></a>
How much purchasing this reserved capacity costs you on a monthly basis.
Type: String
Required: No

 ** numberOfCapacityUnitsToPurchase **   <a name="awscostmanagement-Type-CostOptimizationHub_DynamoDbReservedCapacityConfiguration-numberOfCapacityUnitsToPurchase"></a>
The number of reserved capacity units that AWS recommends that you purchase.
Type: String
Required: No

 ** paymentOption **   <a name="awscostmanagement-Type-CostOptimizationHub_DynamoDbReservedCapacityConfiguration-paymentOption"></a>
The payment option for the commitment.
Type: String
Required: No

 ** reservedInstancesRegion **   <a name="awscostmanagement-Type-CostOptimizationHub_DynamoDbReservedCapacityConfiguration-reservedInstancesRegion"></a>
The AWS Region of the commitment.
Type: String
Required: No

 ** service **   <a name="awscostmanagement-Type-CostOptimizationHub_DynamoDbReservedCapacityConfiguration-service"></a>
The service for which you want recommendations.
Type: String
Required: No

 ** term **   <a name="awscostmanagement-Type-CostOptimizationHub_DynamoDbReservedCapacityConfiguration-term"></a>
The reserved capacity recommendation term in years.
Type: String
Required: No

 ** upfrontCost **   <a name="awscostmanagement-Type-CostOptimizationHub_DynamoDbReservedCapacityConfiguration-upfrontCost"></a>
How much purchasing this reserved capacity costs you upfront.
Type: String
Required: No

## See Also
<a name="API_CostOptimizationHub_DynamoDbReservedCapacityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cost-optimization-hub-2022-07-26/DynamoDbReservedCapacityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cost-optimization-hub-2022-07-26/DynamoDbReservedCapacityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cost-optimization-hub-2022-07-26/DynamoDbReservedCapacityConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
