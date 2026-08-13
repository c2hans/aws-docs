---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-codegenjob-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::CodegenJob Tag
<a name="aws-properties-amplifyuibuilder-codegenjob-tag"></a>

<a name="aws-properties-amplifyuibuilder-codegenjob-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::AmplifyUIBuilder::CodegenJob](aws-resource-amplifyuibuilder-codegenjob.md).

## Syntax
<a name="aws-properties-amplifyuibuilder-codegenjob-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-codegenjob-tag-syntax.json"></a>

```
{
  "[Key](#cfn-amplifyuibuilder-codegenjob-tag-key)" : {{String}},
  "[Value](#cfn-amplifyuibuilder-codegenjob-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-codegenjob-tag-syntax.yaml"></a>

```
  [Key](#cfn-amplifyuibuilder-codegenjob-tag-key): {{String}}
  [Value](#cfn-amplifyuibuilder-codegenjob-tag-value): {{String}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-codegenjob-tag-properties"></a>

`Key`  <a name="cfn-amplifyuibuilder-codegenjob-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-amplifyuibuilder-codegenjob-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
