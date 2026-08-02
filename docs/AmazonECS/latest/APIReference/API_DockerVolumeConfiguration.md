---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DockerVolumeConfiguration.html
---

# DockerVolumeConfiguration
<a name="API_DockerVolumeConfiguration"></a>

This parameter is specified when you're using Docker volumes. Docker volumes are only supported when you're using the EC2 launch type. Windows containers only support the use of the `local` driver. To use bind mounts, specify a `host` instead.

## Contents
<a name="API_DockerVolumeConfiguration_Contents"></a>

 ** autoprovision **   <a name="ECS-Type-DockerVolumeConfiguration-autoprovision"></a>
If this value is `true`, the Docker volume is created if it doesn't already exist.
This field is only used if the `scope` is `shared`.
Type: Boolean
Required: No

 ** driver **   <a name="ECS-Type-DockerVolumeConfiguration-driver"></a>
The Docker volume driver to use. The driver value must match the driver name provided by Docker because it is used for task placement. If the driver was installed using the Docker plugin CLI, use `docker plugin ls` to retrieve the driver name from your container instance. If the driver was installed using another method, use Docker plugin discovery to retrieve the driver name. This parameter maps to `Driver` in the docker container create command and the `xxdriver` option to docker volume create.
Type: String
Required: No

 ** driverOpts **   <a name="ECS-Type-DockerVolumeConfiguration-driverOpts"></a>
A map of Docker driver-specific options passed through. This parameter maps to `DriverOpts` in the docker create-volume command and the `xxopt` option to docker volume create.
Type: String to string map
Required: No

 ** labels **   <a name="ECS-Type-DockerVolumeConfiguration-labels"></a>
Custom metadata to add to your Docker volume. This parameter maps to `Labels` in the docker container create command and the `xxlabel` option to docker volume create.
Type: String to string map
Required: No

 ** scope **   <a name="ECS-Type-DockerVolumeConfiguration-scope"></a>
The scope for the Docker volume that determines its lifecycle. Docker volumes that are scoped to a `task` are automatically provisioned when the task starts and destroyed when the task stops. Docker volumes that are scoped as `shared` persist after the task stops.
Type: String
Valid Values: `task | shared`
Required: No

## See Also
<a name="API_DockerVolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DockerVolumeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DockerVolumeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DockerVolumeConfiguration)
