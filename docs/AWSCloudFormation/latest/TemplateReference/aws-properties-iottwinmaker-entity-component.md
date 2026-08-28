---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iottwinmaker-entity-component.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTTwinMaker::Entity Component
<a name="aws-properties-iottwinmaker-entity-component"></a>

The entity component.

## Syntax
<a name="aws-properties-iottwinmaker-entity-component-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iottwinmaker-entity-component-syntax.json"></a>

```
{
  "[ComponentName](#cfn-iottwinmaker-entity-component-componentname)" : {{String}},
  "[ComponentTypeId](#cfn-iottwinmaker-entity-component-componenttypeid)" : {{String}},
  "[DefinedIn](#cfn-iottwinmaker-entity-component-definedin)" : {{String}},
  "[Description](#cfn-iottwinmaker-entity-component-description)" : {{String}},
  "[Properties](#cfn-iottwinmaker-entity-component-properties)" : {{{{{Key}}: {{Value}}, ...}}},
  "[PropertyGroups](#cfn-iottwinmaker-entity-component-propertygroups)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Status](#cfn-iottwinmaker-entity-component-status)" : {{Status}}
}
```

### YAML
<a name="aws-properties-iottwinmaker-entity-component-syntax.yaml"></a>

```
  [ComponentName](#cfn-iottwinmaker-entity-component-componentname): {{String}}
  [ComponentTypeId](#cfn-iottwinmaker-entity-component-componenttypeid): {{String}}
  [DefinedIn](#cfn-iottwinmaker-entity-component-definedin): {{String}}
  [Description](#cfn-iottwinmaker-entity-component-description): {{String}}
  [Properties](#cfn-iottwinmaker-entity-component-properties): {{
    {{Key}}: {{Value}}}}
  [PropertyGroups](#cfn-iottwinmaker-entity-component-propertygroups): {{
    {{Key}}: {{Value}}}}
  [Status](#cfn-iottwinmaker-entity-component-status): {{
    Status}}
```

## Properties
<a name="aws-properties-iottwinmaker-entity-component-properties"></a>

`ComponentName`  <a name="cfn-iottwinmaker-entity-component-componentname"></a>
The name of the component.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z_\-0-9]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComponentTypeId`  <a name="cfn-iottwinmaker-entity-component-componenttypeid"></a>
The ID of the component type.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z_\-0-9]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefinedIn`  <a name="cfn-iottwinmaker-entity-component-definedin"></a>
The name of the property definition set in the request.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-iottwinmaker-entity-component-description"></a>
The description of the component.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Properties`  <a name="cfn-iottwinmaker-entity-component-properties"></a>
An object that maps strings to the properties to set in the component type. Each string in the mapping must be unique to this object.
*Required*: No
*Type*: Object of [Property](aws-properties-iottwinmaker-entity-property.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropertyGroups`  <a name="cfn-iottwinmaker-entity-component-propertygroups"></a>
An object that maps strings to the property groups in the component type. Each string in the mapping must be unique to this object.
*Required*: No
*Type*: Object of [PropertyGroup](aws-properties-iottwinmaker-entity-propertygroup.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-iottwinmaker-entity-component-status"></a>
The status of the component.
*Required*: No
*Type*: [Status](aws-properties-iottwinmaker-entity-status.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
