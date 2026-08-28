---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportImageTask.html
---

# ImportImageTask
<a name="API_ImportImageTask"></a>

Describes an import image task.

## Contents
<a name="API_ImportImageTask_Contents"></a>

 ** architecture **
The architecture of the virtual machine.
Valid values: `i386` \| `x86_64` \| `arm64`
Type: String
Required: No

 ** bootMode **
The boot mode of the virtual machine.
Type: String
Valid Values: `legacy-bios | uefi | uefi-preferred`
Required: No

 ** description **
A description of the import task.
Type: String
Required: No

 ** encrypted **
Indicates whether the image is encrypted.
Type: Boolean
Required: No

 ** hypervisor **
The target hypervisor for the import task.
Valid values: `xen`
Type: String
Required: No

 ** imageId **
The ID of the Amazon Machine Image (AMI) of the imported virtual machine.
Type: String
Required: No

 ** importTaskId **
The ID of the import image task.
Type: String
Required: No

 ** kmsKeyId **
The identifier for the KMS key that was used to create the encrypted image.
Type: String
Required: No

 ** LicenseSpecifications.N **
The ARNs of the license configurations that are associated with the import image task.
Type: Array of [ImportImageLicenseConfigurationResponse](API_ImportImageLicenseConfigurationResponse.md) objects
Required: No

 ** licenseType **
The license type of the virtual machine.
Type: String
Required: No

 ** platform **
The description string for the import image task.
Type: String
Required: No

 ** progress **
The percentage of progress of the import image task.
Type: String
Required: No

 ** SnapshotDetailSet.N **
Information about the snapshots.
Type: Array of [SnapshotDetail](API_SnapshotDetail.md) objects
Required: No

 ** status **
A brief status for the import image task.
Type: String
Required: No

 ** statusMessage **
A descriptive status message for the import image task.
Type: String
Required: No

 ** TagSet.N **
The tags for the import image task.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** usageOperation **
The usage operation value.
Type: String
Required: No

## See Also
<a name="API_ImportImageTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ImportImageTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ImportImageTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ImportImageTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
