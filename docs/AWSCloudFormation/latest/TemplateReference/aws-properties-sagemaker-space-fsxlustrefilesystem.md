---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-space-fsxlustrefilesystem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Space FSxLustreFileSystem
<a name="aws-properties-sagemaker-space-fsxlustrefilesystem"></a>

A custom file system in Amazon FSx for Lustre.

## Syntax
<a name="aws-properties-sagemaker-space-fsxlustrefilesystem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-space-fsxlustrefilesystem-syntax.json"></a>

```
{
  "[FileSystemId](#cfn-sagemaker-space-fsxlustrefilesystem-filesystemid)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-space-fsxlustrefilesystem-syntax.yaml"></a>

```
  [FileSystemId](#cfn-sagemaker-space-fsxlustrefilesystem-filesystemid): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-space-fsxlustrefilesystem-properties"></a>

`FileSystemId`  <a name="cfn-sagemaker-space-fsxlustrefilesystem-filesystemid"></a>
Amazon FSx for Lustre file system ID.
*Required*: Yes
*Type*: String
*Pattern*: `^(fs-[0-9a-f]{8,})$`
*Minimum*: `11`
*Maximum*: `21`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
