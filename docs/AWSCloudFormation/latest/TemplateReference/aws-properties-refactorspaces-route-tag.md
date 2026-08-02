---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-refactorspaces-route-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RefactorSpaces::Route Tag
<a name="aws-properties-refactorspaces-route-tag"></a>

<a name="aws-properties-refactorspaces-route-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::RefactorSpaces::Route](aws-resource-refactorspaces-route.md).

## Syntax
<a name="aws-properties-refactorspaces-route-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-refactorspaces-route-tag-syntax.json"></a>

```
{
  "[Key](#cfn-refactorspaces-route-tag-key)" : {{String}},
  "[Value](#cfn-refactorspaces-route-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-refactorspaces-route-tag-syntax.yaml"></a>

```
  [Key](#cfn-refactorspaces-route-tag-key): {{String}}
  [Value](#cfn-refactorspaces-route-tag-value): {{String}}
```

## Properties
<a name="aws-properties-refactorspaces-route-tag-properties"></a>

`Key`  <a name="cfn-refactorspaces-route-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:).+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-refactorspaces-route-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
