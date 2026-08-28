---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_NatGatewayAttachment.html
---

# NatGatewayAttachment
<a name="API_NatGatewayAttachment"></a>

The definition and status of the attachment between a proxy mode firewall and a NAT gateway that proxies its traffic.

## Contents
<a name="API_NatGatewayAttachment_Contents"></a>

 ** NatGatewayId **   <a name="networkfirewall-Type-NatGatewayAttachment-NatGatewayId"></a>
A unique identifier for the NAT gateway to use with proxy resources.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** Status **   <a name="networkfirewall-Type-NatGatewayAttachment-Status"></a>
The current status of the NAT gateway attachment.
When this value is `READY`, the attachment is available to proxy traffic. Otherwise, this value reflects its state, for example `CREATING` or `DELETING`.
Type: String
Valid Values: `CREATING | READY | UPDATING | FAILED | DELETING`
Required: Yes

 ** DnsName **   <a name="networkfirewall-Type-NatGatewayAttachment-DnsName"></a>
The DNS name that resolves to the firewall's proxy for traffic sent through this NAT gateway attachment.
Type: String
Required: No

 ** StatusMessage **   <a name="networkfirewall-Type-NatGatewayAttachment-StatusMessage"></a>
If Network Firewall encounters an issue with the NAT gateway attachment, it populates this with an explanation of the problem.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9- ]+$`
Required: No

## See Also
<a name="API_NatGatewayAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/NatGatewayAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/NatGatewayAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/NatGatewayAttachment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
