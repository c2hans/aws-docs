---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_FirewallSyncReason.html
---

# FirewallSyncReason
<a name="API_FirewallSyncReason"></a>

Describes why a firewall is out of sync. Exactly one of `missingFirewall`, `invalidFirewall`, or `invalidResource` contains a value.

## Contents
<a name="API_FirewallSyncReason_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** invalidFirewall **   <a name="networksecuritymanager-Type-FirewallSyncReason-invalidFirewall"></a>
Details about a firewall whose configuration does not match the intended configuration.
Type: [InvalidFirewallReasons](API_InvalidFirewallReasons.md) object
Required: No

 ** invalidResource **   <a name="networksecuritymanager-Type-FirewallSyncReason-invalidResource"></a>
A map of related resources whose configuration does not match the intended configuration, grouped by resource type. Each entry lists the resources of that type that are out of sync. For example, subnets whose connectivity type differs from the connectivity type that the policy specifies.
Type: String to array of [InvalidResourceIssue](API_InvalidResourceIssue.md) objects map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Valid Keys: `AWS::ApiGateway::Stage | AWS::CloudFront::Distribution | AWS::EC2::EIP | AWS::ElasticLoadBalancingV2::LoadBalancer::application | AWS::ElasticLoadBalancing::LoadBalancer | AWS::WAFv2::WebACL | AWS::Shield::Protection | AWS::ShieldRegional::Protection | AWS::EC2::VPC | AWS::EC2::TransitGateway | AWS::EC2::Subnet | AWS::EC2::RouteTable | AWS::NetworkFirewall::Firewall | AWS::NetworkFirewall::FirewallPolicy | AWS::NetworkFirewall::FirewallPolicyV2 | AWS::RAM::ResourceShare`
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** missingFirewall **   <a name="networksecuritymanager-Type-FirewallSyncReason-missingFirewall"></a>
Indicates that an expected firewall is missing. The value describes the missing firewall.
Type: String
Required: No

## See Also
<a name="API_FirewallSyncReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/FirewallSyncReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/FirewallSyncReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/FirewallSyncReason)
