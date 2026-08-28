---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_MountPoint.html
---

# MountPoint
<a name="API_MountPoint"></a>

Details for a Docker volume mount point that's used in a job's container properties. This parameter maps to `Volumes` in the [Create a container](https://docs.docker.com/engine/api/latest/#tag/Container/operation/ContainerCreate) section of the *Docker Remote API* and the `--volume` option to docker run.

## Contents
<a name="API_MountPoint_Contents"></a>

 ** containerPath **   <a name="Batch-Type-MountPoint-containerPath"></a>
The path on the container where the host volume is mounted.
Type: String
Required: No

 ** readOnly **   <a name="Batch-Type-MountPoint-readOnly"></a>
If this value is `true`, the container has read-only access to the volume. Otherwise, the container can write to the volume. The default value is `false`.
Type: Boolean
Required: No

 ** sourceVolume **   <a name="Batch-Type-MountPoint-sourceVolume"></a>
The name of the volume to mount.
Type: String
Required: No

## See Also
<a name="API_MountPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/MountPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/MountPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/MountPoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
