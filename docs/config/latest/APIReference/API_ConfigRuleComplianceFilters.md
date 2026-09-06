---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigRuleComplianceFilters.html
---

# ConfigRuleComplianceFilters
<a name="API_ConfigRuleComplianceFilters"></a>

Filters the compliance results based on account ID, region, compliance type, and rule name.

## Contents
<a name="API_ConfigRuleComplianceFilters_Contents"></a>

 ** AccountId **   <a name="config-Type-ConfigRuleComplianceFilters-AccountId"></a>
The 12-digit account ID of the source account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** AwsRegion **   <a name="config-Type-ConfigRuleComplianceFilters-AwsRegion"></a>
The source region where the data is aggregated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ComplianceType **   <a name="config-Type-ConfigRuleComplianceFilters-ComplianceType"></a>
The rule compliance status.
For the `ConfigRuleComplianceFilters` data type, AWS Config supports only `COMPLIANT` and `NON_COMPLIANT`. AWS Config does not support the `NOT_APPLICABLE` and the `INSUFFICIENT_DATA` values.
Type: String
Valid Values: `COMPLIANT | NON_COMPLIANT | NOT_APPLICABLE | INSUFFICIENT_DATA`
Required: No

 ** ConfigRuleName **   <a name="config-Type-ConfigRuleComplianceFilters-ConfigRuleName"></a>
The name of the AWS Config rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9_-]+`
Required: No

## See Also
<a name="API_ConfigRuleComplianceFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConfigRuleComplianceFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConfigRuleComplianceFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConfigRuleComplianceFilters)
