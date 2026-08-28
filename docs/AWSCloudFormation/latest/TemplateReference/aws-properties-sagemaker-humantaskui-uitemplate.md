---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-humantaskui-uitemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::HumanTaskUi UiTemplate
<a name="aws-properties-sagemaker-humantaskui-uitemplate"></a>

The Liquid template for the worker user interface.

## Syntax
<a name="aws-properties-sagemaker-humantaskui-uitemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-humantaskui-uitemplate-syntax.json"></a>

```
{
  "[Content](#cfn-sagemaker-humantaskui-uitemplate-content)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-humantaskui-uitemplate-syntax.yaml"></a>

```
  [Content](#cfn-sagemaker-humantaskui-uitemplate-content): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-humantaskui-uitemplate-properties"></a>

`Content`  <a name="cfn-sagemaker-humantaskui-uitemplate-content"></a>
The content of the Liquid template for the worker user interface.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
