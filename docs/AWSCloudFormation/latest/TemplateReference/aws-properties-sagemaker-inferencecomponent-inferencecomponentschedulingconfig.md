---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencecomponent-inferencecomponentschedulingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceComponent InferenceComponentSchedulingConfig
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentschedulingconfig"></a>

The scheduling configuration that determines how inference component copies are placed across available instances when copies are added or removed.

## Syntax
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentschedulingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentschedulingconfig-syntax.json"></a>

```
{
  "[AvailabilityZoneBalance](#cfn-sagemaker-inferencecomponent-inferencecomponentschedulingconfig-availabilityzonebalance)" : {{InferenceComponentAvailabilityZoneBalance}},
  "[PlacementStrategy](#cfn-sagemaker-inferencecomponent-inferencecomponentschedulingconfig-placementstrategy)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentschedulingconfig-syntax.yaml"></a>

```
  [AvailabilityZoneBalance](#cfn-sagemaker-inferencecomponent-inferencecomponentschedulingconfig-availabilityzonebalance): {{
    InferenceComponentAvailabilityZoneBalance}}
  [PlacementStrategy](#cfn-sagemaker-inferencecomponent-inferencecomponentschedulingconfig-placementstrategy): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentschedulingconfig-properties"></a>

`AvailabilityZoneBalance`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentschedulingconfig-availabilityzonebalance"></a>
Configuration for balancing inference component copies across Availability Zones.
*Required*: Yes
*Type*: [InferenceComponentAvailabilityZoneBalance](aws-properties-sagemaker-inferencecomponent-inferencecomponentavailabilityzonebalance.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PlacementStrategy`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentschedulingconfig-placementstrategy"></a>
The strategy for placing inference component copies across available instances. If you also set `AvailabilityZoneBalance`, this strategy applies to placement within each Availability Zone.
SPREAD
Distributes copies evenly across available instances for better resilience.
BINPACK
Packs copies onto fewer instances to optimize resource utilization.
*Required*: Yes
*Type*: String
*Allowed values*: `SPREAD | BINPACK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
