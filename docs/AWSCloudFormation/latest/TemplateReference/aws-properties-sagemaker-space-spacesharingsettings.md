---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-space-spacesharingsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Space SpaceSharingSettings
<a name="aws-properties-sagemaker-space-spacesharingsettings"></a>

A collection of space sharing settings.

## Syntax
<a name="aws-properties-sagemaker-space-spacesharingsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-space-spacesharingsettings-syntax.json"></a>

```
{
  "[SharingType](#cfn-sagemaker-space-spacesharingsettings-sharingtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-space-spacesharingsettings-syntax.yaml"></a>

```
  [SharingType](#cfn-sagemaker-space-spacesharingsettings-sharingtype): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-space-spacesharingsettings-properties"></a>

`SharingType`  <a name="cfn-sagemaker-space-spacesharingsettings-sharingtype"></a>
Specifies the sharing type of the space.
*Required*: Yes
*Type*: String
*Allowed values*: `Private | Shared`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
