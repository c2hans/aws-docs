---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConformancePackRuleCompliance.html
---

# ConformancePackRuleCompliance
<a name="API_ConformancePackRuleCompliance"></a>

Compliance information of one or more AWS Config rules within a conformance pack. You can filter using AWS Config rule names and compliance types.

## Contents
<a name="API_ConformancePackRuleCompliance_Contents"></a>

 ** ComplianceType **   <a name="config-Type-ConformancePackRuleCompliance-ComplianceType"></a>
Compliance of the AWS Config rule.
Type: String
Valid Values: `COMPLIANT | NON_COMPLIANT | INSUFFICIENT_DATA`
Required: No

 ** ConfigRuleName **   <a name="config-Type-ConformancePackRuleCompliance-ConfigRuleName"></a>
Name of the AWS Config rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9_-]+`
Required: No

 ** Controls **   <a name="config-Type-ConformancePackRuleCompliance-Controls"></a>
Controls for the conformance pack. A control is a process to prevent or detect problems while meeting objectives. A control can align with a specific compliance regime or map to internal controls defined by an organization.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_ConformancePackRuleCompliance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConformancePackRuleCompliance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConformancePackRuleCompliance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConformancePackRuleCompliance)
