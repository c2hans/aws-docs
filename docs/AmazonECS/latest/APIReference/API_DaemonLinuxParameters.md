---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DaemonLinuxParameters.html
---

# DaemonLinuxParameters
<a name="API_DaemonLinuxParameters"></a>

The Linux-specific options that are applied to the daemon container, such as Linux kernel capabilities.

## Contents
<a name="API_DaemonLinuxParameters_Contents"></a>

 ** capabilities **   <a name="ECS-Type-DaemonLinuxParameters-capabilities"></a>
The Linux capabilities for the container that are added to or dropped from the default configuration provided by Docker.
Type: [KernelCapabilities](API_KernelCapabilities.md) object
Required: No

 ** devices **   <a name="ECS-Type-DaemonLinuxParameters-devices"></a>
Any host devices to expose to the container.
Type: Array of [Device](API_Device.md) objects
Required: No

 ** initProcessEnabled **   <a name="ECS-Type-DaemonLinuxParameters-initProcessEnabled"></a>
Run an `init` process inside the container that forwards signals and reaps processes.
Type: Boolean
Required: No

 ** tmpfs **   <a name="ECS-Type-DaemonLinuxParameters-tmpfs"></a>
The container path, mount options, and size (in MiB) of the tmpfs mount.
Type: Array of [Tmpfs](API_Tmpfs.md) objects
Required: No

## See Also
<a name="API_DaemonLinuxParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DaemonLinuxParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DaemonLinuxParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DaemonLinuxParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
