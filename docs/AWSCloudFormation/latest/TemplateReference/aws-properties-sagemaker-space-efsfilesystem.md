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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
