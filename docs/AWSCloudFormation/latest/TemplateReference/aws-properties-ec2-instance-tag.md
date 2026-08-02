---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-instance-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::Instance Tag
<a name="aws-properties-ec2-instance-tag"></a>

Specifies a tag. For more information, see [Resource tags](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).

## Syntax
<a name="aws-properties-ec2-instance-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-instance-tag-syntax.json"></a>

```
{
  "[Key](#cfn-ec2-instance-tag-key)" : {{String}},
  "[Value](#cfn-ec2-instance-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-instance-tag-syntax.yaml"></a>

```
  [Key](#cfn-ec2-instance-tag-key): {{String}}
  [Value](#cfn-ec2-instance-tag-value): {{String}}
```

## Properties
<a name="aws-properties-ec2-instance-tag-properties"></a>

`Key`  <a name="cfn-ec2-instance-tag-key"></a>
The tag key.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ec2-instance-tag-value"></a>
The tag value.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-ec2-instance-tag--examples"></a>

###
<a name="aws-properties-ec2-instance-tag--examples--"></a>

This example specifies two tags for the instance.

#### JSON
<a name="aws-properties-ec2-instance-tag--examples----json"></a>

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
<a name="aws-properties-ec2-instance-tag--examples----yaml"></a>

```
Tags:
  - Key: "key1"
    Value: "value1"
  - Key: "key2"
    Value: "value2"
```
