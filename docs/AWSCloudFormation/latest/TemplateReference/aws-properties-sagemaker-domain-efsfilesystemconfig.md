---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-domain-efsfilesystemconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Domain EFSFileSystemConfig
<a name="aws-properties-sagemaker-domain-efsfilesystemconfig"></a>

The settings for assigning a custom Amazon EFS file system to a user profile or space for an Amazon SageMaker AI Domain.

## Syntax
<a name="aws-properties-sagemaker-domain-efsfilesystemconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-domain-efsfilesystemconfig-syntax.json"></a>

```
{
  "[FileSystemId](#cfn-sagemaker-domain-efsfilesystemconfig-filesystemid)" : {{String}},
  "[FileSystemPath](#cfn-sagemaker-domain-efsfilesystemconfig-filesystempath)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-domain-efsfilesystemconfig-syntax.yaml"></a>

```
  [FileSystemId](#cfn-sagemaker-domain-efsfilesystemconfig-filesystemid): {{String}}
  [FileSystemPath](#cfn-sagemaker-domain-efsfilesystemconfig-filesystempath): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-domain-efsfilesystemconfig-properties"></a>

`FileSystemId`  <a name="cfn-sagemaker-domain-efsfilesystemconfig-filesystemid"></a>
The ID of your Amazon EFS file system.
*Required*: Yes
*Type*: String
*Pattern*: `^(fs-[0-9a-f]{8,})$`
*Minimum*: `11`
*Maximum*: `21`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FileSystemPath`  <a name="cfn-sagemaker-domain-efsfilesystemconfig-filesystempath"></a>
The path to the file system directory that is accessible in Amazon SageMaker AI Studio. Permitted users can access only this directory and below.
*Required*: No
*Type*: String
*Pattern*: `^\/\S*$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
