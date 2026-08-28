---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsNetworkFirewallFirewallDetails.html
---

# AwsNetworkFirewallFirewallDetails
<a name="API_AwsNetworkFirewallFirewallDetails"></a>

Details about an AWS Network Firewall firewall.

## Contents
<a name="API_AwsNetworkFirewallFirewallDetails_Contents"></a>

 ** DeleteProtection **   <a name="securityhub-Type-AwsNetworkFirewallFirewallDetails-DeleteProtection"></a>
Whether the firewall is protected from deletion. If set to `true`, then the firewall cannot be deleted.
Type: Boolean
Required: No

 ** Description **   <a name="securityhub-Type-AwsNetworkFirewallFirewallDetails-Description"></a>
A description of the firewall.
Type: String
Pattern: `.*\S.*`
Required: No

 ** FirewallArn **   <a name="securityhub-Type-AwsNetworkFirewallFirewallDetails-FirewallArn"></a>
The ARN of the firewall.
Type: String
Pattern: `.*\S.*`
Required: No

 ** FirewallId **   <a name="securityhub-Type-AwsNetworkFirewallFirewallDetails-FirewallId"></a>
The identifier of the firewall.
Type: String
Pattern: `.*\S.*`
Required: No

 ** FirewallName **   <a name="securityhub-Type-AwsNetworkFirewallFirewallDetails-FirewallName"></a>
A descriptive name of the firewall.
Type: String
Pattern: `.*\S.*`
Required: No

 ** FirewallPolicyArn **   <a name="securityhub-Type-AwsNetworkFirewallFirewallDetails-FirewallPolicyArn"></a>
The ARN of the firewall policy.
Type: String
Pattern: `.*\S.*`
Required: No

 ** FirewallPolicyChangeProtection **   <a name="securityhub-Type-AwsNetworkFirewallFirewallDetails-FirewallPolicyChangeProtection"></a>
Whether the firewall is protected from a change to the firewall policy. If set to `true`, you cannot associate a different policy with the firewall.
Type: Boolean
Required: No

 ** SubnetChangeProtection **   <a name="securityhub-Type-AwsNetworkFirewallFirewallDetails-SubnetChangeProtection"></a>
Whether the firewall is protected from a change to the subnet associations. If set to `true`, you cannot map different subnets to the firewall.
Type: Boolean
Required: No

 ** SubnetMappings **   <a name="securityhub-Type-AwsNetworkFirewallFirewallDetails-SubnetMappings"></a>
The public subnets that Network Firewall uses for the firewall. Each subnet must belong to a different Availability Zone.
Type: Array of [AwsNetworkFirewallFirewallSubnetMappingsDetails](API_AwsNetworkFirewallFirewallSubnetMappingsDetails.md) objects
Required: No

 ** VpcId **   <a name="securityhub-Type-AwsNetworkFirewallFirewallDetails-VpcId"></a>
The identifier of the VPC where the firewall is used.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsNetworkFirewallFirewallDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsNetworkFirewallFirewallDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsNetworkFirewallFirewallDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsNetworkFirewallFirewallDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
