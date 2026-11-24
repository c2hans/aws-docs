---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IgwFirewall.html
---

# IgwFirewall

Describes the Automated Internet Firewall that inspects traffic for an internet gateway or egress-only internet gateway route.

## Contents
<a name="API_IgwFirewall_Contents"></a>

 ** firewallArn **
The ARN of the firewall that inspects traffic for this route.
Type: String
Required: No

 ** status **
The status of the firewall that inspects traffic for this route. Uses the same values as `NetworkFirewallAssociation$firewallOnboardingStatus`: `active`, `disabling`, or `pending`.
Type: String
Valid Values: `pending | active | disabling`
Required: No

## See Also
<a name="API_IgwFirewall_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IgwFirewall)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IgwFirewall)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IgwFirewall)
