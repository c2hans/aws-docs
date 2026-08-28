---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-userprofile-applifecyclemanagement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::UserProfile AppLifecycleManagement
<a name="aws-properties-sagemaker-userprofile-applifecyclemanagement"></a>

Settings that are used to configure and manage the lifecycle of Amazon SageMaker Studio applications.

## Syntax
<a name="aws-properties-sagemaker-userprofile-applifecyclemanagement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-userprofile-applifecyclemanagement-syntax.json"></a>

```
{
  "[IdleSettings](#cfn-sagemaker-userprofile-applifecyclemanagement-idlesettings)" : {{IdleSettings}}
}
```

### YAML
<a name="aws-properties-sagemaker-userprofile-applifecyclemanagement-syntax.yaml"></a>

```
  [IdleSettings](#cfn-sagemaker-userprofile-applifecyclemanagement-idlesettings): {{
    IdleSettings}}
```

## Properties
<a name="aws-properties-sagemaker-userprofile-applifecyclemanagement-properties"></a>

`IdleSettings`  <a name="cfn-sagemaker-userprofile-applifecyclemanagement-idlesettings"></a>
Settings related to idle shutdown of Studio applications.
*Required*: No
*Type*: [IdleSettings](aws-properties-sagemaker-userprofile-idlesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
