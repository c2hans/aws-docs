---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_SummaryConfiguration.html
---

# SummaryConfiguration
<a name="API_SummaryConfiguration"></a>

A complex type that specifies which Suricata rule metadata fields to use when displaying threat information. Contains:
+  `RuleOptions` - The Suricata rule options fields to extract and display

These settings affect how threat information appears in both the console and API responses. Summaries are available for rule groups you manage and for active threat defense AWS managed rule groups.

## Contents
<a name="API_SummaryConfiguration_Contents"></a>

 ** RuleOptions **   <a name="networkfirewall-Type-SummaryConfiguration-RuleOptions"></a>
Specifies the selected rule options returned by [DescribeRuleGroupSummary](API_DescribeRuleGroupSummary.md).
Type: Array of strings
Valid Values: `SID | MSG | METADATA`
Required: No

## See Also
<a name="API_SummaryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/SummaryConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/SummaryConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/SummaryConfiguration)
