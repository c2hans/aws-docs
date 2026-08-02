---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-domain-customfilesystemconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Domain CustomFileSystemConfig
<a name="aws-properties-sagemaker-domain-customfilesystemconfig"></a>

The settings for assigning a custom file system to a user profile or space for an Amazon SageMaker AI Domain. Permitted users can access this file system in Amazon SageMaker AI Studio.

## Syntax
<a name="aws-properties-sagemaker-domain-customfilesystemconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-domain-customfilesystemconfig-syntax.json"></a>

```
{
  "[EFSFileSystemConfig](#cfn-sagemaker-domain-customfilesystemconfig-efsfilesystemconfig)" : {{EFSFileSystemConfig}},
  "[FSxLustreFileSystemConfig](#cfn-sagemaker-domain-customfilesystemconfig-fsxlustrefilesystemconfig)" : {{FSxLustreFileSystemConfig}},
  "[S3FileSystemConfig](#cfn-sagemaker-domain-customfilesystemconfig-s3filesystemconfig)" : {{S3FileSystemConfig}}
}
```

### YAML
<a name="aws-properties-sagemaker-domain-customfilesystemconfig-syntax.yaml"></a>

```
  [EFSFileSystemConfig](#cfn-sagemaker-domain-customfilesystemconfig-efsfilesystemconfig): {{
    EFSFileSystemConfig}}
  [FSxLustreFileSystemConfig](#cfn-sagemaker-domain-customfilesystemconfig-fsxlustrefilesystemconfig): {{
    FSxLustreFileSystemConfig}}
  [S3FileSystemConfig](#cfn-sagemaker-domain-customfilesystemconfig-s3filesystemconfig): {{
    S3FileSystemConfig}}
```

## Properties
<a name="aws-properties-sagemaker-domain-customfilesystemconfig-properties"></a>

`EFSFileSystemConfig`  <a name="cfn-sagemaker-domain-customfilesystemconfig-efsfilesystemconfig"></a>
The settings for a custom Amazon EFS file system.
*Required*: No
*Type*: [EFSFileSystemConfig](aws-properties-sagemaker-domain-efsfilesystemconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FSxLustreFileSystemConfig`  <a name="cfn-sagemaker-domain-customfilesystemconfig-fsxlustrefilesystemconfig"></a>
The settings for a custom Amazon FSx for Lustre file system.
*Required*: No
*Type*: [FSxLustreFileSystemConfig](aws-properties-sagemaker-domain-fsxlustrefilesystemconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3FileSystemConfig`  <a name="cfn-sagemaker-domain-customfilesystemconfig-s3filesystemconfig"></a>
Configuration settings for a custom Amazon S3 file system.
*Required*: No
*Type*: [S3FileSystemConfig](aws-properties-sagemaker-domain-s3filesystemconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
