---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyIpamResourceDiscovery.html
---

# ModifyIpamResourceDiscovery
<a name="API_ModifyIpamResourceDiscovery"></a>

Modifies a resource discovery. A resource discovery is an IPAM component that enables IPAM to manage and monitor resources that belong to the owning account.

## Request Parameters
<a name="API_ModifyIpamResourceDiscovery_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AddOperatingRegion.N**
Add operating Regions to the resource discovery. Operating Regions are AWS Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the AWS Regions you select as operating Regions.
Type: Array of [AddIpamOperatingRegion](API_AddIpamOperatingRegion.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 **AddOrganizationalUnitExclusion.N**
Add an Organizational Unit (OU) exclusion to your IPAM. If your IPAM is integrated with AWS Organizations and you add an organizational unit (OU) exclusion, IPAM will not manage the IP addresses in accounts in that OU exclusion. There is a limit on the number of exclusions you can create. For more information, see [Quotas for your IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html) in the *Amazon VPC IPAM User Guide*.
The resulting set of exclusions must not result in "overlap", meaning two or more OU exclusions must not exclude the same OU. For more information and examples, see the AWS CLI request process in [Add or remove OU exclusions ](https://docs.aws.amazon.com/vpc/latest/ipam/exclude-ous.html#exclude-ous-create-delete) in the *Amazon VPC User Guide*.
Type: Array of [AddIpamOrganizationalUnitExclusion](API_AddIpamOrganizationalUnitExclusion.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 **Description**
A resource discovery description.
Type: String
Required: No

 **DryRun**
A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **IpamResourceDiscoveryId**
A resource discovery ID.
Type: String
Required: Yes

 **RemoveOperatingRegion.N**
Remove operating Regions.
Type: Array of [RemoveIpamOperatingRegion](API_RemoveIpamOperatingRegion.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 **RemoveOrganizationalUnitExclusion.N**
Remove an Organizational Unit (OU) exclusion to your IPAM. If your IPAM is integrated with AWS Organizations and you add an organizational unit (OU) exclusion, IPAM will not manage the IP addresses in accounts in that OU exclusion. There is a limit on the number of exclusions you can create. For more information, see [Quotas for your IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html) in the *Amazon VPC IPAM User Guide*.
The resulting set of exclusions must not result in "overlap", meaning two or more OU exclusions must not exclude the same OU. For more information and examples, see the AWS CLI request process in [Add or remove OU exclusions ](https://docs.aws.amazon.com/vpc/latest/ipam/exclude-ous.html#exclude-ous-create-delete) in the *Amazon VPC User Guide*.
Type: Array of [RemoveIpamOrganizationalUnitExclusion](API_RemoveIpamOrganizationalUnitExclusion.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## Response Elements
<a name="API_ModifyIpamResourceDiscovery_ResponseElements"></a>

The following elements are returned by the service.

 **ipamResourceDiscovery**
A resource discovery.
Type: [IpamResourceDiscovery](API_IpamResourceDiscovery.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_ModifyIpamResourceDiscovery_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ModifyIpamResourceDiscovery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyIpamResourceDiscovery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyIpamResourceDiscovery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyIpamResourceDiscovery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyIpamResourceDiscovery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyIpamResourceDiscovery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyIpamResourceDiscovery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyIpamResourceDiscovery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyIpamResourceDiscovery)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyIpamResourceDiscovery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyIpamResourceDiscovery)
