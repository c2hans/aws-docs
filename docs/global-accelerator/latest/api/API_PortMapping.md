---
source_url: https://docs.aws.amazon.com/global-accelerator/latest/api/API_PortMapping.html
---

# PortMapping
<a name="API_PortMapping"></a>

Returns the ports and associated IP addresses and ports of Amazon EC2 instances in your virtual private cloud (VPC) subnets. Custom routing is a port mapping protocol in AWS Global Accelerator that statically associates port ranges with VPC subnets, which allows Global Accelerator to route to specific instances and ports within one or more subnets.

## Contents
<a name="API_PortMapping_Contents"></a>

 ** AcceleratorPort **   <a name="globalaccelerator-Type-PortMapping-AcceleratorPort"></a>
The accelerator port.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** DestinationSocketAddress **   <a name="globalaccelerator-Type-PortMapping-DestinationSocketAddress"></a>
The EC2 instance IP address and port number in the virtual private cloud (VPC) subnet.
Type: [SocketAddress](API_SocketAddress.md) object
Required: No

 ** DestinationTrafficState **   <a name="globalaccelerator-Type-PortMapping-DestinationTrafficState"></a>
Indicates whether or not a port mapping destination can receive traffic. The value is either ALLOW, if traffic is allowed to the destination, or DENY, if traffic is not allowed to the destination.
Type: String
Valid Values: `ALLOW | DENY`
Required: No

 ** EndpointGroupArn **   <a name="globalaccelerator-Type-PortMapping-EndpointGroupArn"></a>
The Amazon Resource Name (ARN) of the endpoint group.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** EndpointId **   <a name="globalaccelerator-Type-PortMapping-EndpointId"></a>
The IP address of the VPC subnet (the subnet ID).
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** Protocols **   <a name="globalaccelerator-Type-PortMapping-Protocols"></a>
The protocols supported by the endpoint group.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `TCP | UDP`
Required: No

## See Also
<a name="API_PortMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/PortMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/PortMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/PortMapping)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query global-accelerator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
