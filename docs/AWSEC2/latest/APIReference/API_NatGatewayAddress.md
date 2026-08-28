---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_NatGatewayAddress.html
---

# NatGatewayAddress
<a name="API_NatGatewayAddress"></a>

Describes the IP addresses and network interface associated with a NAT gateway.

## Contents
<a name="API_NatGatewayAddress_Contents"></a>

 ** allocationId **
[Public NAT gateway only] The allocation ID of the Elastic IP address that's associated with the NAT gateway.
Type: String
Required: No

 ** associationId **
[Public NAT gateway only] The association ID of the Elastic IP address that's associated with the NAT gateway.
Type: String
Required: No

 ** availabilityZone **
The Availability Zone where this Elastic IP address (EIP) is being used to handle outbound NAT traffic.
Type: String
Required: No

 ** availabilityZoneId **
The ID of the Availability Zone where this Elastic IP address (EIP) is being used to handle outbound NAT traffic. Use this instead of AvailabilityZone for consistent identification of AZs across AWS Regions.
Type: String
Required: No

 ** failureMessage **
The address failure message.
Type: String
Required: No

 ** isPrimary **
Defines if the IP address is the primary address.
Type: Boolean
Required: No

 ** networkInterfaceId **
The ID of the network interface associated with the NAT gateway.
Type: String
Required: No

 ** privateIp **
The private IP address associated with the NAT gateway.
Type: String
Required: No

 ** publicIp **
[Public NAT gateway only] The Elastic IP address associated with the NAT gateway.
Type: String
Required: No

 ** status **
The address status.
Type: String
Valid Values: `assigning | unassigning | associating | disassociating | succeeded | failed`
Required: No

## See Also
<a name="API_NatGatewayAddress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/NatGatewayAddress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/NatGatewayAddress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/NatGatewayAddress)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
