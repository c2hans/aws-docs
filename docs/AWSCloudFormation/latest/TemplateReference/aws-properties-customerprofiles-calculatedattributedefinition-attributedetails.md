---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-calculatedattributedefinition-attributedetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::CalculatedAttributeDefinition AttributeDetails
<a name="aws-properties-customerprofiles-calculatedattributedefinition-attributedetails"></a>

Mathematical expression and a list of attribute items specified in that expression.

## Syntax
<a name="aws-properties-customerprofiles-calculatedattributedefinition-attributedetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-calculatedattributedefinition-attributedetails-syntax.json"></a>

```
{
  "[Attributes](#cfn-customerprofiles-calculatedattributedefinition-attributedetails-attributes)" : {{[ AttributeItem, ... ]}},
  "[Expression](#cfn-customerprofiles-calculatedattributedefinition-attributedetails-expression)" : {{String}}
}
```

### YAML
<a name="aws-properties-customerprofiles-calculatedattributedefinition-attributedetails-syntax.yaml"></a>

```
  [Attributes](#cfn-customerprofiles-calculatedattributedefinition-attributedetails-attributes): {{
    - AttributeItem}}
  [Expression](#cfn-customerprofiles-calculatedattributedefinition-attributedetails-expression): {{String}}
```

## Properties
<a name="aws-properties-customerprofiles-calculatedattributedefinition-attributedetails-properties"></a>

`Attributes`  <a name="cfn-customerprofiles-calculatedattributedefinition-attributedetails-attributes"></a>
Mathematical expression and a list of attribute items specified in that expression.
*Required*: Yes
*Type*: Array of [AttributeItem](aws-properties-customerprofiles-calculatedattributedefinition-attributeitem.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Expression`  <a name="cfn-customerprofiles-calculatedattributedefinition-attributedetails-expression"></a>
Mathematical expression that is performed on attribute items provided in the attribute list. Each element in the expression should follow the structure of \\"{ObjectTypeName.AttributeName}\\".
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
