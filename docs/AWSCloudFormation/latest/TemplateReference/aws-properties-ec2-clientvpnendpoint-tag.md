---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-clientvpnendpoint-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::ClientVpnEndpoint Tag
<a name="aws-properties-ec2-clientvpnendpoint-tag"></a>

Specifies a tag. For more information, see [Resource tags](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).

## Syntax
<a name="aws-properties-ec2-clientvpnendpoint-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-clientvpnendpoint-tag-syntax.json"></a>

```
{
  "[Key](#cfn-ec2-clientvpnendpoint-tag-key)" : {{String}},
  "[Value](#cfn-ec2-clientvpnendpoint-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-clientvpnendpoint-tag-syntax.yaml"></a>

```
  [Key](#cfn-ec2-clientvpnendpoint-tag-key): {{String}}
  [Value](#cfn-ec2-clientvpnendpoint-tag-value): {{String}}
```

## Properties
<a name="aws-properties-ec2-clientvpnendpoint-tag-properties"></a>

`Key`  <a name="cfn-ec2-clientvpnendpoint-tag-key"></a>
The tag key.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-ec2-clientvpnendpoint-tag-value"></a>
The tag value.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Examples
<a name="aws-properties-ec2-clientvpnendpoint-tag--examples"></a>

###
<a name="aws-properties-ec2-clientvpnendpoint-tag--examples--"></a>

This example specifies two tags for the Client VPN endpoint.

#### JSON
<a name="aws-properties-ec2-clientvpnendpoint-tag--examples----json"></a>

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
<a name="aws-properties-ec2-clientvpnendpoint-tag--examples----yaml"></a>

```
Tags:
  - Key: "key1"
    Value: "value1"
  - Key: "key2"
    Value: "value2"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
