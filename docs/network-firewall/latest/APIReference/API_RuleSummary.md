---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_RuleSummary.html
---

# RuleSummary
<a name="API_RuleSummary"></a>

A complex type containing details about a Suricata rule. Contains:
+  `SID`
+  `Msg`
+  `Metadata`

Summaries are available for rule groups you manage and for active threat defense AWS managed rule groups.

## Contents
<a name="API_RuleSummary_Contents"></a>

 ** Metadata **   <a name="networkfirewall-Type-RuleSummary-Metadata"></a>
The contents of the rule's metadata.
Type: String
Required: No

 ** Msg **   <a name="networkfirewall-Type-RuleSummary-Msg"></a>
The contents taken from the rule's msg field.
Type: String
Required: No

 ** SID **   <a name="networkfirewall-Type-RuleSummary-SID"></a>
The unique identifier (Signature ID) of the Suricata rule.
Type: String
Required: No

## See Also
<a name="API_RuleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/RuleSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/RuleSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/RuleSummary)
