---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_NatGatewayAttachedAppliance.html
---

# NatGatewayAttachedAppliance
<a name="API_NatGatewayAttachedAppliance"></a>

Information about an appliance attached to a NAT Gateway, providing managed security solutions for traffic filtering and inspection.

## Contents
<a name="API_NatGatewayAttachedAppliance_Contents"></a>

 ** applianceArn **
The Amazon Resource Name (ARN) of the attached appliance, identifying the specific proxy or security appliance resource.
Type: String
Required: No

 ** attachmentState **
The current attachment state of the appliance.
Type: String
Valid Values: `attaching | attached | detaching | detached | attach-failed | detach-failed`
Required: No

 ** failureCode **
The failure code if the appliance attachment or modification operation failed.
Type: String
Required: No

 ** failureMessage **
A descriptive message explaining the failure if the appliance attachment or modification operation failed.
Type: String
Required: No

 ** modificationState **
The current modification state of the appliance.
Type: String
Valid Values: `modifying | completed | failed`
Required: No

 ** type **
The type of appliance attached to the NAT Gateway. For network firewall proxy functionality, this will be "network-firewall-proxy".
Type: String
Valid Values: `network-firewall-proxy`
Required: No

 ** vpcEndpointId **
The VPC endpoint ID used to route traffic from application VPCs to the proxy for inspection and filtering.
Type: String
Required: No

## See Also
<a name="API_NatGatewayAttachedAppliance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/NatGatewayAttachedAppliance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/NatGatewayAttachedAppliance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/NatGatewayAttachedAppliance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
