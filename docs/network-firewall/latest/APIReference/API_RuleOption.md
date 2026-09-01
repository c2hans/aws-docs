---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_RuleOption.html
---

# RuleOption
<a name="API_RuleOption"></a>

Additional settings for a stateful rule. This is part of the [StatefulRule](API_StatefulRule.md) configuration.

## Contents
<a name="API_RuleOption_Contents"></a>

 ** Keyword **   <a name="networkfirewall-Type-RuleOption-Keyword"></a>
The keyword for the Suricata compatible rule option. You must include a `sid` (signature ID), and can optionally include other keywords. For information about Suricata compatible keywords, see [Rule options](https://suricata.readthedocs.io/en/suricata-8.0.3/rules/intro.html#rule-options) in the Suricata documentation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*`
Required: Yes

 ** Settings **   <a name="networkfirewall-Type-RuleOption-Settings"></a>
The settings of the Suricata compatible rule option. Rule options have zero or more setting values, and the number of possible and required settings depends on the `Keyword`. For more information about the settings for specific options, see [Rule options](https://suricata.readthedocs.io/en/suricata-8.0.3/rules/intro.html#rule-options).
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `.*`
Required: No

## See Also
<a name="API_RuleOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/RuleOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/RuleOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/RuleOption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
