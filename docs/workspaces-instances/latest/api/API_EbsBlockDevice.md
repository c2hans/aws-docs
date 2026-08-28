---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_EbsBlockDevice.html
---

# EbsBlockDevice
<a name="API_EbsBlockDevice"></a>

Defines configuration for an Elastic Block Store volume.

## Contents
<a name="API_EbsBlockDevice_Contents"></a>

 ** Encrypted **   <a name="workspacesinstances-Type-EbsBlockDevice-Encrypted"></a>
Indicates if the volume is encrypted.
Type: Boolean
Required: No

 ** Iops **   <a name="workspacesinstances-Type-EbsBlockDevice-Iops"></a>
Input/output operations per second for the volume.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** KmsKeyId **   <a name="workspacesinstances-Type-EbsBlockDevice-KmsKeyId"></a>
KMS key used for volume encryption.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** Throughput **   <a name="workspacesinstances-Type-EbsBlockDevice-Throughput"></a>
Volume data transfer rate.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** VolumeSize **   <a name="workspacesinstances-Type-EbsBlockDevice-VolumeSize"></a>
Size of the EBS volume in gigabytes.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** VolumeType **   <a name="workspacesinstances-Type-EbsBlockDevice-VolumeType"></a>
Type of EBS volume (e.g., gp2, io1).
Type: String
Valid Values: `standard | io1 | io2 | gp2 | sc1 | st1 | gp3`
Required: No

## See Also
<a name="API_EbsBlockDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/EbsBlockDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/EbsBlockDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/EbsBlockDevice)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for WorkSpaces Instances. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-instances` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
