---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apprunner-vpcingressconnection-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppRunner::VpcIngressConnection Tag
<a name="aws-properties-apprunner-vpcingressconnection-tag"></a>

Describes a tag that is applied to an AWS App Runner resource. A tag is a metadata item consisting of a key-value pair.

## Syntax
<a name="aws-properties-apprunner-vpcingressconnection-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apprunner-vpcingressconnection-tag-syntax.json"></a>

```
{
  "[Key](#cfn-apprunner-vpcingressconnection-tag-key)" : {{String}},
  "[Value](#cfn-apprunner-vpcingressconnection-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-apprunner-vpcingressconnection-tag-syntax.yaml"></a>

```
  [Key](#cfn-apprunner-vpcingressconnection-tag-key): {{String}}
  [Value](#cfn-apprunner-vpcingressconnection-tag-value): {{String}}
```

## Properties
<a name="aws-properties-apprunner-vpcingressconnection-tag-properties"></a>

`Key`  <a name="cfn-apprunner-vpcingressconnection-tag-key"></a>
The key of the tag.
*Required*: No
*Type*: String
*Pattern*: `^(?!aws:).+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-apprunner-vpcingressconnection-tag-value"></a>
The value of the tag assigned to `VpcIngressConnection` resource of the App Runner service.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
