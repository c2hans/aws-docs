---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelpackage-modelpackagestatusdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelPackage ModelPackageStatusDetails
<a name="aws-properties-sagemaker-modelpackage-modelpackagestatusdetails"></a>

Specifies the validation and image scan statuses of the model package.

## Syntax
<a name="aws-properties-sagemaker-modelpackage-modelpackagestatusdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelpackage-modelpackagestatusdetails-syntax.json"></a>

```
{
  "[ValidationStatuses](#cfn-sagemaker-modelpackage-modelpackagestatusdetails-validationstatuses)" : {{[ ModelPackageStatusItem, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelpackage-modelpackagestatusdetails-syntax.yaml"></a>

```
  [ValidationStatuses](#cfn-sagemaker-modelpackage-modelpackagestatusdetails-validationstatuses): {{
    - ModelPackageStatusItem}}
```

## Properties
<a name="aws-properties-sagemaker-modelpackage-modelpackagestatusdetails-properties"></a>

`ValidationStatuses`  <a name="cfn-sagemaker-modelpackage-modelpackagestatusdetails-validationstatuses"></a>
The validation status of the model package.
*Required*: No
*Type*: Array of [ModelPackageStatusItem](aws-properties-sagemaker-modelpackage-modelpackagestatusitem.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
