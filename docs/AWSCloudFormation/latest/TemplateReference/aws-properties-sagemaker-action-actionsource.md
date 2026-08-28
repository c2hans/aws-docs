---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-action-actionsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Action ActionSource
<a name="aws-properties-sagemaker-action-actionsource"></a>

A structure describing the source of an action.

## Syntax
<a name="aws-properties-sagemaker-action-actionsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-action-actionsource-syntax.json"></a>

```
{
  "[SourceId](#cfn-sagemaker-action-actionsource-sourceid)" : {{String}},
  "[SourceType](#cfn-sagemaker-action-actionsource-sourcetype)" : {{String}},
  "[SourceUri](#cfn-sagemaker-action-actionsource-sourceuri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-action-actionsource-syntax.yaml"></a>

```
  [SourceId](#cfn-sagemaker-action-actionsource-sourceid): {{String}}
  [SourceType](#cfn-sagemaker-action-actionsource-sourcetype): {{String}}
  [SourceUri](#cfn-sagemaker-action-actionsource-sourceuri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-action-actionsource-properties"></a>

`SourceId`  <a name="cfn-sagemaker-action-actionsource-sourceid"></a>
The ID of the source.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceType`  <a name="cfn-sagemaker-action-actionsource-sourcetype"></a>
The type of the source.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceUri`  <a name="cfn-sagemaker-action-actionsource-sourceuri"></a>
The URI of the source.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
