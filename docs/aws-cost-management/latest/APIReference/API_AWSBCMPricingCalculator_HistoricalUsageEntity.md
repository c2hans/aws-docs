---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_HistoricalUsageEntity.html
---

# HistoricalUsageEntity
<a name="API_AWSBCMPricingCalculator_HistoricalUsageEntity"></a>

 Represents historical usage data for a specific entity.

## Contents
<a name="API_AWSBCMPricingCalculator_HistoricalUsageEntity_Contents"></a>

 ** billInterval **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_HistoricalUsageEntity-billInterval"></a>
 The time interval for the historical usage data.
Type: [BillInterval](API_AWSBCMPricingCalculator_BillInterval.md) object
Required: Yes

 ** filterExpression **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_HistoricalUsageEntity-filterExpression"></a>
 An optional filter expression to apply to the historical usage data.
Type: [Expression](API_AWSBCMPricingCalculator_Expression.md) object
Required: Yes

 ** operation **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_HistoricalUsageEntity-operation"></a>
 The specific operation associated with the usage.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** serviceCode **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_HistoricalUsageEntity-serviceCode"></a>
 The AWS service code associated with the usage.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** usageAccountId **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_HistoricalUsageEntity-usageAccountId"></a>
 The AWS account ID associated with the usage.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** usageType **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_HistoricalUsageEntity-usageType"></a>
 The type of usage.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** location **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_HistoricalUsageEntity-location"></a>
 The location associated with the usage.
Type: String
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_HistoricalUsageEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/HistoricalUsageEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/HistoricalUsageEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/HistoricalUsageEntity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
