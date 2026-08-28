---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamResourceDiscovery.html
---

# IpamResourceDiscovery
<a name="API_IpamResourceDiscovery"></a>

A resource discovery is an IPAM component that enables IPAM to manage and monitor resources that belong to the owning account.

## Contents
<a name="API_IpamResourceDiscovery_Contents"></a>

 ** description **
The resource discovery description.
Type: String
Required: No

 ** ipamResourceDiscoveryArn **
The resource discovery Amazon Resource Name (ARN).
Type: String
Required: No

 ** ipamResourceDiscoveryId **
The resource discovery ID.
Type: String
Required: No

 ** ipamResourceDiscoveryRegion **
The resource discovery Region.
Type: String
Required: No

 ** isDefault **
Defines if the resource discovery is the default. The default resource discovery is the resource discovery automatically created when you create an IPAM.
Type: Boolean
Required: No

 ** OperatingRegionSet.N **
The operating Regions for the resource discovery. Operating Regions are AWS Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the AWS Regions you select as operating Regions.
Type: Array of [IpamOperatingRegion](API_IpamOperatingRegion.md) objects
Required: No

 ** OrganizationalUnitExclusionSet.N **
If your IPAM is integrated with AWS Organizations and you add an organizational unit (OU) exclusion, IPAM will not manage the IP addresses in accounts in that OU exclusion.
Type: Array of [IpamOrganizationalUnitExclusion](API_IpamOrganizationalUnitExclusion.md) objects
Required: No

 ** ownerId **
The ID of the owner.
Type: String
Required: No

 ** state **
The lifecycle state of the resource discovery.
+  `create-in-progress` - Resource discovery is being created.
+  `create-complete` - Resource discovery creation is complete.
+  `create-failed` - Resource discovery creation has failed.
+  `modify-in-progress` - Resource discovery is being modified.
+  `modify-complete` - Resource discovery modification is complete.
+  `modify-failed` - Resource discovery modification has failed.
+  `delete-in-progress` - Resource discovery is being deleted.
+  `delete-complete` - Resource discovery deletion is complete.
+  `delete-failed` - Resource discovery deletion has failed.
+  `isolate-in-progress` - AWS account that created the resource discovery has been removed and the resource discovery is being isolated.
+  `isolate-complete` - Resource discovery isolation is complete.
+  `restore-in-progress` - AWS account that created the resource discovery and was isolated has been restored.
Type: String
Valid Values: `create-in-progress | create-complete | create-failed | modify-in-progress | modify-complete | modify-failed | delete-in-progress | delete-complete | delete-failed | isolate-in-progress | isolate-complete | restore-in-progress`
Required: No

 ** TagSet.N **
A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your AWS costs.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_IpamResourceDiscovery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamResourceDiscovery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamResourceDiscovery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamResourceDiscovery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
