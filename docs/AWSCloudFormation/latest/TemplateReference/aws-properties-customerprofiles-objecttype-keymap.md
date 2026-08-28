---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-objecttype-keymap.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::ObjectType KeyMap
<a name="aws-properties-customerprofiles-objecttype-keymap"></a>

A unique key map that can be used to map data to the profile.

## Syntax
<a name="aws-properties-customerprofiles-objecttype-keymap-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-objecttype-keymap-syntax.json"></a>

```
{
  "[Name](#cfn-customerprofiles-objecttype-keymap-name)" : {{String}},
  "[ObjectTypeKeyList](#cfn-customerprofiles-objecttype-keymap-objecttypekeylist)" : {{[ ObjectTypeKey, ... ]}}
}
```

### YAML
<a name="aws-properties-customerprofiles-objecttype-keymap-syntax.yaml"></a>

```
  [Name](#cfn-customerprofiles-objecttype-keymap-name): {{String}}
  [ObjectTypeKeyList](#cfn-customerprofiles-objecttype-keymap-objecttypekeylist): {{
    - ObjectTypeKey}}
```

## Properties
<a name="aws-properties-customerprofiles-objecttype-keymap-properties"></a>

`Name`  <a name="cfn-customerprofiles-objecttype-keymap-name"></a>
Name of the key.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ObjectTypeKeyList`  <a name="cfn-customerprofiles-objecttype-keymap-objecttypekeylist"></a>
 A list of ObjectTypeKey.
*Required*: No
*Type*: Array of [ObjectTypeKey](aws-properties-customerprofiles-objecttype-objecttypekey.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
