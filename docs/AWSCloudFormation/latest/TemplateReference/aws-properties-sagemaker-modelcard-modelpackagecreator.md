---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelcard-modelpackagecreator.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelCard ModelPackageCreator
<a name="aws-properties-sagemaker-modelcard-modelpackagecreator"></a>

Information about the user who created the model package.

## Syntax
<a name="aws-properties-sagemaker-modelcard-modelpackagecreator-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelcard-modelpackagecreator-syntax.json"></a>

```
{
  "[UserProfileName](#cfn-sagemaker-modelcard-modelpackagecreator-userprofilename)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelcard-modelpackagecreator-syntax.yaml"></a>

```
  [UserProfileName](#cfn-sagemaker-modelcard-modelpackagecreator-userprofilename): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelcard-modelpackagecreator-properties"></a>

`UserProfileName`  <a name="cfn-sagemaker-modelcard-modelpackagecreator-userprofilename"></a>
The user profile name of the model package creator.
*Required*: No
*Type*: String
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
