---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-objecttype-fieldmap.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::ObjectType FieldMap
<a name="aws-properties-customerprofiles-objecttype-fieldmap"></a>

A map of the name and ObjectType field.

## Syntax
<a name="aws-properties-customerprofiles-objecttype-fieldmap-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-objecttype-fieldmap-syntax.json"></a>

```
{
  "[Name](#cfn-customerprofiles-objecttype-fieldmap-name)" : {{String}},
  "[ObjectTypeField](#cfn-customerprofiles-objecttype-fieldmap-objecttypefield)" : {{ObjectTypeField}}
}
```

### YAML
<a name="aws-properties-customerprofiles-objecttype-fieldmap-syntax.yaml"></a>

```
  [Name](#cfn-customerprofiles-objecttype-fieldmap-name): {{String}}
  [ObjectTypeField](#cfn-customerprofiles-objecttype-fieldmap-objecttypefield): {{
    ObjectTypeField}}
```

## Properties
<a name="aws-properties-customerprofiles-objecttype-fieldmap-properties"></a>

`Name`  <a name="cfn-customerprofiles-objecttype-fieldmap-name"></a>
Name of the field.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ObjectTypeField`  <a name="cfn-customerprofiles-objecttype-fieldmap-objecttypefield"></a>
Represents a field in a ProfileObjectType.
*Required*: No
*Type*: [ObjectTypeField](aws-properties-customerprofiles-objecttype-objecttypefield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
