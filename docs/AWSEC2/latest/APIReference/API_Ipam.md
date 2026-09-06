---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Ipam.html
---

# Ipam
<a name="API_Ipam"></a>

IPAM is a VPC feature that you can use to automate your IP address management workflows including assigning, tracking, troubleshooting, and auditing IP addresses across AWS Regions and accounts throughout your AWS Organization. For more information, see [What is IPAM?](https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html) in the *Amazon VPC IPAM User Guide*.

## Contents
<a name="API_Ipam_Contents"></a>

 ** defaultResourceDiscoveryAssociationId **
The IPAM's default resource discovery association ID.
Type: String
Required: No

 ** defaultResourceDiscoveryId **
The IPAM's default resource discovery ID.
Type: String
Required: No

 ** description **
The description for the IPAM.
Type: String
Required: No

 ** enablePrivateGua **
Enable this option to use your own GUA ranges as private IPv6 addresses. This option is disabled by default.
Type: Boolean
Required: No

 ** ipamArn **
The Amazon Resource Name (ARN) of the IPAM.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** ipamId **
The ID of the IPAM.
Type: String
Required: No

 ** ipamRegion **
The AWS Region of the IPAM.
Type: String
Required: No

 ** meteredAccount **
A metered account is an AWS account that is charged for active IP addresses managed in IPAM. For more information, see [Enable cost distribution](https://docs.aws.amazon.com/vpc/latest/ipam/ipam-enable-cost-distro.html) in the *Amazon VPC IPAM User Guide*.
Possible values:
+  `ipam-owner` (default): The AWS account which owns the IPAM is charged for all active IP addresses managed in IPAM.
+  `resource-owner`: The AWS account that owns the IP address is charged for the active IP address.
Type: String
Valid Values: `ipam-owner | resource-owner`
Required: No

 ** OperatingRegionSet.N **
The operating Regions for an IPAM. Operating Regions are AWS Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the AWS Regions you select as operating Regions.
For more information about operating Regions, see [Create an IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/create-ipam.html) in the *Amazon VPC IPAM User Guide*.
Type: Array of [IpamOperatingRegion](API_IpamOperatingRegion.md) objects
Required: No

 ** ownerId **
The AWS account ID of the owner of the IPAM.
Type: String
Required: No

 ** privateDefaultScopeId **
The ID of the IPAM's default private scope.
Type: String
Required: No

 ** publicDefaultScopeId **
The ID of the IPAM's default public scope.
Type: String
Required: No

 ** resourceDiscoveryAssociationCount **
The IPAM's resource discovery association count.
Type: Integer
Required: No

 ** scopeCount **
The number of scopes in the IPAM. The scope quota is 5. For more information on quotas, see [Quotas in IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html) in the *Amazon VPC IPAM User Guide*.
Type: Integer
Required: No

 ** state **
The state of the IPAM.
Type: String
Valid Values: `create-in-progress | create-complete | create-failed | modify-in-progress | modify-complete | modify-failed | delete-in-progress | delete-complete | delete-failed | isolate-in-progress | isolate-complete | restore-in-progress`
Required: No

 ** stateMessage **
The state message.
Type: String
Required: No

 ** TagSet.N **
The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** tier **
IPAM is offered in a Free Tier and an Advanced Tier. For more information about the features available in each tier and the costs associated with the tiers, see [Amazon VPC pricing > IPAM tab](http://aws.amazon.com/vpc/pricing/).
Type: String
Valid Values: `free | advanced`
Required: No

## See Also
<a name="API_Ipam_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/Ipam)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/Ipam)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/Ipam)
