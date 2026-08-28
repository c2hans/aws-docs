---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2VpcPeeringConnectionDetails.html
---

# AwsEc2VpcPeeringConnectionDetails
<a name="API_AwsEc2VpcPeeringConnectionDetails"></a>

Provides information about a VPC peering connection between two VPCs: a requester VPC that you own and an accepter VPC with which to create the connection.

## Contents
<a name="API_AwsEc2VpcPeeringConnectionDetails_Contents"></a>

 ** AccepterVpcInfo **   <a name="securityhub-Type-AwsEc2VpcPeeringConnectionDetails-AccepterVpcInfo"></a>
Information about the accepter VPC.
Type: [AwsEc2VpcPeeringConnectionVpcInfoDetails](API_AwsEc2VpcPeeringConnectionVpcInfoDetails.md) object
Required: No

 ** ExpirationTime **   <a name="securityhub-Type-AwsEc2VpcPeeringConnectionDetails-ExpirationTime"></a>
The time at which an unaccepted VPC peering connection will expire.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RequesterVpcInfo **   <a name="securityhub-Type-AwsEc2VpcPeeringConnectionDetails-RequesterVpcInfo"></a>
Information about the requester VPC.
Type: [AwsEc2VpcPeeringConnectionVpcInfoDetails](API_AwsEc2VpcPeeringConnectionVpcInfoDetails.md) object
Required: No

 ** Status **   <a name="securityhub-Type-AwsEc2VpcPeeringConnectionDetails-Status"></a>
The status of the VPC peering connection.
Type: [AwsEc2VpcPeeringConnectionStatusDetails](API_AwsEc2VpcPeeringConnectionStatusDetails.md) object
Required: No

 ** VpcPeeringConnectionId **   <a name="securityhub-Type-AwsEc2VpcPeeringConnectionDetails-VpcPeeringConnectionId"></a>
The ID of the VPC peering connection.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2VpcPeeringConnectionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2VpcPeeringConnectionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2VpcPeeringConnectionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2VpcPeeringConnectionDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
