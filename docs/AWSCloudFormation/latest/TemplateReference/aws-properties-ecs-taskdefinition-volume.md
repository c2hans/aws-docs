---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-volume.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::TaskDefinition Volume
<a name="aws-properties-ecs-taskdefinition-volume"></a>

The data volume configuration for tasks launched using this task definition. Specifying a volume configuration in a task definition is optional. The volume configuration may contain multiple volumes but only one volume configured at launch is supported. Each volume defined in the volume configuration may only specify a `name` and one of either `configuredAtLaunch`, `dockerVolumeConfiguration`, `efsVolumeConfiguration`, `s3filesVolumeConfiguration`, `fsxWindowsFileServerVolumeConfiguration`, or `host`. If an empty volume configuration is specified, by default Amazon ECS uses a host volume. For more information, see [Using data volumes in tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_data_volumes.html).

## Syntax
<a name="aws-properties-ecs-taskdefinition-volume-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-taskdefinition-volume-syntax.json"></a>

```
{
  "[ConfiguredAtLaunch](#cfn-ecs-taskdefinition-volume-configuredatlaunch)" : {{Boolean}},
  "[DockerVolumeConfiguration](#cfn-ecs-taskdefinition-volume-dockervolumeconfiguration)" : {{DockerVolumeConfiguration}},
  "[EFSVolumeConfiguration](#cfn-ecs-taskdefinition-volume-efsvolumeconfiguration)" : {{EFSVolumeConfiguration}},
  "[FSxWindowsFileServerVolumeConfiguration](#cfn-ecs-taskdefinition-volume-fsxwindowsfileservervolumeconfiguration)" : {{FSxWindowsFileServerVolumeConfiguration}},
  "[Host](#cfn-ecs-taskdefinition-volume-host)" : {{HostVolumeProperties}},
  "[Name](#cfn-ecs-taskdefinition-volume-name)" : {{String}},
  "[S3FilesVolumeConfiguration](#cfn-ecs-taskdefinition-volume-s3filesvolumeconfiguration)" : {{S3FilesVolumeConfiguration}}
}
```

### YAML
<a name="aws-properties-ecs-taskdefinition-volume-syntax.yaml"></a>

```
  [ConfiguredAtLaunch](#cfn-ecs-taskdefinition-volume-configuredatlaunch): {{Boolean}}
  [DockerVolumeConfiguration](#cfn-ecs-taskdefinition-volume-dockervolumeconfiguration): {{
    DockerVolumeConfiguration}}
  [EFSVolumeConfiguration](#cfn-ecs-taskdefinition-volume-efsvolumeconfiguration): {{
    EFSVolumeConfiguration}}
  [FSxWindowsFileServerVolumeConfiguration](#cfn-ecs-taskdefinition-volume-fsxwindowsfileservervolumeconfiguration): {{
    FSxWindowsFileServerVolumeConfiguration}}
  [Host](#cfn-ecs-taskdefinition-volume-host): {{
    HostVolumeProperties}}
  [Name](#cfn-ecs-taskdefinition-volume-name): {{String}}
  [S3FilesVolumeConfiguration](#cfn-ecs-taskdefinition-volume-s3filesvolumeconfiguration): {{
    S3FilesVolumeConfiguration}}
```

## Properties
<a name="aws-properties-ecs-taskdefinition-volume-properties"></a>

`ConfiguredAtLaunch`  <a name="cfn-ecs-taskdefinition-volume-configuredatlaunch"></a>
Indicates whether the volume should be configured at launch time. This is used to create Amazon EBS volumes for standalone tasks or tasks created as part of a service. Each task definition revision may only have one volume configured at launch in the volume configuration.
To configure a volume at launch time, use this task definition revision and specify a `volumeConfigurations` object when calling the `CreateService`, `UpdateService`, `RunTask` or `StartTask` APIs.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DockerVolumeConfiguration`  <a name="cfn-ecs-taskdefinition-volume-dockervolumeconfiguration"></a>
This parameter is specified when you use Docker volumes.
Windows containers only support the use of the `local` driver. To use bind mounts, specify the `host` parameter instead.
Docker volumes aren't supported by tasks run on AWS Fargate.
*Required*: No
*Type*: [DockerVolumeConfiguration](aws-properties-ecs-taskdefinition-dockervolumeconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EFSVolumeConfiguration`  <a name="cfn-ecs-taskdefinition-volume-efsvolumeconfiguration"></a>
This parameter is specified when you use an Amazon Elastic File System file system for task storage.
*Required*: No
*Type*: [EFSVolumeConfiguration](aws-properties-ecs-taskdefinition-efsvolumeconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FSxWindowsFileServerVolumeConfiguration`  <a name="cfn-ecs-taskdefinition-volume-fsxwindowsfileservervolumeconfiguration"></a>
This parameter is specified when you use Amazon FSx for Windows File Server file system for task storage.
*Required*: No
*Type*: [FSxWindowsFileServerVolumeConfiguration](aws-properties-ecs-taskdefinition-fsxwindowsfileservervolumeconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Host`  <a name="cfn-ecs-taskdefinition-volume-host"></a>
This parameter is specified when you use bind mount host volumes. The contents of the `host` parameter determine whether your bind mount host volume persists on the host container instance and where it's stored. If the `host` parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data isn't guaranteed to persist after the containers that are associated with it stop running.
Windows containers can mount whole directories on the same drive as `$env:ProgramData`. Windows containers can't mount directories on a different drive, and mount point can't be across drives. For example, you can mount `C:\my\path:C:\my\path` and `D:\:D:\`, but not `D:\my\path:C:\my\path` or `D:\:C:\my\path`.
*Required*: No
*Type*: [HostVolumeProperties](aws-properties-ecs-taskdefinition-hostvolumeproperties.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-ecs-taskdefinition-volume-name"></a>
The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.
When using a volume configured at launch, the `name` is required and must also be specified as the volume name in the `ServiceVolumeConfiguration` or `TaskVolumeConfiguration` parameter when creating your service or standalone task.
For all other types of volumes, this name is referenced in the `sourceVolume` parameter of the `mountPoints` object in the container definition.
When a volume is using the `efsVolumeConfiguration`, the name is required.
When a volume is using the `s3filesVolumeConfiguration`, the name is required.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3FilesVolumeConfiguration`  <a name="cfn-ecs-taskdefinition-volume-s3filesvolumeconfiguration"></a>
This parameter is specified when you use an Amazon S3 Files file system for task storage.
*Required*: No
*Type*: [S3FilesVolumeConfiguration](aws-properties-ecs-taskdefinition-s3filesvolumeconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
