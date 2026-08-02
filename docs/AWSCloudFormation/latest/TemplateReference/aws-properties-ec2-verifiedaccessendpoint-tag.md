---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-verifiedaccessendpoint-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VerifiedAccessEndpoint Tag
<a name="aws-properties-ec2-verifiedaccessendpoint-tag"></a>

Specifies a tag. For more information, see [Resource tags](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).

## Syntax
<a name="aws-properties-ec2-verifiedaccessendpoint-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-verifiedaccessendpoint-tag-syntax.json"></a>

```
{
  "[Key](#cfn-ec2-verifiedaccessendpoint-tag-key)" : {{String}},
  "[Value](#cfn-ec2-verifiedaccessendpoint-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-verifiedaccessendpoint-tag-syntax.yaml"></a>

```
  [Key](#cfn-ec2-verifiedaccessendpoint-tag-key): {{String}}
  [Value](#cfn-ec2-verifiedaccessendpoint-tag-value): {{String}}
```

## Properties
<a name="aws-properties-ec2-verifiedaccessendpoint-tag-properties"></a>

`Key`  <a name="cfn-ec2-verifiedaccessendpoint-tag-key"></a>
The tag key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ec2-verifiedaccessendpoint-tag-value"></a>
The tag value.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-ec2-verifiedaccessendpoint-tag--examples"></a>

###
<a name="aws-properties-ec2-verifiedaccessendpoint-tag--examples--"></a>

This example specifies two tags for the Verified Access endpoint.

#### JSON
<a name="aws-properties-ec2-verifiedaccessendpoint-tag--examples----json"></a>

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
<a name="aws-properties-ec2-verifiedaccessendpoint-tag--examples----yaml"></a>

```
Tags:
  - Key: "key1"
    Value: "value1"
  - Key: "key2"
    Value: "value2"
```
