---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-domain-hiddensagemakerimage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Domain HiddenSageMakerImage
<a name="aws-properties-sagemaker-domain-hiddensagemakerimage"></a>

The SageMaker images that are hidden from the Studio user interface. You must specify the SageMaker image name and version aliases.

## Syntax
<a name="aws-properties-sagemaker-domain-hiddensagemakerimage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-domain-hiddensagemakerimage-syntax.json"></a>

```
{
  "[SageMakerImageName](#cfn-sagemaker-domain-hiddensagemakerimage-sagemakerimagename)" : {{String}},
  "[VersionAliases](#cfn-sagemaker-domain-hiddensagemakerimage-versionaliases)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-domain-hiddensagemakerimage-syntax.yaml"></a>

```
  [SageMakerImageName](#cfn-sagemaker-domain-hiddensagemakerimage-sagemakerimagename): {{String}}
  [VersionAliases](#cfn-sagemaker-domain-hiddensagemakerimage-versionaliases): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-domain-hiddensagemakerimage-properties"></a>

`SageMakerImageName`  <a name="cfn-sagemaker-domain-hiddensagemakerimage-sagemakerimagename"></a>
 The SageMaker image name that you are hiding from the Studio user interface.
*Required*: No
*Type*: String
*Allowed values*: `sagemaker_distribution`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VersionAliases`  <a name="cfn-sagemaker-domain-hiddensagemakerimage-versionaliases"></a>
 The version aliases you are hiding from the Studio user interface.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `128 | 20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
