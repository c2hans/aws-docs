---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_MountPoint.html
---

# MountPoint
<a name="API_MountPoint"></a>

The details for a volume mount point that's used in a container definition.

## Contents
<a name="API_MountPoint_Contents"></a>

 ** containerPath **   <a name="ECS-Type-MountPoint-containerPath"></a>
The path on the container to mount the host volume at.
Type: String
Required: No

 ** readOnly **   <a name="ECS-Type-MountPoint-readOnly"></a>
If this value is `true`, the container has read-only access to the volume. If this value is `false`, then the container can write to the volume. The default value is `false`.
Type: Boolean
Required: No

 ** sourceVolume **   <a name="ECS-Type-MountPoint-sourceVolume"></a>
The name of the volume to mount. Must be a volume name referenced in the `name` parameter of task definition `volume`.
Type: String
Required: No

## See Also
<a name="API_MountPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/MountPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/MountPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/MountPoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
