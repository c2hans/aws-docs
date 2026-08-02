---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpcBlockPublicAccessExclusion.html
---

# VpcBlockPublicAccessExclusion
<a name="API_VpcBlockPublicAccessExclusion"></a>

A VPC BPA exclusion is a mode that can be applied to a single VPC or subnet that exempts it from the account’s BPA mode and will allow bidirectional or egress-only access. You can create BPA exclusions for VPCs and subnets even when BPA is not enabled on the account to ensure that there is no traffic disruption to the exclusions when VPC BPA is turned on. To learn more about VPC BPA, see [Block public access to VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html) in the *Amazon VPC User Guide*.

## Contents
<a name="API_VpcBlockPublicAccessExclusion_Contents"></a>

 ** creationTimestamp **
When the exclusion was created.
Type: Timestamp
Required: No

 ** deletionTimestamp **
When the exclusion was deleted.
Type: Timestamp
Required: No

 ** exclusionId **
The ID of the exclusion.
Type: String
Required: No

 ** internetGatewayExclusionMode **
The exclusion mode for internet gateway traffic.
+  `allow-bidirectional`: Allow all internet traffic to and from the excluded VPCs and subnets.
+  `allow-egress`: Allow outbound internet traffic from the excluded VPCs and subnets. Block inbound internet traffic to the excluded VPCs and subnets. Only applies when VPC Block Public Access is set to Bidirectional.
Type: String
Valid Values: `allow-bidirectional | allow-egress`
Required: No

 ** lastUpdateTimestamp **
When the exclusion was last updated.
Type: Timestamp
Required: No

 ** reason **
The reason for the current exclusion state.
Type: String
Required: No

 ** resourceArn **
The ARN of the exclusion.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** state **
The state of the exclusion.
Type: String
Valid Values: `create-in-progress | create-complete | create-failed | update-in-progress | update-complete | update-failed | delete-in-progress | delete-complete | disable-in-progress | disable-complete`
Required: No

 ** TagSet.N **
 `tag` - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_VpcBlockPublicAccessExclusion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VpcBlockPublicAccessExclusion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VpcBlockPublicAccessExclusion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VpcBlockPublicAccessExclusion)
