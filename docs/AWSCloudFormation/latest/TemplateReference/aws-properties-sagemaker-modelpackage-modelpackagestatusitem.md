---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelpackage-modelpackagestatusitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelPackage ModelPackageStatusItem
<a name="aws-properties-sagemaker-modelpackage-modelpackagestatusitem"></a>

Represents the overall status of a model package.

## Syntax
<a name="aws-properties-sagemaker-modelpackage-modelpackagestatusitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelpackage-modelpackagestatusitem-syntax.json"></a>

```
{
  "[FailureReason](#cfn-sagemaker-modelpackage-modelpackagestatusitem-failurereason)" : {{String}},
  "[Name](#cfn-sagemaker-modelpackage-modelpackagestatusitem-name)" : {{String}},
  "[Status](#cfn-sagemaker-modelpackage-modelpackagestatusitem-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelpackage-modelpackagestatusitem-syntax.yaml"></a>

```
  [FailureReason](#cfn-sagemaker-modelpackage-modelpackagestatusitem-failurereason): {{String}}
  [Name](#cfn-sagemaker-modelpackage-modelpackagestatusitem-name): {{String}}
  [Status](#cfn-sagemaker-modelpackage-modelpackagestatusitem-status): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelpackage-modelpackagestatusitem-properties"></a>

`FailureReason`  <a name="cfn-sagemaker-modelpackage-modelpackagestatusitem-failurereason"></a>
if the overall status is `Failed`, the reason for the failure.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-sagemaker-modelpackage-modelpackagestatusitem-name"></a>
The name of the model package for which the overall status is being reported.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-sagemaker-modelpackage-modelpackagestatusitem-status"></a>
The current status.
*Required*: Yes
*Type*: String
*Allowed values*: `NotStarted | Failed | InProgress | Completed`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
