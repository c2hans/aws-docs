---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_VpcInfoPeeringOptionsDetails.html
---

# VpcInfoPeeringOptionsDetails
<a name="API_VpcInfoPeeringOptionsDetails"></a>

Provides information about the VPC peering connection options for the accepter or requester VPC.

## Contents
<a name="API_VpcInfoPeeringOptionsDetails_Contents"></a>

 ** AllowDnsResolutionFromRemoteVpc **   <a name="securityhub-Type-VpcInfoPeeringOptionsDetails-AllowDnsResolutionFromRemoteVpc"></a>
Indicates whether a local VPC can resolve public DNS hostnames to private IP addresses when queried from instances in a peer VPC.
Type: Boolean
Required: No

 ** AllowEgressFromLocalClassicLinkToRemoteVpc **   <a name="securityhub-Type-VpcInfoPeeringOptionsDetails-AllowEgressFromLocalClassicLinkToRemoteVpc"></a>
Indicates whether a local ClassicLink connection can communicate with the peer VPC over the VPC peering connection.
Type: Boolean
Required: No

 ** AllowEgressFromLocalVpcToRemoteClassicLink **   <a name="securityhub-Type-VpcInfoPeeringOptionsDetails-AllowEgressFromLocalVpcToRemoteClassicLink"></a>
Indicates whether a local VPC can communicate with a ClassicLink connection in the peer VPC over the VPC peering connection.
Type: Boolean
Required: No

## See Also
<a name="API_VpcInfoPeeringOptionsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/VpcInfoPeeringOptionsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/VpcInfoPeeringOptionsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/VpcInfoPeeringOptionsDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
