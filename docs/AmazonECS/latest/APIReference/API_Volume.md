---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Volume.html
---

# Volume
<a name="API_Volume"></a>

The data volume configuration for tasks launched using this task definition. Specifying a volume configuration in a task definition is optional. The volume configuration may contain multiple volumes but only one volume configured at launch is supported. Each volume defined in the volume configuration may only specify a `name` and one of either `configuredAtLaunch`, `dockerVolumeConfiguration`, `efsVolumeConfiguration`, `s3filesVolumeConfiguration`, `fsxWindowsFileServerVolumeConfiguration`, or `host`. If an empty volume configuration is specified, by default Amazon ECS uses a host volume. For more information, see [Using data volumes in tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_data_volumes.html).

## Contents
<a name="API_Volume_Contents"></a>

 ** configuredAtLaunch **   <a name="ECS-Type-Volume-configuredAtLaunch"></a>
Indicates whether the volume should be configured at launch time. This is used to create Amazon EBS volumes for standalone tasks or tasks created as part of a service. Each task definition revision may only have one volume configured at launch in the volume configuration.
To configure a volume at launch time, use this task definition revision and specify a `volumeConfigurations` object when calling the `CreateService`, `UpdateService`, `RunTask` or `StartTask` APIs.
Type: Boolean
Required: No

 ** dockerVolumeConfiguration **   <a name="ECS-Type-Volume-dockerVolumeConfiguration"></a>
This parameter is specified when you use Docker volumes.
Windows containers only support the use of the `local` driver. To use bind mounts, specify the `host` parameter instead.
Docker volumes aren't supported by tasks run on AWS Fargate.
Type: [DockerVolumeConfiguration](API_DockerVolumeConfiguration.md) object
Required: No

 ** efsVolumeConfiguration **   <a name="ECS-Type-Volume-efsVolumeConfiguration"></a>
This parameter is specified when you use an Amazon Elastic File System file system for task storage.
Type: [EFSVolumeConfiguration](API_EFSVolumeConfiguration.md) object
Required: No

 ** fsxWindowsFileServerVolumeConfiguration **   <a name="ECS-Type-Volume-fsxWindowsFileServerVolumeConfiguration"></a>
This parameter is specified when you use Amazon FSx for Windows File Server file system for task storage.
Type: [FSxWindowsFileServerVolumeConfiguration](API_FSxWindowsFileServerVolumeConfiguration.md) object
Required: No

 ** host **   <a name="ECS-Type-Volume-host"></a>
This parameter is specified when you use bind mount host volumes. The contents of the `host` parameter determine whether your bind mount host volume persists on the host container instance and where it's stored. If the `host` parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data isn't guaranteed to persist after the containers that are associated with it stop running.
Windows containers can mount whole directories on the same drive as `$env:ProgramData`. Windows containers can't mount directories on a different drive, and mount point can't be across drives. For example, you can mount `C:\my\path:C:\my\path` and `D:\:D:\`, but not `D:\my\path:C:\my\path` or `D:\:C:\my\path`.
Type: [HostVolumeProperties](API_HostVolumeProperties.md) object
Required: No

 ** name **   <a name="ECS-Type-Volume-name"></a>
The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.
When using a volume configured at launch, the `name` is required and must also be specified as the volume name in the `ServiceVolumeConfiguration` or `TaskVolumeConfiguration` parameter when creating your service or standalone task.
For all other types of volumes, this name is referenced in the `sourceVolume` parameter of the `mountPoints` object in the container definition.
When a volume is using the `efsVolumeConfiguration`, the name is required.
When a volume is using the `s3filesVolumeConfiguration`, the name is required.
Type: String
Required: No

 ** s3filesVolumeConfiguration **   <a name="ECS-Type-Volume-s3filesVolumeConfiguration"></a>
This parameter is specified when you use an Amazon S3 Files file system for task storage.
Type: [S3FilesVolumeConfiguration](API_S3FilesVolumeConfiguration.md) object
Required: No

## See Also
<a name="API_Volume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/Volume)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/Volume)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/Volume)
