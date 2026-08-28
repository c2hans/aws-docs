---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_PersistentVolumeConfiguration.html
---

# PersistentVolumeConfiguration
<a name="API_PersistentVolumeConfiguration"></a>

Specifies the persistent EBS volume configuration for workers in a service managed fleet.

## Contents
<a name="API_PersistentVolumeConfiguration_Contents"></a>

 ** mountPath **   <a name="deadlinecloud-Type-PersistentVolumeConfiguration-mountPath"></a>
The file system path where the persistent volume is mounted on the worker instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** iops **   <a name="deadlinecloud-Type-PersistentVolumeConfiguration-iops"></a>
The IOPS per persistent volume. The default is 3000.
Type: Integer
Valid Range: Minimum value of 100. Maximum value of 80000.
Required: No

 ** lastUsedTtlHours **   <a name="deadlinecloud-Type-PersistentVolumeConfiguration-lastUsedTtlHours"></a>
The number of hours a persistent volume can remain unused before it is deleted. The default is 168 (7 days).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 8760.
Required: No

 ** sizeGiB **   <a name="deadlinecloud-Type-PersistentVolumeConfiguration-sizeGiB"></a>
The persistent volume size in GiB. The default is 250.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65536.
Required: No

 ** throughputMiB **   <a name="deadlinecloud-Type-PersistentVolumeConfiguration-throughputMiB"></a>
The throughput per persistent volume in MiB. The default is 125.
Type: Integer
Valid Range: Minimum value of 125. Maximum value of 2000.
Required: No

## See Also
<a name="API_PersistentVolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/PersistentVolumeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/PersistentVolumeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/PersistentVolumeConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
