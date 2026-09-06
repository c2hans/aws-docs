---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-serviceenvironment-capacitylimit.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::ServiceEnvironment CapacityLimit
<a name="aws-properties-batch-serviceenvironment-capacitylimit"></a>

Defines the capacity limit for a service environment. This structure specifies the maximum amount of resources that can be used by service jobs in the environment.

## Syntax
<a name="aws-properties-batch-serviceenvironment-capacitylimit-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-serviceenvironment-capacitylimit-syntax.json"></a>

```
{
  "[CapacityUnit](#cfn-batch-serviceenvironment-capacitylimit-capacityunit)" : {{String}},
  "[MaxCapacity](#cfn-batch-serviceenvironment-capacitylimit-maxcapacity)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-batch-serviceenvironment-capacitylimit-syntax.yaml"></a>

```
  [CapacityUnit](#cfn-batch-serviceenvironment-capacitylimit-capacityunit): {{String}}
  [MaxCapacity](#cfn-batch-serviceenvironment-capacitylimit-maxcapacity): {{Integer}}
```

## Properties
<a name="aws-properties-batch-serviceenvironment-capacitylimit-properties"></a>

`CapacityUnit`  <a name="cfn-batch-serviceenvironment-capacitylimit-capacityunit"></a>
The unit of measure for the capacity limit. This defines how the maxCapacity value should be interpreted. For `SAGEMAKER_TRAINING` jobs, use `NUM_INSTANCES`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxCapacity`  <a name="cfn-batch-serviceenvironment-capacitylimit-maxcapacity"></a>
The maximum capacity available for the service environment. This value represents the maximum amount resources that can be allocated to service jobs.
For example, `maxCapacity=50`, `capacityUnit=NUM_INSTANCES`. This indicates that the maximum number of instances that can be run on this service environment is 50. You could then run 5 SageMaker Training jobs that each use 10 instances. However, if you submit another job that requires 10 instances, it will wait in the queue.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
