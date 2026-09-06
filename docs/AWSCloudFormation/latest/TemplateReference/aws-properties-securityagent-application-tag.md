---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityagent-application-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::Application Tag
<a name="aws-properties-securityagent-application-tag"></a>

The tags associated with the resource.

## Syntax
<a name="aws-properties-securityagent-application-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityagent-application-tag-syntax.json"></a>

```
{
  "[Key](#cfn-securityagent-application-tag-key)" : {{String}},
  "[Value](#cfn-securityagent-application-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityagent-application-tag-syntax.yaml"></a>

```
  [Key](#cfn-securityagent-application-tag-key): {{String}}
  [Value](#cfn-securityagent-application-tag-value): {{String}}
```

## Properties
<a name="aws-properties-securityagent-application-tag-properties"></a>

`Key`  <a name="cfn-securityagent-application-tag-key"></a>
The tags to add to the resource.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-securityagent-application-tag-value"></a>
The tags to add to the resource.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
