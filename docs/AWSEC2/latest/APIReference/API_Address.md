---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Address.html
---

# Address
<a name="API_Address"></a>

Describes an Elastic IP address, or a carrier IP address.

## Contents
<a name="API_Address_Contents"></a>

 ** allocationId **
The ID representing the allocation of the address.
Type: String
Required: No

 ** associationId **
The ID representing the association of the address with an instance.
Type: String
Required: No

 ** carrierIp **
The carrier IP address associated. This option is only available for network interfaces which reside in a subnet in a Wavelength Zone (for example an EC2 instance).
Type: String
Required: No

 ** customerOwnedIp **
The customer-owned IP address.
Type: String
Required: No

 ** customerOwnedIpv4Pool **
The ID of the customer-owned address pool.
Type: String
Required: No

 ** domain **
The network (`vpc`).
Type: String
Valid Values: `vpc | standard`
Required: No

 ** instanceId **
The ID of the instance that the address is associated with (if any).
Type: String
Required: No

 ** networkBorderGroup **
The name of the unique set of Availability Zones, Local Zones, or Wavelength Zones from which AWS advertises IP addresses.
Type: String
Required: No

 ** networkInterfaceId **
The ID of the network interface.
Type: String
Required: No

 ** networkInterfaceOwnerId **
The ID of the AWS account that owns the network interface.
Type: String
Required: No

 ** privateIpAddress **
The private IP address associated with the Elastic IP address.
Type: String
Required: No

 ** publicIp **
The Elastic IP address.
Type: String
Required: No

 ** publicIpv4Pool **
The ID of an address pool.
Type: String
Required: No

 ** serviceManaged **
The service that manages the elastic IP address.
The only option supported today is `alb`.
Type: String
Valid Values: `alb | nlb | rnat | rds`
Required: No

 ** subnetId **
The ID of the subnet where the IP address is allocated.
Type: String
Required: No

 ** TagSet.N **
Any tags assigned to the Elastic IP address.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_Address_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/Address)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/Address)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/Address)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
