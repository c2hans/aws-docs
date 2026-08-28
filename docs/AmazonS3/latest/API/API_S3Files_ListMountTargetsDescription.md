---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Files_ListMountTargetsDescription.html
---

# ListMountTargetsDescription
<a name="API_S3Files_ListMountTargetsDescription"></a>

Contains information about a mount target returned in list operations.

## Contents
<a name="API_S3Files_ListMountTargetsDescription_Contents"></a>

 ** mountTargetId **   <a name="AmazonS3-Type-S3Files_ListMountTargetsDescription-mountTargetId"></a>
The ID of the mount target.
Type: String
Length Constraints: Minimum length of 22. Maximum length of 45.
Pattern: `fsmt-[0-9a-f]{17,40}`
Required: Yes

 ** ownerId **   <a name="AmazonS3-Type-S3Files_ListMountTargetsDescription-ownerId"></a>
The AWS account ID of the mount target owner.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 12.
Pattern: `(\d{12})|(\d{4}-{4}-\d{4})`
Required: Yes

 ** subnetId **   <a name="AmazonS3-Type-S3Files_ListMountTargetsDescription-subnetId"></a>
The ID of the subnet where the mount target is located.
Type: String
Length Constraints: Minimum length of 15. Maximum length of 47.
Pattern: `subnet-[0-9a-f]{8,40}`
Required: Yes

 ** availabilityZoneId **   <a name="AmazonS3-Type-S3Files_ListMountTargetsDescription-availabilityZoneId"></a>
The Availability Zone ID where the mount target is located.
Type: String
Required: No

 ** fileSystemId **   <a name="AmazonS3-Type-S3Files_ListMountTargetsDescription-fileSystemId"></a>
The ID of the S3 File System.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `(arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}|fs-[0-9a-f]{17,40})`
Required: No

 ** ipv4Address **   <a name="AmazonS3-Type-S3Files_ListMountTargetsDescription-ipv4Address"></a>
The IPv4 address of the mount target.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 15.
Pattern: `[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}`
Required: No

 ** ipv6Address **   <a name="AmazonS3-Type-S3Files_ListMountTargetsDescription-ipv6Address"></a>
The IPv6 address of the mount target.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 39.
Required: No

 ** networkInterfaceId **   <a name="AmazonS3-Type-S3Files_ListMountTargetsDescription-networkInterfaceId"></a>
The ID of the network interface associated with the mount target.
Type: String
Required: No

 ** status **   <a name="AmazonS3-Type-S3Files_ListMountTargetsDescription-status"></a>
The current status of the mount target.
Type: String
Valid Values: `available | creating | deleting | deleted | error | updating`
Required: No

 ** statusMessage **   <a name="AmazonS3-Type-S3Files_ListMountTargetsDescription-statusMessage"></a>
Additional information about the mount target status.
Type: String
Required: No

 ** vpcId **   <a name="AmazonS3-Type-S3Files_ListMountTargetsDescription-vpcId"></a>
The ID of the VPC where the mount target is located.
Type: String
Required: No

## See Also
<a name="API_S3Files_ListMountTargetsDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3files-2025-05-05/ListMountTargetsDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3files-2025-05-05/ListMountTargetsDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3files-2025-05-05/ListMountTargetsDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
