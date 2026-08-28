---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayMulticastDomainAssociation.html
---

# TransitGatewayMulticastDomainAssociation
<a name="API_TransitGatewayMulticastDomainAssociation"></a>

Describes the resources associated with the transit gateway multicast domain.

## Contents
<a name="API_TransitGatewayMulticastDomainAssociation_Contents"></a>

 ** resourceId **
The ID of the resource.
Type: String
Required: No

 ** resourceOwnerId **
 The ID of the AWS account that owns the transit gateway multicast domain association resource.
Type: String
Required: No

 ** resourceType **
The type of resource, for example a VPC attachment.
Type: String
Valid Values: `vpc | vpn | vpn-concentrator | direct-connect-gateway | connect | peering | tgw-peering | client-vpn`
Required: No

 ** subnet **
The subnet associated with the transit gateway multicast domain.
Type: [SubnetAssociation](API_SubnetAssociation.md) object
Required: No

 ** transitGatewayAttachmentId **
The ID of the transit gateway attachment.
Type: String
Required: No

## See Also
<a name="API_TransitGatewayMulticastDomainAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayMulticastDomainAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayMulticastDomainAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayMulticastDomainAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
