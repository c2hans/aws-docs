---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AddIpamOrganizationalUnitExclusion.html
---

# AddIpamOrganizationalUnitExclusion
<a name="API_AddIpamOrganizationalUnitExclusion"></a>

Add an Organizational Unit (OU) exclusion to your IPAM. If your IPAM is integrated with AWS Organizations and you add an organizational unit (OU) exclusion, IPAM will not manage the IP addresses in accounts in that OU exclusion. There is a limit on the number of exclusions you can create. For more information, see [Quotas for your IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html) in the *Amazon VPC IPAM User Guide*.

## Contents
<a name="API_AddIpamOrganizationalUnitExclusion_Contents"></a>

 ** OrganizationsEntityPath **
An AWS Organizations entity path. Build the path for the OU(s) using AWS Organizations IDs separated by a `/`. Include all child OUs by ending the path with `/*`.
+ Example 1
  + Path to a child OU: `o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-ghi0-awsccccc/ou-jkl0-awsddddd/`
  + In this example, `o-a1b2c3d4e5` is the organization ID, `r-f6g7h8i9j0example` is the root ID , `ou-ghi0-awsccccc` is an OU ID, and `ou-jkl0-awsddddd` is a child OU ID.
  + IPAM will not manage the IP addresses in accounts in the child OU.
+ Example 2
  + Path where all child OUs will be part of the exclusion: `o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-ghi0-awsccccc/*`
  + In this example, IPAM will not manage the IP addresses in accounts in the OU (`ou-ghi0-awsccccc`) or in accounts in any OUs that are children of the OU.
For more information on how to construct an entity path, see [Understand the AWS Organizations entity path](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed-view-data-orgs.html#access_policies_access-advisor-viewing-orgs-entity-path) in the * AWS Identity and Access Management User Guide*.
Type: String
Required: No

## See Also
<a name="API_AddIpamOrganizationalUnitExclusion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AddIpamOrganizationalUnitExclusion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AddIpamOrganizationalUnitExclusion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AddIpamOrganizationalUnitExclusion)
