---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-appimageconfig-kernelspec.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AppImageConfig KernelSpec
<a name="aws-properties-sagemaker-appimageconfig-kernelspec"></a>

The specification of a Jupyter kernel.

## Syntax
<a name="aws-properties-sagemaker-appimageconfig-kernelspec-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-appimageconfig-kernelspec-syntax.json"></a>

```
{
  "[DisplayName](#cfn-sagemaker-appimageconfig-kernelspec-displayname)" : {{String}},
  "[Name](#cfn-sagemaker-appimageconfig-kernelspec-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-appimageconfig-kernelspec-syntax.yaml"></a>

```
  [DisplayName](#cfn-sagemaker-appimageconfig-kernelspec-displayname): {{String}}
  [Name](#cfn-sagemaker-appimageconfig-kernelspec-name): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-appimageconfig-kernelspec-properties"></a>

`DisplayName`  <a name="cfn-sagemaker-appimageconfig-kernelspec-displayname"></a>
The display name of the kernel.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-sagemaker-appimageconfig-kernelspec-name"></a>
The name of the Jupyter kernel in the image. This value is case sensitive.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
