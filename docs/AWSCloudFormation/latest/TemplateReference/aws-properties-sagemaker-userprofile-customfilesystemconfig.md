---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-userprofile-customfilesystemconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::UserProfile CustomFileSystemConfig
<a name="aws-properties-sagemaker-userprofile-customfilesystemconfig"></a>

The settings for assigning a custom file system to a user profile or space for an Amazon SageMaker AI Domain. Permitted users can access this file system in Amazon SageMaker AI Studio.

## Syntax
<a name="aws-properties-sagemaker-userprofile-customfilesystemconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-userprofile-customfilesystemconfig-syntax.json"></a>

```
{
  "[EFSFileSystemConfig](#cfn-sagemaker-userprofile-customfilesystemconfig-efsfilesystemconfig)" : {{EFSFileSystemConfig}},
  "[FSxLustreFileSystemConfig](#cfn-sagemaker-userprofile-customfilesystemconfig-fsxlustrefilesystemconfig)" : {{FSxLustreFileSystemConfig}},
  "[S3FileSystemConfig](#cfn-sagemaker-userprofile-customfilesystemconfig-s3filesystemconfig)" : {{S3FileSystemConfig}}
}
```

### YAML
<a name="aws-properties-sagemaker-userprofile-customfilesystemconfig-syntax.yaml"></a>

```
  [EFSFileSystemConfig](#cfn-sagemaker-userprofile-customfilesystemconfig-efsfilesystemconfig): {{
    EFSFileSystemConfig}}
  [FSxLustreFileSystemConfig](#cfn-sagemaker-userprofile-customfilesystemconfig-fsxlustrefilesystemconfig): {{
    FSxLustreFileSystemConfig}}
  [S3FileSystemConfig](#cfn-sagemaker-userprofile-customfilesystemconfig-s3filesystemconfig): {{
    S3FileSystemConfig}}
```

## Properties
<a name="aws-properties-sagemaker-userprofile-customfilesystemconfig-properties"></a>

`EFSFileSystemConfig`  <a name="cfn-sagemaker-userprofile-customfilesystemconfig-efsfilesystemconfig"></a>
The settings for a custom Amazon EFS file system.
*Required*: No
*Type*: [EFSFileSystemConfig](aws-properties-sagemaker-userprofile-efsfilesystemconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FSxLustreFileSystemConfig`  <a name="cfn-sagemaker-userprofile-customfilesystemconfig-fsxlustrefilesystemconfig"></a>
The settings for a custom Amazon FSx for Lustre file system.
*Required*: No
*Type*: [FSxLustreFileSystemConfig](aws-properties-sagemaker-userprofile-fsxlustrefilesystemconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3FileSystemConfig`  <a name="cfn-sagemaker-userprofile-customfilesystemconfig-s3filesystemconfig"></a>
Configuration settings for a custom Amazon S3 file system.
*Required*: No
*Type*: [S3FileSystemConfig](aws-properties-sagemaker-userprofile-s3filesystemconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
