---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencecomponent-inferencecomponentcapacitysize.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceComponent InferenceComponentCapacitySize
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentcapacitysize"></a>

Specifies the type and size of the endpoint capacity to activate for a rolling deployment or a rollback strategy. You can specify your batches as either of the following:
+ A count of inference component copies
+ The overall percentage or your fleet

For a rollback strategy, if you don't specify the fields in this object, or if you set the `Value` parameter to 100%, then SageMaker AI uses a blue/green rollback strategy and rolls all traffic back to the blue fleet.

## Syntax
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentcapacitysize-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentcapacitysize-syntax.json"></a>

```
{
  "[Type](#cfn-sagemaker-inferencecomponent-inferencecomponentcapacitysize-type)" : {{String}},
  "[Value](#cfn-sagemaker-inferencecomponent-inferencecomponentcapacitysize-value)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentcapacitysize-syntax.yaml"></a>

```
  [Type](#cfn-sagemaker-inferencecomponent-inferencecomponentcapacitysize-type): {{String}}
  [Value](#cfn-sagemaker-inferencecomponent-inferencecomponentcapacitysize-value): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentcapacitysize-properties"></a>

`Type`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentcapacitysize-type"></a>
Specifies the endpoint capacity type.
COPY\_COUNT
The endpoint activates based on the number of inference component copies.
CAPACITY\_PERCENT
The endpoint activates based on the specified percentage of capacity.
*Required*: Yes
*Type*: String
*Allowed values*: `COPY_COUNT | CAPACITY_PERCENT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentcapacitysize-value"></a>
Defines the capacity size, either as a number of inference component copies or a capacity percentage.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
