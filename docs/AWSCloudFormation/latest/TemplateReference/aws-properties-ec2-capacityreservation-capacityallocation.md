---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-capacityreservation-capacityallocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::CapacityReservation CapacityAllocation
<a name="aws-properties-ec2-capacityreservation-capacityallocation"></a>

Information about instance capacity usage for a Capacity Reservation.

## Syntax
<a name="aws-properties-ec2-capacityreservation-capacityallocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-capacityreservation-capacityallocation-syntax.json"></a>

```
{
  "[AllocationType](#cfn-ec2-capacityreservation-capacityallocation-allocationtype)" : {{String}},
  "[Count](#cfn-ec2-capacityreservation-capacityallocation-count)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ec2-capacityreservation-capacityallocation-syntax.yaml"></a>

```
  [AllocationType](#cfn-ec2-capacityreservation-capacityallocation-allocationtype): {{String}}
  [Count](#cfn-ec2-capacityreservation-capacityallocation-count): {{Integer}}
```

## Properties
<a name="aws-properties-ec2-capacityreservation-capacityallocation-properties"></a>

`AllocationType`  <a name="cfn-ec2-capacityreservation-capacityallocation-allocationtype"></a>
The usage type. `used` indicates that the instance capacity is in use by instances that are running in the Capacity Reservation.
*Required*: No
*Type*: String
*Allowed values*: `used | cancelling`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Count`  <a name="cfn-ec2-capacityreservation-capacityallocation-count"></a>
The amount of instance capacity associated with the usage. For example a value of `4` indicates that instance capacity for 4 instances is currently in use.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
