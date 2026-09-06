---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-domain-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Domain Tag
<a name="aws-properties-customerprofiles-domain-tag"></a>

The tags (keys and values) associated with the domain

## Syntax
<a name="aws-properties-customerprofiles-domain-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-domain-tag-syntax.json"></a>

```
{
  "[Key](#cfn-customerprofiles-domain-tag-key)" : {{String}},
  "[Value](#cfn-customerprofiles-domain-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-domain-tag-syntax.yaml"></a>

```
  [Key](#cfn-customerprofiles-domain-tag-key): {{String}}
  [Value](#cfn-customerprofiles-domain-tag-value): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-domain-tag-properties"></a>

`Key`  <a name="cfn-customerprofiles-domain-tag-key"></a>
A string you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-customerprofiles-domain-tag-value"></a>
The value for the specified tag key.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
