---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-capacityreservation-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::CapacityReservation Tag
<a name="aws-properties-ec2-capacityreservation-tag"></a>

Specifies a tag. For more information, see [Resource tags](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).

## Syntax
<a name="aws-properties-ec2-capacityreservation-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-capacityreservation-tag-syntax.json"></a>

```
{
  "[Key](#cfn-ec2-capacityreservation-tag-key)" : {{String}},
  "[Value](#cfn-ec2-capacityreservation-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-capacityreservation-tag-syntax.yaml"></a>

```
  [Key](#cfn-ec2-capacityreservation-tag-key): {{String}}
  [Value](#cfn-ec2-capacityreservation-tag-value): {{String}}
```

## Properties
<a name="aws-properties-ec2-capacityreservation-tag-properties"></a>

`Key`  <a name="cfn-ec2-capacityreservation-tag-key"></a>
The tag key.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-ec2-capacityreservation-tag-value"></a>
The tag value.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Examples
<a name="aws-properties-ec2-capacityreservation-tag--examples"></a>

###
<a name="aws-properties-ec2-capacityreservation-tag--examples--"></a>

This example specifies two tags for the Capacity Reservation.

#### JSON
<a name="aws-properties-ec2-capacityreservation-tag--examples----json"></a>

```
"Tags" : [
   {
      "Key" : "key1",
      "Value" : "value1"
   },
   {
      "Key" : "key2",
      "Value" : "value2"
   }
]
```

#### YAML
<a name="aws-properties-ec2-capacityreservation-tag--examples----yaml"></a>

```
Tags:
  - Key: "key1"
    Value: "value1"
  - Key: "key2"
    Value: "value2"
```
