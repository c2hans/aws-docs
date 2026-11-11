---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_RuleMetadata.html
---

# RuleMetadata
<a name="API_RuleMetadata"></a>

Metadata for a single firewall engine rule. Use it to disable a rule without removing it and to attach a description. When you describe a rule group in `RULES_STRING` format, Network Firewall renders a disabled rule and its description as `#` comment lines above the rule.

## Contents
<a name="API_RuleMetadata_Contents"></a>

 ** RuleDescription **   <a name="networkfirewall-Type-RuleMetadata-RuleDescription"></a>
A description of the rule, up to 512 characters. The description can span multiple lines. A description line can't itself look like a firewall rule; to disable a rule, set `RuleEnabled` to `FALSE` instead.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `[\s\S]*`
Required: No

 ** RuleEnabled **   <a name="networkfirewall-Type-RuleMetadata-RuleEnabled"></a>
Specifies whether the rule is active. The default is `TRUE`. When you set this to `FALSE`, Network Firewall keeps the rule in the rule group but doesn't evaluate it against traffic and doesn't count it toward the rule group's consumed capacity.
Type: Boolean
Required: No

## See Also
<a name="API_RuleMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/RuleMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/RuleMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/RuleMetadata)
