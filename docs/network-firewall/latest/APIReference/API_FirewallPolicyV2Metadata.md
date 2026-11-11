---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_FirewallPolicyV2Metadata.html
---

# FirewallPolicyV2Metadata
<a name="API_FirewallPolicyV2Metadata"></a>

High-level information about a Next Generation policy, returned in a list of policies. To retrieve the policy's full properties, rule groups, and settings, use the Next Generation policy describe operation.

## Contents
<a name="API_FirewallPolicyV2Metadata_Contents"></a>

 ** Arn **   <a name="networkfirewall-Type-FirewallPolicyV2Metadata-Arn"></a>
The Amazon Resource Name (ARN) of the Next Generation policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`
Required: No

 ** Name **   <a name="networkfirewall-Type-FirewallPolicyV2Metadata-Name"></a>
The descriptive name of the Next Generation policy. You can't change the name of a firewall policy after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

## See Also
<a name="API_FirewallPolicyV2Metadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/FirewallPolicyV2Metadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/FirewallPolicyV2Metadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/FirewallPolicyV2Metadata)
