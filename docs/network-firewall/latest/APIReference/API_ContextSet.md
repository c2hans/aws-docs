---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ContextSet.html
---

# ContextSet
<a name="API_ContextSet"></a>

A list of resource identifiers from the context store that is associated with the firewall. Use a context set to write stateful rules against AWS resources instead of IP addresses. This is part of a [RuleVariables](API_RuleVariables.md).

## Contents
<a name="API_ContextSet_Contents"></a>

 ** Definition **   <a name="networkfirewall-Type-ContextSet-Definition"></a>
The list of resource identifiers. Each entry is the ID of a resource that the context store records, for example `vpc-1234567890abcdef0`, `subnet-1234567890abcdef0`, `sg-1234567890abcdef0`, or `tgw-attach-1234567890abcdef0`. You can specify 1-1,000 entries.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## See Also
<a name="API_ContextSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ContextSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ContextSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ContextSet)
