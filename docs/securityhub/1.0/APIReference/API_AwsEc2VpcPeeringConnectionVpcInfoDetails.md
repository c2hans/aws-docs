---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2VpcPeeringConnectionVpcInfoDetails.html
---

# AwsEc2VpcPeeringConnectionVpcInfoDetails
<a name="API_AwsEc2VpcPeeringConnectionVpcInfoDetails"></a>

Describes a VPC in a VPC peering connection.

## Contents
<a name="API_AwsEc2VpcPeeringConnectionVpcInfoDetails_Contents"></a>

 ** CidrBlock **   <a name="securityhub-Type-AwsEc2VpcPeeringConnectionVpcInfoDetails-CidrBlock"></a>
The IPv4 CIDR block for the VPC.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CidrBlockSet **   <a name="securityhub-Type-AwsEc2VpcPeeringConnectionVpcInfoDetails-CidrBlockSet"></a>
Information about the IPv4 CIDR blocks for the VPC.
Type: Array of [VpcInfoCidrBlockSetDetails](API_VpcInfoCidrBlockSetDetails.md) objects
Required: No

 ** Ipv6CidrBlockSet **   <a name="securityhub-Type-AwsEc2VpcPeeringConnectionVpcInfoDetails-Ipv6CidrBlockSet"></a>
The IPv6 CIDR block for the VPC.
Type: Array of [VpcInfoIpv6CidrBlockSetDetails](API_VpcInfoIpv6CidrBlockSetDetails.md) objects
Required: No

 ** OwnerId **   <a name="securityhub-Type-AwsEc2VpcPeeringConnectionVpcInfoDetails-OwnerId"></a>
The ID of the AWS account that owns the VPC.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PeeringOptions **   <a name="securityhub-Type-AwsEc2VpcPeeringConnectionVpcInfoDetails-PeeringOptions"></a>
Information about the VPC peering connection options for the accepter or requester VPC.
Type: [VpcInfoPeeringOptionsDetails](API_VpcInfoPeeringOptionsDetails.md) object
Required: No

 ** Region **   <a name="securityhub-Type-AwsEc2VpcPeeringConnectionVpcInfoDetails-Region"></a>
The AWS Region in which the VPC is located.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VpcId **   <a name="securityhub-Type-AwsEc2VpcPeeringConnectionVpcInfoDetails-VpcId"></a>
The ID of the VPC.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2VpcPeeringConnectionVpcInfoDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2VpcPeeringConnectionVpcInfoDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2VpcPeeringConnectionVpcInfoDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2VpcPeeringConnectionVpcInfoDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
