---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_NetworkFirewallAssociation.html
---

# NetworkFirewallAssociation

Describes an Automated Internet Firewall that inspects traffic between a VPC and its internet gateway or egress-only internet gateway.

## Contents
<a name="API_NetworkFirewallAssociation_Contents"></a>

 ** firewallArn **
The Amazon Resource Name (ARN) of the firewall.
Type: String
Required: No

 ** firewallMode **
The mode of the firewall. Possible values:
+  `enforce`: The firewall applies its policy to traffic.
+  `monitor`: The firewall logs traffic that its policy would act on, but doesn't block it.
Type: String
Valid Values: `monitor | enforce`
Required: No

 ** firewallOnboardingStatus **
The status of the firewall for the VPC. Possible values:
+  `active`: The firewall inspects traffic for the VPC.
+  `disabling`: AWS is removing the firewall from the VPC.
+  `pending`: AWS is setting up the firewall for the VPC. The firewall might not inspect traffic yet.
Type: String
Valid Values: `pending | active | disabling`
Required: No

## See Also
<a name="API_NetworkFirewallAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/NetworkFirewallAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/NetworkFirewallAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/NetworkFirewallAssociation)
