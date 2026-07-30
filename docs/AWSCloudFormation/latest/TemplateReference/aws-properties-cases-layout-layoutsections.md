---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cases-layout-layoutsections.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::Layout LayoutSections
<a name="aws-properties-cases-layout-layoutsections"></a>

Ordered list containing different kinds of sections that can be added. A LayoutSections object can only contain one section.

## Syntax
<a name="aws-properties-cases-layout-layoutsections-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cases-layout-layoutsections-syntax.json"></a>

```
{
  "[Sections](#cfn-cases-layout-layoutsections-sections)" : {{[ Section, ... ]}}
}
```

### YAML
<a name="aws-properties-cases-layout-layoutsections-syntax.yaml"></a>

```
  [Sections](#cfn-cases-layout-layoutsections-sections): {{
    - Section}}
```

## Properties
<a name="aws-properties-cases-layout-layoutsections-properties"></a>

`Sections`  <a name="cfn-cases-layout-layoutsections-sections"></a>
Ordered list containing different kinds of sections that can be added. A LayoutSections object can only contain one section.
*Required*: No
*Type*: Array of [Section](aws-properties-cases-layout-section.md)
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
