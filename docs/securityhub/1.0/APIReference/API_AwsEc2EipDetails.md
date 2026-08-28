---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2EipDetails.html
---

# AwsEc2EipDetails
<a name="API_AwsEc2EipDetails"></a>

Information about an Elastic IP address.

## Contents
<a name="API_AwsEc2EipDetails_Contents"></a>

 ** AllocationId **   <a name="securityhub-Type-AwsEc2EipDetails-AllocationId"></a>
The identifier that AWS assigns to represent the allocation of the Elastic IP address for use with Amazon VPC.
Type: String
Pattern: `.*\S.*`
Required: No

 ** AssociationId **   <a name="securityhub-Type-AwsEc2EipDetails-AssociationId"></a>
The identifier that represents the association of the Elastic IP address with an EC2 instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Domain **   <a name="securityhub-Type-AwsEc2EipDetails-Domain"></a>
The domain in which to allocate the address.
If the address is for use with EC2 instances in a VPC, then `Domain` is `vpc`. Otherwise, `Domain` is `standard`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** InstanceId **   <a name="securityhub-Type-AwsEc2EipDetails-InstanceId"></a>
The identifier of the EC2 instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NetworkBorderGroup **   <a name="securityhub-Type-AwsEc2EipDetails-NetworkBorderGroup"></a>
The name of the location from which the Elastic IP address is advertised.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NetworkInterfaceId **   <a name="securityhub-Type-AwsEc2EipDetails-NetworkInterfaceId"></a>
The identifier of the network interface.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NetworkInterfaceOwnerId **   <a name="securityhub-Type-AwsEc2EipDetails-NetworkInterfaceOwnerId"></a>
The AWS account ID of the owner of the network interface.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PrivateIpAddress **   <a name="securityhub-Type-AwsEc2EipDetails-PrivateIpAddress"></a>
The private IP address that is associated with the Elastic IP address.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PublicIp **   <a name="securityhub-Type-AwsEc2EipDetails-PublicIp"></a>
A public IP address that is associated with the EC2 instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PublicIpv4Pool **   <a name="securityhub-Type-AwsEc2EipDetails-PublicIpv4Pool"></a>
The identifier of an IP address pool. This parameter allows Amazon EC2 to select an IP address from the address pool.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2EipDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2EipDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2EipDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2EipDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
