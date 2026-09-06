---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-space-customfilesystem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Space CustomFileSystem
<a name="aws-properties-sagemaker-space-customfilesystem"></a>

A file system, created by you, that you assign to a user profile or space for an Amazon SageMaker AI Domain. Permitted users can access this file system in Amazon SageMaker AI Studio.

## Syntax
<a name="aws-properties-sagemaker-space-customfilesystem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-space-customfilesystem-syntax.json"></a>

```
{
  "[EFSFileSystem](#cfn-sagemaker-space-customfilesystem-efsfilesystem)" : {{EFSFileSystem}},
  "[FSxLustreFileSystem](#cfn-sagemaker-space-customfilesystem-fsxlustrefilesystem)" : {{FSxLustreFileSystem}},
  "[S3FileSystem](#cfn-sagemaker-space-customfilesystem-s3filesystem)" : {{S3FileSystem}}
}
```

### YAML
<a name="aws-properties-sagemaker-space-customfilesystem-syntax.yaml"></a>

```
  [EFSFileSystem](#cfn-sagemaker-space-customfilesystem-efsfilesystem): {{
    EFSFileSystem}}
  [FSxLustreFileSystem](#cfn-sagemaker-space-customfilesystem-fsxlustrefilesystem): {{
    FSxLustreFileSystem}}
  [S3FileSystem](#cfn-sagemaker-space-customfilesystem-s3filesystem): {{
    S3FileSystem}}
```

## Properties
<a name="aws-properties-sagemaker-space-customfilesystem-properties"></a>

`EFSFileSystem`  <a name="cfn-sagemaker-space-customfilesystem-efsfilesystem"></a>
A custom file system in Amazon EFS.
*Required*: No
*Type*: [EFSFileSystem](aws-properties-sagemaker-space-efsfilesystem.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FSxLustreFileSystem`  <a name="cfn-sagemaker-space-customfilesystem-fsxlustrefilesystem"></a>
A custom file system in Amazon FSx for Lustre.
*Required*: No
*Type*: [FSxLustreFileSystem](aws-properties-sagemaker-space-fsxlustrefilesystem.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3FileSystem`  <a name="cfn-sagemaker-space-customfilesystem-s3filesystem"></a>
A custom file system in Amazon S3. This is only supported in Amazon SageMaker Unified Studio.
*Required*: No
*Type*: [S3FileSystem](aws-properties-sagemaker-space-s3filesystem.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
