---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DaemonVolume.html
---

# DaemonVolume
<a name="API_DaemonVolume"></a>

A data volume definition for a daemon task.

## Contents
<a name="API_DaemonVolume_Contents"></a>

 ** host **   <a name="ECS-Type-DaemonVolume-host"></a>
The contents of the `host` parameter determine whether your bind mount host volume persists on the host container instance and where it's stored.
Type: [HostVolumeProperties](API_HostVolumeProperties.md) object
Required: No

 ** name **   <a name="ECS-Type-DaemonVolume-name"></a>
The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.
Type: String
Required: No

## See Also
<a name="API_DaemonVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DaemonVolume)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DaemonVolume)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DaemonVolume)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
