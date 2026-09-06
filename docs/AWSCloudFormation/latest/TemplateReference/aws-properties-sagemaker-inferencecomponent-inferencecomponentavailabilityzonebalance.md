---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencecomponent-inferencecomponentavailabilityzonebalance.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceComponent InferenceComponentAvailabilityZoneBalance
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentavailabilityzonebalance"></a>

Configuration for balancing inference component copies across Availability Zones.

## Syntax
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentavailabilityzonebalance-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentavailabilityzonebalance-syntax.json"></a>

```
{
  "[EnforcementMode](#cfn-sagemaker-inferencecomponent-inferencecomponentavailabilityzonebalance-enforcementmode)" : {{String}},
  "[MaxImbalance](#cfn-sagemaker-inferencecomponent-inferencecomponentavailabilityzonebalance-maximbalance)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentavailabilityzonebalance-syntax.yaml"></a>

```
  [EnforcementMode](#cfn-sagemaker-inferencecomponent-inferencecomponentavailabilityzonebalance-enforcementmode): {{String}}
  [MaxImbalance](#cfn-sagemaker-inferencecomponent-inferencecomponentavailabilityzonebalance-maximbalance): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentavailabilityzonebalance-properties"></a>

`EnforcementMode`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentavailabilityzonebalance-enforcementmode"></a>
Determines how strictly the Availability Zone balance constraint is enforced.
PERMISSIVE
The endpoint attempts to balance copies across Availability Zones but proceeds with scheduling even if balance can't be achieved due to available capacity or instance distribution across Availability Zones.
*Required*: Yes
*Type*: String
*Allowed values*: `PERMISSIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxImbalance`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentavailabilityzonebalance-maximbalance"></a>
The maximum allowed difference in the number of inference component copies between any two Availability Zones. This parameter applies only when the endpoint has instances across two or more Availability Zones. A copy placement is allowed if it reduces imbalance or the resulting imbalance is within this value.
Default value: `0`.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
