---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PolicyOption.html
---

# PolicyOption
<a name="API_PolicyOption"></a>

Contains the settings to configure a network ACL policy, a AWS Network Firewall firewall policy deployment model, or a third-party firewall policy.

## Contents
<a name="API_PolicyOption_Contents"></a>

 ** NetworkAclCommonPolicy **   <a name="fms-Type-PolicyOption-NetworkAclCommonPolicy"></a>
Defines a Firewall Manager network ACL policy.
Type: [NetworkAclCommonPolicy](API_NetworkAclCommonPolicy.md) object
Required: No

 ** NetworkFirewallPolicy **   <a name="fms-Type-PolicyOption-NetworkFirewallPolicy"></a>
Defines the deployment model to use for the firewall policy.
Type: [NetworkFirewallPolicy](API_NetworkFirewallPolicy.md) object
Required: No

 ** ThirdPartyFirewallPolicy **   <a name="fms-Type-PolicyOption-ThirdPartyFirewallPolicy"></a>
Defines the policy options for a third-party firewall policy.
Type: [ThirdPartyFirewallPolicy](API_ThirdPartyFirewallPolicy.md) object
Required: No

## See Also
<a name="API_PolicyOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/PolicyOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/PolicyOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/PolicyOption)
