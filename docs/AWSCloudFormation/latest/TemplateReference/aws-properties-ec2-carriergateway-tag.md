---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-carriergateway-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::CarrierGateway Tag
<a name="aws-properties-ec2-carriergateway-tag"></a>

Specifies a tag. For more information, see [Resource tags](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).

## Syntax
<a name="aws-properties-ec2-carriergateway-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-carriergateway-tag-syntax.json"></a>

```
{
  "[Key](#cfn-ec2-carriergateway-tag-key)" : {{String}},
  "[Value](#cfn-ec2-carriergateway-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-carriergateway-tag-syntax.yaml"></a>

```
  [Key](#cfn-ec2-carriergateway-tag-key): {{String}}
  [Value](#cfn-ec2-carriergateway-tag-value): {{String}}
```

## Properties
<a name="aws-properties-ec2-carriergateway-tag-properties"></a>

`Key`  <a name="cfn-ec2-carriergateway-tag-key"></a>
The tag key.
*Required*: No
*Type*: String
*Pattern*: `^(?!aws:.*)`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ec2-carriergateway-tag-value"></a>
The tag value.
*Required*: No
*Type*: String
*Pattern*: `^(?!aws:.*)`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-ec2-carriergateway-tag--examples"></a>

###
<a name="aws-properties-ec2-carriergateway-tag--examples--"></a>

This example specifies two tags for the carrier gateway.

#### JSON
<a name="aws-properties-ec2-carriergateway-tag--examples----json"></a>

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
<a name="aws-properties-ec2-carriergateway-tag--examples----yaml"></a>

```
Tags:
  - Key: "key1"
    Value: "value1"
  - Key: "key2"
    Value: "value2"
```
