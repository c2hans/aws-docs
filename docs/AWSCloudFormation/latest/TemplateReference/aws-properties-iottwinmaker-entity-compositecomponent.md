---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iottwinmaker-entity-compositecomponent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTTwinMaker::Entity CompositeComponent
<a name="aws-properties-iottwinmaker-entity-compositecomponent"></a>

Information about a composite component.

## Syntax
<a name="aws-properties-iottwinmaker-entity-compositecomponent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iottwinmaker-entity-compositecomponent-syntax.json"></a>

```
{
  "[ComponentName](#cfn-iottwinmaker-entity-compositecomponent-componentname)" : {{String}},
  "[ComponentPath](#cfn-iottwinmaker-entity-compositecomponent-componentpath)" : {{String}},
  "[ComponentTypeId](#cfn-iottwinmaker-entity-compositecomponent-componenttypeid)" : {{String}},
  "[Description](#cfn-iottwinmaker-entity-compositecomponent-description)" : {{String}},
  "[Properties](#cfn-iottwinmaker-entity-compositecomponent-properties)" : {{{{{Key}}: {{Value}}, ...}}},
  "[PropertyGroups](#cfn-iottwinmaker-entity-compositecomponent-propertygroups)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Status](#cfn-iottwinmaker-entity-compositecomponent-status)" : {{Status}}
}
```

### YAML
<a name="aws-properties-iottwinmaker-entity-compositecomponent-syntax.yaml"></a>

```
  [ComponentName](#cfn-iottwinmaker-entity-compositecomponent-componentname): {{String}}
  [ComponentPath](#cfn-iottwinmaker-entity-compositecomponent-componentpath): {{String}}
  [ComponentTypeId](#cfn-iottwinmaker-entity-compositecomponent-componenttypeid): {{String}}
  [Description](#cfn-iottwinmaker-entity-compositecomponent-description): {{String}}
  [Properties](#cfn-iottwinmaker-entity-compositecomponent-properties): {{
    {{Key}}: {{Value}}}}
  [PropertyGroups](#cfn-iottwinmaker-entity-compositecomponent-propertygroups): {{
    {{Key}}: {{Value}}}}
  [Status](#cfn-iottwinmaker-entity-compositecomponent-status): {{
    Status}}
```

## Properties
<a name="aws-properties-iottwinmaker-entity-compositecomponent-properties"></a>

`ComponentName`  <a name="cfn-iottwinmaker-entity-compositecomponent-componentname"></a>
The name of the component.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z_\-0-9]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComponentPath`  <a name="cfn-iottwinmaker-entity-compositecomponent-componentpath"></a>
The path to the composite component, starting from the top-level component.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z_\-0-9/]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComponentTypeId`  <a name="cfn-iottwinmaker-entity-compositecomponent-componenttypeid"></a>
The ID of the composite component type.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z_\-0-9]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-iottwinmaker-entity-compositecomponent-description"></a>
The description of the component type.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Properties`  <a name="cfn-iottwinmaker-entity-compositecomponent-properties"></a>
Map of strings to the properties in the component type. Each string in the mapping must be unique to this component.
*Required*: No
*Type*: Object of [Property](aws-properties-iottwinmaker-entity-property.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropertyGroups`  <a name="cfn-iottwinmaker-entity-compositecomponent-propertygroups"></a>
The property groups.
*Required*: No
*Type*: Object of [PropertyGroup](aws-properties-iottwinmaker-entity-propertygroup.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-iottwinmaker-entity-compositecomponent-status"></a>
The current status of the composite component.
*Required*: No
*Type*: [Status](aws-properties-iottwinmaker-entity-status.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
