---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-volume.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition Volume
<a name="aws-properties-batch-jobdefinition-volume"></a>

A data volume that's used in a job's container properties.

## Syntax
<a name="aws-properties-batch-jobdefinition-volume-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-volume-syntax.json"></a>

```
{
  "[EfsVolumeConfiguration](#cfn-batch-jobdefinition-volume-efsvolumeconfiguration)" : {{EFSVolumeConfiguration}},
  "[Host](#cfn-batch-jobdefinition-volume-host)" : {{Host}},
  "[Name](#cfn-batch-jobdefinition-volume-name)" : {{String}},
  "[S3FilesVolumeConfiguration](#cfn-batch-jobdefinition-volume-s3filesvolumeconfiguration)" : {{S3FilesVolumeConfiguration}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-volume-syntax.yaml"></a>

```
  [EfsVolumeConfiguration](#cfn-batch-jobdefinition-volume-efsvolumeconfiguration): {{
    EFSVolumeConfiguration}}
  [Host](#cfn-batch-jobdefinition-volume-host): {{
    Host}}
  [Name](#cfn-batch-jobdefinition-volume-name): {{String}}
  [S3FilesVolumeConfiguration](#cfn-batch-jobdefinition-volume-s3filesvolumeconfiguration): {{
    S3FilesVolumeConfiguration}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-volume-properties"></a>

`EfsVolumeConfiguration`  <a name="cfn-batch-jobdefinition-volume-efsvolumeconfiguration"></a>
This parameter is specified when you're using an Amazon Elastic File System file system for job storage. Jobs that are running on Fargate resources must specify a `platformVersion` of at least `1.4.0`.
*Required*: No
*Type*: [EFSVolumeConfiguration](aws-properties-batch-jobdefinition-efsvolumeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Host`  <a name="cfn-batch-jobdefinition-volume-host"></a>
The contents of the `host` parameter determine whether your data volume persists on the host container instance and where it's stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume. However, the data isn't guaranteed to persist after the containers that are associated with it stop running.
This parameter isn't applicable to jobs that are running on Fargate resources and shouldn't be provided.
*Required*: No
*Type*: [Host](aws-properties-batch-jobdefinition-host.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-batch-jobdefinition-volume-name"></a>
The name of the volume. It can be up to 255 characters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_). This name is referenced in the `sourceVolume` parameter of container definition `mountPoints`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3FilesVolumeConfiguration`  <a name="cfn-batch-jobdefinition-volume-s3filesvolumeconfiguration"></a>
This parameter is specified when you're using an S3Files file system for job storage.
*Required*: No
*Type*: [S3FilesVolumeConfiguration](aws-properties-batch-jobdefinition-s3filesvolumeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
