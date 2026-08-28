---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2SubnetDetails.html
---

# AwsEc2SubnetDetails
<a name="API_AwsEc2SubnetDetails"></a>

Contains information about a subnet in Amazon EC2.

## Contents
<a name="API_AwsEc2SubnetDetails_Contents"></a>

 ** AssignIpv6AddressOnCreation **   <a name="securityhub-Type-AwsEc2SubnetDetails-AssignIpv6AddressOnCreation"></a>
Whether to assign an IPV6 address to a network interface that is created in this subnet.
Type: Boolean
Required: No

 ** AvailabilityZone **   <a name="securityhub-Type-AwsEc2SubnetDetails-AvailabilityZone"></a>
The Availability Zone for the subnet.
Type: String
Pattern: `.*\S.*`
Required: No

 ** AvailabilityZoneId **   <a name="securityhub-Type-AwsEc2SubnetDetails-AvailabilityZoneId"></a>
The identifier of the Availability Zone for the subnet.
Type: String
Pattern: `.*\S.*`
Required: No

 ** AvailableIpAddressCount **   <a name="securityhub-Type-AwsEc2SubnetDetails-AvailableIpAddressCount"></a>
The number of available IPV4 addresses in the subnet. Does not include addresses for stopped instances.
Type: Integer
Required: No

 ** CidrBlock **   <a name="securityhub-Type-AwsEc2SubnetDetails-CidrBlock"></a>
The IPV4 CIDR block that is assigned to the subnet.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DefaultForAz **   <a name="securityhub-Type-AwsEc2SubnetDetails-DefaultForAz"></a>
Whether this subnet is the default subnet for the Availability Zone.
Type: Boolean
Required: No

 ** Ipv6CidrBlockAssociationSet **   <a name="securityhub-Type-AwsEc2SubnetDetails-Ipv6CidrBlockAssociationSet"></a>
The IPV6 CIDR blocks that are associated with the subnet.
Type: Array of [Ipv6CidrBlockAssociation](API_Ipv6CidrBlockAssociation.md) objects
Required: No

 ** MapPublicIpOnLaunch **   <a name="securityhub-Type-AwsEc2SubnetDetails-MapPublicIpOnLaunch"></a>
Whether instances in this subnet receive a public IP address.
Type: Boolean
Required: No

 ** OwnerId **   <a name="securityhub-Type-AwsEc2SubnetDetails-OwnerId"></a>
The identifier of the AWS account that owns the subnet.
Type: String
Pattern: `.*\S.*`
Required: No

 ** State **   <a name="securityhub-Type-AwsEc2SubnetDetails-State"></a>
The current state of the subnet. Valid values are `available` or `pending`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SubnetArn **   <a name="securityhub-Type-AwsEc2SubnetDetails-SubnetArn"></a>
The ARN of the subnet.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SubnetId **   <a name="securityhub-Type-AwsEc2SubnetDetails-SubnetId"></a>
The identifier of the subnet.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VpcId **   <a name="securityhub-Type-AwsEc2SubnetDetails-VpcId"></a>
The identifier of the VPC that contains the subnet.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2SubnetDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2SubnetDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2SubnetDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2SubnetDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
