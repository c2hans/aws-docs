---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-integration-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Integration Tag
<a name="aws-properties-customerprofiles-integration-tag"></a>

<a name="aws-properties-customerprofiles-integration-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::CustomerProfiles::Integration](aws-resource-customerprofiles-integration.md).

## Syntax
<a name="aws-properties-customerprofiles-integration-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-integration-tag-syntax.json"></a>

```
{
  "[Key](#cfn-customerprofiles-integration-tag-key)" : {{String}},
  "[Value](#cfn-customerprofiles-integration-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-integration-tag-syntax.yaml"></a>

```
  [Key](#cfn-customerprofiles-integration-tag-key): {{String}}
  [Value](#cfn-customerprofiles-integration-tag-value): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-integration-tag-properties"></a>

`Key`  <a name="cfn-customerprofiles-integration-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-customerprofiles-integration-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
