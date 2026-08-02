---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_RuleGroupSourceStatelessRuleMatchAttributesTcpFlags.html
---

# RuleGroupSourceStatelessRuleMatchAttributesTcpFlags
<a name="API_RuleGroupSourceStatelessRuleMatchAttributesTcpFlags"></a>

A set of TCP flags and masks to inspect for.

## Contents
<a name="API_RuleGroupSourceStatelessRuleMatchAttributesTcpFlags_Contents"></a>

 ** Flags **   <a name="securityhub-Type-RuleGroupSourceStatelessRuleMatchAttributesTcpFlags-Flags"></a>
Defines the flags from the `Masks` setting that must be set in order for the packet to match. Flags that are listed must be set. Flags that are not listed must not be set.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Masks **   <a name="securityhub-Type-RuleGroupSourceStatelessRuleMatchAttributesTcpFlags-Masks"></a>
The set of flags to consider in the inspection. If not specified, then all flags are inspected.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_RuleGroupSourceStatelessRuleMatchAttributesTcpFlags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/RuleGroupSourceStatelessRuleMatchAttributesTcpFlags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/RuleGroupSourceStatelessRuleMatchAttributesTcpFlags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/RuleGroupSourceStatelessRuleMatchAttributesTcpFlags)
