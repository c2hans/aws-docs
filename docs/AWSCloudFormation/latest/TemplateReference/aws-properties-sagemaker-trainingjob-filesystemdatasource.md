---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-trainingjob-filesystemdatasource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TrainingJob FileSystemDataSource
<a name="aws-properties-sagemaker-trainingjob-filesystemdatasource"></a>

Specifies a file system data source for a channel.

## Syntax
<a name="aws-properties-sagemaker-trainingjob-filesystemdatasource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-trainingjob-filesystemdatasource-syntax.json"></a>

```
{
  "[DirectoryPath](#cfn-sagemaker-trainingjob-filesystemdatasource-directorypath)" : {{String}},
  "[FileSystemAccessMode](#cfn-sagemaker-trainingjob-filesystemdatasource-filesystemaccessmode)" : {{String}},
  "[FileSystemId](#cfn-sagemaker-trainingjob-filesystemdatasource-filesystemid)" : {{String}},
  "[FileSystemType](#cfn-sagemaker-trainingjob-filesystemdatasource-filesystemtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-trainingjob-filesystemdatasource-syntax.yaml"></a>

```
  [DirectoryPath](#cfn-sagemaker-trainingjob-filesystemdatasource-directorypath): {{String}}
  [FileSystemAccessMode](#cfn-sagemaker-trainingjob-filesystemdatasource-filesystemaccessmode): {{String}}
  [FileSystemId](#cfn-sagemaker-trainingjob-filesystemdatasource-filesystemid): {{String}}
  [FileSystemType](#cfn-sagemaker-trainingjob-filesystemdatasource-filesystemtype): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-trainingjob-filesystemdatasource-properties"></a>

`DirectoryPath`  <a name="cfn-sagemaker-trainingjob-filesystemdatasource-directorypath"></a>
The full path to the directory to associate with the channel.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FileSystemAccessMode`  <a name="cfn-sagemaker-trainingjob-filesystemdatasource-filesystemaccessmode"></a>
The access mode of the mount of the directory associated with the channel. A directory can be mounted either in `ro` (read-only) or `rw` (read-write) mode.
*Required*: Yes
*Type*: String
*Allowed values*: `rw | ro`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FileSystemId`  <a name="cfn-sagemaker-trainingjob-filesystemdatasource-filesystemid"></a>
The file system id.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Minimum*: `11`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FileSystemType`  <a name="cfn-sagemaker-trainingjob-filesystemdatasource-filesystemtype"></a>
The file system type.
*Required*: Yes
*Type*: String
*Allowed values*: `EFS | FSxLustre`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
