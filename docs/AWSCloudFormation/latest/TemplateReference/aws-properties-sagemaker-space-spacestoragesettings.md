---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-space-spacestoragesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Space SpaceStorageSettings
<a name="aws-properties-sagemaker-space-spacestoragesettings"></a>

The storage settings for a space.

## Syntax
<a name="aws-properties-sagemaker-space-spacestoragesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-space-spacestoragesettings-syntax.json"></a>

```
{
  "[EbsStorageSettings](#cfn-sagemaker-space-spacestoragesettings-ebsstoragesettings)" : {{EbsStorageSettings}}
}
```

### YAML
<a name="aws-properties-sagemaker-space-spacestoragesettings-syntax.yaml"></a>

```
  [EbsStorageSettings](#cfn-sagemaker-space-spacestoragesettings-ebsstoragesettings): {{
    EbsStorageSettings}}
```

## Properties
<a name="aws-properties-sagemaker-space-spacestoragesettings-properties"></a>

`EbsStorageSettings`  <a name="cfn-sagemaker-space-spacestoragesettings-ebsstoragesettings"></a>
A collection of EBS storage settings for a space.
*Required*: No
*Type*: [EbsStorageSettings](aws-properties-sagemaker-space-ebsstoragesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
