---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_Volume.html
---

# Volume
<a name="API_Volume"></a>

A data volume that's used in a job's container properties.

## Contents
<a name="API_Volume_Contents"></a>

 ** efsVolumeConfiguration **   <a name="Batch-Type-Volume-efsVolumeConfiguration"></a>
This parameter is specified when you're using an Amazon Elastic File System file system for job storage. Jobs that are running on Fargate resources must specify a `platformVersion` of at least `1.4.0`.
Type: [EFSVolumeConfiguration](API_EFSVolumeConfiguration.md) object
Required: No

 ** host **   <a name="Batch-Type-Volume-host"></a>
The contents of the `host` parameter determine whether your data volume persists on the host container instance and where it's stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data isn't guaranteed to persist after the containers that are associated with it stop running.
This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.
Type: [Host](API_Host.md) object
Required: No

 ** name **   <a name="Batch-Type-Volume-name"></a>
The name of the volume. It can be up to 255 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_). This name is referenced in the `sourceVolume` parameter of container definition `mountPoints`.
Type: String
Required: No

 ** s3filesVolumeConfiguration **   <a name="Batch-Type-Volume-s3filesVolumeConfiguration"></a>
This parameter is specified when you're using an S3Files file system for job storage.
Type: [S3FilesVolumeConfiguration](API_S3FilesVolumeConfiguration.md) object
Required: No

## See Also
<a name="API_Volume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/Volume)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/Volume)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/Volume)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
