---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_VpcEndpoint.html
---

# VpcEndpoint
<a name="API_VpcEndpoint"></a>

The VPC and subnets for a proxy mode firewall endpoint. This is used in [CreateFirewall](API_CreateFirewall.md) when `NoSourcePreservation` is `TRUE`, to specify where Network Firewall creates the firewall endpoint.

This differs from [VpcEndpointAssociation](API_VpcEndpointAssociation.md), which defines additional secondary endpoints for a firewall in other VPCs.

## Contents
<a name="API_VpcEndpoint_Contents"></a>

 ** SubnetMappings **   <a name="networkfirewall-Type-VpcEndpoint-SubnetMappings"></a>
The subnets in which Network Firewall creates the firewall endpoint for a proxy mode firewall. Each subnet must belong to a different Availability Zone in the VPC.
Type: Array of [SubnetMapping](API_SubnetMapping.md) objects
Required: Yes

 ** VpcId **   <a name="networkfirewall-Type-VpcEndpoint-VpcId"></a>
The unique identifier of the VPC where Network Firewall creates the proxy mode firewall endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^vpc-[0-9a-f]+$`
Required: Yes

## See Also
<a name="API_VpcEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/VpcEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/VpcEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/VpcEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
