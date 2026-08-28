---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_VpcEndpointAssociationStatus.html
---

# VpcEndpointAssociationStatus
<a name="API_VpcEndpointAssociationStatus"></a>

Detailed information about the current status of a [VpcEndpointAssociation](API_VpcEndpointAssociation.md). You can retrieve this by calling [DescribeVpcEndpointAssociation](API_DescribeVpcEndpointAssociation.md) and providing the VPC endpoint association ARN.

## Contents
<a name="API_VpcEndpointAssociationStatus_Contents"></a>

 ** Status **   <a name="networkfirewall-Type-VpcEndpointAssociationStatus-Status"></a>
The readiness of the configured firewall endpoint to handle network traffic.
Type: String
Valid Values: `PROVISIONING | DELETING | READY | FAILED`
Required: Yes

 ** AssociationSyncState **   <a name="networkfirewall-Type-VpcEndpointAssociationStatus-AssociationSyncState"></a>
The list of the Availability Zone sync states for all subnets that are defined by the firewall.
Type: String to [AZSyncState](API_AZSyncState.md) object map
Required: No

## See Also
<a name="API_VpcEndpointAssociationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/VpcEndpointAssociationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/VpcEndpointAssociationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/VpcEndpointAssociationStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
