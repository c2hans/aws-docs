---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstanceVolumeDetailItem.html
---

# ImportInstanceVolumeDetailItem
<a name="API_ImportInstanceVolumeDetailItem"></a>

Describes an import volume task.

## Contents
<a name="API_ImportInstanceVolumeDetailItem_Contents"></a>

 ** availabilityZone **
The Availability Zone where the resulting instance will reside.
Type: String
Required: No

 ** availabilityZoneId **
The ID of the Availability Zone where the resulting instance will reside.
Type: String
Required: No

 ** bytesConverted **
The number of bytes converted so far.
Type: Long
Required: No

 ** description **
A description of the task.
Type: String
Required: No

 ** image **
The image.
Type: [DiskImageDescription](API_DiskImageDescription.md) object
Required: No

 ** status **
The status of the import of this particular disk image.
Type: String
Required: No

 ** statusMessage **
The status information or errors related to the disk image.
Type: String
Required: No

 ** volume **
The volume.
Type: [DiskImageVolumeDescription](API_DiskImageVolumeDescription.md) object
Required: No

## See Also
<a name="API_ImportInstanceVolumeDetailItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ImportInstanceVolumeDetailItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ImportInstanceVolumeDetailItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ImportInstanceVolumeDetailItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
