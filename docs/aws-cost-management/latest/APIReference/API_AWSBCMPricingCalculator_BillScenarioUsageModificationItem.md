---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BillScenarioUsageModificationItem.html
---

# BillScenarioUsageModificationItem
<a name="API_AWSBCMPricingCalculator_BillScenarioUsageModificationItem"></a>

 Represents a usage modification item in a bill scenario.

## Contents
<a name="API_AWSBCMPricingCalculator_BillScenarioUsageModificationItem_Contents"></a>

 ** operation **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioUsageModificationItem-operation"></a>
 The specific operation associated with this usage modification.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** serviceCode **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioUsageModificationItem-serviceCode"></a>
 The AWS service code for this usage modification.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** usageType **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioUsageModificationItem-usageType"></a>
 The type of usage being modified.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** availabilityZone **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioUsageModificationItem-availabilityZone"></a>
 The availability zone associated with this usage modification, if applicable.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: No

 ** group **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioUsageModificationItem-group"></a>
 The group identifier for the usage modification.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 30.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** historicalUsage **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioUsageModificationItem-historicalUsage"></a>
 Historical usage data associated with this modification, if available.
Type: [HistoricalUsageEntity](API_AWSBCMPricingCalculator_HistoricalUsageEntity.md) object
Required: No

 ** id **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioUsageModificationItem-id"></a>
 The unique identifier of the usage modification.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** location **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioUsageModificationItem-location"></a>
 The location associated with this usage modification.
Type: String
Required: No

 ** quantities **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioUsageModificationItem-quantities"></a>
 The modified usage quantities.
Type: Array of [UsageQuantity](API_AWSBCMPricingCalculator_UsageQuantity.md) objects
Required: No

 ** usageAccountId **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioUsageModificationItem-usageAccountId"></a>
 The AWS account ID associated with this usage modification.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_BillScenarioUsageModificationItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/BillScenarioUsageModificationItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/BillScenarioUsageModificationItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/BillScenarioUsageModificationItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
