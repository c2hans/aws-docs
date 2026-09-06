---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-space-efsfilesystem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Space EFSFileSystem
<a name="aws-properties-sagemaker-space-efsfilesystem"></a>

A file system, created by you in Amazon EFS, that you assign to a user profile or space for an Amazon SageMaker AI Domain. Permitted users can access this file system in Amazon SageMaker AI Studio.

## Syntax
<a name="aws-properties-sagemaker-space-efsfilesystem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-space-efsfilesystem-syntax.json"></a>

```
{
  "[FileSystemId](#cfn-sagemaker-space-efsfilesystem-filesystemid)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-space-efsfilesystem-syntax.yaml"></a>

```
  [FileSystemId](#cfn-sagemaker-space-efsfilesystem-filesystemid): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-space-efsfilesystem-properties"></a>

`FileSystemId`  <a name="cfn-sagemaker-space-efsfilesystem-filesystemid"></a>
The ID of your Amazon EFS file system.
*Required*: Yes
*Type*: String
*Pattern*: `^(fs-[0-9a-f]{8,})$`
*Minimum*: `11`
*Maximum*: `21`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
