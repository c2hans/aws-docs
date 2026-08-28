---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-appimageconfig-filesystemconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AppImageConfig FileSystemConfig
<a name="aws-properties-sagemaker-appimageconfig-filesystemconfig"></a>

The Amazon Elastic File System storage configuration for a SageMaker AI image.

## Syntax
<a name="aws-properties-sagemaker-appimageconfig-filesystemconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-appimageconfig-filesystemconfig-syntax.json"></a>

```
{
  "[DefaultGid](#cfn-sagemaker-appimageconfig-filesystemconfig-defaultgid)" : {{Integer}},
  "[DefaultUid](#cfn-sagemaker-appimageconfig-filesystemconfig-defaultuid)" : {{Integer}},
  "[MountPath](#cfn-sagemaker-appimageconfig-filesystemconfig-mountpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-appimageconfig-filesystemconfig-syntax.yaml"></a>

```
  [DefaultGid](#cfn-sagemaker-appimageconfig-filesystemconfig-defaultgid): {{Integer}}
  [DefaultUid](#cfn-sagemaker-appimageconfig-filesystemconfig-defaultuid): {{Integer}}
  [MountPath](#cfn-sagemaker-appimageconfig-filesystemconfig-mountpath): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-appimageconfig-filesystemconfig-properties"></a>

`DefaultGid`  <a name="cfn-sagemaker-appimageconfig-filesystemconfig-defaultgid"></a>
The default POSIX group ID (GID). If not specified, defaults to `100`.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultUid`  <a name="cfn-sagemaker-appimageconfig-filesystemconfig-defaultuid"></a>
The default POSIX user ID (UID). If not specified, defaults to `1000`.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MountPath`  <a name="cfn-sagemaker-appimageconfig-filesystemconfig-mountpath"></a>
The path within the image to mount the user's EFS home directory. The directory should be empty. If not specified, defaults to */home/sagemaker-user*.
*Required*: No
*Type*: String
*Pattern*: `^/.*`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
