---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iottwinmaker-componenttype-propertygroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTTwinMaker::ComponentType PropertyGroup
<a name="aws-properties-iottwinmaker-componenttype-propertygroup"></a>

The property group.

## Syntax
<a name="aws-properties-iottwinmaker-componenttype-propertygroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iottwinmaker-componenttype-propertygroup-syntax.json"></a>

```
{
  "[GroupType](#cfn-iottwinmaker-componenttype-propertygroup-grouptype)" : {{String}},
  "[PropertyNames](#cfn-iottwinmaker-componenttype-propertygroup-propertynames)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-iottwinmaker-componenttype-propertygroup-syntax.yaml"></a>

```
  [GroupType](#cfn-iottwinmaker-componenttype-propertygroup-grouptype): {{String}}
  [PropertyNames](#cfn-iottwinmaker-componenttype-propertygroup-propertynames): {{
    - String}}
```

## Properties
<a name="aws-properties-iottwinmaker-componenttype-propertygroup-properties"></a>

`GroupType`  <a name="cfn-iottwinmaker-componenttype-propertygroup-grouptype"></a>
The group type.
*Required*: No
*Type*: String
*Allowed values*: `TABULAR`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropertyNames`  <a name="cfn-iottwinmaker-componenttype-propertygroup-propertynames"></a>
The property names.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
