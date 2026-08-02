---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_LinuxParameters.html
---

# LinuxParameters
<a name="API_LinuxParameters"></a>

The Linux-specific options that are applied to the container, such as Linux [KernelCapabilities](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_KernelCapabilities.html).

## Contents
<a name="API_LinuxParameters_Contents"></a>

 ** capabilities **   <a name="ECS-Type-LinuxParameters-capabilities"></a>
The Linux capabilities for the container that are added to or dropped from the default configuration provided by Docker.
For tasks that use the Fargate launch type, `capabilities` is supported for all platform versions but the `add` parameter is only supported if using platform version 1.4.0 or later.
Type: [KernelCapabilities](API_KernelCapabilities.md) object
Required: No

 ** devices **   <a name="ECS-Type-LinuxParameters-devices"></a>
Any host devices to expose to the container. This parameter maps to `Devices` in the docker container create command and the `--device` option to docker run.
If you're using tasks that use the Fargate launch type, the `devices` parameter isn't supported.
Type: Array of [Device](API_Device.md) objects
Required: No

 ** initProcessEnabled **   <a name="ECS-Type-LinuxParameters-initProcessEnabled"></a>
Run an `init` process inside the container that forwards signals and reaps processes. This parameter maps to the `--init` option to docker run. This parameter requires version 1.25 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version --format '{{.Server.APIVersion}}'`
Type: Boolean
Required: No

 ** maxSwap **   <a name="ECS-Type-LinuxParameters-maxSwap"></a>
The total amount of swap memory (in MiB) a container can use. This parameter will be translated to the `--memory-swap` option to docker run where the value would be the sum of the container memory plus the `maxSwap` value.
If a `maxSwap` value of `0` is specified, the container will not use swap. Accepted values are `0` or any positive integer. If the `maxSwap` parameter is omitted, the container will use the swap configuration for the container instance it is running on. A `maxSwap` value must be set for the `swappiness` parameter to be used.
If you're using tasks that use the Fargate launch type, the `maxSwap` parameter isn't supported.
If you're using tasks on Amazon Linux 2023 the `swappiness` parameter isn't supported.
Type: Integer
Required: No

 ** sharedMemorySize **   <a name="ECS-Type-LinuxParameters-sharedMemorySize"></a>
The value for the size (in MiB) of the `/dev/shm` volume. This parameter maps to the `--shm-size` option to docker run.
If you are using tasks that use the Fargate launch type, the `sharedMemorySize` parameter is not supported.
Type: Integer
Required: No

 ** swappiness **   <a name="ECS-Type-LinuxParameters-swappiness"></a>
This allows you to tune a container's memory swappiness behavior. A `swappiness` value of `0` will cause swapping to not happen unless absolutely necessary. A `swappiness` value of `100` will cause pages to be swapped very aggressively. Accepted values are whole numbers between `0` and `100`. If the `swappiness` parameter is not specified, a default value of `60` is used. If a value is not specified for `maxSwap` then this parameter is ignored. This parameter maps to the `--memory-swappiness` option to docker run.
If you're using tasks that use the Fargate launch type, the `swappiness` parameter isn't supported.
If you're using tasks on Amazon Linux 2023 the `swappiness` parameter isn't supported.
Type: Integer
Required: No

 ** tmpfs **   <a name="ECS-Type-LinuxParameters-tmpfs"></a>
The container path, mount options, and size (in MiB) of the tmpfs mount. This parameter maps to the `--tmpfs` option to docker run.
Type: Array of [Tmpfs](API_Tmpfs.md) objects
Required: No

## See Also
<a name="API_LinuxParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/LinuxParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/LinuxParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/LinuxParameters)
