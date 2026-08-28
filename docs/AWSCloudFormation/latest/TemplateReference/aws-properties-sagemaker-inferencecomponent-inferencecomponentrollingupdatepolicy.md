---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencecomponent-inferencecomponentrollingupdatepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceComponent InferenceComponentRollingUpdatePolicy
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentrollingupdatepolicy"></a>

Specifies a rolling deployment strategy for updating a SageMaker AI inference component.

## Syntax
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentrollingupdatepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentrollingupdatepolicy-syntax.json"></a>

```
{
  "[MaximumBatchSize](#cfn-sagemaker-inferencecomponent-inferencecomponentrollingupdatepolicy-maximumbatchsize)" : {{InferenceComponentCapacitySize}},
  "[MaximumExecutionTimeoutInSeconds](#cfn-sagemaker-inferencecomponent-inferencecomponentrollingupdatepolicy-maximumexecutiontimeoutinseconds)" : {{Integer}},
  "[RollbackMaximumBatchSize](#cfn-sagemaker-inferencecomponent-inferencecomponentrollingupdatepolicy-rollbackmaximumbatchsize)" : {{InferenceComponentCapacitySize}},
  "[WaitIntervalInSeconds](#cfn-sagemaker-inferencecomponent-inferencecomponentrollingupdatepolicy-waitintervalinseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentrollingupdatepolicy-syntax.yaml"></a>

```
  [MaximumBatchSize](#cfn-sagemaker-inferencecomponent-inferencecomponentrollingupdatepolicy-maximumbatchsize): {{
    InferenceComponentCapacitySize}}
  [MaximumExecutionTimeoutInSeconds](#cfn-sagemaker-inferencecomponent-inferencecomponentrollingupdatepolicy-maximumexecutiontimeoutinseconds): {{Integer}}
  [RollbackMaximumBatchSize](#cfn-sagemaker-inferencecomponent-inferencecomponentrollingupdatepolicy-rollbackmaximumbatchsize): {{
    InferenceComponentCapacitySize}}
  [WaitIntervalInSeconds](#cfn-sagemaker-inferencecomponent-inferencecomponentrollingupdatepolicy-waitintervalinseconds): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentrollingupdatepolicy-properties"></a>

`MaximumBatchSize`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentrollingupdatepolicy-maximumbatchsize"></a>
The batch size for each rolling step in the deployment process. For each step, SageMaker AI provisions capacity on the new endpoint fleet, routes traffic to that fleet, and terminates capacity on the old endpoint fleet. The value must be between 5% to 50% of the copy count of the inference component.
*Required*: No
*Type*: [InferenceComponentCapacitySize](aws-properties-sagemaker-inferencecomponent-inferencecomponentcapacitysize.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumExecutionTimeoutInSeconds`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentrollingupdatepolicy-maximumexecutiontimeoutinseconds"></a>
The time limit for the total deployment. Exceeding this limit causes a timeout.
*Required*: No
*Type*: Integer
*Minimum*: `600`
*Maximum*: `28800`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RollbackMaximumBatchSize`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentrollingupdatepolicy-rollbackmaximumbatchsize"></a>
The batch size for a rollback to the old endpoint fleet. If this field is absent, the value is set to the default, which is 100% of the total capacity. When the default is used, SageMaker AI provisions the entire capacity of the old fleet at once during rollback.
*Required*: No
*Type*: [InferenceComponentCapacitySize](aws-properties-sagemaker-inferencecomponent-inferencecomponentcapacitysize.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WaitIntervalInSeconds`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentrollingupdatepolicy-waitintervalinseconds"></a>
The length of the baking period, during which SageMaker AI monitors alarms for each batch on the new fleet.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `3600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
