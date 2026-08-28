---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_S3ExportConfiguration.html
---

# S3ExportConfiguration
<a name="API_S3ExportConfiguration"></a>

Properties that configure export from your build instance to a compatible file format for your VM.

## Contents
<a name="API_S3ExportConfiguration_Contents"></a>

 ** diskImageFormat **   <a name="imagebuilder-Type-S3ExportConfiguration-diskImageFormat"></a>
Export the updated image to one of the following supported disk image formats:
+  **Virtual Hard Disk (VHD)** – Compatible with Citrix Xen and Microsoft Hyper-V virtualization products.
+  **Stream-optimized ESX Virtual Machine Disk (VMDK)** – Compatible with VMware ESX and VMware vSphere versions 4, 5, and 6.
+  **Raw** – Raw format.
Type: String
Valid Values: `VMDK | RAW | VHD`
Required: Yes

 ** roleName **   <a name="imagebuilder-Type-S3ExportConfiguration-roleName"></a>
The name of the role that grants VM Import/Export permission to export images to your S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** s3Bucket **   <a name="imagebuilder-Type-S3ExportConfiguration-s3Bucket"></a>
The S3 bucket in which to store the output disk images for your VM.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** s3Prefix **   <a name="imagebuilder-Type-S3ExportConfiguration-s3Prefix"></a>
The Amazon S3 path for the bucket where the output disk images for your VM are stored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_S3ExportConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/S3ExportConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/S3ExportConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/S3ExportConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
