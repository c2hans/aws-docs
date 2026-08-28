---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_NetworkInterfaceAssociation.html
---

# NetworkInterfaceAssociation
<a name="API_NetworkInterfaceAssociation"></a>

Describes association information for an Elastic IP address (IPv4 only), or a Carrier IP address (for a network interface which resides in a subnet in a Wavelength Zone).

## Contents
<a name="API_NetworkInterfaceAssociation_Contents"></a>

 ** allocationId **
The allocation ID.
Type: String
Required: No

 ** associationId **
The association ID.
Type: String
Required: No

 ** carrierIp **
The carrier IP address associated with the network interface.
This option is only available when the network interface is in a subnet which is associated with a Wavelength Zone.
Type: String
Required: No

 ** customerOwnedIp **
The customer-owned IP address associated with the network interface.
Type: String
Required: No

 ** ipOwnerId **
The ID of the Elastic IP address owner.
Type: String
Required: No

 ** publicDnsName **
The public DNS name.
Type: String
Required: No

 ** publicIp **
The address of the Elastic IP address bound to the network interface.
Type: String
Required: No

## See Also
<a name="API_NetworkInterfaceAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/NetworkInterfaceAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/NetworkInterfaceAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/NetworkInterfaceAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
