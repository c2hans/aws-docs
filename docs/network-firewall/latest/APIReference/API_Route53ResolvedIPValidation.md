---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_Route53ResolvedIPValidation.html
---

# Route53ResolvedIPValidation
<a name="API_Route53ResolvedIPValidation"></a>

The policy-level configuration for resolved IP validation. When you set this on a firewall policy, you require that the destination IP address of a connection is one that the Amazon Route 53 Resolver returned in a DNS response for a domain. The Route 53 Resolver must have returned the response in a VPC that's associated with the Route 53 Resolver DNS Firewall rule group identified by `DNSFirewallRuleGroupId`. At the policy level, this verifies that the destination IP address was resolved for some domain. To match specific domains, also configure stateful rule groups that use the `AWS_ROUTE_53_RESOLVED_DOMAIN` target type or the `aws_route_53_resolved_domain` rule keyword.

## Contents
<a name="API_Route53ResolvedIPValidation_Contents"></a>

 ** Action **   <a name="networkfirewall-Type-Route53ResolvedIPValidation-Action"></a>
The action that Network Firewall takes for a connection whose destination IP address fails resolved IP validation. A destination IP address fails validation when the Route 53 Resolver didn't return it in a DNS response in an associated VPC. Valid values are the following:
+  `ALERT` – Tags the matching connection in the firewall's flow logs without blocking it, when you enable logging. Use this to observe the effect of resolved IP validation before you enforce it.
+  `DROP` – Silently blocks the connection without sending any response to the client.
+  `REJECT` – Blocks the connection and sends a TCP reset (RST) to the client. Because a TCP reset applies only to TCP connections, Network Firewall drops non-TCP traffic instead of resetting it.
Type: String
Valid Values: `REJECT | DROP | ALERT`
Required: Yes

 ** DNSExpiryExceptionPolicy **   <a name="networkfirewall-Type-Route53ResolvedIPValidation-DNSExpiryExceptionPolicy"></a>
The action that Network Firewall takes when the DNS resolution recorded for a destination IP address has expired from the resolved IP cache. This applies when Network Firewall still sees traffic to that IP address after the expiry. Network Firewall keeps a resolution for longer than the DNS record's time to live (TTL). Valid values are the following:
+  `CONTINUE` – Treats the expired resolution as still valid and doesn't block the connection because of expiry.
+  `DROP` – Silently blocks traffic to the IP address after its resolution has expired, without sending any response to the client.
+  `REJECT` – Blocks traffic to the IP address after its resolution has expired and sends a TCP reset (RST) to the client. Network Firewall drops non-TCP traffic instead of resetting it.
Type: String
Valid Values: `REJECT | DROP | CONTINUE`
Required: Yes

 ** DNSFirewallRuleGroupId **   <a name="networkfirewall-Type-Route53ResolvedIPValidation-DNSFirewallRuleGroupId"></a>
The ID of the Route 53 Resolver DNS Firewall rule group that determines which VPCs' DNS resolutions count for resolved IP validation. A destination IP address counts as resolved for a domain only when the Route 53 Resolver returned it in a DNS response within a VPC that's associated with this rule group. Associate the rule group with the VPCs that send traffic to the firewall. The ID must match the pattern `^rslvr-frg-[0-9a-f]+$`. It must also exist and be accessible from your account. Network Firewall validates this when you create or update the policy.
Changing this value swaps the managed rule group association. Network Firewall processes the swap asynchronously. Each policy can have only one managed Route 53 Resolver DNS Firewall association. While a swap is in progress, Network Firewall rejects further changes to this setting. Wait until the swap completes, then retry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^rslvr-frg-[0-9a-f]+$`
Required: Yes

 ** BypassDestinationValidationIPRanges **   <a name="networkfirewall-Type-Route53ResolvedIPValidation-BypassDestinationValidationIPRanges"></a>
The destination IP address ranges that are exempt from the policy-level resolved IP check. Network Firewall doesn't apply the `Action` in this configuration to a connection whose destination falls in these ranges, even if the Route 53 Resolver didn't return that IP address in an associated VPC. Specify each entry as an IPv4 or IPv6 address or CIDR range, up to 100 entries.
This exemption applies only to the policy-level check. Stateful rules that use the `AWS_ROUTE_53_RESOLVED_DOMAIN` target type or the `aws_route_53_resolved_domain` keyword still evaluate connections to these destinations and match them independently of this list.
Type: Array of [Address](API_Address.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** SourceIPRanges **   <a name="networkfirewall-Type-Route53ResolvedIPValidation-SourceIPRanges"></a>
The client source IP address ranges whose connections are subject to resolved IP validation. Specify each entry as an IPv4 or IPv6 address or CIDR range, up to 100 entries. If you omit this field, resolved IP validation applies to the CIDR ranges of the firewall's VPC and of any additional VPCs attached to the firewall. Specifying an empty list is not the same as omitting the field: an empty list means that Network Firewall doesn't validate any source addresses.
This scope applies to the policy-level check only. Stateful rules that use the `AWS_ROUTE_53_RESOLVED_DOMAIN` target type or the `aws_route_53_resolved_domain` keyword still evaluate their destinations regardless of `SourceIPRanges`.
Type: Array of [Address](API_Address.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

## See Also
<a name="API_Route53ResolvedIPValidation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/Route53ResolvedIPValidation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/Route53ResolvedIPValidation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/Route53ResolvedIPValidation)
