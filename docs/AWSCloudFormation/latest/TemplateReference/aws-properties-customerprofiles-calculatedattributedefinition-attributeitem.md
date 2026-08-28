---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-calculatedattributedefinition-attributeitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::CalculatedAttributeDefinition AttributeItem
<a name="aws-properties-customerprofiles-calculatedattributedefinition-attributeitem"></a>

The details of a single attribute item specified in the mathematical expression.

## Syntax
<a name="aws-properties-customerprofiles-calculatedattributedefinition-attributeitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-calculatedattributedefinition-attributeitem-syntax.json"></a>

```
{
  "[Name](#cfn-customerprofiles-calculatedattributedefinition-attributeitem-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-calculatedattributedefinition-attributeitem-syntax.yaml"></a>

```
  [Name](#cfn-customerprofiles-calculatedattributedefinition-attributeitem-name): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-calculatedattributedefinition-attributeitem-properties"></a>

`Name`  <a name="cfn-customerprofiles-calculatedattributedefinition-attributeitem-name"></a>
The unique name of the calculated attribute.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
